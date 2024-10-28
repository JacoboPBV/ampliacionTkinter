import tkinter as tk
from NotasMode1 import NotasMode1
from VistaNotas import VistaNotas


class ControladorNotas:
    def __init__(self, modelo, vista):
        self.modelo: NotasMode1 = modelo
        self.vista: VistaNotas = vista

        # Asociar eventos
        self.vista.agregarButton.config(command=self.agregar_nota)
        self.vista.eliminarButton.config(command=self.eliminar_nota)
        self.vista.guardarButton.config(command=self.guardar_notas)
        self.vista.cargarButton.config(command=self.cargar_notas)
        self.vista.imagenButton.config(command=self.descargar_imagen)

    def agregar_nota(self):
        nota = self.vista.entrada.get()
        self.actualizar_listbox(self.modelo.agregar_nota(nota))

    def eliminar_nota(self):
        indice = self.vista.listbox.index(self.vista.listbox.curselection()[0])
        self.actualizar_listbox(self.modelo.eliminar_nota(indice))

    def guardar_notas(self):
        self.actualizar_listbox(self.modelo.guardar_notas())

    def cargar_notas(self):
        self.actualizar_listbox(self.modelo.cargar_notas())

    def descargar_imagen(self):
        pass

    def actualizar_coordenadas(self, event):
        pass

    def actualizar_listbox(self, notas):
        self.vista.listbox.delete(0, self.vista.listbox.size() - 1)
        for nota in notas:
            self.vista.listbox.insert(tk.END, nota)
