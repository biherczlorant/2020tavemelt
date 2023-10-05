data = []
with open("tavirathu13.txt", "r") as f:
    for sor in f:
        darab = sor.strip().split(" ")
        adat = {'telepules': darab[0],
                  'ora': darab[1][:2],
                  'perc': darab[1][2:],
                  'szelirany': darab[2][:3],
                  'szelerosseg': int(darab[2][3:]),
                  'homerseklet': int(darab[3])}
        data.append(adat)

# 2. feladat
print("2. feladat")
varos = input("Adja meg egy település kódját! Település:")
utolso = None
for i in data:
    if i["telepules"] == varos:
        utolso = i

try:
    print(f"Az utolsó mérési adat a megadott településről {utolso['ora']}:{utolso['perc']}-kor érkezett.")
except:
    print("Település")
# 3. feladat
print("3. feladat")
minhomer = data[0]
maxhomer = data[0]
for i in data:
    if i["homerseklet"] < minhomer["homerseklet"]:
        minhomer = i
    if i["homerseklet"] > maxhomer["homerseklet"]:
        maxhomer = i

print(
    f"A legalacsonyabb hőmérséklet: {minhomer['telepules']} {minhomer['ora']}:{minhomer['perc']} {minhomer['homerseklet']} fok.\nA legmagasabb hőmérséklet: {maxhomer['telepules']} {maxhomer['ora']}:{maxhomer['perc']} {maxhomer['homerseklet']} fok. ")
# 4. feladat
print("4. feladat")
seged = 0
for i in data:
    if i["szelerosseg"] == 0:
        print(f"{i['telepules']} {i['ora']}:{i['perc']}")
        seged += 1
if seged == 0:
    print("Nem volt szélcsend.")
# 5. feladat
print("5. feladat")
varosidojaras = None
telepulesek = set()
maxhomer = 0
minhomer = 0

for i in data:
    telepulesek.add(i["telepules"])
for varos in telepulesek:
    atlaghelp = 0
    varosidojaras = [i for i in data if i["telepules"] == varos]
    homer1 = [i for i in varosidojaras if i["ora"] == "01"]
    homer2 = [i for i in varosidojaras if i["ora"] == "07"]
    homer3 = [i for i in varosidojaras if i["ora"] == "13"]
    homer4 = [i for i in varosidojaras if i["ora"] == "19"]
    homer = [i for i in varosidojaras if homer1.__len__() > 0 and homer2.__len__() > 0 and homer3.__len__() > 0 and
             homer4.__len__() > 0 and (i["ora"] == "01" or i["ora"] == "07" or i["ora"] == "13" or i["ora"] == "19")]
    homersek = [i["homerseklet"] for i in varosidojaras]
    if homer.__len__() > 0:
        for i in range(0, homer.__len__()):
            atlaghelp += homer[i]["homerseklet"]
    maxhomer = max(homersek)
    minhomer = min(homersek)
    try:
        print(f"{varos} Középhőmérséklet: {(atlaghelp / homer.__len__()).__round__()}; Hőmérséklet-ingadozás: {maxhomer-minhomer}")
    except ZeroDivisionError:
        print(f"{varos} Középhőmérséklet: NA; Hőmérséklet-ingadozás: {maxhomer-minhomer}")
