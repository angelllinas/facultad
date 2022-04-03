

class Despacho():
    def __init__(self, despacho=''):
        self._despacho = despacho

    @property
    def despacho(self):
        return self._despacho

    @despacho.setter
    def despacho(self, value):
        self._despacho = value

    @despacho.deleter
    def despacho(self):
       del self._despacho

