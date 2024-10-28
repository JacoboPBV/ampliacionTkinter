import tkinter as tk

class VistaNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación MVC con Tkinter")

        self.etiqueta = tk.Label(root, text="NoteAPP Agenda\t\tX: 0 | Y: 0")
        self.etiqueta.pack()

        self.listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.listbox.pack()

        self.entrada = tk.Entry(root)
        self.entrada.pack()

        self.agregarButton = tk.Button(root, text="Agregar nota")
        self.agregarButton.pack()
        self.eliminarButton = tk.Button(root, text="Eliminar nota")
        self.eliminarButton.pack()
        self.guardarButton = tk.Button(root, text="Guardar notas")
        self.guardarButton.pack()
        self.cargarButton = tk.Button(root, text="Cargar notas")
        self.cargarButton.pack()
        self.imagenButton = tk.Button(root, text="Descargar imagen")
        self.imagenButton.pack()

        self.imagenLabel = tk.Label(root, text="Imagen GitHub")
        self.imagenLabel.pack()
