import pygame
import addons.SpritesheetMan
import blocks.floors
import blocks.walls
import blocks.doors
import blocks.air
import time

pygame.init()
screen = pygame.display.set_mode([640,640])
pygame.display.set_caption("SpaceStation13 PyEdition")

##### Loader #####
#f_floor = pygame.image.load(".\\textures\\floor\\floor.png")
#f_space = pygame.image.load(".\\textures\\floor\\space.png")

run = True
i = 0
i2 = 0

playerPos = (0, 0)

objectMap = [[blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.walls.wall(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air()],
        [blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.walls.wall(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air()],
        [blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.walls.wall(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air()],
        [blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.walls.wall(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air()],
        [blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.doors.externalDoor(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air()],
        [blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.walls.wall(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air()],
        [blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.walls.wall(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air()],
        [blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.walls.wall(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air()],
        [blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.walls.wall(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air()],
        [blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.walls.wall(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air(), blocks.air.air()],]

floorMap = [[blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space()],
        [blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space()],
        [blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space()],
        [blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space()],
        [blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space()],
        [blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space()],
        [blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space()],
        [blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space()],
        [blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space()],
        [blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.floor(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space(), blocks.floors.space()],]


#f_floor = pygame.transform.scale(f_floor, (64,64))
c = 0
objectMap[4][3].setState("closing")
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255, 255, 255))

    # Just draw floor
    i2 = 0
    while (i2 < 10):
        i = 0
        while (i < 10):
            if (floorMap[i2][i].type != "door"):
                t = pygame.image.load(floorMap[i2][i].texture)
                t = pygame.transform.scale(t, (64, 64))
                screen.blit(t, (i * 64, i2 * 64))
            else:
                if (floorMap[i2][i].needsAnimation):
                    if (floorMap[i2][i].animationStarted == False):
                        ani = addons.SpritesheetMan.spritesheet(floorMap[i2][i].texture)
                        floorMap[i2][i].animationStarted = True
                        floorMap[i2][i].animationTime = time.time()
                    if (floorMap[i2][i].animationTime + 0.1 < time.time()):
                        floorMap[i2][i].animationTime = time.time()
                        floorMap[i2][i].nextFrame()
                        print(floorMap[i2][i].animationFrame)
                        floorMap[i2][i].tick()
                    frame = ani.image_at(floorMap[i2][i].calcAnimationPos())
                    frame = pygame.transform.scale(frame, (64, 64))
                    screen.blit(frame, (i * 64, i2 * 64))
                else:
                    t = pygame.image.load(floorMap[i2][i].texture)
                    t = pygame.transform.scale(t, (64, 64))
                    screen.blit(t, (i * 64, i2 * 64))
            i -= -1
        i2 -=- 1

    ## Just draw objects
    i2 = 0
    while(i2<10):
        i = 0
        while(i< 10):
            if(objectMap[i2][i].type != "door"):
                if(objectMap[i2][i].type == "air"):
                    pass
                else:
                    t = pygame.image.load(objectMap[i2][i].texture)
                    t = pygame.transform.scale(t, (64,64))
                    screen.blit(t, (i*64,i2*64))
            else:
                if(objectMap[i2][i].needsAnimation):
                    if(objectMap[i2][i].animationStarted == False):
                        ani = addons.SpritesheetMan.spritesheet(objectMap[i2][i].texture)
                        objectMap[i2][i].animationStarted = True
                        objectMap[i2][i].animationTime = time.time()
                    if (objectMap[i2][i].animationTime + 0.1 < time.time()):
                        objectMap[i2][i].animationTime = time.time()
                        objectMap[i2][i].nextFrame()
                        print(objectMap[i2][i].animationFrame)
                        objectMap[i2][i].tick()
                    frame = ani.image_at(objectMap[i2][i].calcAnimationPos())
                    frame = pygame.transform.scale(frame, (64, 64))
                    screen.blit(frame, (i * 64, i2 * 64))
                else:
                    t = pygame.image.load(objectMap[i2][i].texture)
                    t = pygame.transform.scale(t, (64, 64))
                    screen.blit(t, (i * 64, i2 * 64))
            i-=-1
        i2 -=- 1




    print("Whole draw done")
    #if(c == 250):
    #    print("door cycle")
    #    objectMap[4][3].cycleState()
    #    c = 0

    c -=-1
    pygame.display.flip()


pygame.quit()