class unity:
    def __init__(self, life, speed):
        self.life = life
        self.speed = speed
        self.type = "unit"
    def __str__(self):
        return "Unit {}. Life: {}. Speed: {}".format(self.type,
                                                     self.life,
                                                     self.speed)
    def workin(self):
        return "Работа не волк, в лес не убежит..."
    def go(self):
        return "Чап-чалап."

class worker(unity):
    def __init__(self, life, speed):
        super().__init__(life, speed)
        self.type = "worker"
    def workin(self):
        return "Эх, мне бы только бы это суметь."
    def go(self):
        return "Тяп-ляп..."

class hunter(unity):
    def __init__(self, life, speed):
        super().__init__(life, speed)
        self.type = "hunter"
    def workin(self):
        return "Волк?!! Где Волк?!"
    def go(self):
        return "Хряп-хряп."

class fermer(unity):
    def __init__(self, life, speed):
        super().__init__(life, speed)
        self.type = "fermer"
    def workin(self):
        return "Узяв дід ріпку за чуб..."
    def go(self):
        return "Гуп-гуп..."

class tank(unity):
    def __init__(self, life, speed):
        super().__init__(life, speed)
        self.type = "tank"
    def workin(self):
        return "Пух. Пу-пух."
    def go(self):
        return "Грррррр..."


if __name__=="__main__":
    units = []
    units.append(worker(50,3))
    units.append(fermer(40,4))
    units.append(hunter(70,5))
    units.append(tank(300,30))
    for item in units:
        print()
        print(item)
        print(item.go(),item.workin(),item.go())
