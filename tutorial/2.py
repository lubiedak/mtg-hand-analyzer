import time
# To metoda, na razie ją zignoruj, wróć do niej na koniec tutoriala
def next_block(nazwa):
  print("\n\n******************** {} ************************\n\n".format(nazwa))
  time.sleep(2)

# Dodatek do tutoriala:

# Warunki if/else. Oznacza to dla programu, że wykona jedną albo drugą operację
tutorial = 1
next_block("Prosty if")
if tutorial == 1:
  print("To pierwszy tutorial")
else:
  print("To kolejny tutorial")

# Bardziej złożone if/else, oraz metoda input()
# Metoda input prosi użytkownika o podanie jakiejś wartości na konsoli, a następnie zapisuje ją do zmiennej
print("Napisz jakiekolwiek zdanie: ")
zdanie = input()
print("Napisałeś zdanie " + zdanie)

if len(zdanie) < 20:
  # metoda format() wrzuci w miejsce {} podaną zmienną
  print("Zdanie jest dosyć krótkie. Ma {} liter".format(len(zdanie)))
elif len(zdanie) > 20 and len(zdanie) < 40:
  print("Zdanie jest średniej wielkości. Ma {} liter, to więcej niż {}".format(len(zdanie), 10))
else:
  print("Twoje zdanie jest długie")

next_block("Słowniki")
# A teraz przyjrzymy się słownikom:
card = {'nazwa': 'Adult Gold Dragon', 'koszt':'3AFP', 'rarity':'r'}
print("Nazwa tej karty to: {}".format(card['nazwa']))
print("Lub nazwa tej karty to: " + card['nazwa'])

print("Ta karta jest rzadka, bo ma " + card['rarity'])


# Napiszmy metodę/ funkcję, która nam wypisze koszt kart i rarirty
# Funkcje są po to, aby powtarzające się operacje zamknąć w blokach, które możemy wywoałać.

next_block("Metody")
# Na poczatku tego tutoriala jest metoda o nazwie next_block()
# Gdy w kodzie widzisz next_block("coś tam") to ją poprostu wypisujemy.
# teraz stworzymy metodę, która zaoszczędzi nam sporo linii kodu:

def opisz_karte(karta):
  print("\nNazwa karty: " + karta['nazwa'])
  print("Koszt karty: " + karta['koszt'])
  rzadkosc = karta['rarity']
  if rzadkosc == 'r':
    print("Ta karta jest rzadka")
  elif rzadkosc == 'u':
    print("To zwykły uncommon")
  elif rzadkosc == 'c':
    print("To zwykły common")
  else:
    print('Nieznana rzadkosc karty')
    
card1 = {'nazwa': 'Adult Gold Dragon', 'koszt':'3AFP', 'rarity':'r'}
card2 = {'nazwa': 'Karta 2', 'koszt':'3AFP', 'rarity':'c'}
card3 = {'nazwa': 'Karta 3', 'koszt':'WP', 'rarity':'jakis'}
card4 = {'nazwa': 'Karta 4', 'koszt':'S', 'rarity':'u'}

opisz_karte(card1)
opisz_karte(card2)
opisz_karte(card3)
opisz_karte(card4)

