from pokedex import *
import os

def menu():
    print('-'*40)
    print(f"{'Search by Name':<20}(1)")
    print(f"{'Search by Type':<20}(2)")
    print(f"{'Search by Number':<20}(3)")
    print(f"{'list by Name':<20}(4)")
    print(f"{'list by Number':<20}(5)")
    print(f"{'Add/Edit Pokémon':<20}(6)")
    print(f"{'Exit':<20}(7)")
    print('-'*40)
    print


def search_by_name(name):
    print('\n','=-'*20, '\n')

    for pokemon_groupy in pokedex151:
        if name == None:
            break

        if name  in pokemon_groupy.values():
            for key, value in pokemon_groupy.items():
                print(f'    {key:<20} {value}')
            print('\n','=-'*20, '\n')
            return 

    print("Not found".center(40))     
    print('\n','=-'*20, '\n')


def  search_by_type(t1, t2):
    print('\n','-'*40)
    print("Type".center(40))

    if t1=='' and t2 =='':
        print("None type selected".center(40))
        return

 
    accumulator = 0
    for pokemon_groupy in pokedex151:
        if t2 == '':
            if t1 in pokemon_groupy["Type1"]:
                print(f"  //{pokemon_groupy['Name']}", end=' // ')
                accumulator +=1
         
        else:
            if t1 in pokemon_groupy.values() and t2 in pokemon_groupy.values():
                print(f"  //{pokemon_groupy['Name']}", end=' // ')
                accumulator +=1

    return accumulator

    
    

    
        

while True: 
    menu()
    option = input("Input: ")
    
    if option =="1":
        name = input("What Pokémon?: ")
        os.system("cls")
        search_by_name(name.upper().strip())

    if option == "2":
        type1 = input("what type1: ").upper().strip()
        type2 = input("what type2: ").upper().strip()
        os.system("cls")
        founds = search_by_type(type1, type2)
        print(f"\n \n {founds} Pokémons found !! \n")


    if option == "7":
        exit = input("Confirm exit [Y] or [N]: ").lower()
        if exit == "y":
            break
        os.system("cls")


os.system("cls")
print("Thank you !!")
        
    