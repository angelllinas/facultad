#Esta clase hereda de la clase persona
from persona import Persona

class Profesor(Persona):
    def __init__(nombre='', apellido='', ide='', estado_civil='',departamento='')
        super().__init__(nombre, apellido, ide, estado_civil)
        self._departamento = departamento
    
    #Propiedades de departamentoo
    @property
    def departamento(self):
        return self._departamento

    @departamento.setter
    def departamento(self, value):
        self._departamento = value

    @departamento.deleter
    def departamento(self):
        del self._departamento

    def __str__(self):
        return f''''Lista de profesores:
    {super().__str__()}
    {sef.departamento}''''

