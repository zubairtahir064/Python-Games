# ==============================
# PROFESSIONAL SNAKE GAME
# ==============================

import pygame
import sys
import random

# ------------------------------
# INITIAL SETUP
# ------------------------------
pygame.init()

# Window size
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Professional Snake Game")

clock = pygame.time.Clock()

# Grid size (important for smooth movement)
BLOCK_SIZE = 20

# Colors
BLACK = (15, 15, 15)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 150, 0)
RED = (220, 0, 0)
WHITE = (255, 255, 255)

# Font
font = pygame.font.SysFont("arial", 35)
big_font = pygame.font.SysFont("arial", 70)


# ------------------------------
# FUNCTION: Draw Text
# ------------------------------
def draw_text(text, font, color, x, y):
    """Render text on screen"""
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


# ------------------------------
# FUNCTION: Generate Food
# ------------------------------
def generate_food():
    """Generate food at random grid position"""
    x = random.randrange(0, WIDTH, BLOCK_SIZE)
    y = random.randrange(0, HEIGHT, BLOCK_SIZE)
    return (x, y)


# ------------------------------
# FUNCTION: Game Loop
# ------------------------------
def game():
    # Initial snake setup
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = "RIGHT"

    food = generate_food()
    score = 0
    game_over = False

    while True:

        # ----------------------
        # HANDLE EVENTS
        # ----------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                # Movement control
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                if event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                if event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

                # Restart game
                if event.key == pygame.K_r and game_over:
                    game()  # restart

        if not game_over:

            # ----------------------
            # MOVE SNAKE
            # ----------------------
            head_x, head_y = snake[0]

            if direction == "RIGHT":
                head_x += BLOCK_SIZE
            elif direction == "LEFT":
                head_x -= BLOCK_SIZE
            elif direction == "UP":
                head_y -= BLOCK_SIZE
            elif direction == "DOWN":
                head_y += BLOCK_SIZE

            new_head = (head_x, head_y)

            # ----------------------
            # COLLISION WITH WALL
            # ----------------------
            if (
                head_x < 0 or head_x >= WIDTH or
                head_y < 0 or head_y >= HEIGHT
            ):
                game_over = True

            # ----------------------
            # COLLISION WITH SELF
            # ----------------------
            if new_head in snake:
                game_over = True

            # Add new head
            snake.insert(0, new_head)

            # ----------------------
            # FOOD COLLISION
            # ----------------------
            if new_head == food:
                score += 10
                food = generate_food()
            else:
                snake.pop()  # remove tail (only if not eating)

        # ----------------------
        # DRAW EVERYTHING
        # ----------------------
        screen.fill(BLACK)

        # Draw snake
        for i, segment in enumerate(snake):
            if i == 0:
                pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))
            else:
                pygame.draw.rect(screen, DARK_GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))

        # Draw food
        pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))

        # Draw score
        draw_text(f"Score: {score}", font, WHITE, 20, 20)

        # ----------------------
        # GAME OVER SCREEN
        # ----------------------
        if game_over:
            draw_text("GAME OVER", big_font, WHITE, WIDTH//2 - 200, HEIGHT//2 - 100)
            draw_text("Press R to Restart", font, WHITE, WIDTH//2 - 170, HEIGHT//2)

        pygame.display.update()
        clock.tick(10)  # Game speed


# ------------------------------
# RUN GAME
# ------------------------------
game()
