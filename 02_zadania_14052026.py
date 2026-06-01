# ####### ####### ####### ZADANIA – 2026.05.14 ####### ####### #######')
#
#
#
# ####### ####### ####### Zadanie 1 – Kino ####### ####### #######
# #
# #     Użytkownik podaje swój wiek
# #     – Jeśli ma mniej niż 12 lat → może obejrzeć tylko bajkę
# #     – Jeśli ma od 12 do 17 lat → zapytaj, czy ma zgodę rodzica
# #     – Jeśli tak → może wejść na film
# #     – Jeśli nie → tylko bajka
# #     – Jeśli ma 18 lub więcej → może obejrzeć dowolny film
#
# age_cinema = int(input('Podaj swój wiek. '))
#
# if 0 < age_cinema < 12:
#     print(f'Możesz obejrzeć tylko bajkę.')
# elif 12 <= age_cinema <=17:
#     pg = input(f'Czy masz zgodę rodzica? [T/N] ')
#     if pg.upper() == 'T':
#         print('Może wejść na film.')
#     else:
#         print(f'Możesz obejrzeć tylko bajkę.')
# elif age_cinema >= 18:
#     print(f'Może obejrzeć dowolny film.')
# else:
#     print('Jeszcze się nie urodziłeś!')
#
#
#
# ##### ####### ####### ZADANIE 2 – Biblioteka ###### ####### #######
# #
# #   Użytkownik podaje liczbę przeczytanych książek w tym miesiącu.
# #   Jeśli 0 → wypisz "Musisz zacząć czytać!".
# #   Jeśli od 1 do 3 → wypisz "Dobry początek".
# #   Jeśli 4 lub więcej → wypisz "Super, jesteś molem książkowym!".
#
# read_books = float(input('Ile książek przeczytałeś w tym miesiącu? '))
#
# if read_books == 0:
#     print('Musisz zacząć czytać!')
# elif 1 <= read_books <= 3:
#     print('Dobry początek.')
# elif read_books >= 4:
#     print('Super, jesteś molem książkowym!')
# else:
#     print('Podana liczba jest mniejsza niż ZERO.')
#
#
#
# ##### ####### ####### ZADANIE 3 – Pogoda ##### ####### #######
# #
# #   Użytkownik wpisuje temperaturę w °C.
# #   Jeśli poniżej 0 → "Mróz, ubierz czapkę".
# #   Jeśli od 0 do 15 → "Chłodno, załóż kurtkę".
# #   Jeśli powyżej 15 → "Ciepło, możesz iść w koszulce".
#
# temp = int(input('Podaj temperaturę w °C? '))
#
# if temp < 0:
#     print('Mróz – Ubierz czapkę!')
# elif 0 <= temp <= 15:
#     print('Chłodno – Załóż kurtkę!')
# else:
#     print('Ciepło – Możesz iść w koszulce.')
#
#
#
# ##### ####### ####### ZADANIE 4 – Zwierzę w domu ##### ####### #######
# #
# #   Użytkownik wpisuje, jakie ma zwierzę (pies, kot, rybka).
# #   Jeśli pies → zapytaj dodatkowo, czy lubi spacery.
# #   Jeśli tak → "Twój pies będzie szczęśliwy!".
# #   Jeśli nie → "Pies potrzebuje ruchu!".
# #   Jeśli kot → "Kot lubi drapanie i spanie".
# #   Jeśli rybka → "Pamiętaj o czystej wodzie".
# #   W innym przypadku → "Nie znam takiego zwierzaka".
#
# pet = input('Jakie masz zwierzę? Czy jest to: pies, kot czy rybka? ')

# if pet.lower() == 'pies' or 'kot' or 'rybka':
#     if pet.lower() == 'pies':
#         walk = input('Czy lubi spacery? [T/N] ')
#         if walk.upper() == 'T':
#             print('Twój PIES musi być bardzo szczęśliwy!')
#         else:
#             print('Pies potrzebuje ruchu!')
#     elif pet.lower() == 'kot':
#         print('Kot lubi drapanie i spanie.')
#     elif pet.lower() == 'rybka':
#         print('Pamiętaj o czystej wodzie.')
# else:
#     print('Nie znam takiego zwierzaka.')
#
# pet = input('Jakie masz zwierzę? Czy jest to: pies, kot czy rybka? ').lower().strip() # Lepszy sposób z tuplą
#
# if pet in ('pies', 'kot', 'rybka'):
#     if pet.lower() == 'pies':
#         walk = input('Czy lubi spacery? [T/N] ')
#         if walk.upper() == 'T':
#             print('Twój PIES musi być bardzo szczęśliwy!')
#         else:
#             print('Pies potrzebuje ruchu!')
#     elif pet.lower() == 'kot':
#         print('Kot lubi drapanie i spanie.')
#     elif pet.lower() == 'rybka':
#         print('Pamiętaj o czystej wodzie.')
# else:
#     print('Nie znam takiego zwierzaka.')

#
#
#
# ##### ####### ####### ZADANIE 5 – Zakupy ##### ####### #######
# #
# #   Operator trójargumentowy (ang. ternary operator), znany również jako wyrażenie warunkowe,
# #   to sposób na zapisanie prostej instrukcji if-else w jednej, zwięzłej linijce kodu.
# #
# #   Użytkownik podaje cenę produktu.
# #   Za pomocą TERNARY OPERATOR przypisz do zmiennej status:
# #   "Drogi", jeśli cena > 100,
# #   "Tani", jeśli cena ≤ 100.
#
# product_price = int(input('Podaj cenę produkty: '))
#
# # if product_price <= 100:
# #     print('Produkt jest TANI.')
# # else:
# #     print('Produkt jest DROGI.')
#
# print('Produkt jest TANI.') if product_price <= 100 else print('Produkt jest DROGI.')
#
#
# product_price = int(input('Podaj cenę produkty: '))
# #
# # if product_price <= 100:
# #     status = 'Tani'
# # else:
# #     status = 'Drogi'
# # print(status)
#
# status = 'Tani' if product_price <= 100 else 'Drogi'
# print(status)

#
#
#
# ##### ####### ####### ZADANIE 6 – Sprawdź poprawność wpisanego hasła.')
# #
# #   Użytkownik wpisuje hasło.
# #
# #   Program ma sprawdzić ##### Problem z niejednoznacznością wymagań hasła. Wiem, co ma sprawdzić, ale nie wiem, jakie warunki są oczekiwane.
# #   – Czy hasło ma minimum 8 znaków / Hasło ma się składać z minimum 8 znaków
# #   – Czy pierwszy znak NIE jest cyfrą / Hasło ma się zaczynać NIE-cyfrą
# #   – Czy w haśle znajduje się znak "!" lub "?" / Hasło NIE zawiera znaków "!" i "?"
# #   – Czy hasło nie zaczyna się i nie kończy tą samą literą / Hasło NIE zaczyna się i kończyć tą samym literą
# #
# #   Jeśli wszystkie warunki są spełnione:
# #   - wypisz "Hasło poprawne"
# #
# #   W przeciwnym razie:
# #   – wypisz konkretny powód błędu
#
# password = input('Podaj hasło: ')
# correct_password = True
#
# if len(password) < 8:
#     print('– Hasło MUSI mieć conajmniej 8 znaków.')
#     correct_password = False
# if password[0].isdigit():
#     print('– Pierwszy znak hasła NIE MOŻE być cyfrą.')
#     correct_password = False
# if '!' in password or '?' in password: # Odruchowo mam ochotę spisać "is in"
#     print('– Hasło NIE może zawierać znaku "!" lub "?".')
#     correct_password = False
# if password[0] == password[-1]:
#     print('– Hasło NIE może zaczyna się i kończy tym samym znakiem.')
#     correct_password = False
# if correct_password:
#     print('Hasło jest poprawne!')

password = input('Podaj hasło: ')
len_pass_cond = len(password) > 8
is_first_digit_cond = password[0].isdigit()
is_special_char_cond = '!' in password or '?' in password
is_first_equal_last_cond = password[0] == password[-1]

if len_pass_cond and not is_first_digit_cond and is_special_char_cond and is_first_equal_last_cond: # Zrób w ten sposób kolejne zadanie
    print('Hasło jest poprawne!')
else:
    if not len_pass_cond:
        print('Hasło jest za krótkie.')
    if is_first_digit_cond:
        print('Pierwsza znak nie może cyfrą.')
    if not is_special_char_cond:
        print('Musi zawierać znaki "!" oraz "?"')
    if not is_first_equal_last_cond:
        print('Pierwsza i ostatnia literma ma być taka sama')

# if len(password) < 8:
#     print('– Hasło MUSI mieć conajmniej 8 znaków.')
#     correct_password = False
# if password[0].isdigit():
#     print('– Pierwszy znak hasła NIE MOŻE być cyfrą.')
#     correct_password = False
# if '!' in password or '?' in password: # Odruchowo mam ochotę spisać "is in"
#     print('– Hasło NIE może zawierać znaku "!" lub "?".')
#     correct_password = False
# if password[0] == password[-1]:
#     print('– Hasło NIE może zaczyna się i kończy tym samym znakiem.')
#     correct_password = False
# if correct_password:
#     print('Hasło jest poprawne!')

#
#
#
# ##### ####### ####### ZADANIE 7 – Sprawdź poprawność wpisanego tekstu ##### ####### #######
# #
# #   Użytkownik wpisuje dowolny tekst
# #
# #   Program ma sprawdzić:
# #   – Czy tekst zaczyna się od "@"
# #   – Czy kończy się liczbą
# #   – Czy środkowy znak tekstu to litera "x"
# #
# #   Jeśli wszystkie warunki są spełnione:
# #   – Wypisz "Wiadomość zaakceptowana"
# #
# #   W przeciwnym razie:
# #   – Wypisz, który warunek nie został spełniony
# #
# #   Dodatkowe utrudnienie:
# #   Program powinien działać również dla tekstów o parzystej długości tekstu
#
#
# text = input('Wpisz dowolny tekst: ')
# center = len(text) // 2
# correct_text = True
#
# if text[0] != '@':
#     print('– Tekst MUSI zaczynać się od @.')
#     correct_text = False
# if text[-1].isalpha():
#     print('– Tekst MUSI kończyć się liczbą.')
#     correct_text = False
# if text[center] != 'x': # TUTAJ mam Problem
#     print('– Środkowym znakiem tekstu MUSI być X.')
#     correct_text = False
# if correct_text:
#     print('Wiadomość zaakceptowana.')
#
# # if text[center] or text[center+1] != 'x':
#
#
#
# ##### ####### ####### ZADANIE 8 – Sprawdź poprawność nicku ##### ####### #######
# #
# #   Użytkownik wpisuje nick w formacie:
# #
# #   imie#123
# #
# #   Program ma sprawdzić:
# #   - Czy nick zawiera dokładnie jeden znak "#"
# #   - Czy część przed "#" ma minimum 3 znaki.
# #   – Czy część po "#" składa się wyłącznie z cyfr.
# #   - Czy numer po "#" ma dokładnie 3 cyfry.
# #   - Czy pierwsza litera nicku jest wielka.
# #
# #   Jeśli wszystko jest poprawne:
# #   - Wypisz "Nick poprawny"
# #
# #   W przeciwnym razie:
# #   - Wypisz konkretny powód błędu
#
# nick = input('Wpisz NICK w formacie imię#123: ')
# index_nick = nick.find("#")
# correct_nick = True
#
# if len(nick[:index_nick]) < 3:
#     print('– Przed # MUSZĄ się znaleźć przynajmniej 3 znaki.')
#     correct_nick = False
# if nick.count('#') != 1:
#     print('– Nick MUSI zawierać dokładnie jeden znak #.')
#     correct_nick = False
# if not nick[index_nick+1:].isdigit():
#     print('– Po znaku # mogą się znaleźć wyłącznie z cyfr.')
#     correct_nick = False
# if int(len(nick[index_nick+1:])) != 3:
#     print('– Po znaku # MUSZĄ się znaleźć dokładnie 3 cyfry.')
#     correct_nick = False
# if correct_nick:
#     print('Nick poprawny!')