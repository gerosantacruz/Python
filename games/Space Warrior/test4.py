import pygame
import sys

pygame.init()

window = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pos_base = [0,0]

img_background = pygame.image.load('universe.jpg').convert()
ship_image = pygame.image.load('ship.png').convert()
bullet_image = pygame.image.load("bullet.png").convert()

class Sprite:
    pass
def display_sprite(sprite):
    window.blit(sprite.image, (sprite.x, sprite.y))


ship_x = 0
ship_y = 0

bullets = []
def fire_bullet():
    bullet = Sprite()
    bullet.x = ship_x + 130
    bullet.y = ship_y + 100
    bullet.image = bullet_image
    bullets.append(bullet)




while True:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        #check the movement of the ship

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_UP]:
            ship_y = ship_y - 10

        if pressed_keys[pygame.K_DOWN]:
            ship_y = ship_y + 10

        if pressed_keys[pygame.K_LEFT]:
            ship_x = ship_x - 10

        if pressed_keys[pygame.K_RIGHT]:
            ship_x = ship_x + 10

        

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire_bullet()

            # Stop ship going out of bounds
        if ship_y < 0:
            ship_y = 0

        if ship_y > window.get_height() - ship_image.get_height():
            ship_y = window.get_height() - ship_image.get_height()

        if ship_x < 0:
            ship_x = 0

        if ship_x > window.get_width() - ship_image.get_width():
            ship_x = window.get_width() - ship_image.get_width()




    window.blit(img_background, pos_base)
    window.blit(ship_image, (ship_x,ship_y))

    for bullet in bullets:
        bullet.x = bullet.x + 13


    for bullet in bullets:
        display_sprite(bullet)

    pygame.display.flip()

    clock.tick(60)