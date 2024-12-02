import pygame
import math

# Initialize Game
pygame.init()
# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense")

# Set game clock
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Define fonts
font = pygame.font.SysFont(None, 36)

# Player stats
money = 500  # Starting money
tower_cost = 100  # Tower placement cost

# Enemy class
class Enemy:
    def __init__(self, path):
        self.path = path
        self.x, self.y = self.path[0]
        self.speed = 2
        self.path_index = 0
        self.health = 100

    def move(self):
        if self.path_index < len(self.path) - 1:
            target_x, target_y = self.path[self.path_index + 1]
            distance = math.sqrt((target_x - self.x) ** 2 + (target_y - self.y) ** 2)

            if distance > 1:
                direction_x = (target_x - self.x) / distance
                direction_y = (target_y - self.y) / distance
                self.x += direction_x * self.speed
                self.y += direction_y * self.speed
            else:
                self.path_index += 1

    def draw(self, surface):
        pygame.draw.circle(surface, RED, (int(self.x), int(self.y)), 10)

# Tower class
class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = 100
        self.damage = 20
        self.reload_time = 30
        self.last_shot = 0

    def draw(self, surface):
        pygame.draw.rect(surface, GREEN, (self.x - 20, self.y - 20, 40, 40))

    def shoot(self, enemies):
        if pygame.time.get_ticks() - self.last_shot >= self.reload_time:
            for enemy in enemies:
                distance = math.sqrt((enemy.x - self.x) ** 2 + (enemy.y - self.y) ** 2)
                if distance <= self.range:
                    enemy.health -= self.damage
                    self.last_shot = pygame.time.get_ticks()
                    break

# Define the path for the enemies
path = [(50, 50), (200, 50), (200, 400), (600, 400), (600, 100)]

# Create enemies list
enemies = []

# Create towers list
towers = []

# Define enemy spawn timer
SPAWN_DELAY = 500  # 5 seconds in milliseconds
last_spawn_time = pygame.time.get_ticks()  # Store when the last enemy spawned

# Function to display player stats
def display_stats():
    money_text = font.render(f"Money: ${money}", True, BLACK)
    screen.blit(money_text, (10, 10))
towerimg = pygame.image.load('C:\Users\shrey\OneDrive\Desktop\programs\MyGames\Locker\Tower.png')
towerimg = pygame.transform.scale(towerimg, 200, 200)
# Game loop
running = True
placing_tower = False
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the player is placing a tower
            if not placing_tower:
                placing_tower = True
            else:
                # If already placing a tower, finalize its position
                x, y = pygame.mouse.get_pos()
                if money >= tower_cost:
                    towers.append(Tower(x, y))
                    money -= tower_cost
                placing_tower = False

    # Spawn enemies every 5 seconds
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time >= SPAWN_DELAY:
        enemies.append(Enemy(path))  # Add a new enemy to the list
        last_spawn_time = current_time

    # Move and draw enemies
    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)

    # Draw and shoot towers
    for tower in towers:
        screen.blit(towerimg,x,y)
        tower.shoot(enemies)

    # Remove dead enemies and earn money for kills
    for enemy in enemies[:]:
        if enemy.health <= 0:
            enemies.remove(enemy)
            money += 50  # Earn $50 for each kill

    # Display stats
    display_stats()

    # Show a preview of tower placement if placing a tower
    if placing_tower:
        x, y = pygame.mouse.get_pos()
        pygame.draw.rect(screen, GREEN, (x - 20, y - 20, 40, 40), 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
