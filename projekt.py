from random import randint
from os import system
from time import sleep

#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#

def valid_choice(var, list):
    while var not in list:
        var = input("Nincs ilyen opció!\nVálassz mást: ")
    return var

def combine(x):
    y = ""
    for i in range(len(x)):
        y += x[i]
    return y

def areusure():
    good = ["y", "n"]
    response = input("Biztosan ezzel a választással szeretnéd folytatni? (y/n): ")
    response = valid_choice(response, good)

    if response == "y":
        return True
    else:
        return False

def load_text(x):
    fr = open("text.txt", "r", encoding="UTF-8")
    line = fr.readline()
    current = []
    while line != "":
        if line == "---\n":
            x.append(combine(current).rstrip("\n"))
            current = []
        else:
            current.append(line)
        line = fr.readline()
    x.append(combine(current).rstrip("\n"))
    fr.close()
    return x

def conditional_round(x, db, header, choice, tool):
    good = ["y", "n"]
    isrounded = input("Szeretnél kerekíteni kiírás előtt? (y/n): ")
    isrounded = valid_choice(isrounded, good)
    
    if tool != 1:
        text = "összege"
    else:
        text = "átlaga"


    if isrounded == "y":
        dot = 0
        if x != int(x):
            for i in range(len(str(x/db))):
                if str(x/db)[i] == ".":
                    dot = i
            db2 = -1
            for i in range(dot, len(str(x/db))):
                db2 += 1
        else:
            db2 = 0
        
            
        print(f"\nEnnél a számnál maximum a(z) {db2}. tizedesjegyig lehet kerekíteni!")
        point = int(input("Kerekítés pontossága (tizedesjegyek száma): "))
        while point > db2 or point < 0:
            print(f"\nEnnél a számnál maximum a(z) {db2}. tizedesjegyig lehet kerekíteni!")
            point = int(input("Kerekítés pontossága (tizedesjegyek száma): "))


        if point != 0:
            print(f"A(z) {header[choice-1]} elemek {text} kerekítve {point} tizedesjegy pontosságra: {round(x/db, point)}")
        else:
            print(f"A(z) {header[choice-1]} elemek {text} kerekítve {point} tizedesjegy pontosságra: {int(round(x/db))}")
    else:    
        if x != int(x):
            print(f"A(z) {header[choice-1]} elemek {text} kerekítés nélkül: {x/db}")
        else:
            print(f"A(z) {header[choice-1]} elemek {text} kerekítés nélkül: {int(x/db)}")

#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#

def start_choice(text):
    system("cls")
    print(text[0])
    sleep(2)
    system("cls")
    print(text[1])
    good = ["1", "2", "3"]
    choice = input(text[2])
    return int(valid_choice(choice, good))

def fchoose(text, choice):
    print(f"A(z) {choice}. módot választottad ki!")
    file_choice = input(text[4])
    print(f'Sikeresen kiválasztottad a "{file_choice}" fájlt!')
    certain = areusure()
    
    while not certain:
        file_choice = input(text[4])
        print(f'Sikeresen kiválasztottad a "{file_choice}" fájlt!')
        certain = areusure()
    sleep(0.5)
    system("cls")
    return file_choice

def whichdata(text, file, x):
    good = []
    
    file.seek(0)
    line = file.readline()
    headers = line.split(";")
    print("\nMelyik adattal szeretnél dolgozni?")
    for i in range(x, len(headers)):
        print(f"{i+1}. {headers[i]}")
        good.append(str(i+1))
    
    choice = input(text[2])
    return int(valid_choice(choice, good))

def wantexit(text, choice, fr):
    good = ["y", "n"]
    isexit = input("Ki szeretnél lépni a programból? (y/n): ")
    isexit = valid_choice(isexit, good)

    if isexit == "y":
        print("\nKilépés...")
        exit()
    else:
        sleep(0.25)
        system("cls")
        modes(text, choice, fr)

def modes(text, choice, fr):
    if choice == 1:
        print(text[5])
        choice2 = input(text[2])
        good = ["1","2","3","4","5","6"]
        tool_choice = int(valid_choice(choice2, good))
        if tool_choice == 1:
            mode1(text, choice, fr)
        elif tool_choice == 2:
            mode2(text, choice, fr)
        elif tool_choice == 3:
            mode3(text, choice, fr)
        elif tool_choice == 4:
            mode4(text, choice, fr)
        elif tool_choice == 5:
            mode5(text, choice, fr)
        else:
            mode6(text, choice, fr)

    elif choice == 2:
        print("work in progress")
        
    else:
        print("work in progress")

def mode1(text, choice, fr):
    db = 0
    
    fr.seek(0)
    header = fr.readline()
    line = fr.readline()
    while line != "":
        db += 1
        line = fr.readline()
    print(f"Az adattömböd összesen {db}db rekordot tartalmaz!\n")
    wantexit(text, choice, fr)

def mode2(text, choice, fr):
    tool = 0
    x = 0
    db = 1
    datachoice = whichdata(text, fr, 1)

    fr.seek(0)
    header = fr.readline().strip().split(";")
    line = fr.readline()
    while line != "":
        cut = line.split(";")
        x += float(cut[datachoice-1])
        line = fr.readline()
    
    conditional_round(x, db, header, datachoice, tool)
    wantexit(text, choice, fr)


def mode3(text, choice, fr):
    tool = 1
    x = 0
    db = 0
    datachoice = whichdata(text, fr, 1)

    fr.seek(0)
    header = fr.readline().strip().split(";")
    line = fr.readline()
    while line != "":
        db += 1
        cut = line.split(";")
        x += float(cut[datachoice-1])
        line = fr.readline()
    
    conditional_round(x, db, header, datachoice, tool)
    wantexit(text, choice, fr)

def mode4(text, choice, fr):
    datachoice = whichdata(text, fr, 1)
    data = []
    
    fr.seek(0)
    header = fr.readline().strip().split(";")
    line = fr.readline()
    while line != "":
        cut = line.split(";")
        data.append(cut[datachoice-1])
        line = fr.readline()
    
    mini = 0
    for i in range(len(data)):
        if data[i] < data[mini]:
           mini = i

    print(f"A(z) {header[datachoice-1]} legkisebb eleme: {data[i]}")
    wantexit(text, choice, fr)

def mode5(text, choice, fr):
    ...

def mode6(text, choice, fr):
    ...

def main():
    text_list = []
    load_text(text_list)

    pick = start_choice(text_list)    
    
    f = open(fchoose(text_list, pick), mode="a+", encoding="UTF-8")

    modes(text_list, pick, f)
    
    f.close()

main()