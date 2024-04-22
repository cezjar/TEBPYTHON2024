#Stwórz program, dzięki któremu użytkownik przekonwertuje odległość podaną w kilometrach na podane jednostki: milimetry, centrymentry, metry, cale, stopy, mile.

distance = int(input("Podaj odległość w kilometrach która chcesz przekonwertować"))
print(f'Podano {distance} km')

milimeters = distance * 1000000
centimeters = distance * 100000
meters = distance * 1000
inches = distance * 39.3701
feet = distance * 3280.84
miles = distance * 0.6214

print('Twój dystans w innych jednostkach miary to: ')
print(milimeters, ' mm')
print(centimeters, ' cm')
print(meters, ' m')
print(round(inches, 2), 'cali')
print(round(feet, 2), 'stóp')
print(round(miles, 2), 'mil')

#Należy wykonać wszystkie laboratoria z modułu 2 z kursu python na netacad.

#LAB1
print('Wlazl kotek na plotek')
print('Cezary Jaremek')

#LAB2

print("Kurs","Programowania","w",sep = "***", end = "...")
print("Pythonie")

#LAB3
print("    *    " * 2 + "\n" +
      "   * *   " * 2 + "\n" +
      "  *   *  " * 2 + "\n" +
      " *     * " * 2 + "\n" +
      "***   ***" * 2 + "\n" +
      "  *   *  " * 2 + "\n" +
      "  *   *  " * 2 + "\n" +
      "  *****  " * 2)

#LAB4
print('"Ucze się" \n ""jezyka"" \n """Python"""')

#LAB5
pomaranczowy_krol = 3
agnieszka = 5
adam = 6
print(pomaranczowy_krol, agnieszka, adam, sep = ',')

pomaranczowy_razem = pomaranczowy_krol + agnieszka + adam
print(pomaranczowy_razem)
print(f"Całkowita liczba pomarańczy {pomaranczowy_razem}")

#LAB6
kilometry = 12.25
mile = 7.38

mile_na_kilometry =  mile * 1.61
kilometry_na_mile =  kilometry / 1.61

print(mile, "mi to", round(mile_na_kilometry, 2), "km")
print(kilometry, "km to", round(kilometry_na_mile, 2), "mi")


#LAB7
x =  1
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x -1
print("y =", y)

#LAB8
#Ten program oblicza liczbę sekund w danej liczbie godzin.
godziny = 3 #liczba godzin
sekundy_w_godzinie = 3600 #liczba sekund w 1 godzinie

print("Godzin: ", godziny) # wyświetla ilość godzin
print("Sekund w godzinach: ", godziny * sekundy_w_godzinie)  # wyswietla ilość sekund w zadanej liczbie godzin
print("Do widzenia")
# to jest koniec programu, który oblicza liczbę sekund w 3 godzinach

#LAB9

a = 2.1
b = 3.1

print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("\nI to by było na tyle!")

#LAB10

x = float(input("Wprowadź wartość dla x: "))

y = (1/(x+(1/(x+(1/(x+(1/x)))))))

print("y =", y)


#LAB11
h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))

minuta_zakonczenia = (m + d) % 60
ilosc_godzin_do_dodania = (m + d) // 60

godzina_zakonczenia = (h + ilosc_godzin_do_dodania) % 24


print(godzina_zakonczenia, minuta_zakonczenia, sep=':')
