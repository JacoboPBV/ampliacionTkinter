import threading
import tkinter as tk
from io import BytesIO

from pybuilder.core import after

from NotasMode1 import NotasMode1
from VistaNotas import VistaNotas
from PIL import Image, ImageTk
import requests


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

        self.vista.root.bind("<Button-1>", self.actualizar_coordenadas)

    def agregar_nota(self):
        if self.vista.entrada.get().strip() != "":
            nota = self.vista.entrada.get().strip()
            self.actualizar_listbox(self.modelo.agregar_nota(nota))

    def eliminar_nota(self):
        if self.vista.listbox.curselection():
            self.actualizar_listbox(self.modelo.eliminar_nota(self.vista.listbox.curselection()[0]))

    def guardar_notas(self):
        self.actualizar_listbox(self.modelo.guardar_notas())

    def cargar_notas(self):
        self.actualizar_listbox(self.modelo.cargar_notas())

    def iniciar_descarga(self, url, callback):
        try:
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            imagen = Image.open(BytesIO(respuesta.content))
            imagen_tk = ImageTk.PhotoImage(imagen)

            self.vista.imagenLabel.config(image=imagen_tk)
            self.vista.root.after(0, callback, imagen_tk)
        except requests.exceptions.RequestException as e:
            print(f"Error al descargar la imagen: {e}")
            self.vista.root.after(0, callback, None)

    def actualizar_etiqueta(self, imagen_tk):
        if imagen_tk:
            self.vista.imagenLabel.config(image=imagen_tk)
            self.vista.imagenLabel.image = imagen_tk  # Mantener una referencia
        else:
            self.vista.imagenLabel.config(text="Error al descargar la imagen.")
    def descargar_imagen(self):
        url = "https://raw.githubusercontent.com/JacoboPBV/notesApp/refs/heads/main/fotoEjemplo.jpg"
        hilo = threading.Thread(target=self.iniciar_descarga, args=(url, self.actualizar_etiqueta))
        hilo.start()


    def actualizar_coordenadas(self, event):
        self.vista.etiqueta.config(text=f"NoteAPP Agenda\t\tX: {event.x} | Y: {event.y}")

    def actualizar_listbox(self, notas):
        self.vista.listbox.delete(0, self.vista.listbox.size() - 1)
        for nota in notas:
            self.vista.listbox.insert(tk.END, nota)
