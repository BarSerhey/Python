def first_task():
    print("ПЕРВОЕ ЗАДАНИЕ.\n")
    try:
        quantity =  int(input("Сколько Вы хотите ввести чисел: "))
    except:
        print("Вы не ввели целое число!! Извините!")
        exit()

    num = 0
    rez = 1
    while num < quantity:
        try:
            number = int(input("Введите {0} число: ".format(num+1)))
            rez *= number
            num += 1
        except:
            print("Вы не ввели число!! Попробуем еще раз!")

    print("Произведение {0}-ти(х) введенных чисел составляет {1}".format(quantity, rez))

def second_task():
    print("ВТОРОЕ ЗАДАНИЕ.\n")

    num = int(input("Введите целое число: "))

    rezult = {"even":0,"odd":0,"pozitive":0,"negative":0,"zero":0}
    quantity = 0

    while num != -47:
        quantity += 1
        if num == 0:
            rezult["zero"] += 1

        if num % 2 == 0:
            rezult["even"] += 1
        else:
            rezult["odd"] += 1

        if num > 0:
            rezult["pozitive"] += 1
        elif num < 0:
            rezult["negative"] += 1

        num = int(input("Еще число (для выхода введите -47): "))

    print("\nРезультаты по введенным числам.\
          \nВсего введено {0} чисел. Из них:".format(quantity))
    for key, rez in rezult.items():
        print("{0} = {1}".format(key,rez))


first_task()
print()
second_task()
