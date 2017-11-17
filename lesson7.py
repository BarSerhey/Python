from random import randint

def randString(num, ordstart=1040, ordend=1104):
    """ num      - количество символов
        интервал генерируемых символов с ordstart по ordend"""
    return "".join([chr(randint(ordstart,ordend)) for _ in range(num)])

def countletter(string):
    count={}
    for ch in string:
        try:
            count[ch] += 1
        except:
            count[ch] = 1
    return count

def main():
    string = randString(100,1040,1060)
    print(string)
    count = countletter(string)
    for letter, num in count.items():
        print(letter, "->", num)

main()
