#x=int(input("Podaj liczbe całkowitą: "))

#for i in range(x):
 #   print("*"*x,end=" ")
  #  print()

from random import randint
#x = int(input("Podaj liczbe elementow: "))
#lista1 = []
#for i in range (x):
#    n = random.randint(1,10)
#    lista1.append(n)
#print(lista1)
#x1 = int(input("Podaj liczbe elementow dla drugiej listy: "))
#lista2 = []
#for i in range (x1):
#    n2 = random.randint(5,15)
#    lista2.append(n2)
#print(lista2)
#x3 = int(input("Podaj liczbe której szukasz: "))
#if x3 in lista1:
#    print("Liczba występuje w lista1")
#elif x3 in lista2:
#    print("Liczba występuje w lista2")
#else:
#    print("Nie ma takiej liczby w obu zestawach")

lista_zwierzęta=[]
l=int(input("Podaj liczbe zwierząt: "))
for i in range(l):
    x=input("Podaj nazwe zwierzęcia: ")
    lista_zwierzęta.append(x)


lista_zwierzęta.sort()
print(lista_zwierzęta)

print(lista_zwierzęta[1], lista_zwierzęta[-3:-1])
print(len.lista_zwierzęta)