import csv

datum = []
naam = []
score = []
temp = []

with open("gamers.csv", "r") as file:
    reader = csv.reader(file, delimiter=";")

    for x in reader:
        temp.append(x)

    for y in range(len(temp)):
        naam.append(temp[y][0])
        datum.append(temp[y][1])
        score.append(int(temp[y][2]))

        mx = max(score)
indx = score.index(mx)
print("De hoogste score is:", mx, "op", datum[indx], "behaald door", naam[indx])
