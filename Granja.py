

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
