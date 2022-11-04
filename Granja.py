from Perro import Perro 
from Bovino import Bovino

class Granja:

    def __init__(self):

        self.misPerros=[]
        self.misBovinos=[]

    def agregarBovino(self,peso,edad,raza,propietario,fechaVacunacion,establo):
        
        miBovino=Bovino()
        self.miBovino.peso=peso
        self.miBovino.edad=edad
        self.miBovino.raza=raza
        self.miBovino.propietario=propietario
        self.miBovino.fechaVacunacion=fechaVacunacion
        self.miBovino.establo=establo
        self.misBovinos.append(miBovino)

    def obtenerBovino(self,codigo):

        return self.misBovinos[codigo]
    
     def obtenerPerro(self, indice):
        return self.MisPerros[indice]
    
     def agregarPerro(self,peso,edad,raza,propietario,fechaVacunacion):
        miPerro=Perro()
        miPerro.edad=edad
        miPerro.edad=peso
        miPerro.edad=raza
        miPerro.edad=propietario
        miPerro.edad=fechaVacunacion

        self.MisPerros.append(miPerro)
