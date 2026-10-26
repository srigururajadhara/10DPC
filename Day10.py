import random
import sys
import pygame

# -------------------- Settings --------------------
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 25
HUD_HEIGHT = 60
WIDTH = GRID_WIDTH * CELL_SIZE
HEIGHT = GRID_HEIGHT * CELL_SIZE + HUD_HEIGHT
FPS = 60
MOVE_DELAY_MS = 110

# Colors (R, G, B)
BACKGROUND = (18, 24, 32)
BOARD_COLOR = (25, 34, 43)
GRID_COLOR = (34, 44, 54)
SNAKE_COLOR = (75, 220, 125)
SNAKE_HEAD_COLOR = (120, 255, 160)
FOOD_COLOR = (255, 90, 90)
TEXT_COLOR = (245, 248, 250)
MUTED_TEXT = (175, 190, 200)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)
small_font = pygame.font.Font(None, 24)
large_font = pygame.font.Font(None, 54)


def new_food(snake):
    """Choose a random grid position that is not occupied by the snake."""
    empty_cells = [
        (x, y)
        for x in range(GRID_WIDTH)
        for y in range(GRID_HEIGHT)
        if (x, y) not in snake
    ]
    return random.choice(empty_cells) if empty_cells else None


def reset_game():
    start_x = GRID_WIDTH // 2
    start_y = GRID_HEIGHT // 2
    snake = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
    direction = (1, 0)
    food = new_food(snake)
    score = 0
    game_over = False
    paused = False
    return snake, direction, food, score, game_over, paused


def draw_text(text, font_obj, color, x, y, center=False):
    image = font_obj.render(text, True, color)
    rect = image.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(image, rect)

def draw_board(snake, food, score, high_score, paused, game_over):
    screen.fill(BACKGROUND)
    draw_text(f"Score: {score}", font, TEXT_COLOR, 15, 17)
    draw_text(f"Best: {high_score}", font, MUTED_TEXT, 170, 17)
    draw_text("Move: Arrows / WASD   Pause: P   Restart: R", small_font, MUTED_TEXT, 310, 21)

    board_rect = pygame.Rect(0, HUD_HEIGHT, WIDTH, GRID_HEIGHT * CELL_SIZE)
    pygame.draw.rect(screen, BOARD_COLOR, board_rect)

    # Subtle grid lines
    for x in range(0, WIDTH + 1, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, HUD_HEIGHT), (x, HEIGHT), 1)
    for y in range(HUD_HEIGHT, HEIGHT + 1, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y), 1)

    if food is not None:
        food_rect = pygame.Rect(
            food[0] * CELL_SIZE + 2,
            HUD_HEIGHT + food[1] * CELL_SIZE + 2,
            CELL_SIZE - 4,
            CELL_SIZE - 4,
        )
        pygame.draw.rect(screen, FOOD_COLOR, food_rect, border_radius=6)

    for index, (x, y) in enumerate(snake):
        segment = pygame.Rect(
            x * CELL_SIZE + 1,
            HUD_HEIGHT + y * CELL_SIZE + 1,
            CELL_SIZE - 2,
            CELL_SIZE - 2,
        )
        color = SNAKE_HEAD_COLOR if index == 0 else SNAKE_COLOR
        pygame.draw.rect(screen, color, segment, border_radius=5)

    if paused or game_over:
        overlay = pygame.Surface((WIDTH, GRID_HEIGHT * CELL_SIZE), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, HUD_HEIGHT))
        if game_over:
            title = "You Win!" if food is None else "Game Over"
            draw_text(title, large_font, TEXT_COLOR, WIDTH // 2, HEIGHT // 2 - 25, center=True)
            draw_text("Press R to play again or Esc to quit", font, TEXT_COLOR,
                      WIDTH // 2, HEIGHT // 2 + 22, center=True)
        else:
            draw_text("Paused", large_font, TEXT_COLOR, WIDTH // 2, HEIGHT // 2 - 10, center=True)
            draw_text("Press P to continue", font, TEXT_COLOR,
                      WIDTH // 2, HEIGHT // 2 + 30, center=True)

    pygame.display.flip()


def main():
    snake, direction, food, score, game_over, paused = reset_game()
    high_score = 0
    last_move_time = pygame.time.get_ticks()

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_r:
                    snake, direction, food, score, game_over, paused = reset_game()
                    last_move_time = pygame.time.get_ticks()
                    continue

                if event.key == pygame.K_p and not game_over:
                    paused = not paused

                if not game_over and not paused:
                    requested_direction = direction
                    if event.key in (pygame.K_UP, pygame.K_w):
                        requested_direction = (0, -1)
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        requested_direction = (0, 1)
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        requested_direction = (-1, 0)
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        requested_direction = (1, 0)

                    # Prevent the snake from reversing directly into itself.
                    if requested_direction != (-direction[0], -direction[1]):
                        direction = requested_direction

        now = pygame.time.get_ticks()
        if not game_over and not paused and now - last_move_time >= MOVE_DELAY_MS:
            last_move_time = now
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])

            # Wall collision
            if not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT):
                game_over = True
            else:
                eating = new_head == food
                body_to_check = snake if eating else snake[:-1]

                # Self collision
                if new_head in body_to_check:
                    game_over = True
                else:
                    snake.insert(0, new_head)
                    if eating:
                        score += 1
                        high_score = max(high_score, score)
                        food = new_food(snake)
                        if food is None:
                            game_over = True
                    else:
                        snake.pop()

        draw_board(snake, food, score, high_score, paused, game_over)


if __name__ == "__main__":
    main()
    