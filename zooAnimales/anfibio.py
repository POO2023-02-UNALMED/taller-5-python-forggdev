from zooAnimales.animal import Animal

class Anfibio(Animal):
    # Class atributes
    _Anfibio=[]
    ranas=0
    salamandras=0
    
    def __init__(self,nombre,edad,habitat,genero,colorPiel, venenoso):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio._Anfibio+=[self]

    @classmethod
    def crearRana(cls,nombre,edad,genero):
        rana=Anfibio(nombre,edad,"selva",genero,"rojo", True)
        cls.ranas+=1
        return rana
    
    @classmethod
    def crearSalamandra(cls,nombre,edad,genero):
        salamandra=Anfibio(nombre,edad,"selva",genero,"negro y amarillo", False)
        cls.salamandras+=1
        return salamandra

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._Anfibio)
    
    # Set and get methods
    def isVenenoso(self):
        return self._venenoso
    
    def getColorPiel(self):
        return self._colorPiel

    
