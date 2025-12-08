# PĘTLE
# Skrypt będzie prosił o podanie wieku
# do momentu aż podam stringa, którego
# można przerobić na inta

while True:
    wiek = input("Podaj wiek: ")
    # Obsługa wyjątków
    # Spróbuj wykonać:
    try:
        # (Zakładam, że to się może nie powieść)
        wiek_int = int(wiek)
        if wiek_int >= 120:
            raise SystemError()
        elif wiek_int < 1:
            raise SystemError()
        break
    except ValueError:
        print("Podaj właściwy wiek")
        continue
    except SystemError:
        print("Wartość wieku jest zbyt mała lub zbyt duża")
    except:
        print("Inny błąd")
    finally:
        # Zawsze się wykonuje
        print("Skończonu obsługę błędów")


