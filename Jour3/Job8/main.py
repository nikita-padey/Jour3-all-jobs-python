#Job8
a = float(input("Entrez la longueur du côté a : "))
b = float(input("Entrez la longueur du côté b : "))
c = float(input("Entrez la longueur du côté c : "))

if a + b > c and a + c > b and b + c > a:
    print("Les longueurs peuvent former un triangle.")

    if a == b == c:
        print("Le triangle est équilatéral.")
    elif a == b or b == c or a == c:
        print("Le triangle est isocèle.")

        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Le triangle est aussi rectangle.")
        else:
            print("Le triangle est quelconque.")

    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Le triangle est rectangle.")
else:
    print("Les longueurs ne peuvent pas former un triangle.")












