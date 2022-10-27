"Zadanie 4 (4.py) Zmodyfikuj program z zad. 1 tak, aby przechodząc po kolejnych liczbach przedziału, wypisywać"
"tylko liczby parzyste, a nieparzyste – pomijać. Użyj instrukcji continue."


x = int(input("Pierwszą liczbę: "))
y = int(input("Drugą liczbę: "))
if x > y:
    x,y = y,x

while x <= y:
    if x%2 == 1:
        x = x + 1
        continue
    print(x)
    x += 1




