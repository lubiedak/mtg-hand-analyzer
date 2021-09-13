import requests

url = 'https://api.scryfall.com/cards/search?order=name&q=e:stx&page=2'
fields = ['name', 'mana_cost', 'type_line', 'oracle_text', 'set', 'rarity']

response = requests.get(url)
cards = []
for card_json in response.json()['data']:
    card = {}
    for field in fields:
        try:
            card[field] = card_json[field].replace('\n', ' ').replace('\r', '')
        except KeyError:
            card[field] = ""
    cards.append(card)


for card in cards:
    for field in fields:
        print(card[field], end=",")
    print("")
