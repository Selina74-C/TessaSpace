import math
import pygame

def draw_spiral(screen, tidal_data, t):
    cx, cy = screen.get_width() // 2, screen.get_height() // 2
    num_points = len(tidal_data)
    base_radius = 30
    spiral_growth = 1.0
    twist = 0.5 + 0.3 * math.sin(t * 0.04)
    wave_amplitude = 18 + 8 * math.sin(t * 0.02)
    for i, value in enumerate(tidal_data):
        # Fashionable spiral: add twist and wave
        angle = (0.18 * i) + (t * 0.02) + (value * twist) + math.sin(i * 0.13 + t * 0.04) * 0.7
        radius = base_radius + spiral_growth * i + value * wave_amplitude + math.cos(i * 0.09 + t * 0.03) * 8
        x = cx + int(radius * math.cos(angle))
        y = cy + int(radius * math.sin(angle))
        # Colorful gradient with pastel effect
        hue = int(120 + 120 * math.sin(i * 0.07 + t * 0.05)) % 360
        color = pygame.Color(0)
        color.hsva = (hue, 60, 95, 100)
        pygame.draw.circle(screen, color, (x, y), 3)
    # Optionally, connect points for a flowing effect
    points = []
    for i, value in enumerate(tidal_data):
        angle = (0.18 * i) + (t * 0.02) + (value * twist) + math.sin(i * 0.13 + t * 0.04) * 0.7
        radius = base_radius + spiral_growth * i + value * wave_amplitude + math.cos(i * 0.09 + t * 0.03) * 8
        x = cx + int(radius * math.cos(angle))
        y = cy + int(radius * math.sin(angle))
        points.append((x, y))
    if len(points) > 1:
        pygame.draw.aalines(screen, (220, 220, 220), False, points, 2)
