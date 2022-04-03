# Esta clase hereda las propiedades de la clase Persona 
from persona import Persona

class Empleado(Persona):
    def __init__(self, nombre='', apellido='', ide='', estado_civil='', años_facultad=None, numero_despacho=None):
        super().__init__(nombre, apellido, ide, estado_civil)
        self._años_facultad = años_facultad
        self._numero_despacho = numero_despacho

    #Propiedades de los años que paso el empleado en la facultad
    @property
    def añosFacultad(self):
        return self._años_facultad

    @añosFacultad.setter
    def añosFacultad(self, value):
        self._años_facultad = value

    @añosFacultad.deleter
    def añosFacultad(self):
        del self._años_faculta

    #Propiedades del numero de despacho del empleado
    @property
    def numeroDespacho(self):
        return self._numero_despacho
    
    @numeroDespacho.setter
    def numeroDespacho(self, value):
        self._numero_despacho = value

    @numeroDespacho.deleter
    def numeroDespacho(self):
        del self._numero_despacho

    def __str__(self):
        return f'''Lista de empleados:
    {super().__str__()}
    {self.año_facultad}
    {self.numero_despacho}'''
