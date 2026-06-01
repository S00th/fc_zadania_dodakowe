# ####### ####### ####### ZADANIA – 2026.05.12 ####### ####### #######')
#
#
# ####### ####### ####### ZADANIE 1 — Ukryte rozszerzenie pliku ####### ####### #######
#
#     # filename = "raport_finansowy_2026_final.csv"
#     #
#     # Bez używania:
#     # - endswith()
#     # - split()
#     #
#     # Sprawdź:
#     #     1. Czy plik ma rozszerzenie .csv
#     #     2. Jaka jest nazwa pliku bez rozszerzenia
#     #     3. Jakie są 3 ostatnie znaki przed kropką
#     #
#     # Podpowiedź – Użyj metody find
#
# filename1 = 'raport_finansowy_2026_final.csv'
# filename2 = 'raport_finansowy_2026_final.cssv'
# filename3 = 'raport_finansowy_2026_final.csvv'
#
# print(f'Czy plik ma rozszerzenie .csv (metoda: find)? {filename1.find('.csv')!=-1}')
# # Wydaje mi się, że zastosowanie metody find() nie jest najlepszym rozwiązaniem.
# # Plik może zawierać błąd nie tylko w środku rozszerzenia (cssv), ale też an końcu (csvv).
# print(f'Czy plik ma rozszerzenie .csv (metoda: find)? {filename2.find('.csv')!=-1}')
# print(f'Czy plik ma rozszerzenie .csv (metoda: find)? {filename3.find('.csv')!=-1}')
# # Lepszym rozwiązaniem wydaje zastosowanie string() – jak niżej
# print(f'Czy plik ma rozszerzenie .csv (metoda: slicing)? {filename1[-4:]=='.csv'}')
# print(f'Czy plik ma rozszerzenie .csv (metoda: slicing)? {filename2[-4:]=='.csv'}')
# print(f'Czy plik ma rozszerzenie .csv (metoda: slicing)? {filename3[-4:]=='.csv'}') # Najlepsza metoda!!!
# # print(f'Rozszerzenie pliku to: {filename1[-4:]}')
#
# print(f'Nazwa pliku (bez rozszerzenia) to: {filename1[:-4]}')
# #lub
# print(f'Nazwa pliku (bez rozszerzenia) to: {filename1[:filename1.find('.')]}') # Policz ile jest kropek w tekści, można w stne sposób jesli jets tylko jedna kropka
#
# print(f'Trzy ostatnie znaki przed kropką to: {filename1[-7:-4]}')
# #lub
# print(f'Trzy ostatnie znaki przed kropką to: {filename1[-7:filename1.find('.')]}')
# #lub
# print(f'Trzy ostatnie znaki przed kropką to: {filename1[filename1.find('.')-3:filename1.find('.')]}')
#
#
#
# ####### ####### ####### ZADANIE 2 — Środek napisu ####### ####### #######
#
# #     text = "ProgramowaniePython"
# #
# #     1. Znajdź środkowy indeks napisu.
# #     2. Jeśli długość tekstu jest parzysta:
# #        - Wypisz 2 środkowe znaki
# #     3. Jeśli nieparzysta:
# #        - Wypisz 1 środkowy znak
# #
# #     Spróbuj zrobić to samym slicingiem i len().
#
# text = 'ProgramowaniePythonn'
# text_lenght = len(text)
# text_center = text_lenght // 2
#
# print(f"Długość zdania: {text_lenght}")
# print(f"Index środka: {text_center}")
# # print(text_center -1)
# # print(text_center)
# # print(text_center +1)
# # print(text[text_center -1: text_center +1]) # Druga wartość zakresu jest brana bez ostatniego znaku zakresu, dlatego trzeba dodać +1.
#
# if text_lenght % 2 == 0:
#     print(f'Liczba znaków w tekście jest parzysta, a jej dwa środkowe znaki to: {text[text_center -1: text_center +1]}')
# else:
#     print(f"Liczba znaków w tekście nieparzysta, a jej środkowy znak to: {text[text_center]}")
#
#
#
# ####### ####### ####### ZADANIE 3 — Odwracanie fragmentów ####### ####### #######
#
# #     sentence = "Python jest super"
# #
# #     Utwórz nowe zmienne:
# #
# #     1. Pierwszy wyraz od tyłu
# #     2. Ostatni wyraz od tyłu
# #     3. Cały napis od tyłu
# #     4. Cały napis co drugi znak
# #
# #     Przykład:
# #     "Python" -> "nohtyP"
#
sentence = "Python jest super"

# pierwsza_spacja = sentence.find(' ')
# druga_spacja = sentence.find(' ', pierwsza_spacja +1) # Byłem ciekawy jak znaleźć drugie wystąpienie SPACJI. Pomógł INTERNET.
# # print(pierwsza_spacja)
# # print(druga_spacja)
#
#
# print(f'1. Pierwszy wyraz od tyłu: {sentence[5::-1]}')
# print(f'2. Ostatni wyraz od tyłu: {sentence[:-6:-1]}')
# print(f'4. Cały napis co drugi znak: {sentence[::2]}')

word_list = sentence.split(' ') # Zrób w ten sposób kolejne zadanie
word_1 = word_list[0]
print(word_1[::-1])



# ####### ####### ####### ZADANIE 4 — Wyciąganie danych z kodu produktu ####### ####### #######
#
#     # product_code = "LAPTOP-DELL-2026-PRO"
#     #
#     # Bez używania split():
#     #
#     # 1. Wyciągnij nazwę marki (DELL)
#     # 2. Wyciągnij rok (2026)
#     # 3. Wyciągnij ostatni fragment (PRO)
#     # 4. Sprawdź, czy kod kończy się na "PRO" bez użycia endswith()
#     #
#     # Podpowiedź – Wżyj indeksowania, slicing oraz find()
#
# product_code = 'LAPTOP-DELL-2026-PRO'
#
# przerwa1 = product_code.find('-')
# przerwa2 = product_code.find('-', przerwa1 +1)
# przerwa3 = product_code.find('-', przerwa2 +1)
# # print(przerwa1)
# # print(przerwa2)
# # print(przerwa3)
#
# print(f'Produkt: LAPTOP-DELL-2026-PRO')
# print()
#
# print(f'Nazwa marki: {product_code[7:11]}')
# # lub
# print(f'Nazwa marki: {product_code[przerwa1+1:przerwa2]}')
#
# print(f'Rok: {product_code[-8:-4]}')
# # #lub
# print(f'Rok: {product_code[przerwa2+1:przerwa3]}')
#
# print(f'Ostatni fragment to: {product_code[-3:]}')
# #lub
# print(f'Ostatni fragment to: {product_code[przerwa3+1:]}')
#
# print(f'Czy kod kończy się na "PRO" (Metoda: slicing)? {product_code[-3:]=='PRO'}')
# # lub
# print(f'Czy kod kończy się na "PRO" (Metoda: find)? {product_code.find('PRO')!= -1}')
#
#
#
# ####### ####### ####### ZADANIE 5 — Maskowanie numeru telefonu ####### ####### #######
#
# #     phone = "123456789"
# #
# #     Stwórz nowy napis w formacie:
# #     *****6789
# #
# #     Czyli:
# #     - Wszystkie cyfry poza ostatnimi czterema mają zostać zamienione na *
# #
# #     Dodatkowo:
# #     – Policz, ile gwiazdek trzeba dodać automatycznie, na podstawie długości napisu.
#
# phone = '123456789'
# # phone_pt1 = phone[:-4]
# # print(phone_pt1)
#
# print(f'Zaszyfrowany numer telefonu (sposób 1): {phone.replace('12345', '*****')}')
# # lub
# print(f'Zaszyfrowany numer telefonu (sposób 2): {phone.replace(phone[:-4], '*****')}')
# # lub
#
# # stars_needed = (len(phone) - 4)
# # changed_half = '*' * (len(phone) - 4)
# # unchanged_half = phone[-4:]
# # print(stars_needed)
# # print(changed_half)
# # print(unchanged_half)
#
# print(f'Zaszyfrowany numer telefonu (sposób 3): {(len(phone) - 4) * '*' + phone[-4:]}') # Bez metody replace()
# print(f'Aby zamienic cały numer telefony na gwiazdki trzeba użyć {len(phone)} gwiazdek.')
# print(f'Cały numer telefony zamieniony na gwiazdki: {'*' * (len(phone))}')
#
#
#
# ####### ####### ####### ZADANIE 6 – E-mail ####### ####### #######
#
# #      email = "jan.kowalski@example.com"
# #
# #      1. Wyciągnij login (jan.kowalski)
# #      2. Wyciągnij domenę (example.com)
# #      3. Sprawdź, czy email jest z domeny .com
# #      4. Wypisz pierwsze 3 znaki loginu
# #      5. Wypisz domenę od tyłu
#
# email = 'jan.kowalski@example.com'
#
# print(f'jan.kowalski@example.com')
# print()
#
# print(f'Login: {email[0:12]}')
# #lub
# print(f'Login: {email[:email.find('@')]}') # staraj sie nie używać finf zrób SPLITem
#
# print(f'Domena: {email[-12:]}')
# # lub
# print(f'Domena: {email[email.find('@'):]}')
#
# print(f'Czy email jest z domeny .com? (metoda: slicing) {email[-4:] == '.com'}')
# # lub
# print(f'Czy email jest z domeny .com? (metoda: find) {email.find('.com') != -1}')
# # lub
# print(f'Czy email jest z domeny .com? (metoda: endswith) {email.endswith('.com')}')
#
# print(f'Pierwsze 3 znaki loginu: {email[:3]}')
# print(f'Domena od tyłu: {email[:-4:-1]}')
# # lub
# print(f'Domena od tyłu: {email[:email.find('com') - 1:-1]}')
# # lub
# print(f'Domena od tyłu: {email[:email.index('com') - 1:-1]}')
