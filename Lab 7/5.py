"""Zadanie 5. Stwórz wykres funkcji sin w przedziale od −π do π z krokiem 0.1 Na tym samym wykresie umieść
wykresy funkcji:
𝑓(𝑥) = 2 ∗ sin(𝑥)
𝑓(𝑥) = 2 + sin (𝑥)
𝑓(𝑥) = sin (2 ∗ 𝑥)"""

import  numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,2*np.pi, 100)

plt.plot(x, np.sin(x))
plt.plot(x, 2*np.sin(x))
plt.plot(x, 2+np.sin(x))
plt.plot(x, np.sin(2/x))
plt.show()