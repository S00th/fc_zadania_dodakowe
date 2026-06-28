# ####### ####### ####### ZADANIA – 2026.05.14 ####### ####### #######')



# ####### ####### ####### Zadanie 1 – Posortuj listę imion wg. długości ####### ####### #######
#
# Posortuj listę imion wg. długości imienia.

people = [
    ('Basia', 23),
    ('Ania', 19),
    ('Katarzyna', 27),
    ('Ola', 21),
    ('Tomek', False, 30)
     ]

# sorted(collection) -> sortuje obiekt KOLEKCJI -> zawsze zwraca LISTĘ (w kolejności wg. ASCI)
#   sorted(iterable, /.., *.., key=none, reverse=False) # W argumencie "key" wpisujemy jakiej FUNKCJI chcemy użyć, żeby posortować.

def pobierz_dlugosc_imienia(element):
    return len(element[0]) # Funkcja zwraca długość pierwszego elementu listy

posortowana_lista = sorted(people, key=pobierz_dlugosc_imienia) # Sortuj według funkcji

for element in posortowana_lista: # Pętla wyświetla posortowane wyniki
    imie = element[0]
    dlugosc = len(imie) # Sprawdź długość imienia
    print(f'{imie}: {dlugosc} znaki.')



# ####### ####### ####### Zadanie 2 – Posortuj listę imion wg. wieku ####### ####### #######
#
# Posortuj listę imion wg. wieku (każdorazowo ostatni element krotki).
# sorted(people, key=lambda x: x[-1])
# Gdzie x to każdym elementem wewnętrznym w LIŚCIE TUPLI ([-1], aby wyciągnąć ostatni element z każdej TUPLI).

people = [
    ('Basia', 23),
    ('Ania', 19),
    ('Katarzyna', 27),
    ('Ola', 21),
    ('Tomek', False, 30)
     ]

def pobierz_wiek(element):
    return element[-1] # Funkcja zwraca ostatni elementu listy

posortowana_lista = sorted(people, key=lambda x: x[-1]) # Sortuj i zwraca LISTĘ w kolejności wg. ASCI

for element in posortowana_lista: # Pętla wyświetla posortowane wyniki
    wiek = element[-1]
    imie = element[0]
    print(f'{wiek}, {imie}')



# ####### ####### ####### Zadanie 3 – Generator haseł ####### ####### #######
#
#  1. Dany jest moduł string.
#  2. Zbuduj funkcję do generowania haseł.
#  3. Funkcja powinna przyjmować następujące argumenty:
#     - Żądana długość hasła,
#     - Czy zawrzeć znaki specjalne:
#       - Jeśli True, to zawrzyj,
#       - Jeśli False, to nie zawieraj.
#  4. Na końcu wymieszaj litery.


import string # Definiujemy zestawy znaków globalnie (raz na początku)
import random

def generate_random_pass(pass_len: int, spec_char: bool) -> str:
    chars_pool = string.ascii_letters + string.digits
    if spec_char:
        chars_pool += string.punctuation
    random_pass = random.choices(chars_pool, k=pass_len)
    random.shuffle(random_pass)
    return ''.join(random_pass)

print(generate_random_pass(30, True))



# ####### ####### ####### Zadanie 4 – Funkcja z dowolną liczbą elementów ####### ####### #######
#
#     Napisz funkcję, która przyjmie dowolną liczbę elementów.
#     Wyodrębnij z niej liczby całkowite, pogrupuj odpowiednio i zwróć:
#         -> liczby parzyste jako osobną listę,
#         -> liczby nieparzyste w osobnej liście.
#     Zignoruj wejścia inne niż integer.

### DOWOLNA liczba ARGUMENTÓW – *args
# ARGUMENT POZYCYJNY to taki argument, który nie ma wartości domyślnej.
# "*" przed nazwą argumentu liczby pełni rolę OPERATORA PAKOWANIA ARGUMENTÓW POZYCYJNYCH (tzw. *args).
# Pozwala on na wywołanie FUNKCJI z dowolną liczbą wartości przekazanych po przecinku.
# Wszystkie wartości przekazane podczas wywołania FUNKCJI zostają SPAKOWANE do jednej struktury danych – TUPLI o nazwie "liczby".
# Wewnątrz funkcji możesz operować na niej jak na zwykłej kolekcji danych.
# def dodaj_wiele(*liczby):
#     return sum(liczby)
# result = dodaj_wiele(1, 2, 3, 100, 200) # Mogę tutaj wpisać dowolną ilość wartości
# print(result)

def grupuj_liczby(*liczby):
    parzyste = [] # Lista liczb parzystych
    nieparzyste = [] # Lista liczb nieparzystych

    for element in liczby:
        if type(element) is int: # Jeżeli int to... (inne wartości – wartości bool)
            if element % 2 == 0: # Jeśli liczba jest parzysta
                parzyste.append(element) # dodaj do listy parzyste
            else: # Jeśli liczba nieparzysta
                nieparzyste.append(element) # dodaj do listy nieparzyste
    return parzyste, nieparzyste

wynik_parzyste, wynik_nieparzyste = grupuj_liczby(1, 2, 3.33, -5, 20, 123, 12.5, 100_000, 'Aga', False)

print(f'Liczby parzyste: {wynik_parzyste}.')
print(f'Liczby nieparzyste: {wynik_nieparzyste}.')



# ####### ####### ####### Zadanie 5 – Funkcja – naturalna i narcystyczna ####### ####### #######
#
#     Napisz funkcję, która przyjmuje na wejściu liczbę naturalną
#     i sprawdza, czy liczba jest narcystyczna.
#
#     Liczba narcystyczna to taka liczba, której suma cyfr
#     podniesionych do potęgi długości tej liczby jest równa
#     wartości tej liczby.

def liczba_narcystyczna(number: int) -> bool:
    if not isinstance(number, int): # Tutaj odbywa się WALIDACJA wejścia. Jeżeli liczba nie jest INT
        raise TypeError('Liczba musi być całkowita.') # to wyjdź z FUNKCJI i podnieś BŁĄD – tutaj jest tylko informacją
    str_number = str(number) # Przypisujemy zmienną (przyda się późnej)
    exponent = len(str_number) # Określamy wykładnik potęgi, aby mieć dynamicznie przypisany (zmienny) wykładnik.
    cum_sum = 0 # Suma, która się kumuluje
    for digit in str_number:
        cum_sum += int(digit)**exponent
    return cum_sum == number # Nie ma potrzeby pisać tutaj "if" ponieważ tutaj i tak otrzymujemy bool.

number = int(input('Podaj liczbę: '))
if liczba_narcystyczna(number):
    print(f'Liczba {number} jest narcystyczna.')
else:
    print(f'Liczba {number} NIE jest narcystyczna.')



# ####### ####### ####### Zadanie 6 – Funkcja Posortuj listę imion wg. wieku ####### ####### #######
#
#     Napisz funkcję, która jako argumenty przyjmie dwie liczby:
#     początek i koniec zakresu.
#
#     1. Zwaliduj dane wejściowe:
#         -> sprawdź, czy oba argumenty są liczbami całkowitymi,
#         -> sprawdź, czy początek zakresu nie jest większy niż koniec zakresu.
#     2. Funkcja ma za zadanie zwracać listę wszystkich liczb
#        narcystycznych z zadanego zakresu.



# ####### ####### ####### Zadanie 7 – Gra w zgadywanie liczby.
#
#     1. Komputer losuje liczbę całkowitą z danego przedziału.
#     2. Użytkownik podaje liczbę, dopóki nie odgadnie liczby wylosowanej przez komputer.
#     3. W trakcie działania programu podpowiadaj użytkownikowi, czy podana przez niego liczba jest:
#         -> większa od wylosowanej,
#         -> mniejsza od wylosowanej.
#     4. Zliczaj liczbę prób.
#     5. Jeśli użytkownik nie odgadnie liczby w trakcie 5 prób,
#        przerwij grę i wyświetl informację o porażce.



# ####### ####### ####### Zadanie 8 – Funkcja obliczająca pierwiatki równania kwadratowego y = ax^2 + b*x + c
#
#     1. Funkcja powinna przyjmować trzy argumenty:
#         -> współczynnik a,
#         -> współczynnik b,
#         -> współczynnik c.
#     2. Rozwiąż równanie postaci:
#         -> y = ax² + bx + c
#     3. Zwaliduj dane wejściowe:
#         -> sprawdź, czy wszystkie argumenty są liczbami,
#         -> sprawdź, czy współczynnik a jest różny od 0 (wówczas mamy do czynienia z funkcja liniową a nie kwadratową)
#     4. Uwzględnij wszystkie możliwe przypadki:
#         -> brak pierwiastków rzeczywistych,
#         -> jeden pierwiastek (funkcja styczna do osi OX),
#         -> dwa różne pierwiastki.
#     5. Zwróć wynik w zależności od liczby znalezionych pierwiastków
#
#
# -> zadanie 9
#     Napisz program, który obliczy średnią:
#         -> arytmetyczną,
#         -> geometryczną,
#         -> harmoniczną
#     liczb podanych przez użytkownika.
#
#     Przy pomocy funkcji wbudowanej input pobieraj od użytkownika liczby.
#
#     Wymagania:
#         1. Waliduj dane wejściowe.
#         2. Dane nienumeryczne ignoruj, wyświetlając odpowiednią informację.
#         3. W momencie, gdy użytkownik wpisze "koniec", zakończ pobieranie danych.
#         4. Po zakończeniu wyświetl:
#             -> wynik wybranej średniej,
#             -> liczbę poprawnie pobranych wartości.
#
#
# -> zadanie 10
#     Napisz algorytm zgadywania kodu do kłódki rowerowej.
#
#     Warunki:
#         1. Kłódka jest 5-cyfrowa.
#         2. Największa możliwa do wprowadzenia cyfra to 8.
#         3. Kod nie zawiera cyfr 0 i 6.
#         4. Suma cyfr wynosi 21.
#         5. Cyfry nie powtarzają się.
#         6. Iloczyn cyfr jest większy lub równy 70.
#         7. Ostatnia cyfra jest nieparzysta.
#
#
# -> zadanie 11
#     Liczba pierwsza to taka liczba naturalna >= 2,
#     która dzieli się tylko przez 1 i samą siebie.
#
#     Napisz funkcję, która sprawdzi, czy liczba wpisana
#     przez użytkownika jest liczbą pierwszą.
#
#     Wymagania:
#         1. Zwaliduj dane wejściowe.
#         2. Funkcja powinna zwrócić informację, czy podana liczba jest liczbą pierwszą.
#
#
# -> zadanie 12
#     Liczba pierwsza to taka liczba naturalna >= 2,
#     która dzieli się tylko przez 1 i samą siebie.
#
#     Napisz program, który pobierze od użytkownika
#     początek i koniec zakresu, a następnie zwróci listę
#     wszystkich liczb pierwszych z podanego przedziału.
#
#     Wymagania:
#         1. Zwaliduj dane wejściowe.
#         2. Sprawdź, czy początek zakresu nie jest większy od końca zakresu.
#         3. Zwróć listę wszystkich liczb pierwszych należących do podanego zakresu.
#
#
# -> zadanie 13
#     Napisz funkcję, która przyjmuje tekst jako argument.
#
#     Funkcja powinna:
#         -> policzyć liczbę liter,
#         -> policzyć liczbę cyfr,
#         -> policzyć liczbę spacji,
#         -> zignorować pozostałe znaki.
#
#     Zwróć wynik w postaci słownika.
#
#
# -> zadanie 14
#     Napisz funkcję, która przyjmuje listę dowolnych elementów.
#
#     Funkcja powinna:
#         -> usunąć duplikaty,
#         -> zachować pierwotną kolejność elementów,
#         -> zwrócić nową listę.
#
#
# -> zadanie 15
#     Napisz program symulujący prosty koszyk zakupowy.
#
#     Użytkownik podaje kolejno:
#     -> nazwę produktu,
#     -> cenę produktu.
#
#     Wymagania:
#         1. Waliduj, czy cena jest liczbą dodatnią.
#         2. Pobieraj produkty do momentu wpisania "koniec".
#         3. Po zakończeniu wyświetl:
#             -> listę produktów,
#             -> łączną wartość koszyka,
#             -> najdroższy produkt.
#
#
# -> zadanie 16
#     Napisz funkcję, która sprawdzi siłę hasła.
#     Hasło uznaj za silne, jeśli:
#         -> ma co najmniej 8 znaków,
#         -> zawiera małą literę,
#         -> zawiera wielką literę,
#         -> zawiera cyfrę,
#         -> zawiera znak specjalny.
#
#     Funkcja powinna zwrócić:
#         -> True, jeśli hasło jest silne,
#         -> False, jeśli nie jest silne.
#
#
# -> zadanie 17
#     Napisz funkcję, która przyjmie dwie listy liczb.
#
#     Funkcja powinna zwrócić:
#         -> liczby występujące w obu listach,
#         -> liczby występujące tylko w pierwszej liście,
#         -> liczby występujące tylko w drugiej liście.
#
#     Wynik zwróć w postaci słownika.
#
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# INFORMACJA DO ZADAŃ
# twierdzenie Bézouta dla wielomianów
# Liczba a jest miejscem zerowym wielomianu W(x) wtedy i tylko wtedy, gdy reszta z dzielenia W(x) przez (x−a) jest równa 0
# https://www.matemaks.pl/twierdzenie-b%C3%A9zouta
#
# SCHEMAT HORNERA
# https://www.matemaks.pl/schemat-hornera
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#
# -> zadanie 18
#     Napisz funkcję sprawdzającą, czy podana liczba jest miejscem zerowym wielomianu.
#
#     1. Funkcja powinna przyjmować:
#         -> listę współczynników wielomianu,
#         -> liczbę x.
#
#     2. Wielomian należy interpretować na podstawie podanych współczynników.
#
#     Przykład:
#         [2, -3, -11, 6]
#
#     oznacza:
#         2x³ - 3x² - 11x + 6
#
#     3. Oblicz wartość wielomianu dla podanej liczby x.
#     4. Wykorzystaj twierdzenie Bézouta:
#         -> jeśli wartość wielomianu wynosi 0,
#            liczba jest miejscem zerowym,
#         -> w przeciwnym przypadku nie jest miejscem zerowym.
#     5. Zwróć odpowiednią informację.
#
#
# -> zadanie 19
#     Napisz funkcję znajdującą wszystkie całkowite miejsca zerowe wielomianu.
#
#     1. Funkcja powinna przyjmować listę współczynników wielomianu.
#     2. Wyznacz wszystkie dzielniki wyrazu wolnego.
#     3. Dla każdego dzielnika sprawdź, czy jest miejscem zerowym
#        wykorzystując twierdzenie Bézouta.
#     4. Zwróć listę wszystkich znalezionych miejsc zerowych.
#
#     Przykład:
#         x³ - 6x² + 11x - 6
#
#     wynik:
#         [1, 2, 3]
#
#
# -> zadanie 20
#     Napisz funkcję realizującą schemat Hornera.
#
#     1. Funkcja powinna przyjmować:
#         -> listę współczynników wielomianu,
#         -> liczbę a.
#
#     2. Oblicz wartość wielomianu w punkcie a.
#     3. Wyznacz współczynniki wielomianu po podzieleniu przez (x - a).
#     4. Zwróć:
#         -> wartość wielomianu,
#         -> współczynniki ilorazu.
#
#     Wskazówka:
#         Jeśli wartość wielomianu wynosi 0,
#         to liczba a jest miejscem zerowym wielomianu.
#
#
# -> zadanie 21
#     Napisz program rozkładający wielomian na czynniki liniowe.
#
#     1. Program powinien przyjmować listę współczynników wielomianu.
#     2. Znajduj kolejne miejsca zerowe przy pomocy twierdzenia Bézouta.
#     3. Po znalezieniu miejsca zerowego dziel wielomian przez (x - a)
#        wykorzystując schemat Hornera.
#     4. Powtarzaj operację aż nie będzie można znaleźć kolejnych
#        całkowitych miejsc zerowych.
#     5. Wyświetl:
#         -> znalezione miejsca zerowe,
#         -> postać iloczynową wielomianu.
#
#
# -> zadanie 22
#     Napisz funkcję sprawdzającą poprawność podanych miejsc zerowych.
#
#     1. Funkcja powinna przyjmować:
#         -> listę współczynników wielomianu,
#         -> listę proponowanych miejsc zerowych.
#
#     2. Dla każdej liczby z listy:
#         -> oblicz wartość wielomianu,
#         -> wykorzystaj twierdzenie Bézouta do weryfikacji.
#
#     3. Zwróć:
#         -> listę poprawnych miejsc zerowych,
#         -> listę błędnych miejsc zerowych.
#
#
#     Przykład:
#
#     wielomian:
#         x³ - 6x² + 11x - 6
#
#     kandydaci:
#         [1, 2, 4, 5]
#
#     wynik:
#         poprawne: [1, 2]
#         błędne: [4, 5]