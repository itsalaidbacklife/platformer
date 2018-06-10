from playerFile import Player
# from FlagpoleFile import Flagpole
class Level:
    def __init__(self, scenes):
        self.scenes = scenes #List of scenes
        self.scene_index = 0
        self.over = ''
        self.player = Player(self.scenes[0].grounds[0].x1 + self.scenes[0].grounds[0].w/2, self.scenes[0].grounds[0].y  - 50)
    def drawLevel(self):
        background(150)
        if self.player.y >= height:
            self.over = 'lose'
        if self.player.x > width:
            self.scene_index += 1
            if self.scene_index >= len(self.scenes):
                self.scene_index -= 1
                self.over = 'win'
            self.player.x = 10
        if self.over == '':
            self.player.onGround = False
            for ground in self.scenes[self.scene_index].grounds:
                ground.display()
                self.player.checkOnGround(ground)
            self.player.move()
            self.player.display()
        elif self.over == 'lose':
            textSize(18)
            text("You died! Pres 'r' to retry", width/2 - 80, height/2-30)
        elif self.over == 'win':
            textSize(18)
            text("You Win! Pres 'r' to retry", width/2 - 80, height/2-30)
        