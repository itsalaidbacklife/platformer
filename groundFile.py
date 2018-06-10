class Ground:
    def __init__(self, x1, y1, w):
        self.x1 = x1 #left edge
        self.y = y1
        self.x2 = x1+w
        self.w = w #width
        
    def display(self):
        fill(0)
        # line(self.x1, self.y, self.x2, self.y)
        rect(self.x1, self.y, self.w, 25)
    