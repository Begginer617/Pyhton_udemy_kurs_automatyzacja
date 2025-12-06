from dataclasses import replace
from operator import truediv

liczba1 = 1
liczba2 = 2.5
liczba3 = "wiesiek"
liczba4 = 'zdzisiek'
liczba5 = True
liczba6 = False

print(type(liczba1))
print(type(liczba2))
print(type(liczba3))
print(type(liczba4))
print(type(liczba5))
print(type(liczba6))

# wynik = liczba1 + liczba2 + liczba3 + liczba4 + liczba5 + liczba6


# taka operacja jest nie dozowolona, tylko na tym samym typie jest dozwolona
# print(liczba1.replace(1,3)) nie nizba zamienic 1 z wieskiem

print(liczba1 + liczba2)

# Python pozwala dodawać tylko typy,
# które mają zdefiniowaną wspólną operację + (np. liczby między sobą, stringi między sobą).
# Mieszanie typów jak int + str nie jest możliwe bez konwersji.

#konwersja strina na liczbe
wiek = 20
print("Mam " + str(wiek) + " lat")

# przy pomocy f-stringów:
wiek = 20
print(f"Mam {wiek} lat")

#konwersja liczby na string
liczba = 123
tekst = str(liczba)

print(tekst)        # "123"
print(type(tekst))  # <class 'str'>

ma_kota= True