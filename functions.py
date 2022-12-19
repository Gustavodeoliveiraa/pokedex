from json import load
from  googletrans import Translator

with open('pokedex.json', encoding='utf8') as file:
    pokedex151 = load(file)


def menu():
    
    return ["[ 1 ]  Search by Name",
        "[ 2 ]  Search by Type",
        "[ 3 ]  Search by Number",
        "[ 4 ]  Setting language",
        "[ 5 ]  Exit"]

def set_langue():
    print('-'*40)
    print("What your langue? Default = English ")
    print("[1] English\n[2] 日本語\n[3] Français")
    num = input("Input: ").replace(" ", "")
    num = int(num) 
    if 1<= num <=3:
        return str(num)
    else:
        num = 1
        return str(num) 


def translate_menu(func, lang="en"):
    translation = Translator()
    for items in func():
        print(translation.translate(items, lang).text)

def translate_word(var, lang):
    translation = Translator()
    return (translation.translate(var, lang).text)


def  initials_by_name(var):
    if var == "en":
        return "english"

    elif var == "ja":
        return "japanese"

    elif var == "fr":
        return "french"


def num_in_initials(var="1"):

    if var ==  "1":
        return "en"

    elif var== "2":
        return "ja"

    elif var== "3":
        return "fr"
   

def search_by_name(name, lang, traduction):
    print('\n','=-'*20,)
    print("information's\n".center(40))

    if name!="":
        for group in pokedex151:
            if name in group['name'].values():
                print("\t",translate_word("Number", traduction),
                f"{'':<3}" ,group['id'])
                
                if lang != "english":
                    print("\t",translate_word("Name", traduction), end='')
                    print(f"{'':<6}", end='')
                    print(group['name'][lang])

                    print(f"\t {'English ':<10} {group['name']['english']}")
                else:
                    print(f"\t {'Name':<10} {group['name'][lang]} ")

                print("\t",translate_word("Type", traduction), end='')
                print(f"{'':<5}", end='')
                for items in group['type']:
                    print(translate_word(items, traduction))
        return
    print("Not Found !")
                

#ãp está sendo traduzido 
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
            if t1 in pokemon_group["type"]:           ###
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
#náo está sendo traduzido
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
