"""Zadanie 5. Napisz program działający jak prosty kalkulator. W tym celu utwórz funkcje dodawanie(),
odejmowanie(), mnożenie() oraz dzielenie(). Następnie utwórz słownik, którego kluczem jest działanie, a
wartością – nazwa odpowiedniej funkcji.
Uwaga: funkcja jest obiektem, a nazwa funkcji – nazwą (referencją) tego obiektu.
"""

def dodawanie(a,b):
    suma = a + b
    return suma

def odejmowanie(a,b):
    różnica = a - b
    return różnica

def mnożenie(a,b):
    iloczyn = a * b
    return iloczyn

def dzielenie(a,b):
    if b !=0:
        return a / b
    else:
        print("Dzielenie przez 0!")

dic = {'+':dodawanie, '-':odejmowanie, '*':mnożenie, '/':dzielenie}

x=int(input("Podaj liczbe 1: "))
y=int(input("Podaj liczbe 2: "))
z=input("Podaj działanie: ")

dic[z](x,y)
print(dic[z](x,y))