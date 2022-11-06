print("Zadanie 1 (1.py) Napisz skrypt, który pobiera długości boków prostokąta, a następnie oblicza jego pole i obwód oraz wyświetla wyniki na ekranie.")

print(" ")

x=float(input("Podaj długość pierwszego boku: "))
print(" ")
y=float(input("Podaj długość drugiego boku: "))

obw=2*x+2*y
pol=x*y
print(" ")

print(str("Zadanie 1_1 (1.py) Wykorzystaj f-stringi do wyświetlenia wyników (pole i obwód) z zadania 1."))
print(" ")


print(f"Pole wynosi: {pol}")
print(" ")

print(f"Obwód wynosi: {obw}")
print(" ")
print(" ")

print("Zadanie 2 (2.py) Napisz skrypt, który pobiera od użytkownika drogę pokonaną przez samochód oraz średnie"
"spalanie (w litrach na 100 km) i wyświetli informację o przewidywanym zużyciu paliwa oraz o szacowanych"
"kosztach podróży (cena paliwa 6.5 zł/l).")




print("Podaj dane: ")
print(" ")
x=float(input("Droga pokonana przez samochud (w KM): "))
y=float(input("Podaj średnie spalanie samochodu (w L): "))
print(" ")
z_pal=(y/x)*100
c_pal=y*6.5
print(" ")
print(f"Przewidywane zużycie paliwa (na 100km) wynosi: {z_pal} L")
print(f"Szacowana cena paliw a (przy cenie 6,50zł/L) wynosi {c_pal} zł.")

print("Zadanie 2_2 (2.py) Zmodyfikuj skrypt tak, aby długość przejechanej drogi była generowana losowo (liczba"
      "całkowita z zakresu <1, 1000>.")

from random import randint

x = randint(1, 100)

print("Podaj dane: ")
print(" ")

y = float(input("Podaj średnie spalanie samochodu (w L): "))
print(" ")
z_pal = (y / x) * 100
c_pal = y * 6.5
print(" ")
print(f"Przewidywane zużycie paliwa (na 100km) wynosi: {z_pal} L")
print(f"Szacowana cena paliw a (przy cenie 6,50zł/L) wynosi {c_pal} zł.")

print(" ")
print(" ")
print("Zadanie 3 (3.py):"
"• Dla osób poniżej 4 roku życia wstęp jest bezpłatny."
"• Dla osób w wieku od 4 do 18 lat bilet kosztuje 10zł."
"• Dla osób powyżej 18 roku życia bilet kosztuje 20zł."
"Przykład: Wprowadź wiek klienta: 5"
"Cena biletu: 10zł")

print(" ")

x=int(input("Ile masz lat?:"))

if x<=4:
    print("Wstęp jest bezpłatny")
elif 4<x<18:
    print("Bilet kosztuje 10 zł")
else:
    print("Bilet kosztuje 20 zł")


print(" ")
print(" ")
print("Zadanie 4 (4.py) Napisz skrypt, który sprawdzi czy litera wprowadzona przez użytkownika jest duża czy mała.")

im = str(input("Podaj litere: "))

if im.isalpha():
    if im.isupper():
            print("Ta litera jest duza ")
    else:
            print("Ta litera jest mała")
else:
        print("To nie jest litera")
print(" ")
print(" ")
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


