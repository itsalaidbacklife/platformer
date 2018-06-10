from groundFile import Ground
# from sceneFile import Scene
from levelFile import Level

### LEVEL 1 ###
scene1 = [Ground(100, 750, 200), Ground(350, 700, 100), Ground(500, 650, 100), Ground(650, 600, 100), Ground(750, 550, 350)]
scene2 = [Ground(0, 550, 150), Ground(200, 500, 50), Ground(300, 430, 50), Ground(550, 700, 100), Ground(700, 650, 50), Ground(800, 600, 50), Ground(900, 850, 200)]
scene3 = [Ground(0, 850, 100), Ground(150, 800, 50), Ground(250, 750, 50), Ground(400, 750, 50), Ground(500, 650, 50), Ground(525, 650, 25), Ground(575, 550, 25), Ground(625, 450, 25), Ground(675, 350, 25), Ground(725, 225, 25), Ground(800, 100, 300)]
scene4 = [Ground(0, 100, 400), Ground(700, 900, 400)]

lev1_scenes = [scene1, scene2, scene3, scene4]
lev1 = Level(lev1_scenes)


### LEVEL 2 ###
scene2_1 = [Ground(100, 750, 1000)]
lev2_scenes = [scene2_1]
lev2 = Level(lev2_scenes)

### List of Completed Levels ###
levels = [lev1, lev2]