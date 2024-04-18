from random import randint, choice
from os import system, path
from time import sleep

#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#

def has(var, list): # Saját "in"
    for e in list:
        if e == var:
            return True
    return False

def valid_choice(var, list):
    while not has(var, list):
        var = input("Nincs ilyen opció!\nVálassz mást: ")
    return var

def combine(x): # Saját ''.join 
    y = ""
    for e in x:
        y += e
    return y

def areusure(text): # "y" vagy "n" bemenet, ha y akkor visszatér Igazzal ha nem akkor Hamissal
    good = ["y", "n"]
    response = input(text[6])
    response = valid_choice(response, good)

    if response == "y":
        return True
    else:
        return False

def load_text(x): # Betölti a szöveget amit használunk a text.txt állományból
    fr = open("text.txt", "r", encoding="UTF-8")
    line = fr.readline()
    current = []
    while line != "":
        if line == "---\n":
            x.append(combine(current).rstrip("\n")) # rstrip --> RIGHT strip, leszedi a szöveg jobb oldaláról (végéről) a whitespacet
            current = [] # Van "---\"? --> Szövegblokk kiürítése
        else:
            current.append(line) # Szövegblokkhoz hozzátenni a sorokat amíg nincs "---\n"
        line = fr.readline()
    x.append(combine(current).rstrip("\n")) # Hozzáteszi az utolsó szövegblokkot egy listához és innen késöbb tudunk rá hivatkozni
    fr.close()
    return x

def conditional_round(x, db, header, choice, tool): # Kerekítés ha a felhasználó kéri
    good = ["y", "n"]
    isrounded = input("Szeretnél kerekíteni kiírás előtt? (y/n): ")
    isrounded = valid_choice(isrounded, good)
    
    texts = ["összege", "átlaga", "minimumja", "maximumja"] # A módok szövegei
    for i in range(len(texts)):
        if tool == i:
            text = texts[i]

    if isrounded == "y": # Ha kerekítés
        dot = 0
        if x != int(x):
            for i in range(len(str(x/db))): # Megkeresi hol van a számban a tizedespont
                if str(x/db)[i] == ".":
                    dot = i
            db2 = -1
            for i in range(dot, len(str(x/db))): # Megnézi hogy hány tizedesjegy van a tizedespont után
                db2 += 1
        else:
            db2 = 0 # Ha a szám az Int típusú akkor a 0. tizedesjegyig lehet kerekíteni
        
            
        print(f"\nEnnél a számnál maximum a(z) {db2}. tizedesjegyig lehet kerekíteni!")
        point = int(input("Kerekítés pontossága (tizedesjegyek száma): "))
        while point > db2 or point < 0: # Felhasználói felület biztosítása, ne lehessen 0-nál kisebb, vagy a tizedesjegy számánál nagyobb
            print(f"\nEnnél a számnál maximum a(z) {db2}. tizedesjegyig lehet kerekíteni!")
            point = int(input("Kerekítés pontossága (tizedesjegyek száma): "))


        if point != 0: # Ez azért kell mert 38.5 int --> 38, de 38.5 int+round --> 39
            print(f"A(z) {header[choice-1]} elemek {text} kerekítve {point} tizedesjegy pontosságra: {round(x/db, point)}")
        else:
            print(f"A(z) {header[choice-1]} elemek {text} kerekítve {point} tizedesjegy pontosságra: {int(round(x/db))}")
    else:    
        if x != int(x):
            print(f"A(z) {header[choice-1]} elemek {text} kerekítés nélkül: {x/db}")
        else:
            print(f"A(z) {header[choice-1]} elemek {text} kerekítés nélkül: {int(x/db)}")

#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#

def start_choice(text): # ASCII art és mód kiválasztása
    system("cls")
    print(text[1])
    good = ["1", "2", "3", "4"]
    choice = input(text[2])
    return int(valid_choice(choice, good))

def fchoose2(text): # Fájl kiválasztása
    file_choice = input(text[4])
    while not path.exists(file_choice) or file_choice == "text.txt": # path.exists(fájl) --> Ha létezik a fájl akkor True, ha nem akkor False
        file_choice = input("Nem létezik ilyen fájl!\nKérlek válassz mást: ")
    else:
        print(f'Sikeresen kiválasztottad a "{file_choice}" fájlt!')
    return file_choice
        

def fchoose(text, choice):
    print(f"A(z) {choice}. módot választottad ki!")
    
    file = fchoose2(text) # Fájl kiválasztása
    certain = areusure(text) # Biztos ezt a fájlt?
    while not certain: # Amíg nem biztos addig...
        file = fchoose2(text)
        certain = areusure(text)

    sleep(0.5)
    system("cls")
    return file

def whichdata(text, file, x): # Ez arra szolgál hogy amíg ugyanabban a formában van megadva az adat, mindig jó legyen a program
    good = []
    
    file.seek(0)
    line = file.readline()
    headers = line.split(";")
    print(text[7])
    for i in range(x, len(headers)): # x változó --> Melyik adatokat használhatja a felhasználó
        print(f"{i+1}. {headers[i]}") # Tudatja a felhasználóval az elérhető adatokat
        good.append(str(i+1)) # Szám hozzáadása a "jók" listához
    
    choice = input(text[2])
    return int(valid_choice(choice, good)) # Amíg a választott szám nincs benne a "jók" listában a felhasználó NEM léphet tovább

def wantexit(text, choice, fr): # Ki akar-e lépni a felhaszáló? függvény
    good = ["y", "n"] # "jók" lista
    isexit = input(text[8]) # választás
    isexit = valid_choice(isexit, good) # választás benne a "jók" listában?

    if isexit == "y":
        print("\nKilépés...")
        exit()
    else:
        sleep(0.25)
        system("cls")
        modes(text, choice, fr)

def modes(text, choice, fr): # Eszközök kiválasztása
    if choice == 1: # Első mód
        print(text[5])
        choice2 = input(text[2])
        good = ["1","2","3","4","5","6","7", "q"]
        modes = [mode1, mode2, mode3, mode4, mode5, mode6, mode7]
        tool_choice = valid_choice(choice2, good)
        
        if tool_choice == "q": # Visszalépés biztosítása a felhasználó számára
            system("cls")
            procedure(text) # Gyakorlatilag újraindítja a programot a 2 másodperces ASCII art nélkül
        else:
            modes[int(tool_choice)-1](text, choice, fr)

    elif choice == 2: # Második mód
        print("work in progress")
        
    else: # Harmadik mód
        print("work in progress")

def randomcolor(text): # Negyedik mód
    system("cls")
    print(text[9])
    colors = ["a","b","c","d","e","f"] # cmd --> "color help"
    for i in range(10):
        colors.append(str(i))
    mode_choice = input(text[2])
    good = ["1","2","3","q"]
    mode_choice = valid_choice(mode_choice, good)
    
    if mode_choice == "1": # Manuálisan megadva
        print(text[10])
        color_choice = input(text[11])
        color_choice = valid_choice(color_choice, colors)
        system(f"color {color_choice}")
        randomcolor(text)
    elif mode_choice == "2": # Alapértelmezett szín
        system("color 7")
        randomcolor(text)
    elif mode_choice == "3": # Choice --> Random kiválasztás listából
        system(f"color {choice(colors)}")
        randomcolor(text)
    else:    
        None

def minimum_or_maximum(l, isMax=False, minindex=0):
    m = minindex
    for i in range(minindex, len(l)):
        if (l[i] < l[m] and not isMax) or (l[i] > l[m] and isMax):
           m = i
    return m

def data_read(datachoice, fr): # Adatok beolvasása az adattömbből majd eltárolása & különböző műveletek végrehajtása
    db, x = 0, 0
    data, output, names = [], [], []

    fr.seek(0)
    header = fr.readline().strip().split(";")
    line = fr.readline().strip()
    while line != "":
        db += 1
        cut = line.split(";")
        names.append(cut[0])
        x += float(cut[datachoice-1])
        data.append(float(cut[datachoice-1].strip()))
        line = fr.readline().strip()
    
    stuff = [x, db, header, data, names]
    for i in range(len(stuff)):
        output.append(stuff[i])
    return output

def mode1(text, choice, fr): # Megszámolás
    datachoice = 2 # Ez lehet probléma lesz a jövőben
    output = data_read(datachoice, fr)
    print(f"Az adattömböd összesen {output[1]}db rekordot tartalmaz!\n")
    wantexit(text, choice, fr)

def mode2(text, choice, fr): # Összegzés
    tool = 0 # Erre hivatkozunk a kerekítés függvénynél hogy a módhoz kapcsolódó szöveget írja ki
    datachoice = whichdata(text, fr, 1)
    output = data_read(datachoice, fr)
    
    conditional_round(output[0], 1, output[2], datachoice, tool)
    wantexit(text, choice, fr)


def mode3(text, choice, fr): # Átlag
    tool = 1
    datachoice = whichdata(text, fr, 1)
    output = data_read(datachoice, fr)
    
    conditional_round(output[0], output[1], output[2], datachoice, tool)
    wantexit(text, choice, fr)

def mode4(text, choice, fr): # Minimum
    tool = 2
    datachoice = whichdata(text, fr, 1)
    output = data_read(datachoice, fr)
    
    mini = minimum_or_maximum(output[3])

    conditional_round(output[3][mini], 1, output[2], datachoice, tool)
    wantexit(text, choice, fr)

def mode5(text, choice, fr): # Maximum
    tool = 3
    datachoice = whichdata(text, fr, 1)
    output = data_read(datachoice, fr)
    
    maxi = minimum_or_maximum(output[3], True)

    conditional_round(output[3][maxi], 1, output[2], datachoice, tool)
    wantexit(text, choice, fr)

def insertion_sort(l, ascending=False): # Minimum/maximum kiválasztásos rendezés
    y = []
    for e in l:
        y.append(e)

    for i in range(len(y)):
        j = minimum_or_maximum(y, ascending, i)
        if y[i] != y[j]:
            y[i], y[j] = y[j], y[i]
    return y

def mode6(text, choice, fr): # Rendezés
    datachoice = whichdata(text, fr, 0)
    data = []
    names = []

    fr.seek(0)
    header = fr.readline().strip().split(";")
    line = fr.readline()
    while line != "":
        cut = line.split(";")
        if datachoice != 1:
            data.append(float(cut[datachoice-1].strip()))
        else:
            data.append(cut[datachoice-1].strip())
        names.append(cut[0].strip())
        line = fr.readline()

    print(*insertion_sort(data, bool(input())))

def mode7(text, choice, fr): # Keresés
    datachoice = whichdata(text, fr, 0)
    output = data_read(datachoice, fr)
    
    
    ans = float(input("Keresés a következőre: "))

    i = 0
    while i < len(output[3]) and output[3][i] != ans:
        i += 1

    if i < len(output[3]):
        print("Sikeres keresés!")
        if datachoice != 1:
            print("A hal neve: " + output[4][i])
    else:
        print("Sikertelen keresés!")
        print("Legközelebbi érték: ") # Ez majd be lesz fejezve valamikor

    
    wantexit(text, choice, fr)

def procedure(text_list): # Ez azért van itt külön mert a visszalépés gomb ezt hívja meg... tiszta kód? Nem.
    pick = start_choice(text_list)
    
    while not pick != 4:
        randomcolor(text_list)
        pick = start_choice(text_list)
    else:
        f = open(fchoose(text_list, pick), mode="a+", encoding="UTF-8")
        modes(text_list, pick, f)

    f.close()
    
def main():
    text_list = []
    load_text(text_list)

    system("cls")
    print(text_list[0]) 
    sleep(2)

    procedure(text_list)

main()