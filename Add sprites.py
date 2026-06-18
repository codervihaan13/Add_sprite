import pygame

# Initialize Pygame
pygame.init()

# Define basic colors
WHITE = (255, 255, 255)
BLUE = (0, 125, 255)
RED = (255, 50, 50)
BACKGROUND_COLOR = (30, 30, 30)

# Set up the game window (500x400)
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Add Sprites Assignment")

# Sprite class representing the rectangular objects
class RectSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5  # Movement speed for the controllable sprite

    # Method to handle keyboard movement
    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            
        # Optional: Keep the sprite inside the screen boundaries
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(SCREEN_WIDTH, self.rect.right)
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(SCREEN_HEIGHT, self.rect.bottom)

# Create a sprite group
all_sprites_list = pygame.sprite.Group()

# 1. Create the controllable sprite (Player)
player_sprite = RectSprite(BLUE, 100, 150, 40, 40)
all_sprites_list.add(player_sprite)

# 2. Create the static/second rectangular sprite 
static_sprite = RectSprite(RED, 300, 150, 50, 50)
all_sprites_list.add(static_sprite)

# Game loop control variables
exit_game = False
clock = pygame.time.Clock()

# Main game loop
while not exit_game:
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

    # Check for player movement keys
    player_sprite.handle_keys()

    # Fill background
    screen.fill(BACKGROUND_COLOR)
    
    # Draw all sprites on the screen
    all_sprites_list.draw(screen)

    # Refresh the display
    pygame.display.flip()
    
    # Cap frame rate to a smooth 60 FPS
    clock.tick(60)

# Clean up and exit
pygame.quit()