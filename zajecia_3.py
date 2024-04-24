##Laboratoria z modułu 4

# ##Laboratorium 4.3.1.6
#
# def czy_przestepny(rok):
#     if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
#         return True
#     else:
#         return False
#
# dane_testowe = [1900, 2000, 2016, 1987]
# wyniki_testow = [False, True, True, False]
# for i in range(len(dane_testowe)):
# 	r = dane_testowe[i]
# 	print(r,"->",end="")
# 	wynik = czy_przestepny(r)
# 	if wynik == wyniki_testow[i]:
# 		print("OK")
# 	else:
# 		print("Nie powiodło się")
#

# ##Laboratorium 4.3.1.7
#
# def czy_przestepny(rok):
#     if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
#         return True
#     else:
#         return False
#
# def dni_w_miesiacu(rok, miesiac):
#     if czy_przestepny(rok) == True and miesiac == 2:
#         return 29
#     elif czy_przestepny(rok) == False and miesiac == 2:
#         return 28
#     elif miesiac in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
#     elif miesiac in [4, 6, 9, 11]:
#         return 30
#     else:
#         return None
#
#
# testuj_lata = [1900, 2000, 2016, 1987, 1999]
# testuj_miesiace = [2, 2, 1, 11, 4]
# testuj_wynik = [28, 29, 31, 30, 30]
# for i in range(len(testuj_lata)):
#     r = testuj_lata[i]
#     m = testuj_miesiace[i]
#     print(r, m, "-> ", end="")
#     wynik = dni_w_miesiacu(r, m)
#     if wynik == testuj_wynik[i]:
#         print("OK")
#     else:
#         print("Nie powiodło się")

# ##Laboratorium 4.3.1.8
#
#
# def czy_przestepny(rok):
#     if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
#         return True
#     else:
#         return False
#
#
# def dni_w_miesiacu(rok, miesiac):
#     if czy_przestepny(rok) == True and miesiac == 2:
#         return 29
#     elif czy_przestepny(rok) == False and miesiac == 2:
#         return 28
#     elif miesiac in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
#     elif miesiac in [4, 6, 9, 11]:
#         return 30
#     else:
#         return None
#
#
# def dzien_w_roku(rok, miesiac, dzien):
#     if miesiac < 1 or miesiac > 12 or dzien < 1 or dzien > dni_w_miesiacu(rok,miesiac):
#         return None
#     else:
#         suma_dni = 0
#         for i in range(1, miesiac):
#             suma_dni += dni_w_miesiacu(rok, i)
#         suma_dni = suma_dni + dzien
#         return suma_dni
#
# print(dzien_w_roku(2000,12,31))
# print(dzien_w_roku(2000,12,21))
# print(dzien_w_roku(2001, 2, 29))
# print(dzien_w_roku(2019, 12, 31))
# print(dzien_w_roku(2020, 4, 30))
# print(dzien_w_roku(2020, 4, 25))

# ##Laboratorium 4.3.1.9
#
# def czy_pierwsza(liczba):
# 	for k in range(2, liczba):
# 		if liczba % k == 0:
# 			return False
# 	else:
# 		return True
#
# for i in range(1, 20):
# 	if czy_pierwsza(i + 1):
# 			print(i + 1, end=" ")
# print()

# ##Laboratorium 4.3.1.10
#
# def l100kmtompg(litry):
# 	galon = 3.785411784
# 	mila = 1.609344
# 	km_na_litr = 100/litry
# 	mil_na_litry = km_na_litr/mila
# 	mil_na_galon = mil_na_litry*galon
# 	return mil_na_galon
#
# def mpgtol100km(mpg):
# 	galon = 3.785411784
# 	mila = 1.609344
# 	kilometery = mpg * mila
# 	litry_na_100 = (100 / kilometery) * galon
# 	return litry_na_100
#
#
# print(l100kmtompg(3.9))
# print(l100kmtompg(7.5))
# print(l100kmtompg(10.))
# print(mpgtol100km(60.3))
# print(mpgtol100km(31.4))
# print(mpgtol100km(23.5))
#
