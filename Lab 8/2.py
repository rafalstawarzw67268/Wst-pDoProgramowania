"""Zadanie 2. Napisz funkcję sum_of_values(), która policzy i zwróci sumę wartości (values) słownika:
dict1 = {'data1':10, 'data2':-4, 'data3':2}
Nie wolno korzystać z funkcji sum().
"""

dict1 = {'data1':10, 'data2':-4, 'data3':2}
dict2 = {'asfsaf':1, 'asfasfasdfgasd':-5, 'sdgdsjghdsjakajskghd':10000}
def sum_of_values(s1):
    j = 0
    for i in s1.values():
        j = j + i
    return(j)
b = sum_of_values(dict1)
c = sum_of_values(dict2)
print(b)
print(c)



