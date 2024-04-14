from random import randint
from os import system
from time import sleep

def combine(x):
    y = ""
    for i in range(len(x)):
        y += x[i]
    return y        

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

def start_choice(text):
    print(text[0])
    sleep(2)
    system("cls")
    print(text[1])
    good = ["1", "2", "3"]
    choice = input(text[2])
    return int(valid_choice(choice, good))

def valid_choice(var, list):
    while var not in list:
        var = input("Nincs ilyen opció!\nVálassz mást: ")
    return var

def areusure():
    response = input("Biztosan ezzel a választással szeretnéd folytatni? (y/n): ")
    if response == 'y':
        return True
    elif response == 'n':
        return False
    else:
        response = input("Nincs ilyen opció!\nVálassz mást: ")

def fm_choose(text, choice):
    if choice == 1:
        print("Az első módot választottad ki!")
    elif choice == 2:
        print("A második módot választottad ki!")
    else:
        print("A harmadik módot választottad ki!")
    file_choice = input(text[4])
    print(f'Sikeresen kiválasztottad a "{file_choice}" fájlt!')
    certain = areusure()
    while not certain:
        x = input(text[4])
        print(f'Sikeresen kiválasztottad a "{x}" fájlt!')
        certain = areusure()
    sleep(0.5)
    system("cls")

def modes(text, choice):
    if choice == 1:
        print(text[5])
        choice2 = input(text[2])
        good = ["1","2","3","4","5","6"]
        choice2 = valid_choice(choice2, good)
        print(choice2)
    elif choice == 2:
        print("work in progress")
    else:
        print("work in progress")

def main():
    text_list = []
    load_text(text_list)

    pick = start_choice(text_list)
        
    fm_choose(text_list, pick)
    modes(text_list, pick)
    
main()