

class Materia():
    def __init__(self, materia=''):
        self._materia = materia
    
    #Porpiedades de las materias
    @property
    def materia(self):
        return self._materia

    @materia.setter
    def materia(self, value):
        self._materia = value

    @materia.deleter
    def materia(self):
        del self._materia
    
