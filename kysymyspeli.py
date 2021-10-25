# Tästä lähtee meidän superhieno kyssäripeli


def main():

    pisteet = 0
    aloitatko = str(input("Paina 'k' jos haluat aloittaa: "))

    if aloitatko == "k":
        while True:
            print("Vastaa k tai e, mikä tahansa muu lopettaa.")

            kysymys1 = input("Onko Thaikuissa kivaa (k/e): ")
            if kysymys1 == "k":
                print("Oikein!")
                pisteet += 1
            elif kysymys1 == "e":
                print("Väärin!")
            else:
                break

            kysymys2 = input("Onko C# parempi kuin Python (k/e): ")
            if kysymys2 == "e":
                print("Oikein!")
                pisteet += 1
            elif kysymys2 == "k":
                print("Väärin!")
            else:
                break

            kysymys3 = input("Onko GCP parasta ikinä (k/e): ")
            if kysymys3 == "k":
                print("Oikein!")
                pisteet += 1
            elif kysymys3 == "e":
                print("Väärin!")
            else:
                break

    print(f"Sait {pisteet} pistettä!")


if __name__ == "__main__":
    print("Tervetuloa kysymyspeliin!")

    main()

    print("Moikka!")