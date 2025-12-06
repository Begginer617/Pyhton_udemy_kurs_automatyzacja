def cwiczenie():  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMEJ GÓRZE

    imie = "Wojtek"
    stanowisko = "programista"
    pensja = 12345

    # KONKATENACJA - TU ROZPOCZNIJ KODOWAĆ
    tekst1 = ("Pan " + imie + " pracuje w dużej firmie informatycznej na stanowisku " + stanowisko + " i zarabia "
    + str(pensja) + " zł")
    print(tekst1)
    # F-STRING - TU ROZPOCZNIJ KODOWAĆ
    tekst2 = f"Pan {imie} pracuje w dużej firmie informatycznej na stanowisku {stanowisko} i zarabia {pensja} zł"
    print(tekst2)
    tekst3 = f"Pan {imie} robi dobry szmal, bo zarbia jako {stanowisko} i ma co miesiac {pensja} zł"
    print(tekst3)
    return (tekst1, tekst2, tekst3)  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMYM DOLE


def cwiczenie():  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMEJ GÓRZE

    # TU ROZPOCZNIJ KODOWAĆ
    dzien = 15
    miesiac = "czerwca"
    rok = 1950

    # KONKATENACJA
    tekst1 = "Dzisiaj mamy " + str(dzien) + " " + miesiac + " "+ str(rok) + " r."
    print(tekst1)
    # F-STRING
    tekst2 = f"Dzisiaj mamy {dzien} {miesiac} {rok} r."
    print(tekst2)

    return (tekst1, tekst2)  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMYM DOLE