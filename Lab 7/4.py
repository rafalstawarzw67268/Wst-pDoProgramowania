"""Zadanie 4. Utwórz macierz o wymiarach 5x5 wypełnioną początkowo zerami. Na każdym brzegu macierzy
ustaw jedynki (góra, dół, lewo, prawo). Napisz funkcję zamieniającą zera na jedynki i odwrotnie.
"""
import  numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,2*np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.plot(x, np.cos(x))
plt.show()