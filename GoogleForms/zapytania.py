import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import random

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

client = gspread.authorize(creds)

sheet = client.open("pierwsze losowanie").sheet1
print("getting all records")
data = sheet.get_all_records()

#row = sheet.row_values(9)
#column = sheet.col_values(5)

#row_test = sheet.row_values(9)  # zwraca liste z elementami
#cell = sheet.cell(1, 2).value  # otrzymujesz komorke 1 2    # najpierw wiersz pozniej kolumna
print('////////////////////////////////////////////////////////////////////////')
ludzie = []  # lista zawierajaca imie nazwisko oraz tak/nie przy kolejnych zadaniach
naglowek = sheet.row_values(1)
for i in range(len(data)):  # iterowanie po kazdym wierszu
    ludzie.append([])
    for j in range(2, len(data[0])):
        ludzie[i].append(data[i][naglowek[j]])

pprint(ludzie)

# zrobic liste z zadaniami
my_dictionary = dict()
zadania = [x for x in naglowek[3:]]  # robi liste zadan na podstawie 1 wiersza w excelu
print(zadania)
for zad in zadania:
    my_dictionary[zad] = []

# dopasowanie osoby do ilosci plusow / stworzenie podlisty [imie, ilosc plusow]
with open('C:\\Users\\sirko\\PycharmProjects\\losowanie\\imie i nazwisko.txt', 'r') as f:
    imie_i_plus = []
    for line in f:
        imie_i_plus.append([line[:len(line)-3], line[-2]])

for i in range(len(ludzie)):
    for j in range(len(imie_i_plus)):
        if ludzie[i][0] == imie_i_plus[j][0]:
            ludzie[i][0] = imie_i_plus[j]
            break

# przydzielanie na podstawie tak/nie do odpowiednich miejsc w dictionary my_dictionary
for osoba in ludzie:
    for i in range(1,len(osoba)):
        if osoba[i] == 'tak':
            my_dictionary[zadania[i-1]].append(osoba[0])


pprint(my_dictionary)
print('//////////////////////////////////// randomizacja///////////////////////////////////////////')
# randomizacja kazdego zadania
for i in range(len(zadania)):
    random.shuffle(my_dictionary[zadania[i]])
pprint(my_dictionary)

# sortowanie osob w kazdym zadaniu na podstawie ich plusow
for i in range(len(zadania)):
    my_dictionary[zadania[i]] = sorted(my_dictionary[zadania[i]], key=lambda x: x[1])
pprint(my_dictionary)

# wybieramy osobe do kolejnych zadan i usuwamy ta osobe z kolejnych zadan
wybrane_osoby_i_zadanie = []
for i in range(len(zadania)):
    do_usuniecia = my_dictionary[zadania[i]][0]
    wybrane_osoby_i_zadanie.append([do_usuniecia[0], zadania[i]])
    for j in range(i, len(zadania)):  # usuwanie w kazdym zadaniu
        if my_dictionary[zadania[j]].count(do_usuniecia) > 0:
            my_dictionary[zadania[j]].remove(do_usuniecia)
    print(my_dictionary)

pprint(wybrane_osoby_i_zadanie)

