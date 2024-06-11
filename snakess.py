import pygame
import random
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLOCK_SIZE = 40
SNAKE_SPEED = 8

class Snake:
    def __init__(self):
        self.snake_list = []
        self.snake_length = 1
        self.snake_head = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
        self.snake_direction = "RIGHT"
        self.snake_head_image = pygame.image.load("./Images/head.png")
        self.snake_head_image = pygame.transform.scale(self.snake_head_image, (BLOCK_SIZE, BLOCK_SIZE))
        self.snake_segment_image = pygame.image.load("./Images/tail.png")
        self.snake_segment_image = pygame.transform.scale(self.snake_segment_image, (BLOCK_SIZE, BLOCK_SIZE))

    def move(self):
        if self.snake_direction == "RIGHT":
            self.snake_head[0] += BLOCK_SIZE
        elif self.snake_direction == "LEFT":
            self.snake_head[0] -= BLOCK_SIZE
        elif self.snake_direction == "UP":
            self.snake_head[1] -= BLOCK_SIZE
        elif self.snake_direction == "DOWN":
            self.snake_head[1] += BLOCK_SIZE

    def expand(self):
        self.snake_length += 1

    def draw(self, screen):
        screen.blit(self.snake_head_image, (self.snake_list[-1][0], self.snake_list[-1][1]))
        for segment in self.snake_list[:-1]:
            screen.blit(self.snake_segment_image, (segment[0], segment[1]))
            
    def update_snake_list(self):
        self.snake_list.append(list(self.snake_head))
        if len(self.snake_list) > self.snake_length:
            del self.snake_list[0]
class Food:
    def __init__(self):
        self.food_x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
        self.food_y = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
        self.food_image = pygame.image.load("./Images/apple.png")
        self.food_image = pygame.transform.scale(self.food_image, (BLOCK_SIZE, BLOCK_SIZE))
    def draw(self, screen):
        screen.blit(self.food_image, (self.food_x, self.food_y))
    def relocate(self):
        self.food_x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
        self.food_y = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
def draw_score(screen, score):
    font = pygame.font.SysFont(None, 35)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, [10, 10])
def main():
    pygame.init()
    pygame.mixer.init() 
    eat_sound = pygame.mixer.Sound("NomNomNom.mp3")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    score = 0
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.snake_direction != "RIGHT":
                    snake.snake_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake.snake_direction != "LEFT":
                    snake.snake_direction = "RIGHT"
                elif event.key == pygame.K_UP and snake.snake_direction != "DOWN":
                    snake.snake_direction = "UP"
                elif event.key == pygame.K_DOWN and snake.snake_direction != "UP":
                    snake.snake_direction = "DOWN"

        # Move the snake
        snake.move()
        # Check for collision with food
        if snake.snake_head[0] == food.food_x and snake.snake_head[1] == food.food_y:
            snake.expand()
            score += 1
            food.relocate()
            eat_sound.play()
        # Update snake's body
        snake.update_snake_list()
        # Check for collision with itself
        for segment in snake.snake_list[:-1]:
            if segment == snake.snake_head:
                game_over = True
        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        draw_score(screen, score)
        pygame.display.update()
        # Set game speed
        clock.tick(SNAKE_SPEED)
    pygame.quit()
    quit()
if __name__ == "__main__":
    main()









