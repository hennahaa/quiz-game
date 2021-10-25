kysymykset =[
"Mistä gcp on lyhenne? \nA: Google Computing Platform \nB: Google Cloud Platform \nC: Google Customer Platform",
"Mistä tietää millä käyttäjällä operoit? \nA: whoami \nB: whereami \nC: whenami",
"Mikä näistä virtuaalikonetyypeistä soveltuu parhaiten intensiivisiin prosessointitöihin? \nA: M2 \nB: E2 \nC: C2"
]
maksimi_pisteet = len(kysymykset)
#tulostaa ohjeet kysymyspelin pelaamiseen
def ohje():
    print("Ohjelmassa voit valita joko 0 tai 1, 0 lopettaa pelin ja 1 jatkaa peliä.")

def pelaa():
    i = 0
    pisteet = 0
    for kysymys in kysymykset:
        try:
            vastaus = str(input(f"\n{kysymys}\n>"))
        except ValueError:
            print("Virheellinen komento")
        if i == 0:
            if vastaus.lower() == "b":
                print("Oikein! Sait yhden pisteen")
                pisteet += 1
            else:
                print("Väärin!")
        elif i == 1:
            if vastaus.lower() == "a":
                print("Oikein! Sait yhden pisteen")
                pisteet += 1
            else:
                print("Väärin!")
        elif i == 2:
            if vastaus.lower() == "c":
                print("Oikein! Sait yhden pisteen")
                pisteet += 1
            else:
                print("Väärin!")
        i += 1
    print(f"Sait {pisteet}/{maksimi_pisteet} pistettä!")

#while-loop joka kutsuu kysymyksentulostusta, käsittelee pelaajan syötteen
#1 pelaa 0 lopeta
def suorita():
    ohje()
    while True:
        print()
        kysymys = int(input("Oletko valmis pelaamaan? 1 = Pelaa, 0 = Lopeta "))
        if kysymys == 1:
            pelaa()
        elif kysymys == 0:
            break
        else:
            ohje()

suorita()

print("Kiitos pelaamisesta!")
