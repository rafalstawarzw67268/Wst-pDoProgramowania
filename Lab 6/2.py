"""Zadanie 2. Napisz funkcje oblicz(), która ma dwa parametry i oblicza ich sumę oraz różnicę. Ponadto zwraca
jednocześnie jak wynik dodawania, tak i odejmowania.
"""

def oblicz(x,y):
    roz = x-y
    sum = x+y
    print(f"Suma: {sum}  Różnica: {roz}")

    a = int(input("Podaj x:"))
    b = int(input("Podaj y:"))

