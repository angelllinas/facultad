#Esta clase hereda de la clase persona
from persona import Persona

class Estudiante(Persona):
    def __init__(self,nombre='', apellido='', ide='', estado_civil='', curso_matriculado=''):
        super().__init__(nombre, apellido, ide, estado_civil)
        self._curso_matriculado = curso_matriculado
    
    #Propiedades de curso_matriculado
    @property
    def cursoMatriculado(self):
        return self._curso_matriculado
    
    @cursoMatriculado.setter
    def cursoMatriculado(self, value):
        self._curso_matriculado = value

    @cursoMatriculado.deleter
    def cursoMatriculado(self):
        del self._curso_matriculado

    
    def __str__(self):
        return f'''Lista Estudiantes:
    {super().__str__()}
    {self.curso_matriculado}'''


