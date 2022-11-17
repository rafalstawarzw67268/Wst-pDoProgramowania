"""Zadanie 1.
• Utwórz listę values zawierającą liczby 10, 20, 30. Utwórz drugą listę keys zawierającą nazwy tych liczb w
języku angielskim (lub polskim). Dokonaj konwersji tych list w słownik.
Wskazówki:
− użyj funkcji zip(), która pobiera dwie sekwencje (takie jak list, dict, str), łączy je w krotki (pary) i
zwraca;
− lub wykonaj iterację listy za pomocą pętli for i funkcji range(). W każdej iteracji dodaj nową parę kluczwartość do słownika.
• Utwórz drugi słownik metodą słów kluczowych ( dict(klucz1=wartość1, klucz2=wartość2)), gdzie kluczem
będą nazwy liczb 30, 40, 50, a wartościami – liczby 30, 40, 50.
• Połącz dwa słowniki w jeden nowy słownik."""

values=[10,20,30]
keys=['Ten','Twenty','Thirty']
D=dict(zip(keys,values))
print(D)
#print(list(zip(keys,values)))
x=len(keys)
for i in range(x):
    D[keys[i]]=values[i]
print(D)
słownik1=dict(zip(keys,values))

D2=dict(Thirty=30, forty=40, fifty=50)

D3= D.copy()
D3.update(D2)
print(D3)









