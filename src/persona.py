class Persona():
    def __init__(self, nombre='', apellido='', ide='', estado_civil=''):
        self._nombre = nombre
        self._apellido = apellido
        self._ide = ide
        self._estado_civil = estado_sivil
    
    #Propiedades del nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @nombre.deleter
    def nombre(self):
        del self._nombre

    #Propiedades del apellido
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @apellido.deleter
    def apellido(self):
        del self._apellido
    
    #Propiedades del ide
    @property
    def ide(self):
       return  self._ide

   @ide.setter
   def ide(self, value):
       self._ide = value

    @ide.deleter
    def ide(self):
        del self._ide
    
    #Propiedades del estado_civil
    @property
    def estadoCivil(self):
        return self._estado_civil

    @estadoCivil.setter
    def estadoCivil(self, value):
        self._estado_civil = value

    @estadoCivil.deleter
    def estadoCivil(self):
        del self._estado_civil

    def __str__(self):
        return f'''   Todas las personas de la universidad:
     nombre: {self.nombre}\napellido:\ {self.apellido}
     \nid:{self.ide}\nestado civil: {self.estado_civil}'''

