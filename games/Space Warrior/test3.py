#Space Invader Game

import pygame
import random
import time

#color
NEGRO = (0, 0, 0)
ROJO = ( 255,   0,   0)

class Asteriodes(pygame.sprite.Sprite):
    def __init__(self,width, height):
        super().__init__()
        self.image = img_ast
        self.image = pygame.Surface([width, height])
        #self.image.set_color(NEGRO)
        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.y = random.randrange(-300,-20)
        self.rect.x = random.randrange(700,-20)

    def update(self):
        self.rect.y +=1

        if self.rect.y > 410:
            self.reset_pos()


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = ship_nav
        self.rect = self.image.sefl_rect()

    def update(self):
        pos = pygame.mouse.get_pos()

class Proyectil(pygame.sprite.Sprite):
    """ Esta clase representa al proyectil . """
    def __init__(self):
        #  Llama al constructor de la clase padre (Sprite)
        super().__init__() 
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(ROJO)
 
        self.rect = self.image.get_rect()
         
    def update(self):
        """ Desplaza al proyectil. """
        self.rect.y -= 3



pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Space Warrior')

posicion_base = [0,0]

bloque_lista = pygame.sprite.Group()
lista_todos_sprites = pygame.sprite.Group()
lista_proyectiles = pygame.sprite.Group()

#Pone los graficos
ship_nav = pygame.image.load('ship.png').convert()
img_background = pygame.image.load('universe.jpg').convert()
img_ast = pygame.image.load('asteroid1.png').convert()
ship_nav.set_colorkey(NEGRO)
shoot_sound = pygame.mixer.Sound('laser5.ogg')

for i in range(25):
    ast = Asteriodes(20,15)

    ast.rect.x = random.randrange(display_height)
    ast.rect.y = random.randrange(display_width)

    bloque_lista.add(ast)
    lista_todos_sprites.add(ast)

prota = Ship()
lista_todos_sprites.add(prota)

hecho = False

clock = pygame.time.Clock()

puntuacion = 0
prota.rect.y = 370






while not hecho:
    clock.tick(10)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho= True

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            proyectil = Proyectil()

            proyectil.rect.x = prota.rect.x
            proyectil.rect.y = prota.rect.y
            lista_todos_sprites.add(proyectil)
            lista_proyectiles.add(proyectil)
            shoot_sound.play()

    #-----Logica 
    lista_todos_sprites.update()

    for proyectil in lista_proyectiles:
        lista_bloques_alcanzados = pygame.sprite.spritecollide(proyectil, bloque_lista, True)

        for bloque in lista_bloques_alcanzados:
            lista_proyectiles.remove(proyectil)
            lista_todos_sprites.remove(proyectil)
            puntuacion += 1
            print(puntuacion)

        if proyectil.rect.y < -10:
            lista_proyectiles.remove(proyectil)
            lista_todos_sprites.remove(proyectil)


    gameDisplay.blit(img_background, posicion_base)

    lista_todos_sprites.draw(gameDisplay)

    posicion_del_personaje = pygame.mouse.get_pos()
    x = posicion_del_personaje[0]
    y = posicion_del_personaje[1]

    #copia de la imagen en pantalla
    gameDisplay.blit(ship_nav, [x, y])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()




