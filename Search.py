import requests


def search(champion):
    if champion == "aurelion-sol":
        champion = "aurelion-sol-130"

    url = f"https://www.mobafire.com/league-of-legends/champion/{champion}"
    result = requests.get(url)
    if result.status_code != 200:
        return False
    else:
        return result
