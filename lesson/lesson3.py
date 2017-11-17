from random import randint

spisok = [str(randint(11,100000)) for _ in range(100)]

# числа, оканчивающиеся на 1
a = [item for item in spisok if item[-1] == '1']
# числа палиндромы
c = [item for item in spisok if item[:] == item[::-1]]

# список для счастливых
b=[]
for item in spisok:
    digitl = list(map(int,item))
    if sum(digitl[:(len(digitl) + 1) // 2]) == sum(digitl[-len(digitl) // 2:]):
        b.append(item)

print("Список чисел:")
print(spisok)
print("\nСписок чисел, оканчивающиеся на 1:")
print(a)
print("\nСписок чисел для счастливых:")
print(b)
print("\nСписок чисел-полиндромов:")
print(c)
