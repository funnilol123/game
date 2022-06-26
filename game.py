import pygame.event
from pygame import *
from random import randint
from pygame import mixer
import time

window = display.set_mode((960, 600))
pygame.display.set_caption("Tax evasion")


FPS = 1

room = pygame.image.load("room.png")

font.init()
font = font.Font(None, 70)
win = font.render("You evaded taxes successfully", True, (0, 215, 0))

# mixer.init()
# mixer.music.load("police.wav")
# mixer.music.play()

def main():
    clock = pygame.time.Clock()
    game = True
    stillgoing = True
    whatappears = 0
    while game:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        window.blit(room, (0, 0))
        window.blit(win, (10, 10))


        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
