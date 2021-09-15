# Example:
# Hand size 7, deck size 60, same_cards 4, expected_picks 2
# 4!/2! *4/60 * 3/59 * 56/58 * 55/57 * 54/56 * 53/55 * 52/54
#               60-2-4+2
# Hand size 7, deck size 60, same_cards 4, expected_picks 3
# 4/60 * 3/59 * 2/58 * 56/57 * 55/56 * 54/55 * 53/54
#                       60-3-4+3
# Hand size 7, deck size 60, same_cards 4, expected_picks 0
# 56/60 * 55/59 * 54/58 * 53/57 * 52/56 * 51/55 * 50/54
#

from math import comb


def exactly_starting_hand_pick(hand_size, deck_size, same_cards_in_deck, expected_picks):
    probability = 100.0 * comb(hand_size, expected_picks)
    for i in range(hand_size):
        if i < expected_picks:
            probability = probability * (same_cards_in_deck - i) / (deck_size - i)
        else:
            probability = probability * (deck_size - i - same_cards_in_deck + expected_picks) / (deck_size - i)
    return probability


print(range(7))
total = 0.0
cards_in_deck = 4
for i in range(cards_in_deck + 1):
    print(str(i) + " : " + str(exactly_starting_hand_pick(7, 60, cards_in_deck, i)))
    total = total + exactly_starting_hand_pick(7, 60, cards_in_deck, i)

print(total)
total = 0.0
print("****")
cards_in_deck = 25
for i in range(cards_in_deck + 1):
    print(str(i) + " : " + str(exactly_starting_hand_pick(7, 60, cards_in_deck, i)))
    total = total + exactly_starting_hand_pick(7, 60, cards_in_deck, i)
print(total)

print("****")
