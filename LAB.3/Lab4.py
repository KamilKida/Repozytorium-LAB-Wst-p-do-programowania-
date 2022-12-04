##Zadanie 1.
#• Utwórz listę values zawierającą liczby 10, 20, 30. Utwórz drugą listę keys zawierającą nazwy tych liczb w
#języku angielskim (lub polskim). Dokonaj konwersji tych list w słownik.
#Wskazówki:
#− użyj funkcji zip(), która pobiera dwie sekwencje (takie jak list, dict, str), łączy je w krotki (pary) i
#zwraca;
#− lub wykonaj iterację listy za pomocą pętli for i funkcji range(). W każdej iteracji dodaj nową parę kluczwartość do słownika.
#• Utwórz drugi słownik metodą słów kluczowych ( dict(klucz1=wartość1, klucz2=wartość2)), gdzie kluczem
#będą nazwy liczb 30, 40, 50, a wartościami – liczby 30, 40, 50.
#• Połącz dwa słowniki w jeden nowy słownik.


value=[10,20,30]
keys= ["ten", "twenty", "thirty"]

#d=dict(zip(value,keys))
#print(d)


#D1= {}
#for i in range(len(keys)):
#    D1[keys[i]]=value[i]

#print(D1)


D1=dict(thirty=30, forty=40, fifty = 50)
print("D1= ",D1)

D2={keys[i]: value[i] for i in range(len(keys))}
print("D2= ",D2)
D3 = D2.copy()
D3.update(D1)

print("D3= ",D3)
