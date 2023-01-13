import requests
from dataclasses import dataclass

characterids = ['11161699', '35126937', '55924214', '55996945', '51518136']

class Character:
    '''Class for defining a dndbeyond character'''

    def __init__(self, id):
        self.id = id
        character = self.getCharacterInfo()

        self.name = character['data']['name']
        self.username = character['data']['username']
        self.classes = character['data']['classes']
        self.inspiration = character['data']['inspiration']
        self.stats = character['data']['stats']
        self.bonusStats = character['data']['bonusStats']
        self.baseHitPoints = character['data']['baseHitPoints']

    def getCharacterInfo(self):
        # Get character info from API
        character = 'https://character-service.dndbeyond.com/character/v5/character/'+self.id
        r = requests.get(character)
        return r.json()




def main():
    characters = {}
    # Get character info
    for character in characterids:
        next = Character(character)
        characters[next.name] = next

    # Print character info
    for character in characters:
        print(characters[character].name + '   ' + characters[character].username + "  HP:" + str(characters[character].baseHitPoints))



main()

