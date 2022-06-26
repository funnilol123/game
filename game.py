import pygame.event
from pygame import *
import os

window = display.set_mode((960, 600))
pygame.display.set_caption("Tax evasion")

FPS = 60

room = pygame.image.load("room.png")


def main():
    clock = pygame.time.Clock()
    game = True
    while game:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        window.blit(room, (0, 0))
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
