import pygame.event
from pygame import *
from random import randint
from pygame import mixer
import time
game = True

window = display.set_mode((960, 600))
pygame.display.set_caption("Bobby's new friend")


FPS = 60

room = pygame.image.load("room.png")

dooranim1 = pygame.image.load("dooropen1.png")
dooranim2 = pygame.image.load("dooropen2.png")
behindoor = pygame.image.load("roombehindoor.png")
doorblock = pygame.image.load("roomdoorblock.png")
windowblock = pygame.image.load("roomwinblock.png")
ventblock = pygame.image.load("roomventblock.png")
behindwindow = pygame.image.load("behindwindow.png")
behinddoor = pygame.image.load("behinddoor.png")
behinddoor2 = pygame.image.load("behinddoor21.png")
behinddoorx = pygame.image.load("behinddoorwihtoutcact.png")
jumpscare = pygame.image.load("jumpscare.png")
fake = pygame.image.load("fakemirror.png")

font.init()
font = font.Font(None, 30)



mixer.init()
mixer.music.load("cact.wav")
mixer.music.play()
clock = pygame.time.Clock()

current_time = 0
animhappened_time = 0
lose = 0
overalllost = 0
pressed = 0
success = 0
am = 0

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

        if current_time > 6000 and lose == 0:
            whatappears = randint(1, 5)
            current_time = 0
            lose = 1
            if whatappears == 1:
                mixer.init()
                mixer.music.load("steps.wav")
                mixer.music.play()
                while current_time < 2000 and pressed == 0:
                    current_time = current_time + 17
                    print("dog")
                    print(current_time)

                    if key.get_pressed()[K_l]:
                        current_time = 0
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(ventblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        mixer.init()
                        mixer.music.load("jumpscare.wav")
                        mixer.music.play()
                        current_time = 0
                        while current_time < 3000:
                            current_time = current_time + 17
                            window.blit(jumpscare, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        game = False
                        pressed = 1

                    if key.get_pressed()[K_k]:
                        current_time = 0
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(windowblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        mixer.init()
                        mixer.music.load("jumpscare.wav")
                        mixer.music.play()
                        current_time = 0
                        while current_time < 3000:
                            current_time = current_time + 17
                            window.blit(jumpscare, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        game = False
                        pressed = 1

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
                        lose = 0
                        pressed = 1
                        mixer.init()
                        mixer.music.load("cact.wav")
                        mixer.music.play()

                    window.blit(behinddoor, (0, 0))
                    clock.tick(FPS)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game = False

            if whatappears == 4:
                mixer.init()
                mixer.music.load("steps.wav")
                mixer.music.play()
                while current_time < 2000:
                    pressed = 1
                    current_time = current_time + 17
                    print("dog")
                    print(current_time)

                    if key.get_pressed()[K_l]:
                        current_time = 0
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(ventblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        mixer.init()
                        mixer.music.load("jumpscare.wav")
                        mixer.music.play()
                        current_time = 0
                        while current_time < 3000:
                            current_time = current_time + 17
                            window.blit(jumpscare, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        game = False
                        pressed = 0

                    if key.get_pressed()[K_k]:
                        current_time = 0
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(windowblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        mixer.init()
                        mixer.music.load("jumpscare.wav")
                        mixer.music.play()
                        current_time = 0
                        while current_time < 3000:
                            current_time = current_time + 17
                            window.blit(jumpscare, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        game = False
                        pressed = 0

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
                        mixer.init()
                        mixer.music.load("jumpscare.wav")
                        mixer.music.play()
                        current_time = 0
                        while current_time < 3000:
                            current_time = current_time + 17
                            window.blit(jumpscare, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        game = False
                        pressed = 0
                    window.blit(fake, (0, 0))
                    clock.tick(FPS)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game = False
                pressed = 1
                lose = 0


            if whatappears == 5:
                mixer.init()
                mixer.music.load("tap.wav")
                mixer.music.play()
                while current_time < 2000:
                    pressed = 1
                    current_time = current_time + 17
                    print("dog")
                    print(current_time)

                    if key.get_pressed()[K_l]:
                        current_time = 0
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(ventblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        mixer.init()
                        mixer.music.load("jumpscare.wav")
                        mixer.music.play()
                        current_time = 0
                        while current_time < 3000:
                            current_time = current_time + 17
                            window.blit(jumpscare, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        game = False
                        pressed = 0

                    if key.get_pressed()[K_k]:
                        current_time = 0
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(windowblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        mixer.init()
                        mixer.music.load("jumpscare.wav")
                        mixer.music.play()
                        current_time = 0
                        while current_time < 3000:
                            current_time = current_time + 17
                            window.blit(jumpscare, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        game = False
                        pressed = 0

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
                        mixer.init()
                        mixer.music.load("jumpscare.wav")
                        mixer.music.play()
                        current_time = 0
                        while current_time < 3000:
                            current_time = current_time + 17
                            window.blit(jumpscare, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        game = False
                        pressed = 0
                    window.blit(fake, (0, 0))
                    clock.tick(FPS)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game = False
                pressed = 1
                lose = 0



            if whatappears == 2:
                mixer.init()
                mixer.music.load("tap.wav")
                mixer.music.play()
                while current_time < 2000 and pressed == 0:
                    current_time = current_time + 17
                    print("dog2")
                    print(current_time)
                    if key.get_pressed()[K_j]:
                        current_time = 0
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(doorblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        mixer.init()
                        mixer.music.load("jumpscare.wav")
                        mixer.music.play()
                        current_time = 0
                        while current_time < 3000:
                            current_time = current_time + 17
                            window.blit(jumpscare, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        game = False
                        pressed = 1

                    if key.get_pressed()[K_l]:
                        current_time = 0
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(ventblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        mixer.init()
                        mixer.music.load("jumpscare.wav")
                        mixer.music.play()
                        current_time = 0
                        while current_time < 3000:
                            current_time = current_time + 17
                            window.blit(jumpscare, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        game = False
                        pressed = 1

                    if key.get_pressed()[K_k]:
                        mixer.init()
                        mixer.music.load("curtains.wav")
                        mixer.music.play()
                        current_time = 0
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(windowblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        lose = 0
                        pressed = 1
                        mixer.init()
                        mixer.music.load("cact.wav")
                        mixer.music.play()


                    window.blit(behindwindow, (0, 0))
                    clock.tick(FPS)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game = False
            if whatappears == 3:
                mixer.init()
                mixer.music.load("vent.wav")
                mixer.music.play()
                while current_time < 2000 and pressed == 0:
                    current_time = current_time + 17
                    print("dog3")
                    print(current_time)

                    if key.get_pressed()[K_j]:
                        current_time = 0
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(doorblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        mixer.init()
                        mixer.music.load("jumpscare.wav")
                        mixer.music.play()
                        current_time = 0
                        while current_time < 3000:
                            current_time = current_time + 17
                            window.blit(jumpscare, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        game = False
                        pressed = 1


                    if key.get_pressed()[K_k]:
                        current_time = 0
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(windowblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        mixer.init()
                        mixer.music.load("jumpscare.wav")
                        mixer.music.play()
                        current_time = 0
                        while current_time < 3000:
                            current_time = current_time + 17
                            window.blit(jumpscare, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                            game = False
                        pressed = 1

                    if key.get_pressed()[K_l]:
                        mixer.init()
                        mixer.music.load("hammer.wav")
                        mixer.music.play()
                        current_time = 0
                        while current_time < 1000:
                            current_time = current_time + 17
                            window.blit(ventblock, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        print("Done")
                        lose = 0
                        pressed = 1
                        mixer.init()
                        mixer.music.load("cact.wav")
                        mixer.music.play()

                    window.blit(room, (0, 0))
                    clock.tick(FPS)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game = False

            if current_time > 6000 and lose == 1 or pressed == 0:
                if overalllost >= 3:
                    mixer.init()
                    mixer.music.load("jumpscare.wav")
                    mixer.music.play()
                    current_time = 0
                    while current_time < 3000:
                        current_time = current_time + 17
                        window.blit(jumpscare, (0, 0))
                        clock.tick(FPS)
                        pygame.display.update()
                        game = False
                if overalllost < 3:
                    current_time = 0
                    print("lost1")
                    while current_time < 5000:
                        print("lost2")
                        current_time = current_time + 17
                        if key.get_pressed()[K_r]:
                            mixer.init()
                            mixer.music.load("breathing.wav")
                            mixer.music.play()
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
                            while current_time < 4000:
                                current_time = current_time + 17
                                window.blit(behindoor, (0, 0))
                                clock.tick(FPS)
                                pygame.display.update()
                            while current_time < 4500:
                                current_time = current_time + 17
                                window.blit(behinddoor2, (0, 0))
                                clock.tick(FPS)
                                pygame.display.update()
                            while current_time < 5000:
                                current_time = current_time + 17
                                window.blit(behinddoorx, (0, 0))
                                clock.tick(FPS)
                                pygame.display.update()
                            if current_time > 5000:
                                lose = 0
                                overalllost = overalllost + 1
                                success = 1
                                mixer.init()
                                mixer.music.load("cact.wav")
                                mixer.music.play()
                                whatappears = 0
                                current_time = 0
                                print("dogawter")

                        print("lost2end")
                        print(current_time)
                        window.blit(room, (0, 0))
                        clock.tick(FPS)
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                game = False

                    if success == 0:
                        mixer.init()
                        mixer.music.load("jumpscare.wav")
                        mixer.music.play()
                        current_time = 0
                        while current_time < 3000:
                            current_time = current_time + 17
                            window.blit(jumpscare, (0, 0))
                            clock.tick(FPS)
                            pygame.display.update()
                        game = False



            pressed = 0

        am = am + 17
        trueam = am/1000
        clock.tick(FPS)
        hp = font.render("Room used: " + str(overalllost), True, (255, 255, 255))
        win = font.render("Victory! " + str(overalllost), True, (0, 255, 0))
        window.blit(hp, (0, 0))
        AM = font.render("Time: " + str(trueam), True, (255, 255, 255))
        window.blit(AM, (800, 0))
        if trueam >= 10:
            window.blit(win, (0, 0))
            pygame.display.update()
            current_time = 0
            while current_time < 10000:
                window.blit(win, (0, 0))
                pygame.display.update()
                current_time = 0
            stillgoing = False

        pygame.display.update()


    pygame.quit()


