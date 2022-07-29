import pygame
import os
from funtions.handles import drawWindow, naveHandleMovement, ufoHandleMovement, bulletHandle, drawWinner, NAVEHEIGHT, NAVEWIDTH, FPS, MAX_BULLETS, UFOHIT, NAVEHIT, WIN

pygame.mixer.init()

hitSound = pygame.mixer.Sound('assets/boom.wav')
shotSound = pygame.mixer.Sound('assets/disparo.wav')

BOOM_IMG = pygame.image.load(os.path.join('assets', 'boom.png'))
BOOM = pygame.transform.scale(BOOM_IMG, (NAVEWIDTH, NAVEHEIGHT))




#función principal
def main():

    #hitbox de las naves
    naveBox = pygame.Rect(200, 300, NAVEWIDTH, NAVEHEIGHT)
    ufoBox = pygame.Rect(900, 300, NAVEWIDTH, NAVEHEIGHT)

    naveBullets = []
    ufoBullets = []

    #vida de las naves
    naveHealt = 15
    ufoHealt = 15

    clock = pygame.time.Clock()
    run = True

    while run:
        #se encarga que el bucle se repita 60 veces por segundo
        clock.tick(FPS)

        #pygame.event es una lista de eventos que pasan en el juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            #condicional que comprueba si se ha disparado y cuantas balas
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(naveBullets) < MAX_BULLETS:
                    bullet = pygame.Rect(naveBox.x + naveBox.width, naveBox.y + naveBox.height//2 + 5, 15, 7)
                    naveBullets.append(bullet)
                    shotSound.play()

                if event.key == pygame.K_RCTRL and len(ufoBullets) < MAX_BULLETS:
                    bullet = pygame.Rect(ufoBox.x - 5, ufoBox.y + ufoBox.height//2 + 5, 15, 7)
                    ufoBullets.append(bullet)
                    shotSound.play()

            
            if event.type == UFOHIT:
                ufoHealt -= 1
                hitSound.play()
            if event.type == NAVEHIT:
                naveHealt -= 1
                hitSound.play()

        winnerText = ''
        if naveHealt <= 0:
            hitSound.play()
            winnerText = 'Jugador2 Wins!'
            WIN.blit(BOOM, (naveBox.x ,naveBox.y))
        if ufoHealt <= 0:
            hitSound.play()
            winnerText = 'Jugador1 Wins!'
            WIN.blit(BOOM, (ufoBox.x ,ufoBox.y))
        if winnerText != '':
            drawWinner(winnerText)
            break #con el break sales del bucle para que se vuelva a ejecutar el main y por lo tanto el juego


        teclasPulsadas = pygame.key.get_pressed()
        naveHandleMovement(teclasPulsadas, naveBox)
        ufoHandleMovement(teclasPulsadas, ufoBox)
        bulletHandle(naveBullets, ufoBullets, naveBox, ufoBox)
        drawWindow(naveBox, ufoBox, naveBullets, ufoBullets, naveHealt, ufoHealt)
    
    main()

if __name__ == '__main__':
    main()