"""Zadanie 1. Napisz funkcję find(), która w liście sprawdza czy występuje podana wartość. Lista i wartość są
parametrami funkcji. Funkcja ma zwracać listę indeksów, pod którymi wystąpiła wartość. Nie wolno korzystać z
operatora in w celu sprawdzenia czy wartość występuje w liście.
"""
def find(wartosc, lista):
    x = 0
    indeksy = []
    for i in lista:
        if i == wartosc:
            indeksy.append(x)
        x+=1
    return indeksy
E = find(3, [8, 9, 5, 4])
print(E)