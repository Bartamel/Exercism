class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.filas = []
        self.columnas = []
        pass

    def row(self, index):
        self.filas.append(self.matrix_string.split("/n"))
        return self.filas[index-1]

    def column(self, index):
        return self.columnas[index]
