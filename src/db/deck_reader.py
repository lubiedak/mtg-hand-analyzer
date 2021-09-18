
def read_deck(input_list):
    cards = input_list.splitlines()
    deck = []
    for card in cards:
        n = int(card[:2].strip())
        name = card[2:]
        deck.append({'name': name, 'quantity': n})
    return deck

def deck_size(deck):
    total = 0
    for card in deck:
        total += card['quantity']
    return total

def get_card_by_name(card_name):
    with(open('db/cards.csv', 'r')) as db:
        for line in db:
            if line.startswith(card_name):
                return line


def card_to_dict(card_text):
    fields = card_text.split(',')
    card_dict = {'name': fields[0], 'cost': fields[1], 'type': fields[2].split(" — ")[0]}
    return card_dict


def cards_to_list(deck_input):
    deck = []
    for card in deck_input:
        card_text = get_card_by_name(card['name'])
        card_dict = card_to_dict(card_text)
        card_dict['quantity'] = card['quantity']
        deck.append(card_dict)
    return deck
