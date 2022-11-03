"""Zadanie 8 (8.py) Napisz skrypt, który wyświetli gwiazdki jak poniżej. Liczba wierszy (lub gwiazdek w linii)
powinna być podawana przez użytkownika.
Przykład: 3
* * *
* * *
* * *"""

x = int(input("Liczba wierszy:"))
y = int(input("Liczba wierszy 2:"))

w = "*"

for v in range(x):

 for z in range(x):
    print(w, end = " ")
 print(" ")


