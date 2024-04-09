import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Fruit Catching Game")

# Load basket image
BASKET_WIDTH = 100
BASKET_HEIGHT = 100
basket_image = pygame.image.load('basket.png')
basket_image = pygame.transform.scale(basket_image, (BASKET_WIDTH, BASKET_HEIGHT))

# Load fruit images
apple_image = pygame.image.load('apple.png')
new_apple_width = apple_image.get_width() // 50
new_apple_height = apple_image.get_height() // 50
apple_image = pygame.transform.scale(apple_image, (new_apple_width, new_apple_height))
banana_image = pygame.image.load('banana.png')
new_width = banana_image.get_width() // 10
new_height = banana_image.get_height() // 10
banana_image = pygame.transform.scale(banana_image, (new_width, new_height))
orange_image = pygame.image.load('orange.png')
new_orange_width = orange_image.get_width() // 50
new_orange_height = orange_image.get_height() // 50
orange_image = pygame.transform.scale(orange_image, (new_orange_width, new_orange_height))
bomb_image = pygame.image.load('bomb.png')
new_bomb_height = bomb_image.get_height() // 5
new_bomb_width = bomb_image.get_width() // 5
bomb_image = pygame.transform.scale(bomb_image, (new_bomb_width, new_bomb_height))

# Define fruit properties
FRUIT_WIDTH = 40
FRUIT_HEIGHT = 40
FRUIT_INITIAL_SPEED = 1
FRUIT_SPEED_INCREMENT = 0.4
FRUIT_TYPES = [apple_image, banana_image, orange_image]

# Define basket properties
BASKET_SPEED = 5
BOMB_PROBABILITY = 0.1  # Adjusted bomb probability

# Define game variables
score = 0
level = 1
balls_missed = 0
level_up_score = 20
game_over = False

# Load sound effects
ding_sound = pygame.mixer.Sound('ding.wav')
bomb_sound = pygame.mixer.Sound('bomb_sound.wav')

# Load background music
pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)  # Play music indefinitely

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

background_color = random_color()  # Initialize background color

# Define game functions
def create_fruit():
    if random.random() < BOMB_PROBABILITY:
        fruit_image = bomb_image
        fruit_x = random.randint(FRUIT_WIDTH // 2, WINDOW_WIDTH - FRUIT_WIDTH // 2)
        fruit_y = -FRUIT_HEIGHT // 2
        fruit_speed = FRUIT_INITIAL_SPEED + (level - 1) * FRUIT_SPEED_INCREMENT
        return [fruit_x, fruit_y, fruit_image, fruit_speed]
    else:
        fruit_type = random.choice(FRUIT_TYPES)
        fruit_x = random.randint(FRUIT_WIDTH // 2, WINDOW_WIDTH - FRUIT_WIDTH // 2)
        fruit_y = -FRUIT_HEIGHT // 2
        fruit_speed = FRUIT_INITIAL_SPEED + (level - 1) * FRUIT_SPEED_INCREMENT
        return [fruit_x, fruit_y, fruit_type, fruit_speed]

def move_basket(keys):
    basket_x = basket[0]
    if keys[pygame.K_LEFT] and basket_x > BASKET_WIDTH // 2:
        basket_x -= BASKET_SPEED
    if keys[pygame.K_RIGHT] and basket_x < WINDOW_WIDTH - BASKET_WIDTH // 2:
        basket_x += BASKET_SPEED
    return [basket_x, basket[1]]

def check_collision(fruit, basket):
    fruit_x, fruit_y, fruit_image, _ = fruit
    basket_x, basket_y = basket
    if (basket_x - BASKET_WIDTH // 2 <= fruit_x <= basket_x + BASKET_WIDTH // 2) and \
       (basket_y - BASKET_HEIGHT // 2 <= fruit_y + FRUIT_HEIGHT // 2 <= basket_y):
        if fruit_image == apple_image or fruit_image == banana_image or fruit_image == orange_image:
            pygame.mixer.Sound.play(ding_sound)  # Play the "ding" sound effect
            return 10
        elif fruit_image == bomb_image:
            return -1  # Return -1 to indicate a bomb collision
    return 0

def draw_game_over_screen():
    game_window.fill((255, 255, 255))
    font = pygame.font.Font(None, 48)
    text = font.render("Game Over", True, (255, 0, 0))
    game_window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
    play_again_text = font.render("Would you like to play again (y/n)", True, (0, 0, 0))
    game_window.blit(play_again_text, (WINDOW_WIDTH // 2 - play_again_text.get_width() // 2, WINDOW_HEIGHT // 2 + text.get_height()))

# Game loop
running = True
fruits = []
basket = [WINDOW_WIDTH // 2, WINDOW_HEIGHT - BASKET_HEIGHT // 2]
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y and game_over:
                score = 0
                level = 1
                balls_missed = 0
                level_up_score = 20
                game_over = False
                fruits = []
                basket = [WINDOW_WIDTH // 2, WINDOW_HEIGHT - BASKET_HEIGHT // 2]
                background_color = random_color()  # Reset background color
            elif event.key == pygame.K_n and game_over: 
                running = False
    if not game_over:
        # Move the basket
        keys = pygame.key.get_pressed()
        basket = move_basket(keys)

        # Create new fruits
        if len(fruits) < level:
            fruits.append(create_fruit())

        # Move and check fruits
        for fruit in fruits[:]:
            fruit[1] += fruit[3]
            points = check_collision(fruit, basket)
            if points > 0:
                score += points
                if score >= level_up_score * level:
                    level += 1
                    level_up_score += 20
                    balls_missed = 0
                    # Increase fruit speed with each level
                    for fruit in fruits:
                        fruit[3] = FRUIT_INITIAL_SPEED + (level - 1) * FRUIT_SPEED_INCREMENT
                    background_color = random_color()  # Change background color
                fruits.remove(fruit)
            elif points == -1:  # Bomb caught
                pygame.mixer.Sound.play(bomb_sound)
                fruits.remove(fruit)  # Remove the bomb from the list
                score = 0  # Reset score
                level = 1  # Reset level
                balls_missed = 0  # Reset missed balls counter
                game_over = True
            elif fruit[1] > WINDOW_HEIGHT + FRUIT_HEIGHT // 2 and fruit[2] != bomb_image:  # Exclude bomb from missed fruit count
                fruits.remove(fruit)
                balls_missed += 1
                if balls_missed >= 5:
                    score = 0
                    level = 1
                    balls_missed = 0
                    game_over = True

        # Clear the game window
        game_window.fill(background_color)

        # Draw the basket
        game_window.blit(basket_image, (basket[0] - BASKET_WIDTH // 2, basket[1] - BASKET_HEIGHT // 2))

        # Draw the fruits
        for fruit in fruits:
            game_window.blit(fruit[2], (fruit[0] - FRUIT_WIDTH // 2, fruit[1] - FRUIT_HEIGHT // 2))

        # Display the score and level
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, (0, 0, 0))
        game_window.blit(text, (10, 10))
        text = font.render(f"Level: {level}", True, (0, 0, 0))
        game_window.blit(text, (10, 40))
        missed_text = font.render(f"Missed: {balls_missed}", True, (0, 0, 0))
        game_window.blit(missed_text, (10, 70))

    else:
        draw_game_over_screen()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
