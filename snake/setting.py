
class Setting():

    def __init__(self):
        self.screen_width = 900
        self.screen_heigth = 900
        self.bg_color = (20,50,70)

        self.size_square = 20
        self.boundary_square = 3
        self.size_square_tail = self.size_square - self.boundary_square

        self.max_square_x = int(self.screen_width/self.size_square)
        self.max_square_y = int(self.screen_heigth/self.size_square)

        self.speed_apple=1000
        self.mass_apple=[]
        self.new_apple=0