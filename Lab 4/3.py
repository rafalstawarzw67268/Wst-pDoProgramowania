"""Zadanie 3. Utwórz pustą listę zwierzeta. Następnie
• Dodaj kilka nazw zwierząt do listy
• Posortuj listę
• Wyświetl pierwszy oraz trzy ostatnie elementy na liście
• Wyświetl informację o liczbie zwierząt na liście"""

zwierzęta = []
x = 5
for i in range (x):
    a = input("podaj nazwę zwierzęcia: ")
    zwierzęta.append(a)

zwierzęta.sort()

print(zwierzęta[0])
print(zwierzęta[-3:])
print(len(zwierzęta))






