import pygame
import random
import math
from particle import Particle
import time

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

names = ["Alice", "Bob", "Charlie", "David", "James"]
font = pygame.font.SysFont(None, 36)

center = (WIDTH // 2, HEIGHT // 2)
radius = WIDTH // 2 - 10

particles = []
celebrate = False
celebrate_time = 0 
MAX_CELEBRATE_TIME = 200 

colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in names]

def draw_text_with_outline(surface, text, position, font, text_color, outline_color):
    x, y = position
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for dx, dy in directions:
        surface.blit(font.render(text, True, outline_color), (x + dx, y + dy))

    surface.blit(font.render(text, True, text_color), position)

def draw_ticker():
    ticker_base_width = 20
    ticker_height = 30
    pygame.draw.polygon(screen, BLACK, [(WIDTH//2 - ticker_base_width//2, 0), (WIDTH//2 + ticker_base_width//2, 0), (WIDTH//2, ticker_height)])

def draw_wheel(angle):
    segment_angle = 360 / len(names)
    
    for idx, name in enumerate(names):
        start_angle = segment_angle * idx + angle
        end_angle = segment_angle * (idx + 1) + angle
        
        color = colors[idx]

        points = [center]
        num_points = 20 
        for i in range(num_points):
            segment_start = start_angle + (end_angle - start_angle) * i / (num_points - 1)
            points.append((center[0] + radius * math.cos(math.radians(segment_start)), center[1] + radius * math.sin(math.radians(segment_start))))
        pygame.draw.polygon(screen, color, points)
        
        name_position = (center[0] + (radius // 2) * math.cos(math.radians((start_angle + end_angle) / 2)),
                     center[1] + (radius // 2) * math.sin(math.radians((start_angle + end_angle) / 2)))

        text_surface = font.render(name, True, BLACK)
        text_position = (name_position[0] - text_surface.get_width() // 2, name_position[1] - text_surface.get_height() // 2)
        draw_text_with_outline(screen, name, text_position, font, BLACK, WHITE)

def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # filter out brown shades (will need adjust prolly)
    while (abs(r - g) < 50 and b < r and b < g) or (r + g > 2.5 * b and r > 100 and g > 100 and b < 100):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

    return (r, g, b)

angle = 0
spin_speed = random.randint(5, 15)



while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0) 

    screen.fill(WHITE)
    draw_wheel(angle)
    draw_ticker()

    if celebrate:
        for particle in particles:
            particle.move()
            particle.draw(screen)
        celebrate_time += 1

        if celebrate_time >= MAX_CELEBRATE_TIME:
            break

    else:
        angle += spin_speed
        angle %= 360
        spin_speed -= 0.05
        if spin_speed <= 0 and not celebrate:
            for _ in range(200): 
                color = generate_color()
                particles.append(Particle(random.randint(0, WIDTH), 0, color))
            celebrate = True

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
