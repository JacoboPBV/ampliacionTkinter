class NotasMode1:
    def __init__(self):
        self.notas = []

    def agregar_nota(self, nueva_nota):
        self.notas = self.notas.append(nueva_nota)

    def eliminar_nota(self, indice):
        del self.notas[indice]

    def obtener_notas(self):
        return self.notas

    def guardar_notas(self):
        fichero = open("notas.txt", "w")
        for nota in self.notas:
            fichero.write(nota)

    def cargar_notas(self):
        fichero = open("notas.txt", "r")
        self.notas = []
        for notaGuardada in self.notas:
            nota = fichero.read(notaGuardada).strip()
            self.notas.append(nota)

