"Zadanie 1 (1.py) Napisz skrypt, który pobierze od użytkownika dwie liczby całkowite. Następnie zaczynając "
"od mniejszej liczby,wypisze kolejne liczby aż do osiągnięcia wartości drugiej (większej) liczby."

x = int(input("Pierwszą liczbę: "))
y = int(input("Drugą liczbę: "))
if x > y:
    x,y = y,x
while x < y:
    print(x)
    x += 1










