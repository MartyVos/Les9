import datetime
import csv

bestand = "inloggers.csv"

while 1:
    naam = input("Wat is je achternaam? ")
    if naam == "einde":
        break
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")

    datum = datetime.datetime.today()
    d = datum.strftime("%a %d %B %Y at %H:%M")

    with open(bestand, "a", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow((d, naam, voorl, gbdatum, email))
