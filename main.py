import os

from functions import menu, set_langue, translate_menu, \
translate_word, initials_by_name, num_in_initials, \
search_by_name, search_by_type, search_by_id




    
os.system("cls") 


lang = num_in_initials() 

while True: 

    print("-"*40)
    translate_menu(menu, lang)
    

    
    lang_in_json = initials_by_name(lang)

    option_ = translate_word("option", lang)
    option = input(f"{option_}: ").strip()

    print("-"*40)
    
    if option == "1": 
        
        name = input(translate_word("Name of Pokémon: ", lang))
        os.system("cls")
        search_by_name(name.capitalize().strip(), initials_by_name(lang), lang)

    elif  option == "2":
        
        # inputs não estao sendo traduzidos 
        type1 = input("what primary type: ").capitalize().strip()
        type2 = input("what Secondary  type: ").capitalize().strip()
        os.system("cls")
        founds = search_by_type(type1, type2)
        print(f"\n \n {founds} Pokémon's found !! \n")

    elif option == "3":
        id_num = input(translate_word("Number: ", lang))
        os.system("cls")
        search_by_id(id_num, lang_in_json)

    elif option == "4":
        os.system("cls")
        lang_set = set_langue()
        lang = num_in_initials(lang_set) 
        os.system("cls")
        

    elif option == "5":
         # inputs não estao sendo traduzidos 
        exit = input("Confirm exit [Y] or [N]: ").lower()
        if exit == "y":
            break
        os.system("cls")


os.system("cls")
print("Thank you !!")
        
    