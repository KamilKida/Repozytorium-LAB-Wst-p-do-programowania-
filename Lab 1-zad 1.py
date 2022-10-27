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
