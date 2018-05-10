import pygame as pg

TAMANO_VENTANA = (960, 600)
CAPTION = "Level 1"

VERDE = (0,255,0)
ROJO = (255,0,0)
NEGRO = (0,0,0)

MenuGraficos = {"MenuBackground": pg.image.load("recursos/menuback.png"),
                "BotonPlay": pg.image.load("recursos/btnplay.png"),
                "BotonQuit": pg.image.load("recursos/btnquit.png"),
                "BotonCredits": pg.image.load("recursos/btncredits.png"),
                "Puntero": pg.image.load("recursos/puntero1.png")
                }
