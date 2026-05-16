print()
print('####### ####### ####### ZADANIA – 2026.05.11 ####### ####### #######')
print()

print('ZADANIE 1 – Sklep komputerowy. Ceny brutto')
print()

# ## 1. sklep komputerowy – ceny brutto
# utwórz zmienne dla 4 produktów:
# – klawiatura
# – myszka
# – monitor
# – słuchawki
#
# dodaj stawkę vat i oblicz:
# – cenę brutto każdego produktu
# – sumę wszystkich produktów
# i
# na końcu wypisz wynik w czytelnej formie.
#
# Przykład:
# monitor kosztuje: 1229,99 zł brutto

keyboard, mouse, monitor, headphones = 120, 55, 2000, 250
tax_rate = 0.23
keyboard_brutto = keyboard + (keyboard * tax_rate)
mouse_brutto = mouse + (mouse * tax_rate)
monitor_brutto = monitor + (monitor * tax_rate)
headphones_brutto = headphones + (headphones * tax_rate)

print(f'Klawiatura kosztuje: {keyboard_brutto:.2f} zł brutto') # f-string rounding
print(f'Myszka kosztuje: {mouse_brutto:.2f} zł brutto')
print(f'Monitor kosztuje: {monitor_brutto:.2f} zł brutto')
print(f'Słuchawki kosztują: {headphones_brutto:.2f} zł brutto')

print()
print('Za wszystko zapłacisz:', keyboard_brutto + mouse_brutto + monitor_brutto + headphones_brutto, 'zł brutto')

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 2 – Dane użytkownika')
print()

# ## 2. dane użytkownika
# utwórz zmienne:
# – imię
# – wiek
# – wzrost
#
# wyświetl jedno zdanie wykorzystując:
# - konkatenację (+)
# - f-string
#
# przykład:
# Cześć! Mam na imię ania, mam 25 lat i 168.5 cm wzrostu.

name = 'Aga'
age, height = 40, 165
welcome_text_1 = 'Cześć! Mam na imię ' + name +', ' 'mam ' + str(age) + ' lat i ' + str(height) + ' cm wzrostu.'
# lub
welcome_text_2 = f'Cześć! Mam na imię {name}, mam {age} lat i {height} cm wzrostu.'

print(welcome_text_1)
print(welcome_text_2)

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 3 – Matematyczny kalkulator')
print()

# ## 3. matematyczny kalkulator
# dla liczb:
# a = 15
# b = 4
#
# oblicz:
# - dodawanie
# – odejmowanie
# – mnożenie
# – dzielenie
# – potęgowanie
# – dzielenie całkowite
# – modulo
#
# wypisz wszystkie wyniki.

a, b = 15, 4

print('Operacje arytmetyczne dla liczb 15 i 4.' )
print('Dodawanie:', a + b)
print('Odejmowanie:', a - b)
print('Mnożenie:', a * b)
print('Potęgowanie:', a ** b)
print('Dzielenie:', a / b)
print('Dzielenie całkowite:', a // b)
print('Dzielenie modulo:', a % b)

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 4 – Czy liczba jest parzysta?')
print()

# ## 4. czy liczba jest parzysta?
# utwórz zmienną:
# number = 17
#
# sprawdź za pomocą operatora modulo:
# – czy liczba jest parzysta
# – czy jest nieparzysta

number = 17
modulo_number = 17 % 2

print('Czy liczba 17 jest parzysta?', number == modulo_number)
print('Czy liczba 17 jest nieparzysta?', number != modulo_number)

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 5 – Formatowanie liczby pi')
print()

#  ## 5. formatowanie liczby pi
# utwórz zmienną:
# pi = 3.14159265359
#
# wyświetl:
# – pi zaokrąglone do 2 miejsc
# – pi zaokrąglone do 4 miejsc
# – pi jako integer

pi = 3.14159265359

print(f'Liczba PI zaokrąglona do 2 miejsc po przecinko wynosi: {pi:.2f}')
print(f'Liczba PI zaokrąglona do 4 miejsc po przecinko wynosi: {pi:.4f}')
print('Liczba PI jako INTEGER to:', int(pi))

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 6 – Generator loginu')
print()

# ## 6. generator loginu
# utwórz zmienne:
# – imię
# – nazwisko
# – rok urodzenia
#
# stwórz login według schematu:
# imię_nazwisko_rok
#
# wszystko ma być małymi literami.
#
# przykład:
# jan_kowalski_1999

name = input('Jak masz na imię? ')
last_name = input('Jak się się nazywasz? ')
birth_date = input('Podaj rok urodzenia? ')
print()

print(f'Twój login to: {name}{last_name}{birth_date}')

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 7 – Operacje na stringach')
print()

# ## 7. operacje na stringach
# dla zmiennej:
# city = "kraków"
#
# wyświetl:
# – wszystko wielkimi literami
# – wszystko małymi literami
# – pierwsze litery wielkie (title())

city = 'kraków'

print(city.upper())
print(city.lower())
print(city.title())

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 8 – Konwerter temperatury')
print()

# ## 8. konwerter temperatury
# utwórz zmienną:
# celsius = 28
#
# przelicz temperaturę na fahrenheit według wzoru:
#
# f = c * 9/5 + 32
#
# wypisz wynik.

# celsius = 28
# fahr_temp = celsius * 9/5 + 32
# print(fahr_temp * 9/5 + 32) # Nieaktywny kalkulator z zadania (przelicz 28 stopni Celsjusza na stopnie Fahrenheita)

celsius_2 = input('Podaj wartość temperatury w stopniach Celsjusza, którą chcesz przeliczyć: ')
fahr_temp_2 = int(celsius_2) * 9/5 + 32

print('Podana temperatura w stopniach Fahrenheita wynosi:', int(fahr_temp_2)) # Dodałem kalkulator temperatury wpisanej przez użytkownika

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 9 – Mini profil gracza')
print()

# ## 9. mini profil gracza
# utwórz zmienne:
# – nick gracza
# – liczba punktów
# – poziom
# – liczba żyć
#
# wypisz ładne podsumowanie profilu gracza.
#
# dodaj zaokrąglenie punktów, jeśli będą floatem.

player_nick = input('Podaj ksywkę? ')
player_lvl = float(input('Podaj aktualny poziom swojej postaci? '))
player_pts = float(input('Podaj aktualną liczbę punktów doświadczenia? '))
player_hp = float(input('Podaj aktualną liczbę punktów życia? '))

print()
print('       PROFIL GRACZA:', player_nick.upper())
print('      Poziom postaci:', round(player_lvl))
print(f'Punkty doświadczenia: {round(player_pts)}')
print(f'        Punkty życia: {round(player_hp)}')
# Czy istnieje inny sposób, aby wiersze zostały wyrównane jeden pod drugim (na wysokości dwukropka), aby wyświetlały w taki sposób, w jaki ułożyły się w wyniku print?

print()
print('--------------------------------------------------------------------')
print()

print(' ZADANIE 10 – Porównania liczb')
print()

# ## 10. porównania liczb
# dla:
# x = 12
# y = 20
#
# sprawdź:
# – czy x jest większe od y
# – czy są równe
# – czy x jest różne od y
# – czy x jest mniejsze lub równe y

x = 12
y = 20

print('Czy 12 jest większe od 20?', x > y)
print('Czy 12 jest równe 20?', x == y)
print('Czy 12 jest różne od 20?', x != y)
print('Czy 12 jest większe od 20?', x < y)

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 11 – Rachunek w restauracji')
print()

# ## 11. rachunek w restauracji
# masz:
# – cenę pizzy
# – cenę napoju
# – cenę deseru
#
# oblicz:
# – sumę zamówienia
# – napiwek 10%
# – końcową kwotę do zapłaty

pizza_price = float(input('    Cena pizzy: '))
drink_price = float(input('   Cena napoju: '))
dessert_price = float(input('   Cena ciasta: '))
tip = 0.1
price = pizza_price + drink_price + dessert_price
tip_price = (pizza_price + drink_price + dessert_price) * tip

print()
print(f'Rachunek netto: {price:.2f} zł')
print(f'   Napiwek 10%: {tip_price:.2f} zł')
print(f'    DO ZAPŁATY: {price + tip_price:.2f} zł')

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 12 – Tajny napis')
print()

# ## 12. tajny napis
# utwórz zmienną:
# message = "python jest super"
#
# wyświetl:
# - cały napis wielkimi literami
# - długość napisu (len())
# - napis powtórzony 3 razy

message = "Python jest super"
print(f'Wyświetl cały napis wielkimi iterami: {message.upper()}')
print(f'Długość napisu: {len(message)}')
print(f'Wyświetl cały napis 3x: {message*3}')

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 13 – Budżet wakacyjny')
print()

# ## 13. budżet wakacyjny
# masz budżet:
# budget = 2500
#
# koszty:
# – hotel
# – transport
# – jedzenie
#
# oblicz:
# – ile pieniędzy zostanie po wakacjach
# – czy budżet wystarczy

budget = 2500
hotel = float(input('Koszt hotelu: '))
transport = float(input('Koszt transportu: '))
food = float(input('Koszt wyżywienia: '))
total_expenses = (hotel + transport + food)

print()

print('Wakacyjny budżet wynosił: 2500 zł')
# print('Wydaliśmy:', (round(total_expenses, 2)))
print('Po wakacjach zostało nam:', (round((budget - total_expenses), 2)) , 'zł')
print('Czy zmieściliśmy się w budżecie?', budget >= total_expenses)


print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 14 – Super proste BMI')
print()

# ## 14. super proste bmi
# utwórz:
# - wagę
# - wzrost w metrach
#
# oblicz bmi według wzoru:
#
# bmi = m / h^2
#
# wypisz wynik zaokrąglony do 2 miejsc po przecinku przy pomocy f-string

weight = float(input('Podaj swoją wagę: '))
height = float(input('Podaj swój wzrost (w metrach): '))
bmi = weight / (height ** 2)

print('Twoje BMI wynosi:', (round(bmi, 2)))
# lub
print(f'Twoje BMI wynosi: {bmi:.2f}')

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 15 – Błąd do znalezienia')
print()

# ## 15. błąd do znalezienia
# co jest nie tak w tym kodzie?
#
# age = "25"
# result = age + 5
#
# print(result)
#
# popraw kod tak, aby działał poprawnie.

age = 25
result = age + 5

print(result, '– Zmienna "age" była STRINGIEM, więc nie można jej było dodać do liczby.')

print()
print('--------------------------------------------------------------------')
print()