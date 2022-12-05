import os
import json

with open('pokedex.json', encoding='utf8') as file:
    pokedex151 = json.load(file)


def menu():
    print('-'*40)
    print(f"{'Search by Name':<20}(1)")
    print(f"{'Search by Type':<20}(2)")
    print(f"{'Search by Number':<20}(3)")
    print(f"{'list by Name':<20}(4)")
    print(f"{'list by Number':<20}(5)")
    print(f"{'Add/Edit Pokémon':<20}(6)")
    print(f"{'Setting langue':<20}(7)")
    print(f"{'Exit':<20}(8)")
    print('-'*40)
    print


def langue():
    print('-'*40)
    print("What your langue? Default = English ")
    print("[1] English\n[2] Japanese\n[3] chinese\n[4] french")
    lang = input("Input: ")
    os.system("cls")
    if lang =="1":
        return "english"

    elif lang =="2":
        return "japanese"

    elif lang =="3":
        return "chinese"

    elif lang =="4":
        return "french"
    
    else:
        print("Invalid Option\nEnglish  defined")
        return "english"


def search_by_name(p1, lang='english'):
    print('\n','=-'*20,)
    print("information's\n".center(40))

    if p1!="":
        for group in pokedex151:
            if p1 in group['name'].values():
                print(f"\t{'ID Num':<10} {group['id']}")
                if lang != "english":
                     print(f"\t{'Name':<10} {group['name'][lang]} //English: {group['name']['english']}//")
                else:
                    print(f"\t{'Name':<10} {group['name'][lang]} ")
                print(f"\t{'Type':<10}" ,*group['type'], sep=' // ')
        return
    print("Not Found !")
                


def  search_by_type(t1, t2):
    print('\n','-'*40)
    print("Type".center(40))

    if t1=='' and t2 =='':
        print("None type selected".center(40))
        return

 
    accumulator = 0
    for pokemon_group in pokedex151:
        if t2 == '':
            if t1 in pokemon_group["Type1"]:
                print(f"  //{pokemon_group['Name']}", end=' // ')
                accumulator +=1
         
        else:
            if t1 in pokemon_group.values() and t2 in pokemon_group.values():
                print(f"  //{pokemon_group['Name']}", end=' // ')
                accumulator +=1

    return accumulator

    
    

    
os.system("cls")  
lang = langue()

while True: 
    
    menu()
    option = input("Input: ")
    
    if option =="1":
        
        name = input("What Pokémon?: ")
        os.system("cls")
        search_by_name(name.capitalize().strip(), lang)

    if option == "2":
        type1 = input("what type1: ").upper().strip()
        type2 = input("what type2: ").upper().strip()
        os.system("cls")
        founds = search_by_type(type1, type2)
        print(f"\n \n {founds} Pokémons found !! \n")

    if option == "7":
        os.system("cls")
        lang = langue()


    if option == "8":
        exit = input("Confirm exit [Y] or [N]: ").lower()
        if exit == "y":
            break
        os.system("cls")


os.system("cls")
print("Thank you !!")
        
    