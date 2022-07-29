import pygame
import os

pygame.font.init()

WIDTH, HEIGHT = 1200, 700   
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#título del juego
pygame.display.set_caption("Space Game")

WHITE = (255, 255 , 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

#fuente del texto
FONT = pygame.font.SysFont('cosmicsans', 40)

#fotogramas por segundo y velocidad
FPS = 60
VEL = 5

#datos de las balas
MAX_BULLETS = 5
VEL_BULLETS = 7

NAVEHIT = pygame.USEREVENT + 1
UFOHIT = pygame.USEREVENT + 2

#imagenes de las naves
NAVEWIDTH, NAVEHEIGHT = 70, 60
NAVE_IMG = pygame.image.load(os.path.join('assets', 'nave.png'))
NAVE = pygame.transform.rotate(pygame.transform.scale(NAVE_IMG, (NAVEWIDTH, NAVEHEIGHT)), 270)

UFO_IMG = pygame.image.load(os.path.join('assets', 'ufo.png'))
UFO = pygame.transform.scale(UFO_IMG, (NAVEWIDTH, NAVEHEIGHT))


#bariable que guarda la imagen de fondo, que se consigue usando os
BG = pygame.image.load(os.path.join('assets', 'fondo.jpg'))

#le damos el tamaño de la ventana
SPACE = pygame.transform.scale(BG, (WIDTH, HEIGHT))
#función para pintar elementos en la pantalla
def drawWindow(naveBox, ufoBox, naveBullets, ufoBullets, naveHealt, ufoHealt):
    WIN.blit(SPACE, (0,0))
    WIN.blit(NAVE, (naveBox.x, naveBox.y))
    WIN.blit(UFO, (ufoBox.x, ufoBox.y))

    naveText = FONT.render('Vida '+ str(naveHealt), 1, WHITE)
    ufoText = FONT.render('Vida '+ str(ufoHealt), 1, WHITE)
    WIN.blit(naveText, (50,50))
    WIN.blit(ufoText, (1050,50))

    for bullet in naveBullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in ufoBullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

#función para mover la nave y que no se salga de la ventana
def naveHandleMovement(teclasPulsadas, nave):
    if teclasPulsadas[pygame.K_a] and nave.x - VEL > 0: #izquierda
        nave.x -= VEL
    if teclasPulsadas[pygame.K_d] and nave.x + VEL + nave.width < WIDTH: #derecha
        nave.x += VEL
    if teclasPulsadas[pygame.K_w] and nave.y - VEL > 0: #arriba
        nave.y -= VEL
    if teclasPulsadas[pygame.K_s] and nave.y + VEL + nave.height < HEIGHT - 15: #abajo
        nave.y += VEL

#función para mover el ovni y que no se salga de la ventana
def ufoHandleMovement(teclasPulsadas, ufo):
    if teclasPulsadas[pygame.K_LEFT] and ufo.x - VEL > 0: #izquierda
        ufo.x -= VEL
    if teclasPulsadas[pygame.K_RIGHT] and ufo.x + VEL + ufo.width < WIDTH: #derecha
        ufo.x += VEL
    if teclasPulsadas[pygame.K_UP] and ufo.y - VEL > 0: #arriba
        ufo.y -= VEL
    if teclasPulsadas[pygame.K_DOWN] and ufo.y + VEL + ufo.height < HEIGHT - 15: #abajo
        ufo.y += VEL

#función para las balas
def bulletHandle(naveBullets, ufoBullets, naveBox, ufoBox):
    for bullet in naveBullets:
        bullet.x += VEL_BULLETS
        if ufoBox.colliderect(bullet):
            naveBullets.remove(bullet)
            pygame.event.post(pygame.event.Event(UFOHIT))
        elif bullet.x > WIDTH:
            naveBullets.remove(bullet)


    for bullet in ufoBullets:
        bullet.x -= VEL_BULLETS
        if naveBox.colliderect(bullet):
            ufoBullets.remove(bullet)
            pygame.event.post(pygame.event.Event(NAVEHIT))
        elif bullet.x < 0:
            ufoBullets.remove(bullet)

def drawWinner(text):
    drawText = FONT.render(text, 1, WHITE)
    WIN.blit(drawText, (WIDTH/2 - drawText.get_width()/2, HEIGHT/2 - 100))
    pygame.display.update()
    pygame.time.delay(5000)