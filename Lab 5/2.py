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

sample_dict = {"name": "Kelly","surname": "Jones","age": 25,"salary": 8000,"city": "New york"}
for k in sample_dict.keys():
    k



