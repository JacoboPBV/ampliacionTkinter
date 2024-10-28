from NotasMode1 import NotasMode1
from VistaNotas import VistaNotas


class ControladorNotas:
    def __init__(self, modelo, vista):
        self.modelo: NotasMode1 = modelo
        self.vista: VistaNotas = vista

        # Inicializar la vista con datos del modelo
        self.vista.actualizar_etiqueta(self.modelo.obtener_notas())

        # Asociar eventos
        self.vista.agregarButton.config(command=self.agregar_nota())
        self.vista.eliminarButton.config(command=self.eliminar_nota())
        self.vista.guardarButton.config(command=self.guardar_notas())
        self.vista.cargarButton.config(command=self.cargar_notas())
        self.vista.imagenButton.config(command=self.descargar_imagen())
        self.vista.agregarButton.config(command=self.agregar_nota())

    def agregar_nota(self):
        nota = self.vista.entrada.get()
        self.modelo.agregar_nota(nota)
        self.vista.actualizar_etiqueta(self.modelo.obtener_notas())

    def eliminar_nota(self):
        nuevo_texto = self.vista.entrada.get()
        self.modelo.eliminar_nota(nuevo_texto)
        self.vista.actualizar_etiqueta(self.modelo.obtener_notas())

    def guardar_notas(self):
        nuevo_texto = self.vista.entrada.get()
        self.modelo.guardar_notas(nuevo_texto)
        self.vista.actualizar_etiqueta(self.modelo.obtener_notas())

    def cargar_notas(self):
        nuevo_texto = self.vista.entrada.get()
        self.modelo.cargar_notas(nuevo_texto)
        self.vista.actualizar_etiqueta(self.modelo.obtener_notas())

    def descargar_imagen(self):
        nuevo_texto = self.vista.entrada.get()
        self.modelo.actualizar_datos(nuevo_texto)
        self.vista.actualizar_etiqueta(self.modelo.obtener_notas())

    def actualizar_coordenadas(self):
        nuevo_texto = self.vista.entrada.get()
        self.modelo.actualizar_datos(nuevo_texto)
        self.vista.actualizar_etiqueta(self.modelo.obtener_notas())

    def actualizar_listbox(self):
        pass
