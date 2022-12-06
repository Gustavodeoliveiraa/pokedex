import os
from json import load
from time import sleep
from  googletrans import Translator

with open('pokedex.json', encoding='utf8') as file:
    pokedex151 = load(file)


def menu():
    
    return [("[ 1 ]  Search by Name"),
        ("[ 2 ]  Search by Type"),
        ("[ 3 ]  Search by Number"),
        ("[ 4 ]  Setting langue"),
        ("[ 5 ]  Exit")]

# def set_langue():
#     print('-'*40)
#     print("What your langue? Default = English ")
#     print("[1] English\n[2] Japanese\n[3] French ")
#     num = input("Input: ")
  
def translate_menu(func, lang="en"):
    translation = Translator()
    for items in func():
        print(translation.translate(items, lang).text)

    return lang
    

def  initials_by_name(var):
    if var == "en":
        return "english"

    elif var== "ja":
        return "japanase"
    
    elif var== "fr":
        return "french"

   

def search_by_name(name, lang='english'):
    print('\n','=-'*20,)
    print("information's\n".center(40))

    if name!="":
        for group in pokedex151:
            if name in group['name'].values():
                print(f"\t{'ID Num':<10} {group['id']}")
                if lang != "english":
                     print(f"\t{'Name':<10} {group['name'][lang]}")
                     print(f"\t{'English':<10} {group['name']['english']}")
                else:
                    print(f"\t{'Name':<10} {group['name'][lang]} ")
                print(f"\t{'Type':<10}" ,*group['type'], sep=' // ')
        return
    print("Not Found !")
                


def search_by_type(t1, t2):
    print('\n','-'*40)
    print("Type".center(40))

    if t1=='' and t2 =='':
        print("None type selected".center(40))
        return
 
    accumulator = 0
    c = 0
    for pokemon_group in pokedex151:
        
        if t2 == '':
            if t1 in pokemon_group["type"]: 
                print(f"  // {pokemon_group['name']['english']}", end='// ')
                accumulator +=1
                c += 1
                if c ==  8:
                    print()
                    c = 0
         
        else:
            if t1 in pokemon_group.values() and t2 in pokemon_group.values():
                
                print(f"  //{pokemon_group['name']}", end='// ')
                accumulator +=1

    return accumulator

def search_by_id(var,lang):
    try: 
        num = int(var)
        for pokemon_group in pokedex151:
            if num in pokemon_group.values():
                print(f"\t{'ID Num':<10} {pokemon_group['id']}")
                print(f"\t{'Name':<10} {pokemon_group['name'][lang]}")
                print(f"\t{'Type':<10} ", end='')
                if len(pokemon_group['type']) > 1:
                    print(*pokemon_group['type'], sep='// ')
                else:
                    print(*pokemon_group['type'])
    
    except ValueError:
        print("\tIt is not number\n")

def translate_word(var, lang):
    translation = Translator()
    return (translation.translate(var,lang).text)
    
os.system("cls")  


while True: 

    print("-"*40)
    lang = translate_menu(menu)
    
    lang_in_json = initials_by_name(lang)

    option_ = translate_word("input", lang)
    option = input(f"{option_}: ")

    print("-"*40)
    
    if option =="1":
        
        name = input("What Pokémon?: ")
        os.system("cls")
        search_by_name(name.capitalize().strip(), lang_in_json)

    if option == "2":
        type1 = input("what primary type: ").capitalize().strip()
        type2 = input("what Secondary  type: ").capitalize().strip()
        os.system("cls")
        founds = search_by_type(type1, type2)
        print(f"\n \n {founds} Pokémon's found !! \n")

    if option == "3":
        id_num = input("Number: ")
        os.system("cls")
        search_by_id(id_num, lang_in_json)

    if option == "4":
        set_lang()
        

    if option == "5":
        exit = input("Confirm exit [Y] or [N]: ").lower()
        if exit == "y":
            break
        os.system("cls")


os.system("cls")
print("Thank you !!")
        
    