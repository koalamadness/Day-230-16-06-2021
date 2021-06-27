class MaquinaEstado:
    
    def __init__(self):
        self.manipuladores = {}
        self.inicialEstado = None
        self.finalEstado = []

    def anadir_estado(self, nombre, manipulador, estado_final=0):
        nombre = nombre.upper()
        self.manipuladores[nombre] = manipulador
        if estado_final:
            self.finalEstado.append(nombre)

    def fijar_empiezo(self, nombre):
        self.inicialEstado = nombre.upper()

    def ejecutar(self, cargo):
        manipulador = self.manipuladores[self.inicialEstado]

        while True:
            (nuevoEstado, cargo) = manipulador(cargo)
            if nuevoEstado.upper() in self.finalEstado:
                print("Alcanzado: ", nuevoEstado)
                break 
            else:
                manipulador = self.manipuladores[nuevoEstado.upper()]  