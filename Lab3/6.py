""" Zadanie 6 (6.py):Zastosuj instrukcje continue w programie z zad. 5 tak, aby po podaniu liczby punktów spoza
przedziału 0 – 100 pomijać dalsze wykonywanie pętli. Sprawdź działanie programu. Następnie zmień pętlę na
nieskończoną, czyli taką której warunek zawsze jest prawdziwy. Zakończ działanie pętli przy użyciu instrukcji
break"""


n = int(input("Proszę podać liczbę studentów: "))
a = 1  # wyświetlanie od 1 studenta
suma = 0  # podstawienie pod dodawanie punktów
while True:
    b = int(input(f"Proszę podać punkty studenta {a}: "))
    if b<0 or b>100:
        continue
    suma += b  # sumowanie punktów studentów
    a += 1  # przechodzenie do kolejnego studenta
    if a>n:
        break
y = suma / n  # obliczanie średniej
print("Średnia wszystkich studentów", round(y, 2))
