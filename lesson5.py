from random import randint

def generator_int(size, numstart, numend):
    """Генерирует список размером size в диапазоне от numstart до numend
    с сортировкой по убыванию"""
    return sorted([randint(numstart,numend) for _ in range(size)],reverse=True)

def combine(sp1, sp2):
    """Объединяем два списка и сортируем по возрастанию"""
    lenSP1, lenSP2 = len(sp1)-1, len(sp2)-1
    sp3 = []
    #Записываем в новый список элементы обоих списков по возрастанию
    while lenSP1>=0 and lenSP2>=0:
        if sp1[lenSP1] >= sp2[lenSP2]:
            sp3.append(sp2[lenSP2])
            lenSP2 -= 1
        elif sp2[lenSP2] >= sp1[lenSP1]:
            sp3.append(sp1[lenSP1])
            lenSP1 -= 1
    #Дозаписываем остаток первого списка
    while lenSP1>=0:
        sp3.append(sp1[lenSP1])
        lenSP1 -= 1
    #Дозаписываем остаток второго списка
    while lenSP2>=0:
        sp3.append(sp2[lenSP2])
        lenSP2 -= 1
    return sp3

def combine2(sp1, sp2):
    sp4 = (sp1+sp2).sort()
    return sp4

def main_combine():
    sp1 = generator_int(10, 0, 100)
    sp2 = generator_int(10, 0, 100)
    sp3 = combine(sp1[:], sp2[:])
    sp4 = combine(sp1[:], sp2[:])

    print("***** Сортировка списка и сливание в один упорядоченный *****")
    print("Список 1:",sp1)
    print("Список 2:",sp2)
    print("Комби 1: ",sp3)
    print("Комби 2: ",sp4)


""" **********************  Шифр Цезаря  ********************************* """
#import string
#**************************************************  добавил украинские буквы
alfabet_ru_lower = [chr(i) for i in range(1072, 1104)] + ['і','ї','є']
alfabet_ru_up = [chr(i) for i in range(1040, 1072)] + ['І','Ї','Є']
alfabet_eng_lower = [chr(i) for i in range(97, 123)]
alfabet_eng_up = [chr(i) for i in range(65, 91)]

def shifr(item, key):
    # В английском алфавите 26 букв,
    # В русском + украинском - 32+3=35 .
    if item in alfabet_eng_up:
        item = alfabet_eng_up[(alfabet_eng_up.index(item) + key) % 26]
    elif item in alfabet_eng_lower:
        item = alfabet_eng_lower[(alfabet_eng_lower.index(item) + key) % 26]
    elif item in alfabet_ru_up:
        item = alfabet_ru_up[(alfabet_ru_up.index(item) + key) % 35]
    elif item in alfabet_ru_lower:
        item = alfabet_ru_lower[(alfabet_ru_lower.index(item) + key) % 35]
    return item

def shifr_cesar(text, key):
    char = [shifr(text[num], key) for num in range(len(text))]
    #Записываем первым символом ключ
    rez = chr(1072 + key) + "".join(char)
    return rez

def deshifr_cesar(text):
    #Первый символ - ключ
    key = int(ord(text[0])-1072)
    char = [shifr(text[num], -key) for num in range(1,len(text))]
    return "".join(char)

def main_shifr():
    #text = input("Введите строку для шифрования: ")
    #print("Ключ вводить от -25 до 25 для английского текста.\
    #\nДля русско-украинского текста ключ должен быть от -34 до 34.")
    #key = int(input("Введите число, значение сдвига: "))
    text =  "Hello world. Я приветствую ВАС, Земляне! Їжачок єхидно індючився."
    key = -8
    textshifr = shifr_cesar(text, key)
    textdeshifr = deshifr_cesar(textshifr)

    print("\n***** Шифр Цезаря *****")
    print("\nСтрока для шифрации   --> ",text)
    print("Зашифрованная строка  --> ",textshifr)
    print("Расшифрованная строка --> ",textdeshifr)


main_combine()
main_shifr()
