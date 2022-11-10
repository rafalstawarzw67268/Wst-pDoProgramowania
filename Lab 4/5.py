"""Zadanie 5. Utwórz listę punkty będącą listą punktów zdobytych z pewnego egzaminu przez grupę 15 studentów.
Punkty niech będą liczbami rzeczywistymi z przedziału [0; 50]. Następnie
• Wyświetl informację o największej i najmniejszej ilości zdobytych punktów
• Wyświetl indeks pierwszego wystąpienia punktów podanych przez użytkownika. Jeżeli taka liczba
punktów nie występuje na liście, wyświetl odpowiedni komunikat
• Oblicz średnią punktów liczbę punktów z egzaminu
• Oblicz, ile osób zdobyło punkty powyżej, a ile poniżej średniej
• Wyświetl punkty poniżej średniej
• Wyświetl punkty powyżej średniej"""

import random
#punkty=[]
#for a in range(15):
    #p = random.uniform(0, 50)
    #p=round(p,2)
    #punkty.append(p)
punkty=[round(random.uniform(0,50),2) for a in range(15)]
print(punkty)
print(f'Wartość minimalna wynosi: {min(punkty)}')
print(f'Wartość maksymalna wynosi: {max(punkty)}')
a = input("Podaj indeks wybranej liczby: ")
if a in punkty:
    print(punkty.index(a))
else:
    print("Liczba nie występuje na liście")

średnia = sum(punkty)/15
print(f"Średnia wynosi {round(średnia,3)}")
powyzej=[]
for s in punkty:
    if s>średnia:
        powyzej.append(s)
print(powyzej,len(powyzej))

ponizej=[s for s in punkty if s < średnia]
print(ponizej,len(ponizej))






