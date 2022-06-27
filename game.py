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
lose = 0

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
            current_time = 0
            lose = 1
            while current_time < 10000:
                current_time = current_time + 17
                print("dog")
                print(current_time)
                if key.get_pressed()[K_DOWN]:
                    print("Done")
                    lose = 0
                window.blit(room, (0, 0))
                clock.tick(FPS)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game = False

        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()


