
class Zoologico:
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas=[]

    def agregarZonas(self,zona):
        self._zonas+=[zona]

    def cantidadTotalAnimales(self):
        totAnimales=0
        for zonita in self._zonas:
            totAnimales+=zonita.cantidadAnimales()
        return totAnimales
    
    # Set and get methods

    def setNombre(self,nombre):
        self._nombre=nombre
    def getNombre(self):
        return self._nombre
    
    def setUbicacion(self,ubicacion):
        self._ubicacion=ubicacion
    def getUbicacion(self):
        return self._ubicacion
    
    def setZona(self,zonas):
        self._zonas=zonas
    def getZona(self):
        return self._zonas
