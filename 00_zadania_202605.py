# ####### ####### ####### ZADANIA – 2026.05.11 ####### ####### #######
#
#
#
# ####### ####### ####### ZADANIE 1 – Sklep komputerowy – ceny brutto ####### ####### #######
# #
# # Utwórz zmienne dla 4 produktów:
# # – klawiatura
# # – myszka
# # – monitor
# # – słuchawki
# #
# # Dodaj stawkę vat i oblicz:
# # – cenę brutto każdego produktu
# # – sumę wszystkich produktów
# #
# # Na końcu wypisz wynik w czytelnej formie.
# #
# # Przykład:
# # monitor kosztuje: 1229,99 zł brutto
#
# keyboard, mouse, monitor, headphones = 120, 55, 2000, 250
# tax_rate = 0.23
# keyboard_brutto = keyboard + (keyboard * tax_rate)
# mouse_brutto = mouse + (mouse * tax_rate)
# monitor_brutto = monitor + (monitor * tax_rate)
# headphones_brutto = headphones + (headphones * tax_rate)
#
# print(f'Klawiatura kosztuje: {keyboard_brutto:.2f} zł brutto') # f-string rounding
# print(f'Myszka kosztuje: {mouse_brutto:.2f} zł brutto')
# print(f'Monitor kosztuje: {monitor_brutto:.2f} zł brutto')
# print(f'Słuchawki kosztują: {headphones_brutto:.2f} zł brutto')
# print('Za wszystko zapłacisz:', keyboard_brutto + mouse_brutto + monitor_brutto + headphones_brutto, 'zł brutto \n')
#
#
#
# ####### ####### ####### ZADANIE 2 – Dane użytkownika ####### ####### #######
# #
# # Utwórz zmienne:
# # – imię
# # – wiek
# # – wzrost
# #
# # Wyświetl jedno zdanie wykorzystując:
# # - konkatenację (+)
# # - f-string
# #
# # Przykład:
# # Cześć! Mam na imię ania, mam 25 lat i 168.5 cm wzrostu.

# name, age, height = 'Aga', 40, 165
# print('Cześć! Mam na imię ' + name +', ' 'mam ' + str(age) + ' lat i ' + str(height) + ' cm wzrostu.')
# # lub
# print(f'Cześć! Mam na imię {name}, mam {age} lat i {height} cm wzrostu.')
#
#
#
# ####### ####### ####### ZADANIE 3 – Matematyczny kalkulator ####### ####### #######
# #
# # Dla liczb:
# # a = 15
# # b = 4
# #
# # Oblicz:
# # - dodawanie
# # – odejmowanie
# # – mnożenie
# # – dzielenie
# # – potęgowanie
# # – dzielenie całkowite
# # – modulo
# #
# # Wypisz wszystkie wyniki.
#
# a, b = 15, 4
#
# print('Operacje arytmetyczne dla liczb 15 i 4.' )
# print(f'Dodawanie: {a + b}')
# print('Odejmowanie:', a - b)
# print('Mnożenie:', a * b)
# print('Potęgowanie:', a ** b)
# print('Dzielenie:', a / b)
# print('Dzielenie całkowite:', a // b)
# print('Dzielenie modulo:', a % b)
#
#
#
# ####### ####### ####### 4 – Czy liczba jest parzysta? ####### ####### #######
# #
# # Utwórz zmienną:
# # number = 17
# #
# # Sprawdź za pomocą operatora modulo:
# # – czy liczba jest parzysta
# # – czy jest nieparzysta
#
# number = 17
# print('Czy liczba 17 jest parzysta?', number % 2 == 0)
# print('Czy liczba 17 jest nieparzysta?', number % 2 == 1)
#
#
#
# ####### ####### ####### ZADANIE 5 – Formatowanie liczby pi ####### ####### #######
# #
# # utwórz zmienną:
# # pi = 3.14159265359
# #
# # Wyświetl:
# # – pi zaokrąglone do 2 miejsc
# # – pi zaokrąglone do 4 miejsc
# # – pi jako integer
#
# pi = 3.14159265359
#
# print(f'Liczba PI zaokrąglona do 2 miejsc po przecinko wynosi: {pi:.2f}')
# print(f'Liczba PI zaokrąglona do 4 miejsc po przecinko wynosi: {pi:.4f}')
# print('Liczba PI jako INTEGER to:', round(pi, 2))

#
#
# ####### ####### ####### ZADANIE 6 – Generator loginu ####### ####### #######
# #
# # Utwórz zmienne:
# # – imię
# # – nazwisko
# # – rok urodzenia
# #
# # Stwórz login według schematu:
# # imię_nazwisko_rok
# #
# # Wszystko ma być małymi literami.
# #
# # Przykład:
# # jan_kowalski_1999
#
# name = input('Jak masz na imię? ')
# last_name = input('Jak się się nazywasz? ')
# birth_date = input('Podaj rok urodzenia? ')
# print()
#
# print(f'Twój login to: {name.lower()}_{last_name.lower()}_{birth_date.lower()}')
#
#
#
# ####### ####### ####### ZADANIE 7 – Operacje na stringach ####### ####### #######
# #
# # Dla zmiennej:
# # city = "kraków"
# #
# # Wyświetl:
# # – wszystko wielkimi literami
# # – wszystko małymi literami
# # – pierwsze litery wielkie (title())
#
# city = 'nowy sącz'
#
# print(city.upper())
# print(city.lower())
# print(city.title())
# print(city.capitalize())
#
#
#
# ####### ####### ####### ZADANIE 8 – Konwerter temperatury ####### ####### #######
# #
# # Utwórz zmienną:
# # celsius = 28
# #
# # Przelicz temperaturę na fahrenheit według wzoru:
# # f = c * 9/5 + 32
# #
# # Wypisz wynik.
#
# celsius = 28
# print(f'Temperatura 28°C jest równa {(celsius * 9/5 + 32)}°F.')
#
# # lub kalkulator, który przelicza temperaturę podaną przez użytkownika.
#
# celsius_2 = int(input('Podaj wartość temperatury w °C, którą chcesz przeliczyć na °F: '))
# print(f'Temperatura {celsius_2}°C jest równa {(celsius_2 * 9/5 + 32)}°F.')
#
#
#
# ####### ####### ####### ZADANIE 9 – Mini profil gracza ####### ####### #######
# #
# # Utwórz zmienne:
# # – nick gracza
# # – liczba punktów
# # – poziom
# # – liczba żyć
# #
# # Wypisz ładne podsumowanie profilu gracza.
# #
# # Dodaj zaokrąglenie punktów, jeśli będą floatem.
#
# player_nick = input('Podaj ksywkę? ')
# player_lvl = float(input('Podaj aktualny poziom swojej postaci? '))
# player_pts = float(input('Podaj aktualną liczbę punktów doświadczenia? '))
# player_hp = float(input('Podaj aktualną liczbę punktów życia? '))
#
# print()
# print('       PROFIL GRACZA:', player_nick.upper())
# print('      Poziom postaci:', round(player_lvl))
# print(f'Punkty doświadczenia: {round(player_pts)}')
# print(f'        Punkty życia: {round(player_hp)}')
# Czy istnieje inny sposób, aby wiersze zostały wyrównane jeden pod drugim (na wysokości dwukropka), aby wyświetlały w taki sposób, w jaki ułożyły się w wyniku print?

#
#
# ####### ####### ####### ZADANIE 10 – Porównania liczb ####### ####### #######
# #
# # Dla:
# # x = 12
# # y = 20
# #
# # Sprawdź:
# # – czy x jest większe od y
# # – czy są równe
# # – czy x jest różne od y
# # – czy x jest mniejsze lub równe y
#
# x = 12
# y = 20
#
# print('Czy 12 jest większe od 20?', x > y)
# print('Czy 12 jest równe 20?', x == y)
# print('Czy 12 jest różne od 20?', x != y)
# print('Czy 12 jest mniejsze od 20?', x < y)
#
#
#
# ####### ####### ####### ZADANIE 11 – Rachunek w restauracji ####### ####### #######
# #
# # Masz:
# # – cenę pizzy
# # – cenę napoju
# # – cenę deseru
# #
# # Oblicz:
# # – sumę zamówienia
# # – napiwek 10%
# # – końcową kwotę do zapłaty
#
# pizza_price = float(input('    Cena pizzy: '))
# drink_price = float(input('   Cena napoju: '))
# dessert_price = float(input('   Cena ciasta: '))
# tip = 0.1
# price = pizza_price + drink_price + dessert_price
# tip_price = (pizza_price + drink_price + dessert_price) * tip
#
# print()
# print(f'   Rachunek: {price:.2f} zł')
# print(f'Napiwek 10%: {tip_price:.2f} zł')
# print(f' DO ZAPŁATY: {price + tip_price:.2f} zł')
#
#
#
# ####### ####### ####### ZADANIE 12 – Tajny napis ####### ####### #######
# #
# # Utwórz zmienną:
# # message = "python jest super"
# #
# # Wyświetl:
# # - cały napis wielkimi literami
# # - długość napisu (len())
# # - napis powtórzony 3 razy
#
# message = "Python jest super"
# print(f'Wyświetl cały napis wielkimi iterami: {message.upper()}')
# print(f'Długość napisu: {len(message)}')
# print(f'Wyświetl cały napis 3x: {message * 3}')
#
#
#
# ####### ####### ####### ZADANIE 13 – Budżet wakacyjny ####### ####### #######
# #
# # Masz:
# # budget = 2500
# #
# # Koszty:
# # – hotel
# # – transport
# # – jedzenie
# #
# # Oblicz:
# # – ile pieniędzy zostanie po wakacjach
# # – czy budżet wystarczy
#
# budget = 2500
# hotel = float(input('Koszt hotelu: '))
# transport = float(input('Koszt transportu: '))
# food = float(input('Koszt wyżywienia: '))
# total_expenses = (hotel + transport + food)
#
# print()

# print('Wakacyjny budżet wynosił: 2500 zł')
# print('Wydaliśmy:', (round(total_expenses, 2)))
# print('Po wakacjach zostało nam:', (round((budget - total_expenses), 2)) , 'zł')
# print('Czy zmieściliśmy się w budżecie?', budget >= total_expenses)
# lib w f-string
# print('Wakacyjny budżet wynosił: 2500 zł')
# print(f'Wydaliśmy: {(round(total_expenses, 2))}.')
# print(f'Po wakacjach zostało nam: {(round((budget - total_expenses), 2))}), zł.')
# print(f'Czy zmieściliśmy się w budżecie? {budget >= total_expenses}')

#
#
# ####### ####### ####### ZADANIE 14 – Super proste BMI ####### ####### #######
# #
# # Utwórz:
# # – wagę
# # – wzrost w metrach
# #
# # Oblicz bmi według wzoru: bmi = m / h^2
# # Wypisz wynik zaokrąglony do 2 miejsc po przecinku przy pomocy f-string
#
# weight = float(input('Podaj swoją wagę: '))
# height = float(input('Podaj swój wzrost (w metrach): '))
# bmi = weight / (height ** 2)
#
# print('Twoje BMI wynosi:', (round(bmi, 2)))
# # lub
# print(f'Twoje BMI wynosi: {bmi:.2f}')
#
#
#
# ####### ####### ####### ZADANIE 15 – Błąd do znalezienia ####### ####### #######
# #
# # Co jest nie tak w tym kodzie?
# #
# # age = '25'
# # result = age + 5
# #
# # print(result)
# #
# # Popraw kod tak, aby działał poprawnie.
#
age = 25
# lub
# age = int('25')
result = age + 5

print(f'{result} – Zmienna "age" była STRINGIEM, więc nie można jej było dodać do LICZBY.')
#
# ####### ####### ####### ####### ####### ####### ####### #######
