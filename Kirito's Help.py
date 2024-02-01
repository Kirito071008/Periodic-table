import pyfiglet,platform,os
from mendeleev import element
if platform.system() == "Windows":
    def clear(): os.system("cls")
else:
    def clear(): os.system("clear")

def menu():
    clear()
    ascii_banner = pyfiglet.figlet_format("Kirito's Help")
    print(ascii_banner)
    print("Benvenuto!, Cosa vuoi fare??")
    x = input("1)Calcolo Elettroni di valenza 2)Calcolo Carica Formale\n")
    if x == "1":
        ev()
    elif x == "2":
        cf()
    elif x == "exit":
        exit()
    else:
        menu()
def ev():
    x = input("Quanti elementi sono?\n")
    if x == "2":
        y = input("Simbolo primo elemento:\t")
        y2 = input("Quanti ne sono?:\t")
        z = input("Simbolo secondo elemento:\t")
        z2 = input("Quanti ne sono?:\t")
        c = input("Indicare eventuali elettroni aggiunti o rimossi da '-/+' (0 se non ce ne sono):\t")
        elemento1 = element(y)
        elemento2 = element(z)
        g1 = elemento1.group_id
        g2 = elemento2.group_id
        if int(g1) > 10:
            g1 = int(g1)-10
        if int(g2) > 10:
            g2 = int(g2)-10
        ev = int(g1)*int(y2)+int(g2)*int(z2)+int((c))
        print(f"Carica formale: {ev}")
menu()