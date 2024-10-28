class NotasMode1:
    def __init__(self):
        self.notas = []

    def agregar_nota(self, nueva_nota):
        self.notas.append(nueva_nota)
        return self.notas

    def eliminar_nota(self, indice):
        del self.notas[indice]
        return self.notas

    def obtener_notas(self):
        return self.notas

    def guardar_notas(self):
        fichero = open("notas.txt", "w")
        for nota in self.notas:
            fichero.write(nota + "\n")

        return self.notas

    def cargar_notas(self):
        fichero = open("notas.txt", "r")
        self.notas = []
        notas = fichero.readlines()
        for nota in notas:
            self.notas.append(nota.strip())

        return self.notas
