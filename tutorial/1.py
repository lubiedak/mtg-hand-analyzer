# To jest komentarz, zaczal sie od # - nic nie zmienia w kodzie, ale go opisuje
print('1. Wstęp:\n\n')
# 1. Poniżej mamy 2 zmienne o typie tekstowym
text1 = 'Hello '
text2 = 'World'
#Funkcja print dluzy do wypisania czegos na ekran
#Dodawanie tekstu do tekstu oznacza łączenie go
print(text1 + text2)
#Dodawanie lub inne działania na liczbach są wykonywane jak na kalkulatorze
print(1+0.2*4-10000)

#2. Zmienne mają: typ, oraz aktualną wartość. Może się ona zmienić
print('2. Zmienne:\n\n')
a = '2'
print('Wartosc a:' + a)
print(type(a))
a = a + 'costamcostam'
print(a)

# Więcej typów
print('3. Popularne typy:\n\n')
b = 2    # liczba
c = 0.2  # liczba zmiennoprzecinkowa
d = []   # lista
e = {}   # słownik
print('Wartosc a:' + a)
print(type(a))
print('Wartosc b:' + str(b))
print(type(b))
print('Wartosc c:' + str(c))
print(type(c))
print('Wartosc d:' + str(d))
print(type(d))
print('Wartosc e:' + str(e))
print(type(e))

#Bardziej rozbudowane kolekcje
print('4. Rozbudowane kolekcje:\n\n')
card1 = {'nazwa': '+2 Mace', 'koszt':'AP', 'rarity':'c'}
card2 = {'nazwa': 'Adult Gold Dragon', 'koszt':'3AFP', 'rarity':'r'}
card3 = {'nazwa': '+2 Mace', 'koszt':'AP', 'rarity':'m'}
print("typ card1: " + str(type(card1)))
print('5. Lista słowników może istnieć, słownik list także')

lista_kart = [card1, card2, card3]
print(lista_kart)
print('typ listy kart: ' + str(type(lista_kart)))
