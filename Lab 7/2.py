"""Zadanie 2.
• Utwórz losową macierz o wymiarach 5x5. Znajdź największy i najmniejszy element. (patrz tab4_2d;
metoda max(), min())
• Wypisz największe elementy w każdym z wierszy (axis = 1) i w każdej z kolumn (axis = 0).
• Policz sumę wartości w poszczególnych wierszach."""

import numpy as np

macierz = np.random.randint(low=0, high = 25, size = (5,5))
print(macierz)
print()
print("Wartosc minimalna:", macierz.min())
print("Wartosc maksymalna:", macierz.max())

print("Wartosc minimalna wiersza: ", macierz.min(axis = 1))
print("Wartosc maksymalna wiersza: ", macierz.max(axis = 0))

print("Suma poszczegolnych wierszy wynosi: ", macierz.sum(axis = 1))