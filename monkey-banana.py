import pygame

# Initialize Pygame
pygame.init()

# Screen Dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monkey and Banana Problem")

# Load JPG Images
background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Increase sizes of objects
monkey_img = pygame.image.load("monkey.png")
monkey_img = pygame.transform.scale(monkey_img, (80, 100))  # Increased size

box_img = pygame.image.load("box.png")
box_img = pygame.transform.scale(box_img, (80, 80))  # Increased size

banana_img = pygame.image.load("banana.png")
banana_img = pygame.transform.scale(banana_img, (70, 50))  # Increased size

door_img = pygame.image.load("door.png")
door_img = pygame.transform.scale(door_img, (120, 200))  # Increased size

# Initial Positions
monkey_x, monkey_y = 30, 250  # Monkey starts near the door
box_x, box_y = 700, 270  # Adjusted for new size
banana_x, banana_y = 380, 80  # Adjusted for new size
door_open = False  # Door is closed at the start
on_box = False

clock = pygame.time.Clock()  # FPS control

# Main Game Loop
running = True
while running:
    screen.blit(background_img, (0, 0))  # Draw Background
    screen.blit(door_img, (10, 180))  # Adjusted position for larger door
    screen.blit(monkey_img, (monkey_x, monkey_y))  # Draw Monkey
    screen.blit(box_img, (box_x, box_y))  # Draw Box
    screen.blit(banana_img, (banana_x, banana_y))  # Draw Banana

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_o]:  # Open door
        door_open = True
        print("Door is open!")

    if door_open:  # Allow movement only after opening the door
        if keys[pygame.K_RIGHT]:  # Move Monkey Right
            monkey_x += 5
        if keys[pygame.K_LEFT]:  # Move Monkey Left
            monkey_x -= 5

        if keys[pygame.K_SPACE] and abs(monkey_x - box_x) < 50:  # Push Box
            box_x += 5 if monkey_x < box_x else -5
            print("Pushing box...")

        if keys[pygame.K_UP] and abs(monkey_x - box_x) < 50:  # Climb Box
            monkey_y = box_y - 80  # Adjusted for larger monkey
            on_box = True
            print("Monkey climbed the box!")

        if keys[pygame.K_g] and on_box and abs(box_x - banana_x) < 50:  # Grab Banana
            print("Monkey grabbed the banana!")
            running = False

    pygame.display.update()
    clock.tick(30)  # FPS limit

pygame.quit()
