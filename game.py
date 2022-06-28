import pygame.event
from pygame import *
from random import randint
from pygame import mixer
import time
game = True

window = display.set_mode((960, 600))
pygame.display.set_caption("Tax evasion")


FPS = 60

room = pygame.image.load("room.png")

font.init()
font = font.Font(None, 70)
win = font.render("You evaded taxes successfully", True, (0, 215, 0))

# mixer.init()
# mixer.music.load("police.wav")
# mixer.music.play()
clock = pygame.time.Clock()

current_time = 0
animhappened_time = 0
loses = 0
loseh = 0
losev = 0
pressed = 0
closet = 0
bed = 0
underdesk = 0
lookingleft = 0
lookingback = 0
lookingright = 0
belowbedtime = 0

while game:
    game = True
    stillgoing = True
    whatappears = 0
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        window.blit(room, (0, 0))

        current_time = current_time + 17
        print(current_time)


        if current_time > 10000 and loses == 0 and loseh == 0 and losev == 0:
            whatappears = randint(1, 3)
            current_time = 0
            if whatappears == 1:
                loses = 1
                mixer.init()
                mixer.music.load("steps.wav")
                mixer.music.play()
                while current_time < 10000 and pressed == 0:
                    current_time = current_time + 17
                    print("dog")
                    print(current_time)
                    if key.get_pressed()[K_j]:
                        print("Done")
                        loses = 0
                        pressed = 1
                    window.blit(room, (0, 0))
                    clock.tick(FPS)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game = False
            if whatappears == 2:
                loseh = 1
                mixer.init()
                mixer.music.load("Helicopter.wav")
                mixer.music.play()
                while current_time < 10000 and pressed == 0:
                    current_time = current_time + 17
                    print("dog2")
                    print(current_time)
                    if key.get_pressed()[K_k]:
                        print("Done2")
                        loseh = 0
                        pressed = 1
                    window.blit(room, (0, 0))
                    clock.tick(FPS)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game = False
            if whatappears == 3:
                losev = 1
                mixer.init()
                mixer.music.load("vent.wav")
                mixer.music.play()
                while current_time < 10000 and pressed == 0:
                    current_time = current_time + 17
                    print("dog3")
                    print(current_time)
                    if key.get_pressed()[K_l]:
                        print("Done3")
                        losev = 0
                        pressed = 1
                    window.blit(room, (0, 0))
                    clock.tick(FPS)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game = False

            if current_time > 10000 and loses == 1:
                game = False

            if current_time > 10000 and losev == 1:
                game = False

            if current_time > 10000 and loseh == 1:
                game = False

            pressed = 0
        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()


