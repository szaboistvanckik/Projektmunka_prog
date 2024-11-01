from random import randint, choice
from os import system, path
from time import sleep

#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#

def has(var, list): # Saját "in"
    for e in list:
        if e == var:
            return True
    return False

def valid_choice(var, list): # Ha nincs benne egy változó a jók listában akkor valami mást kell megadni
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

def conditional_round(x, db, header, choice, tool, text): # Kerekítés ha a felhasználó kéri
    good = ["y", "n"]
    isrounded = input("Szeretnél kerekíteni kiírás előtt? (y/n): ")
    isrounded = valid_choice(isrounded, good)
    
    texts = ["összege", "átlaga", "minimumja", "maximumja"] # A módok szövegei
    for i in range(len(texts)):
        if tool == i:
            text_r = texts[i]

    dot = 0
    if x % db != 0: 
        for i in range(len(str(x/db))): # Megkeresi hol van a számban a tizedespont
            if str(x/db)[i] == ".":
                dot = i
        db2 = -1
        for i in range(dot, len(str(x/db))): # Megnézi hogy hány tizedesjegy van a tizedespont után
            db2 += 1
    else:
        db2 = 0 # Ha a szám az Int típusú akkor a 0. tizedesjegyig lehet kerekíteni

    if isrounded == "y": # Ha kerekítés
        print(f"\nEnnél a számnál maximum a(z) {db2}. tizedesjegyig lehet kerekíteni!")
        point = input(text[15])
        while not is_number(point, int):
            point = input(text[16])
        point = int(point)

        while point > db2 or point < 0: # Felhasználói felület biztosítása, ne lehessen 0-nál kisebb, vagy a tizedesjegy számánál nagyobb
            print(f"\nEnnél a számnál maximum a(z) {db2}. tizedesjegyig lehet kerekíteni!")
            point = input(text[15])
            while not is_number(point, int):
                point = input(text[16])
            point = int(point)

        if point != 0: # Ez azért kell mert 38.5 int --> 38, de 38.5 int+round --> 39
            print(f"\nA(z) {header[choice-1]} elemek {text_r} kerekítve {point} tizedesjegy pontosságra: {round(x/db, point)}")
        else:
            print(f"\nA(z) {header[choice-1]} elemek {text_r} kerekítve {point} tizedesjegy pontosságra: {int(round(x/db))}")
    else:    
        if db2 != 0: # Nincs kerekítés + nem int
            print(f"\nA(z) {header[choice-1]} elemek {text_r} kerekítés nélkül: {x/db}")
        else:
            print(f"\nA(z) {header[choice-1]} elemek {text_r} kerekítés nélkül: {int(x/db)}")

#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#

def start_choice(text): # ASCII art és mód kiválasztása
    system("cls")
    print(text[1])
    good = ["1", "2", "3", "q"]
    choice = input(text[2])
    return valid_choice(choice, good)

def fchoose2(text): # Fájl kiválasztása
    file_choice = input(text[4])
    while not path.exists(file_choice) or file_choice == "text.txt" or file_choice == "ki.txt": # path.exists(fájl) --> Ha létezik a fájl akkor True, ha nem akkor False
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

def whichdata(text, filename, x): # Ez arra szolgál hogy amíg ugyanabban a formában van megadva az adat, mindig jó legyen a program
    fr = open(filename, "r", encoding="UTF-8")
    headers = fr.readline().strip().split(";")
    fr.close()
    
    good = []
    print(text[7])
    for i in range(x, len(headers)): # x változó --> Melyik adatokat használhatja a felhasználó
        print(f"{i+1}. {headers[i]}") # Tudatja a felhasználóval az elérhető adatokat
        good.append(str(i+1)) # Szám hozzáadása a "jók" listához
    
    choice = input(text[2])
    return int(valid_choice(choice, good)) # Amíg a választott szám nincs benne a "jók" listában a felhasználó NEM léphet tovább

def wantexit(text, choice, filename): # Ki akar-e lépni a felhaszáló? függvény
    good = ["y", "n"] # "jók" lista
    isexit = input(text[8]) # választás
    isexit = valid_choice(isexit, good) # választás benne a "jók" listában?

    if isexit == "y":
        print("\nKilépés...")
        exit()
    else:
        sleep(0.25)
        system("cls")
        modes(text, choice, filename)

def add_data(filename, text): # Hozzáfűzés
    system("cls")
    output = data_read(0, filename)
    print("Új rekord hozzáfűzése a fájlhoz:\n")

    newrecord = []
    for i in range(len(output[2])):
        ans = input(f'Add meg a(z) "{output[2][i]}" adatot: ') # Felhasználó sorban megad annyi adatot ahány fejléc van
        if i != 0:
            while not is_number(ans, float):
                ans = input(f'A(z) "{output[2][i]}" adat csak szám lehet!\nKérlek adj meg valami mást: ')
        else:
            while is_number(ans, float):
                ans = input(f'A(z) "{output[2][i]}" adat csak szöveg lehet!\nKérlek adj meg valami mást: ')
        newrecord.append(ans)
    
    fa = open(filename, "a", encoding="UTF-8")
    n = len(newrecord)
    fa.write("\n")
    for i in range(len(newrecord)):
        fa.write(newrecord[i])
        if i != n-1:
            fa.write(";")
    fa.close()

    print("\nSikeres hozzáfűzés!\n")
    certain = input("Szeretnél még adatot hozzáfűzni a fájlhoz? (y/n): ").lower() # .lower() : "DÁVID" --> "dávid"

    good = ["y", "n"]
    certain = valid_choice(certain, good)
    while not certain:
        certain = input(text[3])
    if certain == "y":
        add_data(filename, text) # Futtassa le a függvényt újra
    else:
        procedure(text) # Indítsa újra az egészet (tiszta kód)

def modes(text, choice, filename): # Eszközök kiválasztása
    if choice == "1": # Első mód
        print(text[5])
        choice2 = input(text[2])
        good = ["1","2","3","4","5","6","7","8","9","q"]
        modes = [mode1, mode2, mode3, mode4, mode5, mode6, mode7, mode8, mode9]
        tool_choice = valid_choice(choice2, good)
        
        if tool_choice == "q": # Visszalépés biztosítása a felhasználó számára
            system("cls")
            procedure(text) # Gyakorlatilag újraindítja a programot a 2 másodperces ASCII art nélkül
        else:
            modes[int(tool_choice)-1](text, choice, filename)

    else: # Második mód
        add_data(filename, text)

def randomcolor(text): # Harmadik mód
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
        procedure(text)

def minimum_or_maximum(l, isMax=False, minindex=0):
    m = minindex
    for i in range(minindex, len(l)):
        actual = l[i]
        actual_m = l[m]
        if isinstance(l[i], str):
            actual = actual.lower()
            actual_m = actual_m.lower()

        if (actual < actual_m and not isMax) or (actual > actual_m and isMax):
           m = i
    return m

def cons_or_file(text, output, current): # Konzolra vagy fájlba szeretné kiíratni a felhasználó az adatokat
    good = ["1", "2"]
    chc = input(text[13])
    chc = valid_choice(chc, good)
    while not chc:
        chc = input(text[3])
        
    if chc == "2":
        fw = open("ki.txt", "w", encoding="UTF-8")
        for i in range(len(output[2])):
            if i == 0:
                fw.write(f"{output[2][i]}")
            else:
                fw.write(f";{output[2][i]}")
        fw.write("\n")
        for i in range(len(current)):
            for j in range(len(output[5][i])):
                if j == 0:
                    fw.write(f"{output[5][current[i]][j]}")
                else:
                    fw.write(f";{output[5][current[i]][j]}")
            fw.write("\n")
        fw.close()
        print('\nSikeres írás!\nNézd meg a "ki.txt" fájlt!\n')
        return True
    else:
        return False

def mode1(text, choice, filename): # Megszámolás
    output = data_read(0, filename)
    print(f"Az adattömböd összesen {output[1]}db rekordot tartalmaz!\n")
    wantexit(text, choice, filename)

def mode2(text, choice, filename): # Összegzés
    tool = 0 # Erre hivatkozunk a kerekítés függvénynél hogy a módhoz kapcsolódó szöveget írja ki
    datachoice = whichdata(text, filename, 1) # Melyik adatot választja a felhasználó
    output = data_read(datachoice, filename) # Beolvassa az összes adatot a felhasználó választásával
    
    conditional_round(output[0], 1, output[2], datachoice, tool, text) # Feltételes kerekítés
    wantexit(text, choice, filename) # Ki szeretne lépni a felhasználó?


def mode3(text, choice, filename): # Átlag
    tool = 1
    datachoice = whichdata(text, filename, 1)
    output = data_read(datachoice, filename)
    
    conditional_round(output[0], output[1], output[2], datachoice, tool, text)
    wantexit(text, choice, filename)

def mode4(text, choice, filename): # Minimum
    tool = 2
    datachoice = whichdata(text, filename, 1)
    output = data_read(datachoice, filename)
    
    mini = minimum_or_maximum(output[3])

    conditional_round(output[3][mini], 1, output[2], datachoice, tool, text)
    print(f"A(z) {output[2][0]}: {output[4][mini]}\n")
    wantexit(text, choice, filename)

def mode5(text, choice, filename): # Maximum
    tool = 3
    datachoice = whichdata(text, filename, 1)
    output = data_read(datachoice, filename)
    
    maxi = minimum_or_maximum(output[3], True)

    conditional_round(output[3][maxi], 1, output[2], datachoice, tool, text)
    print(f"A(z) {output[2][0]}: {output[4][maxi]}\n")
    wantexit(text, choice, filename)

def insertion_sort(l, ascending=False, wantindeces=False): # Minimum/maximum kiválasztásos rendezés
    y = []
    y_i = []
    for i in range(len(l)):
        y.append(l[i])
        y_i.append(i)

    for i in range(len(y)):
        j = minimum_or_maximum(y, ascending, i)
        if y[i] != y[j]:
            y[i], y[j] = y[j], y[i]
            y_i[i], y_i[j] = y_i[j], y_i[i]
    if not wantindeces:
        return y
    else:
        return y_i

def mode6(text, choice, filename): # Rendezés
    datachoice = whichdata(text, filename, 0)
    output = data_read(datachoice, filename)

    print(text[14])
    chc = input("Milyen sorrendben szeretnéd látni az adatokat?: ").lower()
    good = ["1", "2"]
    chc = valid_choice(chc, good)

    assorted = insertion_sort(output[3], chc == "2", True)

    done = cons_or_file(text, output, assorted)
    if not done:
        for i in range(len(output[3])):
            if datachoice != 1:
                print(str(i + 1) + ". " + output[4][i] + ": " + str(output[3][assorted[i]]))
            else:
                print(str(i + 1) + ". " + str(output[3][assorted[i]].capitalize()))

    print()

    wantexit(text, choice, filename)

def mode7(text, choice, filename): # Keresés
    datachoice = whichdata(text, filename, 0)
    output = data_read(datachoice, filename)

    if datachoice != 1: # Ha nem név alapján keresünk akkor legyen az adatunk Float hogy össze tudjuk hasonlítani
        ans = input("Keresés a következőre: ")
        while not is_number(ans, float):
            ans = input("Csak számot adhatsz meg!\nKérlek adj meg valami mást: ")
        ans = float(ans)
    else:
        ans = input("Keresés a következőre: ")
        while is_number(ans, float):
            ans = input("Csak szöveget adhatsz meg!\nKérlek adj meg valami mást: ")
        ans = ans.lower()

    db = 0
    indexes = []
    for i in range(len(output[3])):
        if ans == output[3][i]:
            db += 1
            indexes.append(i)
        
    i = 0 # Megszámolja hogy többször ismétlődik-e ugyanaz az adat
    while i < len(output[3]) and output[3][i] != ans:
        i += 1

    if i < len(output[3]):
        print("Sikeres keresés!\n")
        print("A keresett elem rekordja:")
        for j in range(len(output[5][i])):
            if datachoice-1 == j:
                print(f"*{output[2][j]}: {output[5][i][j]}")
            else:
                print(f"{output[2][j]}: {output[5][i][j]}")
        if db > 1: # Ha többször ismétlődik akkor a felhasználó választhat hogy a többit is kiírja vagy sem
            certain = input(f"\nTöbb ilyen rekordot is találtunk: összesen {db-1}db-ot ezen kívül.\nAzokat is szeretnéd kiírni a konzolra? (y/n): ")
            
            good = ["y", "n"]
            certain = valid_choice(certain, good)
            while not certain:
                certain = input(text[3])

            if certain == "y":
                for j in range(1, len(indexes)):
                    print(f"{indexes[j]+1}. rekord:")
                    for k in range(len(output[5][i])):
                        if datachoice-1 == k:
                            print(f"*{output[2][k]}: {output[5][indexes[j]][k]}")
                        else:    
                            print(f"{output[2][k]}: {output[5][indexes[j]][k]}")
                    print()

    else:
        if datachoice != 1:
            print("Sikertelen keresés!\n")
            mini = 0 # Abszolút értékes minkiválasztás --> Legközelebbi elem
            min_distance = abs(output[3][0] - ans)
            for i in range(1, len(output[3])):
                distance = abs(output[3][i] - ans)
                if distance < min_distance:
                    mini = i
                    min_distance = distance
                
            print(f"Legközelebbi elem rekordja:")
            for j in range(len(output[5][mini])):
                if datachoice-1 == j:
                    print(f"*{output[2][j]}: {output[5][mini][j]}")
                else:
                    print(f"{output[2][j]}: {output[5][mini][j]}")
        else:
            print("Sikertelen keresés!") # Szöveg alapján nincs legközelebbi elem mert azt nem tudom hogy kell megcsinálni

    wantexit(text, choice, filename)

def is_number(x, type):
    try: # Lehetővé teszi hogy valamit leteszteljünk hogy Error lesz-e vagy sem
        type(x)
    except ValueError: # Ha error akkor
        return False # False-al térünk vissza
    return True # Ha nem kapunk errort akkor True

def mode8(text, choice, filename): # Kiválogatás
    datachoice = whichdata(text, filename, 1)
    output = data_read(datachoice, filename)

    assorted, current = [], []
    print(f"\nMi alapján szeretnéd a(z) {output[2][datachoice-1]} elemeket kiválogatni?")
    print(text[12])
    good = ["1", "2"]
    assort_by = input(text[2])
    assort_by = valid_choice(assort_by, good)
    if assort_by == "1":
        assort_text = "kisebb"
    else:
        assort_text = "nagyobb"

    x = input(f'Add meg a számot aminél {assort_text} legyen a(z) "{output[2][datachoice-1]}" elemei: ')
    while not is_number(x, float):
        x = input(f"Csak számot adhatsz meg!\nKérlek adj meg valami mást: ")
    x = float(x)

    for i in range(len(output[3])): # Kisebbek legyenek az elemek mint x
        if assort_by == "1":
            if output[3][i] < x:
                assorted.append(output[3][i])
                current.append(i)
        else:
            if output[3][i] > x: # Nagyobbak legyenek az elemek mint x
                assorted.append(output[3][i])
                current.append(i)
    if assorted == []:
        print("Nincsenek ilyen elemek!")
    else:
        done = cons_or_file(text, output, current)
        if not done:
            print(f'\nKiválogatott "{output[2][datachoice-1]}" adat(ok):')
            for i in range(len(assorted)):
                print(f"{current[i]+1}. rekord: {assorted[i]}")
            print()
    
    wantexit(text, choice, filename)

def mode9(text, choice, filename): # Random rekord sorsolás
    output = data_read(0, filename)
    r = randint(0, len(output[5])-1)
    print(f"{r+1}. rekord:\n")
    for i in range(len(output[2])):
        print(f"{output[2][i]}: {output[5][r][i]}")
    
    good = ["y", "n", "q"]
    another = input("\nKérsz még egy random rekordot? (y/n): ")
    another = valid_choice(another, good)
    if another == "y":
        mode9(text, choice, filename)
    else:
        sleep(0.25)
        system("cls")
        modes(text, choice, filename)

def data_read(datachoice, filename): # Adatok beolvasása az adattömbből majd eltárolása & különböző műveletek végrehajtása
    db, x = 0, 0
    data, output, names, alldata = [], [], [], []

    fr = open(filename, mode="r", encoding="UTF-8")
    fr.seek(0)
    header = fr.readline().strip().split(";")
    line = fr.readline().strip()
    while line != "":
        db += 1
        cut = line.split(";")
        names.append(cut[0])
        alldata.append(cut)
        if datachoice != 1: # Ha nem str típussal dolgozunk akkor legyen float az adat hogy össze lehessen hasonlítani
            x += float(cut[datachoice-1])
            data.append(float(cut[datachoice-1].strip()))
        else: # Ha str-el dolgozunk akkor maradjon str az adat :)
            data.append(cut[datachoice-1].strip().lower())
        line = fr.readline().strip()
    fr.close()

    stuff = [x, db, header, data, names, alldata]
    for i in range(len(stuff)):
        output.append(stuff[i])
    return output

def procedure(text_list): # Ez azért van itt külön mert a visszalépés gomb ezt hívja meg... tiszta kód? Nem.
    pick = start_choice(text_list)
    
    while not pick != "q":
        print("\nKilépés...")
        exit()

    while not pick != "3":
        randomcolor(text_list)
        pick = start_choice(text_list)
    else:
        file_name = fchoose(text_list, pick)
        modes(text_list, pick, file_name)
    
def main():
    text_list = []
    load_text(text_list) # Szöveg betöltése a "text.txt" állományból

    system("cls")
    print(text_list[0]) # Ascii art
    sleep(2) # 2 másodperc várakozás

    procedure(text_list) # Program fő része

main()