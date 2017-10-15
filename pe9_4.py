import csv

with open("artikel.csv", "r") as file:
    reader = csv.reader(file, delimiter=";")
    next(file)
    prijs = []
    naam = []

    nummer = []
    voorraad = []

    for rij in reader:
        prijs.append(float(rij[4]))
        naam.append(rij[2])
        nummer.append(int(rij[0]))
        voorraad.append(int(rij[3]))

    mx_naam = naam[prijs.index(max(prijs))]
    mn_nummer = nummer[voorraad.index(min(voorraad))]
    totaal = sum(voorraad)

    print("Het duurste artikel is", mx_naam, "en die kost {:.2f} Euro".format(max(prijs)))
    print("Er zijn slechts", min(voorraad), "exemplaren in voorraad van het product met nummer", mn_nummer)
    print("In totaal hebben wij", totaal, "producten in ons magazijn liggen")
