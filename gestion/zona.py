from zooAnimales.animal import Animal

class Zona:
    def __init__(self, nombre, zoo=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales=[]
    
    def agregarAnimales(self,animal):
        self._animales+=[animal]

    def cantidadAnimales(self):
        return len(self._animales)
    
    # Set and get methods

    def setNombre(self,nombre):
        self._nombre=nombre
    def getNombre(self):
        return self._nombre
    
    def setZoo(self,zoo):
        self._zoo = zoo
    def getZoo(self):
        return self._zoo
    
    def setAnimales(self,animales):
        self._animales=animales
    def getAnimales(self):
        return self._animales

    
