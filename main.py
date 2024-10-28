import tkinter as tk
from NotasMode1 import NotasMode1
from VistaNotas import VistaNotas
from ControladorNotas import ControladorNotas


def main():
    root = tk.Tk()
    modelo = NotasMode1()
    vista = VistaNotas(root)
    controlador = ControladorNotas(modelo, vista)

    root.mainloop()


if __name__ == "__main__":
    main()
