def whot_part_coordinates(x, y):
    part = 0
    if x >= 0 and y >= 0:
        part = 1
    elif x <= 0 and y >= 0:
        part = 2
    elif x <= 0 and y <= 0:
        part = 3
    elif x >= 0 and y <= 0:
        part = 4
    return part

def whot_part_lines(a, b):
    part = 0
    if a > 0 and b > 0:
        # \ ниже
        part = 3
    elif a < 0 and b > 0:
        # / ниже
        part = 4
    elif a < 0 and b < 0:
        # \ выше
        part = 1
    elif a > 0 and b < 0:
        # / выше
        part = 2
    return part

def main():
    print("Введите первую координату: ")
    x1 = float(input("x:"))
    y1 = float(input("y: "))
    print("Введите вторую координату: ")
    x2 = float(input("x: "))
    y2 = float(input("y: "))

    if x1 == x2 == y1 == y2 == 0:
        print("Начало координат")
    elif x1 == x2 == 0:
        print("Ось X")
    elif y1 == y2 == 0:
        print("Ось Y")
    else:
        # Находим положение точек
        part1 = whot_part_coordinates(x1,y1)
        part2 = whot_part_coordinates(x2, y2)

        # Уравнение прямой по двум точкам:
        # A * x + B * y + C = 0
        # (y1 - y2) * X + (x2 - x1) * Y + (x1 * y2 - x2 * y1) = 0
        a = (y1 - y2)
        b = (x2 - x1)
        c = (x1 * y2 - x2 * y1)


        if part1 == part2:
            # Отрезок находится в одной области
            print("Отрезок находится в {0}-й области.".format(part1))
        elif (abs(part2 - part1) != 2) or (c == 0):
            # Отрезок находится в соседних областях или по диагонали через начало координат
            print("Отрезок находится в {0}-й и {1}-й областях.".format(part1, part2))
        else:
            # Приведем к правильному уровнению
            a /= c
            b /= c
            # Найдем третью область
            part3 = whot_part_lines(a, b)
            print("Отрезок находится в {0}-й, {1}-й и {2}-й областях.".format(part1, part2, part3))

if __name__ == '__main__':
    main()
