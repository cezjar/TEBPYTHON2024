##Laboratoria z modułu 3

##Laboratorium 3.1.1.4
n = int(input("Wprowadź liczbę:"))
if n < 100:
    print("False")
else:
    print("True")

##Laboratorium 3.1.1.10
n = input("Podaj słowo:")
if n == "Skrzydłokwiat":
    print("Skrzydłokwiat jest najlepszą rośliną w historii!")
else:
    print("Nie, ja chcę Skrzydłokwiat...!")


##Laboratorium 3.1.1.11
dochod = float(input("Wprowadź swój roczny dochód: "))

if dochod <= 85528.00:
    podatek = (dochod * 0.18) - 556.02
else:
    podatek = 14839.02 + (dochod - 85528) * 0.32
podatek = max(podatek, 0.00)

podatek = round(podatek, 0)
print("Podatek wynosi:", podatek)

##Laboratorium 3.1.1.12
rok = int(input("Wprowadź rok: "))

if rok < 1582:
    print("Nie w kalendarzu gregoriańskim")
else:
    if rok % 4 != 0:
        print("Rok zwykły")
    elif rok % 100 != 0:
        print("Rok przestępny")
    elif rok % 400 != 0:
        print("Rok zwykły")
    else:
        print("Rok przestępny")
##Laboratorium 3.2.1.3

tajny_numer = 777
print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")
liczba = 0
while liczba != tajny_numer:
    liczba = int(input("Podaj liczbę: "))
    if liczba != tajny_numer:
        print("Nie, to nie jest ta liczba, którą wybrałem dla ciebie. Spróbuj ponownie")
    else:
        print("Dobra robota! To numer, który wybrałem dla ciebie! Jesteś teraz wolny.")

##Laboratorium 3.2.1.6
import time
for i in range(1, 6):
    time.sleep(1) # LINIA II
    print(f"iteracja numer {i}, Mississippi")

# Napisz funkcję print, która wyświetli wiadomość końcową.
print("Ready or not, here I come!")

##Laboratorium 3.2.1.9
while True:
    x = input("Wpisz słowo: ")
    if x == "pumpernikiel":
        print("Udało ci się opuścić pętlę.")
        break

##Laboratorium 3.2.1.10
# Poproś użytkownika o wprowadzenie słowa
# i przypisz je do zmiennej slowo_uzytkownika
slowo_uzytkownika = input("Wprowadź słowo: ")
slowo_uzytkownika = slowo_uzytkownika.upper()

for litera in slowo_uzytkownika:
    if litera in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        continue
    print(litera)

# ##Laboratorium 3.2.1.11
slowo_bez_samoglosek = ""
slowo_uzytkownika = input("Wprowadź słowo: ")
slowo_uzytkownika = slowo_uzytkownika.upper()

for litera in slowo_uzytkownika:
    if litera in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        continue
    else:
        slowo_bez_samoglosek = slowo_bez_samoglosek + litera
print(slowo_bez_samoglosek)

# Wyświetl słowo przypisane do zmiennej slowo_bez_samoglosek.

##Laboratorium 3.2.1.14

blokow = int(input("Wprowadź liczbę bloków: "))
wysokosc = 0

while True:
    blokow = blokow - wysokosc
    if blokow > wysokosc:
        wysokosc += 1
    else:
        break
print("Wysokość piramidy wynosi:", wysokosc)

##Laboratorium 3.2.1.15

c0 = int(input("Wprowadź dowolną, nieujemną i niezerową liczbę całkowitą: "))
i = 0
while True:
    if c0 % 2 == 0:
        i += 1
        c0 = c0/2
        print(c0)
    elif c0 == 1:
        print(f"liczba kroków = {i}")
        break
    else:
        i += 1
        c0 = 3*c0 + 1
        print(c0)

##Laboratorium 3.4.1.6
liczby_z_kapelusza = [1, 2, 3, 4, 5]  # Istniejąca lista liczb ukrytych w kapeluszu.

# Krok 1: Napisz wiersz kodu, który prosi użytkownika o zastąpienie środkowego numeru liczbą całkowitą wprowadzoną przez użytkownika.
liczby_z_kapelusza[2] = int(input("Czym chcesz zastąpić środkowy numer w liście? "))

# Krok 2: Napisz tutaj wiersz kodu, który usuwa ostatni element z listy.
del liczby_z_kapelusza[-1]

# Krok 3: Napisz tutaj wiersz kodu, który wypisuje długość istniejącej listy.
print(len(liczby_z_kapelusza))
print(liczby_z_kapelusza)  # Wyświetlanie zawartości listy.


##Laboratorium 3.4.1.13
# Krok 1
beatles = []
print("Krok 1:", beatles)

# Krok 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Krok 2:", beatles)

# Krok 3
muzycy = ["Stu Sutcliffe", "Pete Best"]
for i in muzycy:
    beatles.append(i)
print("Krok 3:", beatles)

# Krok 4
del beatles[3:5]
print("Krok 4:", beatles)

# Krok 5
beatles.insert(0,"Ringo Starr")
print("Krok 5:", beatles)


# Sprawdzanie długości listy.
print("The Fab", len(beatles))

##Laboratorium 3.6.1.9

moja_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista_tymczasowa = []


for i in moja_lista:
    if i not in lista_tymczasowa:
        lista_tymczasowa.append(i)
    else:
        continue
moja_lista = lista_tymczasowa[:]

print("Lista tylko z unikalnymi elementami:")
print(moja_lista)