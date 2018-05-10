
import pygame as pg
from componentes import Jugador
import constantes as c


class Menu():
    def __init__(self):
        self.caption = "Main Menu"
        self.fin = False
        self.siguienteEstado = "Level"
        self.ventana = pg.display.get_surface()
        pg.display.set_caption(self.caption)
        self.opciones = {"Play": (448,300), "Quit": (448,364), "Credits": (416,428)}
        self.n = 0
        self.fbtn = False

    def actualizar(self):   
        self.ventana.blit(c.MenuGraficos["MenuBackground"],(0,0))
        self.ventana.blit(c.MenuGraficos["BotonPlay"],(448,300))
        self.ventana.blit(c.MenuGraficos["BotonQuit"],(448,364))
        self.ventana.blit(c.MenuGraficos["BotonCredits"],(416,428))

        key = pg.key.get_pressed()
        if (key[pg.K_DOWN] or key[pg.K_RIGHT]) and not self.fbtn:
            self.fbtn = True
            if self.n < 2:
                self.n+=1
            else:
                self.n = 0
        if (key[pg.K_UP] or key[pg.K_LEFT]) and not self.fbtn:
            self.fbtn = True
            if self.n > 0:
                self.n-=1
            else:
                self.n = 2
        if (not key[pg.K_UP]) and (not key[pg.K_RIGHT]) and (not key[pg.K_DOWN]) and (not key[pg.K_LEFT]):
            self.fbtn = False

        if key[pg.K_SPACE]:
            if self.n == 0:
                self.siguienteEstado = "Level"
                self.fin = True
            elif self.n == 1:
                self.siguienteEstado = "QUIT"
                self.fin = True
            else:
                pass

        if self.n == 0:
            self.ventana.blit(c.MenuGraficos["Puntero"],(400,296))
        elif self.n == 1:
            self.ventana.blit(c.MenuGraficos["Puntero"],(400,360))
        else:
            self.ventana.blit(c.MenuGraficos["Puntero"],(368,424))



class Level1():
    def __init__(self):
        self.fin = False
        self.siguienteEstado = "GameOver"

        self.jugador = Jugador()
        self.todos = pg.sprite.Group()
        self.todos.add(self.jugador)
        self.ventana = pg.display.get_surface()

    def actualizar(self):
        self.todos.update()
        self.ventana.fill(c.NEGRO)
        self.todos.draw(self.ventana)
        key = pg.key.get_pressed()
        if key[pg.K_b]:
            self.fin = True

class GameOver():
    def __init__(self):
        self.fin = False
        self.siguienteEstado = "Menu"
        self.ventana = pg.display.get_surface()

    def actualizar(self):
        self.ventana.fill(c.NEGRO)
        pg.draw.line(pg.display.get_surface(), c.ROJO, (0,0), (100,100))
        key = pg.key.get_pressed()
        if key[pg.K_c]:
            self.fin = True
