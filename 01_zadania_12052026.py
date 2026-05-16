print()
print('####### ####### ####### ZADANIA – 2026.05.12 ####### ####### #######')
print()

print('ZADANIE 1 — Ukryte rozszerzenie pliku')
print()

    # filename = "raport_finansowy_2026_final.csv"
    #
    # Bez używania:
    # - endswith()
    # - split()
    #
    # sprawdź:
    #     1. czy plik ma rozszerzenie .csv
    #     2. jaka jest nazwa pliku bez rozszerzenia
    #     3. jakie są 3 ostatnie znaki przed kropką
    #
    # podpowiedź – użyj metody find

filename = 'raport_finansowy_2026_final.csv'

print(f'Czy plik ma rozszerzenie .csv (metoda: find)? {filename.find('.csv')!=-1}')
# Wydaje mi się, że zastosowanie metody find() nie jest najlepszym rozwiązaniem.
# Jeśli plik będzie zawierał błąd w środku rozszerzenia np. cssv, to rzeczywiście nie ma problemu.
# Jednak, jeśli plik będzie zawierał błąd na końcu rozszerzenia np. csvv, to zwróci True,
# ponieważ rozszerzenie .csv wciąż znajdzie się w tekście, a przecież nie o to nam chodzi.
# Lepszym rozwiązaniem wydaje zastosowanie string() – jak niżej
print(f'Czy plik ma rozszerzenie .csv (metoda: slicing)? {filename[-4:]=='.csv'}')
# print(f'Rozszerzenie pliku to: {filename[-4:]}')

print(f'Nazwa pliku (bez rozszerzenia) to: {filename[:-4]}')
#lub
print(f'Nazwa pliku (bez rozszerzenia) to: {filename[:filename.find('.')]}')

print(f'Trzy ostatnie znaki przed kropką to: {filename[-7:-4]}')
#lub
print(f'Trzy ostatnie znaki przed kropką to: {filename[-7:filename.find('.')]}')


print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 2 — Środek napisu')
print()

#     text = "ProgramowaniePython"
#
#     1. Znajdź środkowy indeks napisu.
#     2. Jeśli długość tekstu jest parzysta:
#        - wypisz 2 środkowe znaki
#     3. Jeśli nieparzysta:
#        - wypisz 1 środkowy znak
#
#     spróbuj zrobić to samym slicingiem i len().

text = 'ProgramowaniePython'
text_lenght = len(text)
text_center = text_lenght // 2

# print(f"Długość zdania: {text_lenght}")
print(f"Index środka: {text_center}")

if text_lenght % 2 == 0:
    print(f'Liczba znaków w tekście jest parzysta, a jej dwa środkowe znaki to: {text[text_center -1: text_center +1]}')
else:
    print(f"Liczba znaków w tekście nieparzysta, a jej środkowy znak to: {text[text_center]}")

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 3 — Odwracanie fragmentów')
print()

#     sentence = "Python jest super"
#
#     Utwórz nowe zmienne:
#
#     1. pierwszy wyraz od tyłu
#     2. ostatni wyraz od tyłu
#     3. cały napis od tyłu
#     4. cały napis co drugi znak
#
#     Przykład:
#     "Python" -> "nohtyP"

sentence = "Python jest super"

first_word_back = sentence[5::-1]
lost_word_back = sentence[:-6:-1]
all_sentence_back = sentence[::-1]
all_sentence_3nd_char = sentence[::2]

pierwsza_spacja = sentence.find(' ')
druga_spacja = sentence.find(' ', pierwsza_spacja +1)

print(f'Zdanie: Python jest super')
print()

print(f'1. Pierwszy wyraz od tyłu: {first_word_back}')
# lub
print(f'1. Pierwszy wyraz od tyłu: {sentence[sentence.find(' ') -1::-1]}')

print(f'2. Ostatni wyraz od tyłu: {lost_word_back}')
# lub
print(f'2. Ostatni wyraz od tyłu: {sentence[:druga_spacja:-1]}')

print(f'3. Cały napis od tyłu: {all_sentence_back}')
print(f'4. Cały napis co drugi znak: {all_sentence_3nd_char}')

# lub bez tworzenia zmiennych.

# print(f'1. Pierwszy wyraz od tyłu: {sentence[5::-1]}')
# print(f'2. Ostatni wyraz od tyłu: {sentence[:-6:-1]}')
# print(f'3. Cały napis od tyłu: {sentence[::-1]}')
# print(f'4. Cały napis co drugi znak: {sentence[::2]}')

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 4 — Wyciąganie danych z kodu produktu')
print()

# ## Zadanie 4 — wyciąganie danych z kodu produktu
#
#     # product_code = "LAPTOP-DELL-2026-PRO"
#     #
#     # Bez używania split():
#     #
#     # 1. wyciągnij nazwę marki (DELL)
#     # 2. wyciągnij rok (2026)
#     # 3. wyciągnij ostatni fragment (PRO)
#     # 4. sprawdź, czy kod kończy się na "PRO" bez użycia endswith()
#     #
#     # Podpowiedź:
#     # użyj indeksowania, slicing oraz find()

product_code = 'LAPTOP-DELL-2026-PRO'

print(f'Produkt: LAPTOP-DELL-2026-PRO')
print()

print(f'Nazwa marki: {product_code[7:11]}')
# # lub
# print(f'Nazwa marki: {product_code[product_code.index('DELL'):product_code.index('-')]}')

print(f'Rok: {product_code[-8:-4]}')
# #lub
# print(f'Rok: {product_code[product_code.index('2026'):product_code.index('-')]}')

print(f'Ostatni fragment to: {product_code[-3:]}')
#lub
print(f'Ostatni fragment to: {product_code[product_code.index('PRO'):]}')

print(f'Czy kod kończy się na "PRO" (Metoda: slicing)? {product_code[-3:]=='PRO'}') #Jak w zadaniu 1 – lepsza metoda
# lub
print(f'Czy kod kończy się na "PRO" (Metoda: find)? {product_code.find('PRO')!= -1}') #Jak w zadaniu 1 – gorsza metoda

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 5 — Maskowanie numeru telefonu')
print()

#     # phone = "123456789"
#     #
#     # Stwórz nowy napis w formacie:
#     #
#     # "*****6789"
#     #
#     # czyli:
#     # - wszystkie cyfry poza ostatnimi 4 mają zostać zamienione na *
#     #
#     # Dodatkowo:
#     # – policz, ile gwiazdek trzeba dodać automatycznie, na podstawie długości napisu.

phone = '123456789'
# phone_pt1 = phone[:-4]
# print(phone_pt1)

print(f'Zaszyfrowany numer telefonu (sposób 1): {phone.replace('12345', '*****')}')
# lub
print(f'Zaszyfrowany numer telefonu (sposób 2): {phone.replace(phone[:-4], '*****')}')
# lub

# stars_needed = (len(phone) - 4)
# changed_half = '*' * (len(phone) - 4)
# unchanged_half = phone[-4:]
# print(stars_needed)
# print(changed_half)
# print(unchanged_half)

print(f'Zaszyfrowany numer telefonu (sposób 3): {'*' * (len(phone) - 4) + phone[-4:]}')

print(f'Aby zamienic cały numer telefony na gwiazdki trzeba użyć {len(phone)} gwiazdek.')
print(f'Cały numer telefony zamieniony na gwiazdki: {'*' * (len(phone))}')

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 6 – E-mail')
print()

#      email = "jan.kowalski@example.com"
#
#      1. wyciągnij login (jan.kowalski)
#      2. wyciągnij domenę (example.com)
#      3. sprawdź czy email jest z domeny .com
#      4. wypisz pierwsze 3 znaki loginu
#      5. wypisz domenę od tyłu

email = 'jan.kowalski@example.com'

print(f'jan.kowalski@example.com')
print()

print(f'Login: {email[0:12]}')
#lub
print(f'Login: {email[:email.index('@')]}')

print(f'Domena: {email[-12:]}')
# lub
print(f'Domena: {email[email.index('@'):]}')

print(f'Czy email jest z domeny .com? (metoda: slicing)? {email[-4:] == '.com'}')
# lub
print(f'Czy email jest z domeny .com? (metoda: endswith) {email.endswith('.com')}')

print(f'Pierwsze 3 znaki loginu: {email[:3]}')
print(f'Domena od tyłu: {email[:-4:-1]}')
# lub
print(f'Domena od tyłu: {email[:email.index('com') - 1:-1]}')

print()
print('--------------------------------------------------------------------')
print()
