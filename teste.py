from googletrans import Translator



# def traduz(texto, lang):
#     x = Translator()
#     print(x.translate(texto, dest=lang).text)


# x=(f"{'Search by Name':<20}(1)")
# traduz(x, "en")



def menu():
    
    return [("[ 1 ]  Search by Name"),
        ("[ 2 ]  Search by Type"),
        ("[ 3 ]  Search by Number"),
        ("[ 4 ]  Setting langue"),
        ("[ 5 ]  Exit")]
    



def analise(func,lang='zh-tw'):
    x = Translator()
    for item in func():
        print(x.translate(item, dest=lang).text)


analise(menu, 'ja')


