import pygame as pg
import constantes as c


class Jugador(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((20,20))
        self.image.fill(c.VERDE)
        self.rect = self.image.get_rect()
        self.rect.centerx = 512
        self.rect.bottom = 512
        self.xspeed = 0
        self.yspeed = 0
        self.speed = 5
        self.speedjump = 9
        self.fjump = True
        self.gravity = 0.5
        self.floorcollide = False

    def update(self):
        self.xspeed = 0
        self.rect.y += self.yspeed

        if self.yspeed == 0:
            self.yspeed = 1
        else:
            self.yspeed += self.gravity



        keystate = pg.key.get_pressed()

        if keystate[pg.K_SPACE]:
            self.speed = 10
        else:
            self.speed = 5

        if keystate[pg.K_LEFT]:
            self.xspeed = -self.speed
        if keystate[pg.K_RIGHT]:
            self.xspeed = self.speed
        self.rect.x += self.xspeed


        if keystate[pg.K_UP] and self.fjump and self.floorcollide:
            self.yspeed = -self.speedjump
            self.fjump = False
            self.floorcollide = False

        if not keystate[pg.K_UP]:
            self.fjump = True
        '''
        if keystate[pg.K_DOWN]:
            self.yspeed = self.speed
        self.rect.y += self.yspeed
        '''

        if self.rect.right > c.TAMANO_VENTANA[0]:
            self.rect.right = c.TAMANO_VENTANA[0]
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > c.TAMANO_VENTANA[1]:
            self.rect.bottom = c.TAMANO_VENTANA[1]
            self.floorcollide = True
        if self.rect.top < 0:
            self.rect.top = 0
