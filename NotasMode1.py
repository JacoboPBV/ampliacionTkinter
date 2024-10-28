class NotasMode1:
    def __init__(self):
        self.notas = []

    def obtener_notas(self):
        return self.notas

    def agregar_nota(self, nueva_nota):
        self.notas.append(nueva_nota)
        return self.obtener_notas()

    def eliminar_nota(self, indice):
        del self.notas[indice]
        return self.obtener_notas()

    def guardar_notas(self):
        with open("notas.txt", "w") as fichero:
            for nota in self.notas:
                fichero.write(nota + "\n")

        return self.obtener_notas()

    def cargar_notas(self):
        self.notas = []
        with open("notas.txt", "r") as fichero:
            for nota in fichero.readlines():
                self.notas.append(nota.strip())

        return self.obtener_notas()
