def dodaj(a, b):
    print("Jestem w środku funkcji!")
    return a + b

wynik = dodaj(2, 3)
print("Wynik:", wynik)



def odejmij(c,d):
    print("jestem w srodku funkcji odejmij")
    return c-d

wynik = odejmij(4, 1)
print("Wynik:", wynik)



#bez return
def iloczyn(c,d):
    print("jestem w srodku funkcji iloczyn")
    #return c*d

    print(iloczyn())

#wynik = iloczyn(4, 1)
#print("Wynik:", wynik)


#Przykład, który idealnie pokazuje różnicę miedzy return a print
def pomnoz(a, b):
    #print() w środku funkcji — wyświetla 8
    print(a * b)
    #return — zwraca 8 do zmiennej x
    return a * b

#zmienna x korzysta z funkcji pomnoz
x = pomnoz(2, 4)
#ostatni print — wyświetla wartość zmiennej x
print("x to:", x)
