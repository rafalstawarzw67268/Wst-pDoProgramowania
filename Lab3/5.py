"Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik). Wprowadzamy liczbę punktów dla każdego"
"studenta. Napisz program, który obliczy średnią liczbę punktów w grupie z wykorzystaniem pętli while."

n = int(input("Podaj liczbę studentów: "))
i = 1
suma = 0

while i < n + 1:
    punkty = float(input(f"Podaj liczbę punktów studenta {i}: "))
    suma = suma + punkty
    i = i + 1


średnia = suma / n
print("Średnia wynosi: ", średnia)









