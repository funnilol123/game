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

dooranim1 = pygame.image.load("dooropen1.png")
dooranim2 = pygame.image.load("dooropen2.png")
behindoor = pygame.image.load("roombehindoor.png")
doorblock = pygame.image.load("roomdoorblock.png")
windowblock = pygame.image.load("roomwinblock.png")
ventblock = pygame.image.load("roomventblock.png")

font.init()
font = font.Font(None, 70)
win = font.render("You evaded taxes successfully", True, (0, 215, 0))

# mixer.init()
# mixer.music.load("police.wav")
# mixer.music.play()
clock = pygame.time.Clock()

current_time = 0
animhappened_time = 0
lose = 0
overalllost = 0
pressed = 0
success = 0

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


        if current_time > 10000 and lose == 0:
            whatappears = randint(1, 3)
            current_time = 0
            lose = 1
            if whatappears == 1:
                mixer.init()
                mixer.music.load("steps.wav")
                mixer.music.play()
                while current_time < 10000 and pressed == 0:
                    current_time = current_time + 17
                    print("dog")
                    print(current_time)

                    if key.get_pressed()[K_l]:
                        current_time = 0
                        mixer.init()
                        mixer.music.load("hammer.wav")
                        mixer.music.play()
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(ventblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        game = False
                        pressed = 1

                    if key.get_pressed()[K_k]:
                        current_time = 0
                        mixer.init()
                        mixer.music.load("curtains.wav")
                        mixer.music.play()
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(windowblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        game = False
                        pressed = 1

                    if key.get_pressed()[K_j]:
                        current_time = 0
                        mixer.init()
                        mixer.music.load("hammer.wav")
                        mixer.music.play()
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(doorblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        lose = 0
                        pressed = 1


                    window.blit(room, (0, 0))
                    clock.tick(FPS)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game = False
            if whatappears == 2:
                mixer.init()
                mixer.music.load("Helicopter.wav")
                mixer.music.play()
                while current_time < 10000 and pressed == 0:
                    current_time = current_time + 17
                    print("dog2")
                    print(current_time)

                    if key.get_pressed()[K_j]:
                        current_time = 0
                        mixer.init()
                        mixer.music.load("hammer.wav")
                        mixer.music.play()
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(doorblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        game = False
                        pressed = 1

                    if key.get_pressed()[K_l]:
                        current_time = 0
                        mixer.init()
                        mixer.music.load("hammer.wav")
                        mixer.music.play()
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(ventblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        game = False
                        pressed = 1

                    if key.get_pressed()[K_k]:
                        current_time = 0
                        mixer.init()
                        mixer.music.load("curtains.wav")
                        mixer.music.play()
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(windowblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        lose = 0
                        pressed = 1



                    window.blit(room, (0, 0))
                    clock.tick(FPS)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game = False
            if whatappears == 3:
                mixer.init()
                mixer.music.load("vent.wav")
                mixer.music.play()
                while current_time < 10000 and pressed == 0:
                    current_time = current_time + 17
                    print("dog3")
                    print(current_time)

                    if key.get_pressed()[K_j]:
                        mixer.init()
                        mixer.music.load("hammer.wav")
                        mixer.music.play()
                        current_time = 0
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(doorblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        game = False
                        pressed = 1


                    if key.get_pressed()[K_k]:
                        current_time = 0
                        mixer.init()
                        mixer.music.load("curtains.wav")
                        mixer.music.play()
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(windowblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        game = False
                        pressed = 1

                    if key.get_pressed()[K_l]:
                        current_time = 0
                        mixer.init()
                        mixer.music.load("hammer.wav")
                        mixer.music.play()
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(ventblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        lose = 0
                        pressed = 1


                    window.blit(room, (0, 0))
                    clock.tick(FPS)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game = False

            if current_time > 10000 and lose == 1:
                if overalllost >= 3:
                    game = False

                if overalllost < 3:
                    current_time = 0
                    print("lost1")
                    while current_time < 5000:
                        print("lost2")
                        current_time = current_time + 17
                        if key.get_pressed()[K_f]:
                            print("lost3")
                            current_time = 0
                            while current_time < 500:
                                current_time = current_time + 17
                                window.blit(dooranim1, (0, 0))
                                clock.tick(FPS)
                                pygame.display.update()
                            while current_time < 1000:
                                current_time = current_time + 17
                                window.blit(dooranim2, (0, 0))
                                clock.tick(FPS)
                                pygame.display.update()
                            while current_time < 10000:
                                current_time = current_time + 17
                                window.blit(behindoor, (0, 0))
                                clock.tick(FPS)
                                pygame.display.update()
                            if current_time > 10000:
                                lose = 0
                                overalllost = overalllost + 1
                                success = 1

                        print("lost2end")
                        print(current_time)
                        window.blit(room, (0, 0))
                        clock.tick(FPS)
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                game = False

                    if success == 0:
                        game = False


            pressed = 0
        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()


