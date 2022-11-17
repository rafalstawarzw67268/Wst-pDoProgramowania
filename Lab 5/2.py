"""Zadanie 2.
• Wypisz wszystkie pary klucz:wartość występujące w słowniku:
sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
• Utwórz słownik, wybierając ze słownika sample_dict pary o kluczach zapisanych w liście.
Wskazówki:
− przejdź za pomocą pętli po kluczach zapisanych w liście;
− następnie sprawdź, czy dany klucz występuje w słowniku; jeśli występuje, dodaj go (parę
klucz:wartość) do nowego słownika.
• Usuń ze słownika wartości, których klucze występują w liście.
• Sprawdź, czy wartość „Jones” występuje w słowniku.
• Zmień w słowniku klucz ‘city’ na ‘location’."""

sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
for k, v in sample_dict.items():
 print (f'{k:<10} = {v:>8}')
d2={}
l = ["name","age","city"]
for k in l:
    if k in sample_dict.keys():
        d2[k]=sample_dict[k]

d2={k:sample_dict[k] for k in l if k in sample_dict.keys()}
print(d2)

d3=sample_dict.copy()

for i in l:
    if i in d3:
        d3.pop(i)
print(d3)

if "Jones" in sample_dict.values():
    print("Wartość występuje")
else:
    print("Wartosc niewystepuje")

sample_dict["location"] = sample_dict["city"]
del sample_dict["city"]
print(sample_dict)



