import pygame

def init_tail(center_party,number):
    rez=[(center_party,num) for num in range(number)]
    return rez


class Snake():

    def __init__(self, sn_setting):
        self.sn_setting = sn_setting

        self.color_tail = (230,230,230)
        self.color_head = (120, 20, 30)

        self.speed = 0.004
        self.go = 0.0
        self.go_x = 0
        self.go_y = 1

        self.error = False

        self.del_tail=False

        self.tail = init_tail(int(self.sn_setting.max_square_x/2)-1, 5)


    def update_snake(self):
        #Вычисляем позицию червя
        self.go += self.speed
        if self.go >= 1:
            # Вычисляем следующий ход червя
            self.go=0.0
            old_head = self.tail[-1]
            new_head = (old_head[0] + self.go_x, old_head[1] + self.go_y)

            #добавляем следующую позицию головы
            self.tail.append(new_head)

            #удаляем хвост
            if self.del_tail:
                self.tail.pop(0)
            else:
                self.del_tail=True


    def flip_tail(self, screen):
        #Выводим хвост червя
        for (x,y) in self.tail:
            rect = ((x * self.sn_setting.size_square + self.sn_setting.boundary_square,
                     y * self.sn_setting.size_square + self.sn_setting.boundary_square),
                    (self.sn_setting.size_square_tail,
                     self.sn_setting.size_square_tail))
            pygame.draw.rect(screen, self.color_tail, rect)


    def flip_head(self, screen):
        #Рисуем в голове (кружек)
        head = self.tail[-1]
        circle_pos = (head[0]*self.sn_setting.size_square+int(self.sn_setting.size_square/2)+1,
                      head[1]*self.sn_setting.size_square+int(self.sn_setting.size_square/2)+1)
        circle_radius=int(self.sn_setting.size_square/3)
        pygame.draw.circle(screen,self.color_head,circle_pos,circle_radius)


    def test_tail(self):
        #Проверяем: укусила ли голова тело
        head = self.tail[-1]
        if head in self.tail[:-1]:
            self.error = True

    def eat_apple(self):
        head = self.tail[-1]

        new_mass_apple = []
        for num in range(len(self.sn_setting.mass_apple)):
            apple = self.sn_setting.mass_apple.pop()
            if head == apple.coordinat:
                self.del_tail = False
            else:
                new_mass_apple.append(apple)
        self.sn_setting.mass_apple = new_mass_apple
