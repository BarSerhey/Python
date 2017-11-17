def text_year(old):
    # для чисел, которые заканчиваются на 11,12,13,14 - пишется "лет"
    year = old%10
    dyear = old%100//10
    if year in [2,3,4] and dyear != 1:
        return "года"
    elif year == 1 and dyear !=1:
        return "год"
    else:
        return "лет"

def human(name, sex):
    def how_old():
        old = int(input("\n{}, cколько Вам полных лет: ".format(name.title())))
        print("Добрый день, {0} {1}. Вам {2} {3}.".format(_sexWrite[sex],
            name.title(), old, text_year(old)))
    return how_old

def input_sex():
    man = ["m","м","man"]
    sex = input("Ваш пол ({}/{}): ".format(*_sex))
    if sex.lower() in man:
        return _sex[0]
    else:
        return _sex[1]

def main():
    fhello = []
    for num in range(1,4):
        name = input("Как зовут {}-го пользователя: ".format(num))
        sex = input_sex()
        fhello.append(human(name, sex))
    for fn in fhello:
        fn()

_sex = ("м","ж")
_sexWrite = {"м":"г-н","ж":"г-жа"}
main()
