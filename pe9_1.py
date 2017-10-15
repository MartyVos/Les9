prijs = 4356.0

try:
    pers = int(input("Hoeveel personen gaan er mee op reis? "))
    pp = prijs / pers
    print("De prijs per persoon is €" + str(format(pp, ".2f")))
except ValueError:
    print("Gebruik cijfers voor het invoeren van het aantal!")
except ZeroDivisionError:
    print("Delen door nul kan niet!")
except:
    print("Onjuiste invoer!")