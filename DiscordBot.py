import discord
from Search import search
from bs4 import BeautifulSoup

file = open("token.txt", "r")
token = file.read()

client = discord.Client()

channelIds = [790988424814919720, 472863919246016533, 833986892844105761, 835624329164357724]


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="!mobafire "
                                                                                                   "<champion>"))


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.channel.id not in channelIds and not isinstance(msg.channel, discord.channel.DMChannel):
        return

    if msg.content.split(' ')[0] == '!mobafire':
        champ = msg.content.replace('!mobafire ', '')
        champ = champ.replace(' ', '-')
        result = search(champ)
        if not result:
            await msg.channel.send(content="Wrong champion name!🤦")
        else:
            soup = BeautifulSoup(search(champ).content, "html.parser")
            results = soup.find(class_="mf-listings__item", href=True)

            guideUrl = "https://www.mobafire.com" + results['href']
            votes = results.find(class_="mf-listings__item__rating__info").get_text(separator=" ", strip=True)
            voteContent = [int(i) for i in votes.split() if i.isdigit()]
            imgURL = "\n\nhttps://www.mobafire.com" + results.find('img')['data-original']

            embed = discord.Embed(
                title=results.find(class_="mf-listings__item__info__title").text,
                url=guideUrl
            )
            embed.set_thumbnail(
                url=imgURL
            )
            embed.add_field(
                name="Thumbs Up",
                value=str(voteContent[0])
            )
            embed.add_field(
                name="Thumbs Down",
                value=str(voteContent[1])
            )
            if isinstance(msg.channel, discord.channel.DMChannel):
                await msg.author.send(embed=embed)
            else:
                await msg.channel.send(embed=embed)


client.run(token)
