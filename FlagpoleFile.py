class Flagpole:
    def __init__(self, x, bottom, h):
        self.x = x
        self.bottom = bottom
        self.height = h
        self.max_height = bottom + h
        self.flag_height = self.max_height

    def display(self):
        rectMode(CENTER)
        fill(255)
        rect(self.x, self.bottom - self.height/2, 20, self.height)
        fill(0, 200, 0)
        triangle(self.x - 10, self.flag_height, self.x - 10, self.flag_height + 30, self.x - 50, self.flag_height - 15)
        print("drew triangle: (%s, %s), (%s, %s), (%s, %s)" %(self.x - 10, self.flag_height, self.x - 10, self.flag_height + 30, self.x - 50, self.flag_height - 15)) 