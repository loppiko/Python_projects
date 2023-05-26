# Zadanie z6.1. Niech m=13. Zdefiniujmy następujące funkcje haszujące (Wariant [U] + [OL  ]):
# h1(k) = k mod m
# h2(k) = 1 + (k mod (m-2)). 


# Zaprogramować wybrane operacje na tablicy z haszowaniem z adresowaniem otwartym oraz przeprowadzić testy i pomiary:

#     Operacje przetestować osobno na małej tablicy, z wydrukiem kontrolnym,
#     testy/pomiary przeprowadzić na tablicy większego rozmiaru, np. rzędu kilku tysięcy.

# W tablicy haszowań mają być obiekty zawierające dwa pola:
# 1. ilosc – typu int
# 2. nazwisko – ciąg znaków 


#  [U] Operacje WSTAW i USUŃ. Pomiar: wstawiać elementy aż do wypełnienia tablicy w 80%, potem usunąć połowę wstawionych elementów i następnie znowu dopełnić tablicę innymi elementami do 80%. Po tych operacjach zliczyć i wypisać, ile pozycji w tablicy jest wypełnionych znacznikiem DEL (miejsce po usuniętym elemencie) 
#  [OD] adresowanie otwarte, dwukrotne haszowanie


def file_managment():
    try:
        file = open("consts/pairs.txt", "r")
        array = []
        for arg in file:
            array.append(arg.split())
        return array
    except:
        print("File does not exist")
        return []

def generowaniePustychList(length):
    array = []
    for i in range(length):
        array.append([])
    return array

def hashing(mainArray, element, word, i = 0):
    m = len(mainArray)
    if (mainArray[ ((hash(word) % m) + i) % m ] == []):
        mainArray[ ((hash(word) % m) + i) % m ] = element
        global iloscProb 
        iloscProb = iloscProb + i + 1
    else:
        hashing(mainArray, element, word, i + 1)
    return mainArray


def wstaw(mainArray, element):
    return hashing(mainArray, element, element[1])



data = file_managment()
pierwsza = 281

# 50%
mainArray = generowaniePustychList(pierwsza)
procentZapelnienia = 0.5
tablica = []
iloscProb = 0

for arg in data:
  if (pierwsza * procentZapelnienia <= len(tablica) ):
    break
  tablica.append(arg)

for arg in tablica:
    temp = wstaw(mainArray, arg)
    

print("\nIlość prób przy tablicy wielkości", len(tablica), "to", round(iloscProb / len(tablica), 3))



# 70%
mainArray = generowaniePustychList(pierwsza)
procentZapelnienia = 0.7
tablica = []
iloscProb = 0

for arg in data:
  if (pierwsza * procentZapelnienia <= len(tablica) ):
    break
  tablica.append(arg)

for arg in tablica:
    temp = wstaw(mainArray, arg)
    

print("Ilość prób przy tablicy wielkości", len(tablica), "to", round(iloscProb / len(tablica), 3))



# 90%
mainArray = generowaniePustychList(pierwsza)
procentZapelnienia = 0.9
tablica = []
iloscProb = 0

for arg in data:
  if (pierwsza * procentZapelnienia <= len(tablica) ):
    break
  tablica.append(arg)

for arg in tablica:
    temp = wstaw(mainArray, arg)
    

print("Ilość prób przy tablicy wielkości", len(tablica), "to", round(iloscProb / len(tablica), 3), "\n")
# mainArray = generowaniePustychList(pierwsza)





# WARIANT U + OD
