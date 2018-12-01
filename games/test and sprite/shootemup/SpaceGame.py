"""
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/4YqIKncMJNs
 Explanation video: http://youtu.be/ONAK8VZIcI4
 Explanation video: http://youtu.be/_6c4o41BIms
"""
 
import pygame
 
# Definimos algunos colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


 
# Inicializamos
pygame.init()
 
# Creamos una pantalla de 800x600.
pantalla = pygame.display.set_mode([800, 600])
 
# Establecemos el nombre de la ventana.
pygame.display.set_caption('CMSC 150 es divertido')
 
reloj = pygame.time.Clock()
 
# Antes del bucle cargamos el sonido:
sonido_click = pygame.mixer.Sound("laser5.ogg")
 
# Establecemos la posición de los gráficos
posicion_base = [0, 0]
 
# Carga y sitúa los gráficos.
imagen_de_fondo = pygame.image.load("universe.jpg").convert()
imagen_personaje = pygame.image.load("ship.png").convert()
imagen_personaje.set_colorkey(NEGRO)
 
hecho = False
 
while not hecho:
    reloj.tick(10)
     
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            sonido_click.play() 
             
    # Copia la imagen en pantalla:
    pantalla.blit(imagen_de_fondo, posicion_base)
 
    # Obtiene la posición actual del ratón. Devuelve ésta como
    # una lista de dos números.
    posicion_del_personaje = pygame.mouse.get_pos()
    x = posicion_del_personaje[0]
    y = posicion_del_personaje[1]
     
    # Copia la imagen en pantalla:
    pantalla.blit(imagen_personaje, [x, y])
     
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()