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