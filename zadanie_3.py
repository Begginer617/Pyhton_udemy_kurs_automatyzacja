#POPRAW
wiek =int(input("podaj wiek:"))
if wiek >= 18:
    print("luzik")
elif wiek < 18:
    print("masz lipe")
else:
    pass

#ctrl + /  zaznacznie kilka linijek jako komentarz

#DOBRE ROZWIAZANIE
wiek = int(input("Podaj wiek: "))
if wiek >= 18:
    print("Możesz kupić energola")
    print("Zapraszam")
elif wiek < 18:
    print("Spadaj do lekcji!")
else:
    pass