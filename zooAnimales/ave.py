from zooAnimales.animal import Animal

class Ave(Animal):
    # Class atributes
    _Ave=[]
    halcones=0
    aguilas=0
    
    def __init__(self,nombre,edad,habitat,genero,colorPlumas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPlumas = colorPlumas
        Ave._Ave+=[self]

    @classmethod
    def crearHalcon(cls,nombre,edad,genero):
        halcon=Ave(nombre,edad,"montanas",genero,"cafe glorioso")
        cls.halcones+=1
        return halcon
    
    @classmethod
    def crearAguila(cls,nombre,edad,genero):
        aguila=Ave(nombre,edad,"montanas",genero,"blanco y amarillo")
        cls.aguilas+=1
        return aguila

    @classmethod
    def cantidadAves(cls):
        return len(cls._Ave)
    
    # Set and get methods
    def getColorPlumas(self):
        return self._colorPlumas


    
