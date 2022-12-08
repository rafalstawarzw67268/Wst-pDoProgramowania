"""Zadanie 3. Napisz funkcję potęga(), która podniesie wartości z pierwszej listy do potęg z drugiej listy. Sprawdź,
czy listy są tej samej długości. Parametrami funkcji są dwie listy. Funkcja ma zwracać listę z wynikami."""

def potęga(liczby, potęgi):
    i = 0
    lista3 = []
    if len(liczby) != len(potęgi):
        print("Listy są różne")
        return lista3
    for i in range(len(liczby)):
        x = liczby[i] ** potęgi[i]
        lista3.append(x)
    return lista3
w = potęga([2,2,2,2],[1,2,3,])
print(w)


