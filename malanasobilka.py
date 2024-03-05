import random

def nasobeni(a, b):
    vysledek = a * b
    return vysledek

def kontrola(vysledek, vysledek_zak):
    body = False
    if vysledek == vysledek_zak:
        print("Jsi šikulka, máš to správně!")
        body = True
    else:
        print("Jejda, spletl jsi se!")

    return body


for i in range(9):
    x = random.randint(1,10)
    y = random.randint(1,10)

    vysledek_zak = int(input(f"{x} * {y} = "))

    vysledek = nasobeni(x,y)

    kontrola(vysledek,vysledek_zak)