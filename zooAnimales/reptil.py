from zooAnimales.animal import Animal

class Reptil(Animal):
    # Class atributes
    _Reptil=[]
    iguanas=0
    serpientes=0
    
    def __init__(self,nombre,edad,habitat,genero,colorEscamas, largoCola):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola
        Reptil._Reptil+=[self]

    @classmethod
    def crearIguana(cls,nombre,edad,genero):
        iguana=Reptil(nombre,edad,"humedal",genero,"verde",3)
        cls.iguanas+=1
        return iguana
    
    @classmethod
    def crearSerpiente(cls,nombre,edad,genero):
        serpiente=Reptil(nombre,edad,"jungla",genero,"blanco",1)
        cls.serpientes+=1
        return serpiente

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._Reptil)
    
    # Set and get methods
    def getColorEscamas(self):
        return self._colorEscamas
    
    def getLargoCola(self):
        return self._largoCola

    
