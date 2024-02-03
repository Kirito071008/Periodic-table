import pyfiglet,platform,os
from mendeleev import element
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
if platform.system() == "Windows":
    def clear(): os.system("cls")
else:
    def clear(): os.system("clear")

def menu():
    clear()
    ascii_banner = pyfiglet.figlet_format("Kirito's Help")
    print(ascii_banner)
    print("Benvenuto!, Cosa vuoi fare?")
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
    list = []
    list2 = []
    list3 = []
    count = 0
    x = input("Inserisci la molecola:\t")
    for elementi in x:
        if elementi in uppercase:
            list3.append(elementi)
            x = element(elementi)
            h = x.group_id
            if int(h) > 10:
                h -= 10
                if count == 1:
                    z = sum(list2)
                    list.append(z)
                    list2.clear()
                    list2.append(h)
                    count -= 1
                else:
                    list2.append(h)
                    count += 1
            else:
                if count == 1:
                    z = sum(list2)
                    list.append(z)
                    list2.clear()
                    list2.append(h)
                    count -= 1
                else:
                    list2.append(h)
                    count += 1
        elif elementi in lowercase:
            p = list3[0]
            list3.clear()
            count -= 1
            y = str(p)+str(elementi)
            z = element(y)
            j = z.group_id
            if int(j) > 10:
                j -= 10
                list.append(j)
            else:
                list.append(j)
        elif elementi in numbers:
            z = sum(list2)
            list2.clear()
            count -= 1
            y = z*int(elementi)
            list.append(int(y))
    if count == 1:
        g = sum(list)+sum(list2)
    else:
        g = sum(list)
    print(f"Elettroni di valenza: {g}")
menu()
