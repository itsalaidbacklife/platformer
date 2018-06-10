class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.r = 15
        self.onGround = False

    #Checks if player is on specific ground
        # if so, sets onGround = True, and keeps player's y on top of ground
    def checkOnGround(self, ground):
        if self.x + self.r >= ground.x1 and self.x - self.r <= ground.x2:
            if self.y + 5*self.r >= ground.y and self.y + 2 * self.r < ground.y:
                self.onGround = True
                self.y = ground.y - 5* self.r
                
    def move(self):
        if self.onGround:
            self.vy = 0 #don't move vertically while on ground
        else:
            self.vy += 1 #gravity
        self.x += self.vx
        self.y += self.vy
    
    def display(self):
        fill(255)
        ellipse(self.x, self.y, 2*self.r, 2*self.r) #head
        line(self.x, self.y + self.r, self.x, self.y + 4*self.r) #body
        line(self.x, self.y + 2*self.r, self.x-self.r, self.y+self.r) #left arm
        line(self.x, self.y + 2*self.r, self.x+self.r, self.y + self.r) #right arm
        line(self.x, self.y+4*self.r, self.x-self.r, self.y+5*self.r) #left leg
        line(self.x, self.y+4*self.r, self.x+self.r, self.y+5*self.r) #right leg
        
        