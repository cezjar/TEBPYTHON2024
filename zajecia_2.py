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

