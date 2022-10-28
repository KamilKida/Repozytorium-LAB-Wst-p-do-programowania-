print("Zadanie 5 (5.py) Napisz program działający jak prosty kalkulator, który potrafi dodawać, odejmować,"
"mnożyć, dzielić oraz obliczać potęgę."
"Przykład: Jaką operację chcesz wykonać?"
"1) dodawanie"
"2) odejmowanie"
"3) mnożenie"
"4) dzielenie"
"5) potęgowanie"
"Wpisz numer operacji: 2"
"Podaj argument 1: 34"
"Podaj argument 2: 5"
"Wynik: 29")

print("Podaj dwie liczby: ")
print(" ")
x=float(input("Pierwsza 1 liczba: "))
y=float(input("Podaj 2 liczbe: "))

print("JAKOM OPERACJE CHCESZ WYKONAĆ?")
print("1) dodawanie")
print("2) odejmowanie")
print("3) mnożenie")
print("4) dzielenie")
print("5) potęgowanie")
wyb=int(input("WYBÓR:"))
print(" ")
if wyb == 1:
   print(float(x+y))
elif wyb==2:
    print(float(x-y))
elif wyb==3:
    print(float(x*y))
elif wyb==4:
    print(float(x/y))
elif wyb==5:
    print(float(x**y))
else:
    print("NIE MA TAKIE OPCJI")

