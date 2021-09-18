from analyzer.mana_curve import count_cost
import db.deck_reader as dr
import analyzer.mana_curve as mana

deck = dr.read_deck(open('db/deck_example.txt', 'r').read())
size = dr.deck_size(deck)
deck_with_cost = mana.deck_with_costs(dr.cards_to_list(deck))
