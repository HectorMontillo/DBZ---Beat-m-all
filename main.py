from control import Control
from preparacion import Preparar
import estados

def main():
    Preparar()
    diccionarioEstados = {"Menu": estados.Menu() , "Level" : estados.Level1(), "GameOver": estados.GameOver()}
    controlador = Control()
    controlador.preparar_estados(diccionarioEstados,diccionarioEstados["Menu"])
    controlador.main()
