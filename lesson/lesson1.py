import datetime

year = datetime.date.today().year
#year = int(input("Введите текущий год: "))
name = input("Как Вас зовут: ")
old = int(float(input("Введите Ваш возраст: ")))

pension_year = 65
number_year = 65 - old
birthday_year = year - old

if old > pension_year:
    message = "Ты уже на пенсии... Сожелею.."
elif number_year == 1:
    message = "Ну ты продержись еще годик."
elif number_year < 5:
    message = "Уже нелолго осталось. Всего навсего {0} года".format(number_year)
else:
    message = "Да тебе еще пахать, лет этак {0} ... Расслабся...".format(number_year)

print("Хорошо, {0}, {1} года рождения!".format(name,birthday_year),message)
