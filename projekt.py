from random import randint, choice
from os import system, path
from time import sleep

#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#

def has(var, list):
    for e in list:
        if e == var:
            return True
    return False

def valid_choice(var, list):
    while not has(var, list):
        var = input("Nincs ilyen opció!\nVálassz mást: ")
    return var

def combine(x):
    y = ""
    for e in x:
        y += e
    return y

def areusure(text):
    good = ["y", "n"]
    response = input(text[6])
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
    print(text[1])
    good = ["1", "2", "3", "4"]
    choice = input(text[2])
    return int(valid_choice(choice, good))

def fchoose2(text):
    file_choice = input(text[4])
    while not path.exists(file_choice) or file_choice == "text.txt":
        file_choice = input("Nem létezik ilyen fájl!\nKérlek válassz mást: ")
    else:
        print(f'Sikeresen kiválasztottad a "{file_choice}" fájlt!')
    return file_choice
        

def fchoose(text, choice):
    print(f"A(z) {choice}. módot választottad ki!")
    
    file = fchoose2(text)
    certain = areusure(text)
    while not certain:
        file = fchoose2(text)
        certain = areusure(text)

    sleep(0.5)
    system("cls")
    return file

def whichdata(text, file, x):
    good = []
    
    file.seek(0)
    line = file.readline()
    headers = line.split(";")
    print(text[7])
    for i in range(x, len(headers)):
        print(f"{i+1}. {headers[i]}")
        good.append(str(i+1))
    
    choice = input(text[2])
    return int(valid_choice(choice, good))

def wantexit(text, choice, fr):
    good = ["y", "n"]
    isexit = input(text[8])
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
        good = ["1","2","3","4","5","6","7"]
        modes = [mode1, mode2, mode3, mode4, mode5, mode6, mode7]
        tool_choice = int(valid_choice(choice2, good))
        modes[tool_choice-1](text, choice, fr)

    elif choice == 2:
        print("work in progress")
        
    else:
        print("work in progress")

def randomcolor(text):
    system("cls")
    print(text[9])
    colors = ["a","b","c","d","e","f"]
    for i in range(10):
        colors.append(str(i))
    mode_choice = input(text[2])
    good = ["1","2","3","q"]
    mode_choice = valid_choice(mode_choice, good)
    
    if mode_choice == "1":
        print(text[10])
        color_choice = input(text[11])
        color_choice = valid_choice(color_choice, colors)
        print(color_choice)
        system(f"color {color_choice}")
    elif mode_choice == "2":
        system("color 7")
    else:    
        system(f"color {choice(colors)}")

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
    datachoice = whichdata(text, fr, 1)
    data = []
    
    fr.seek(0)
    header = fr.readline().strip().split(";")
    line = fr.readline()
    while line != "":
        cut = line.split(";")
        data.append(float(cut[datachoice-1].strip()))
        line = fr.readline()
    
    maxi = 0
    for i in range(len(data)):
        if data[i] > data[maxi]:
           maxi = i

    print(f"A(z) {header[datachoice-1]} legnagyobb eleme: {data[maxi]}")
    wantexit(text, choice, fr)

def mode6(text, choice, fr):
    ...

def mode7(text, choice, fr):
    datachoice = whichdata(text, fr, 0)
    data = []
    names = []

    fr.seek(0)
    header = fr.readline().strip().split(";")
    line = fr.readline()
    while line != "":
        cut = line.split(";")
        data.append(cut[datachoice-1].strip())
        names.append(cut[0])
        line = fr.readline()
    
    ans = input("Keresés a következőre: ")
    i = 0
    n = len(data)
    while i < n and data[i] != ans:
        i += 1

    if i < n:
        print("Sikeres keresés!")
        if datachoice != 1:
            print("A hal neve: " + names[i])
    else:
        print("Sikertelen keresés!")
        print("Legközelebbi érték: ")

    
    wantexit(text, choice, fr)

def main():
    text_list = []
    load_text(text_list)


    system("cls")
    print(text_list[0]) 
    sleep(2)

    pick = start_choice(text_list)

    while not pick != 4:
        randomcolor(text_list)
        pick = start_choice(text_list)
    else:
        f = open(fchoose(text_list, pick), mode="a+", encoding="UTF-8")
        modes(text_list, pick, f)
    
    f.close()

main()