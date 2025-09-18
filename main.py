import pygame
import sys
from visualization.spiral import draw_spiral
from data.tidal import get_tidal_data

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Tidal Spiral Visualization')
    clock = pygame.time.Clock()

    # Load tidal data (placeholder)
    tidal_data = get_tidal_data()

    running = True
    t = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((10, 10, 30))
        draw_spiral(screen, tidal_data, t)
        pygame.display.flip()
        t += 1
        clock.tick(60)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
