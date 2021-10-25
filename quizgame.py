#This is the amazing quiz game made by Elina and Miia (and Tiina)

kysymys1 = "Mikä on maailman pienin valtio?\n"
kysymys2 = "Mikä on maailman pisin joki?\n"
kysymys3 = "Kuinka monta raitaa Yhdysvaltain lipussa on?\n"
kysymykset = [kysymys1,kysymys2,kysymys3]
vastaukset = ["vatikaani", "niili", "13"]
oikein = 0
kysymys = 3
j = 0

start = input("Haluatko käynnistää pelin? Y/N: ")
if start == "Y"or start =="y":
    while True:
        for i in kysymykset:
            vastaus = input(kysymykset[j])
            if vastaus == vastaukset[j].lower():
                oikein +=1
                j+=1
            else:
                print("Nope.")
                j+=1                          
        print(f"Pisteet: {oikein}/3")
        break
elif start == "N" or start == "n":
    pass
    