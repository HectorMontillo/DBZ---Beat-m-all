
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

        self.opciones = ["Jugar", "Creditos", "Salir"]

    def actualizar(self):
        #self.ventana.fill(c.NEGRO)
        self.ventana.blit(c.MenuGraficos["MenuBackground"],(0,0))



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
