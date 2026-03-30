
import sys
import pygame

from constants import *
from logger import log_state, log_event


def main():
    pygame_version = pygame.version.ver
    print("Hello from players-handbook-2024!")
    print(f"Starting {TITLE} with pygame version: {pygame_version}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    clock = pygame.time.Clock()
    dt = 0 # dt = "delta time"

    font = pygame.font.SysFont("Arial", 36)
    text_surface = font.render(TITLE, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updatable.update(dt)

        for d in drawable:
            d.draw(screen)

        # Inside the main game loop:
        screen.fill((127, 127, 127)) # Clear screen with background color
        screen.blit(text_surface, text_rect) # Draw the text

        pygame.display.flip()
        # wait 1/{param} of a second, return # of ms
        # divide by 1000 = delta time in seconds
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
