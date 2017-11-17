class Language:
    en="english"
    ua="українська"
    ru="русский"
    de="deutsche"

class Human:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def __str__(self):
        return "Name: {:>10}, age:{:3}, language:{}".format(self.name,
                                                      self.age,
                                                      self.language)
    def speak(self):
        if self.language == Language.en:
            print("Hello, {}!".format(self.name))
        elif self.language == Language.ua:
            print("Привіт, {}!".format(self.name))
        elif self.language == Language.ru:
            print("Привет, {}!".format(self.name))
        elif self.language == Language.de:
            print("Guten Tag, {}!".format(self.name))

if __name__=="__main__":
    humans=[]
    humans.append(Human("Broderick", 45, Language.en))
    humans.append(Human("Кирил", 15, Language.ru))
    humans.append(Human("Софія", 18, Language.ua))
    humans.append(Human("Otto", 32, Language.de))
    for thishuman in humans:
        print(thishuman)
        thishuman.speak()
        print()
