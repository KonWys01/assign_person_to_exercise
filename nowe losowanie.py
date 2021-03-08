import csv
from pprint import pprint
import random
from difflib import SequenceMatcher
# robi liste w ktorej kazdy element to oddzielna lista zawierajaca imie osoby oraz odopwiedzi czy chce zrobic dane zadanie
ludzie = []
with open('pierwsze_losowanie.csv', 'r') as f:
    for line in f:
        glosy = line.split(",")
        for i in range(len(glosy)):
            if i == 0:  # w pierwszym trzeba usunac '""" oraz ""'
                glosy[i] = glosy[i][3:-2]
            else:  # '"" oraz ""'
                glosy[i] = glosy[i][2:5]
        ludzie.append(glosy)
#print(ludzie)

# porownanie osob z osobami z pliku tekstowego
with open('imie i nazwisko.txt', 'r') as f:
    dobre_imiona = []
    for line in f:
        dobre_imiona.append(line[:len(line)-3])
    #print(dobre_imiona)
    for element in ludzie:
        oficjalny = 0
        s_1 = element[0]
        for imie in dobre_imiona:
            s_2 = imie
            wynik = SequenceMatcher(a=s_1, b=s_2).ratio()
            #print(s_1, s_2, wynik)
            if wynik > oficjalny:
                oficjalny = wynik
                prawdziwe_imie = s_2
        #print(element[0], prawdziwe_imie, oficjalny)
        element[0] = prawdziwe_imie
# bedzie sie wiecej powtarzac bo pare imion z csv dopasowuje sie do 1 imienia z pliku tekstowego z plusami


# zrobic dictionary z zadaniami
# for element in ludzie:
#     print(element)
my_dictionary = dict()
zadania = []

# robi sie lista zadan do dictionary oraz lista z tymi zadaniami
with open('lista_zadan.txt','r') as f:
    for line in f:
        line = line[:-1]
        my_dictionary[line] = []
        zadania.append(line)
#print(my_dictionary)
#print(zadania)

# tutaj bylo stare przydzielanie osob do zadania



# dopasowanie osoby do ilosci plusow / stworzenie podlisty [imie, ilosc plusow]
with open('imie i nazwisko.txt', 'r') as f:
    imie_i_plus = []
    for line in f:
        imie_i_plus.append([line[:len(line)-3], line[-2]])
    #pprint(imie_i_plus)
    #print()
    #random.shuffle(imie_i_plus)
    #pprint(imie_i_plus)
for i in range(len(ludzie)):
    for j in range(len(imie_i_plus)):
        if ludzie[i][0] == imie_i_plus[j][0]:
            ludzie[i][0] = imie_i_plus[j]
            break
    #random.shuffle(ludzie)
    #print(ludzie[i])

# tutaj jest na nowo przydzielanie do zadan
# przydzielanie na podstawie tak/nie do odpowiednich miejsc w dictionary my_dictionary
for osoba in ludzie:
    for i in range(1,len(osoba)):
        if osoba[i] == 'tak':
            my_dictionary[zadania[i-1]].append(osoba[0])

#sortowanie kazdego zadania
for i in range(len(zadania)):
    random.shuffle(my_dictionary[zadania[i]])
    #pprint(my_dictionary[zadania[i]])
pprint(my_dictionary)


# mamy juz liste zadan i osoba oraz obok plus, potrzebujemy teraz posortowac na podstawie liczby po prawej stronei od osoby


# najpirew posortuje po ilosci plusów
# pozniej lece po kazdym zadaniu
# w kazdym zadaniu lece po plusach
# co kazdego plusa licze ile ich jest
# co kazdego plusa dodaje 1
# jesli kolejny plus sie rozni to zrob randomizacje po sumie i ustaw sumie na 0





print("///////////////////////////////////////////////sorted/////////////////////////////////////////")
# sortowanie osob w kazdym zadaniu na podstawie ich plusow
for i in range(len(zadania)):
    my_dictionary[zadania[i]] = sorted(my_dictionary[zadania[i]], key=lambda x: x[1])
#for i in range(len(zadania)):
pprint(my_dictionary)

print('//////////////zaczynamy usuwac////////////////')
# wybieramy osobe do kolejnych zadan i usuwamy ta osobe z kolejnych zadan
wybrane_osoby_i_zadanie = []
for i in range(len(zadania)):
    do_usuniecia = my_dictionary[zadania[i]][0]
    wybrane_osoby_i_zadanie.append([do_usuniecia[0], zadania[i]])
    for j in range(i, len(zadania)):  # usuwanie w kazdym zadaniu
        #print(j, do_usuniecia)
        if my_dictionary[zadania[j]].count(do_usuniecia) > 0:
            my_dictionary[zadania[j]].remove(do_usuniecia)

    #print(i, zadania[i])
    #print(do_usuniecia, zadania[i])
    #pprint(my_dictionary)
        #pprint(my_dictionary[zadania[j]])

        #if do_usuniecia in my_dictionary[zadania[j]]:
            #my_dictionary[zadania[j]].remove(do_usuniecia)
    # print(type(do_usuniecia))
    # my_dictionary[zadania[i]].pop(0)
    # print(do_usuniecia)
print('//////////////po usunieciu//////////')
#pprint(my_dictionary)
pprint(wybrane_osoby_i_zadanie)







# czas na wybranie jednej osoby oraz zrobienie listy kto ma które zadanie
"""kto_ma_zadanie = []
for i in range(len(zadania)):
    random.shuffle(my_dictionary[zadania[i]])
    infinite_loop = 0
    while True:
        if my_dictionary[zadania[i]][0] not in kto_ma_zadanie:
            kto_ma_zadanie.append(my_dictionary[zadania[i]][0])
            break
        random.shuffle(my_dictionary[zadania[i]])
        infinite_loop +=1
        if infinite_loop > 1000:
            random.shuffle(my_dictionary[zadania[i]])
            kto_ma_zadanie.append(my_dictionary[zadania[i]][0])
            print("!!!!!!!!!!!!!no i sie zjebalo!!!!!!!!!!!!")
            break
    print(zadania[i], kto_ma_zadanie[i])"""

# wypisywanie kto ma zadanie


# dobranie osoby do zadania
#pprint(my_dictionary)
#pprint(kto_ma_zadanie)