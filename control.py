import pygame as pg
from estados import Menu

class Control():
    def __init__(self):
        self.ventana = pg.display.get_surface()
        self.fin = False
        self.reloj = pg.time.Clock()
        self.caption = "None"
        self.fps = 60
        self.keys = pg.key.get_pressed()
        self.estados = None
        self.estado = None

    def update(self):
        if not self.estado.fin:
            self.estado.actualizar()
        else:
            if self.estado.siguienteEstado == "QUIT":
                self.fin = True
            else:
                self.estado.fin = False
                self.estado = self.estados[self.estado.siguienteEstado]

    def preparar_estados(self, estados, estadoinicial):
        self.estado = estadoinicial
        self.estados = estados

    def eventos(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.fin = True
            elif event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()

    def main(self):
        #self.preupdate()
        while not self.fin:
            self.eventos()
            self.update()
            pg.display.update()
            self.reloj.tick(self.fps)
