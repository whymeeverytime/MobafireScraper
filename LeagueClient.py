import requests
import json


# Returns the champion name of the given champion key from the latest champion list
def idToNameCh(champKey):
    versions = json.loads(requests.get('https://ddragon.leagueoflegends.com/api/versions.json').text)
    latest = versions[0]

    listJson = json.loads(
        requests.get(f'https://ddragon.leagueoflegends.com/cdn/{latest}/data/en_US/champion.json').text)

    for champ in listJson['data']:
        if listJson['data'][champ]['key'] == champKey:
            return champ
