
#importy
import os
import time
from PIL import Image
from termcolor import colored
from pyfiglet import Figlet


#funkcje menu
def menu():
     print("\n")
     print("Funkcje programu:")
     print("Aby wyświetlić obraz wpisz \"pokaż\"")
     print("Aby obrócić obraz wpisz \"obróć\"")
     print("Aby przeskalowac wpisz \"skaluj\"")
     print("Aby usunąć kolory wpisz \"czarno-biały\"")
     print("Aby zapisać obraz wpisz \"zapisz\"")
     print("Aby wyjść wpisz \"wyjdź\"")
     print("Wybieram: ", end='')
     wybor=input()
     return wybor

def logo(tekst):
    banner=Figlet(font="slant").renderText(tekst)
    print (colored(banner, "cyan"))

def spis_plikow(lista_plikow):
    for plik in os.listdir("."):
        if plik.endswith(".jpg"):
            lista_plikow.append(plik)


#funkcje programu
def lista():
    print("\n")
    print("Dostępne pliki:")
    for plik in os.listdir("."):
        if plik.endswith(".jpg"):
            print(plik)
          
def pokaz(plik):
    plik.show()
    print(colored("Obraz wyświetlony!", "green"))
     
def zapisz(plik, nazwa):
    plik.save(nazwa)
    print(colored("Zapisano plik!", "green"))    #TUTAJ WRZUCAMY FUNKCJE#

 def skaluj(plik, szerokosc, wysokosc):
    plik=plik.resize([szerokosc, wysokosc])
    print(colored("Przeskalowano!", "green"))
    return plik
     
#zmienne globalne
lista_dostepnych_plikow=[]


#init
spis_plikow(lista_dostepnych_plikow)
logo("Pythonshop")
time.sleep(1.5)


#wybieranie pliku
while True:
    print("\n")
    print("Wpisz \"lista\", aby wyświeltić dostępne pliki w folderze")
    print("Wpisz \"wyjdź\", aby opuścić program")
    print("Podaj nazwę pliku i rozszerzenie: ", end='')
    wybor=input()

    if wybor=="lista":
        lista()

    elif wybor=="wyjdź":
        break                              #MIEJSCE NA TWOJĄ FUNKCJĘ

    elif wybor in lista_dostepnych_plikow:
        obraz=Image.open(wybor)
        print(colored("Wybrano plik!", "green"))
        break

    else:
        print(colored("Błędna nazwa pliku!", "red"))


#główne menu funkcyjne
while True:

    funkcja=menu()

    if funkcja=="pokaż":
        pokaz(obraz)                      
     
    elif funkcja=="obróć":
        break                              #MIEJSCE NA TWOJĄ FUNKCJĘ

    elif funkcja=="skaluj":
        print("Wprowadź szerokość obrazu: ", end='')
        szerokosc=int(input())
        print("Wprowadź wysokość obrazu: ", end='')
        wysokosc=int(input())
        obraz=skaluj(obraz, szerokosc, wysokosc)
                                            

    elif funkcja=="czarno-biały":
        break                              #MIEJSCE NA TWOJĄ FUNKCJĘ

    elif funkcja=="zapisz":
        print("Wprowadź nazwę pliku (opcjonalnie z rozszerzeniem): ", end='')
        output_nazwa=input()
        zapisz(obraz, output_nazwa)
                           
    elif funkcja=="wyjdź":
        break                              #MIEJSCE NA TWOJĄ FUNKCJĘ

    else:
        print(colored("Błędna funkcja!", "red"))
=======
#importy
import os
import time
from PIL import Image
from termcolor import colored
from pyfiglet import Figlet


#funkcje menu
def menu():
     print("\n")
     print("Funkcje programu:")
     print("Aby wyświetlić obraz wpisz \"pokaż\"")
     print("Aby obrócić obraz wpisz \"obróć\"")
     print("Aby przeskalowac wpisz \"skaluj\"")
     print("Aby usunąć kolory wpisz \"czarno-biały\"")
     print("Aby zapisać obraz wpisz \"zapisz\"")
     print("Aby wyjść wpisz \"wyjdź\"")
     print("Wybieram: ", end='')
     wybor=input()
     return wybor

def logo(tekst):
    banner=Figlet(font="slant").renderText(tekst)
    print (colored(banner, "cyan"))

def spis_plikow(lista_plikow):
    for plik in os.listdir("."):
        if plik.endswith(".jpg"):
            lista_plikow.append(plik)


#funkcje programu
def lista():
    print("\n")
    print("Dostępne pliki:")
    for plik in os.listdir("."):
        if plik.endswith(".jpg"):
            print(plik)
          
def pokaz(plik):
    plik.show()

    print(colored("Obraz wyświetlony!", "green"))
     

def obroc(plik, stopnie):
    plik=plik.rotate(stopnie)
    print(colored("Obrócono!", "green"))
    return plik


def zapisz(plik, nazwa):
    plik.save(nazwa)
    print(colored("Zapisano plik!", "green"))
   

    print(colored("Obraz wyświetlony!", "green")

def czarno_bialy(plik):
    plik=plik.convert("L")
    print(colored("Usunięto kolory!", "green"))
    return plik

     
def zapisz(plik, nazwa):
    plik.save(nazwa)
    print(colored("Zapisano plik!", "green"))

                                            #TUTAJ WRZUCAMY FUNKCJE#

#zmienne globalne
lista_dostepnych_plikow=[]


#init
spis_plikow(lista_dostepnych_plikow)
logo("Pythonshop")
time.sleep(1.5)


#wybieranie pliku
while True:
    print("\n")
    print("Wpisz \"lista\", aby wyświeltić dostępne pliki w folderze")
    print("Wpisz \"wyjdź\", aby opuścić program")
    print("Podaj nazwę pliku i rozszerzenie: ", end='')
    wybor=input()

    if wybor=="lista":
        lista()

    elif wybor=="wyjdź":
        break                              #MIEJSCE NA TWOJĄ FUNKCJĘ

    elif wybor in lista_dostepnych_plikow:
        obraz=Image.open(wybor)
        print(colored("Wybrano plik!", "green"))
        break

    else:
        print(colored("Błędna nazwa pliku!", "red"))


#główne menu funkcyjne
while True:

    funkcja=menu()

    if funkcja=="pokaż":
        pokaz(obraz)                      
     
    elif funkcja=="obróć":

        print("Wprowadź liczbę stopni: ", end='')
        stopnie=int(input())
        obraz=obroc(obraz, stopnie)                            

        break                              #MIEJSCE NA TWOJĄ FUNKCJĘ


    elif funkcja=="skaluj":
        break                              #MIEJSCE NA TWOJĄ FUNKCJĘ

    elif funkcja=="czarno-biały":

        break                              #MIEJSCE NA TWOJĄ FUNKCJĘ

        obraz=czarno_bialy(obraz)                         


    elif funkcja=="zapisz":
        print("Wprowadź nazwę pliku (opcjonalnie z rozszerzeniem): ", end='')
        output_nazwa=input()
        zapisz(obraz, output_nazwa)
                           
    elif funkcja=="wyjdź":
        break                              #MIEJSCE NA TWOJĄ FUNKCJĘ

    else:
        print(colored("Błędna funkcja!", "red"))

