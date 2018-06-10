from playerFile import Player
from groundFile import Ground
from levelFile import Level
from levelInstances import lev1_scenes, lev1, levels

def setup():
    size(1000, 1000)
    global levNum, finalVictory
    levNum = 0
    finalVictory = False
    

def draw():
    global lev1, levNum, finalVictory
    if not finalVictory:
        levels[levNum].drawLevel()
    else:
        background(150)
        text("Final Victory", 500, 500)
        
    
def keyPressed():
    global levels, levNum, finalVictory
    if key == 'w':
        # Only jump if you are on the ground
        if levels[levNum].player.onGround:
            levels[levNum].player.y -= 10
            levels[levNum].player.vy = -15
    if key == 'a':
        levels[levNum].player.vx = -5
    if key == 'd':
        levels[levNum].player.vx = 5
    if key == ' ':
        if levels[levNum].over == 'win':
            levNum += 1
            if levNum >= len(levels):
                finalVictory = True
                levNum -= 1
        else:
            levNum = 0
            for level in levels:
                level.over = ''
                level.scene_index = 0
            levels[levNum].player.x = levels[levNum].scenes[levels[levNum].scene_index][0].x1
            levels[levNum].player.y = levels[levNum].scenes[levels[levNum].scene_index][0].y - 100

def keyReleased():
    global lev1
    if key == 'a' or key == 'd':
        lev1.player.vx = 0