from playerFile import Player
from groundFile import Ground
from levelFile import Level
from levelOne import scenes, lev1
def setup():
    size(1000, 1000)
    # global p, g
    # p = Player(225, 100)
    # g = Ground(100, 750, 200)
def draw():
    global lev1
    lev1.drawLevel()
    fill(200, 0, 0)
    
    
def keyPressed():
    global lev1
    if key == 'w':
        # Only jump if you are on the ground
        if lev1.player.onGround:
            lev1.player.y -= 10
            lev1.player.vy = -15
    if key == 'a':
        lev1.player.vx = -5
    if key == 'd':
        lev1.player.vx = 5
    if key == 'r':
        # p = Player(300, 100)
        lev1 = Level(scenes)

def keyReleased():
    global lev1
    if key == 'a' or key == 'd':
        lev1.player.vx = 0