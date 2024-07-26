class Baskara:
    def __init__(self, coeficienteA=1, coeficienteB=0, coeficienteC=0):
        self.__coeficienteA = coeficienteA
        self.__coeficienteB = coeficienteB
        self.__coeficienteC = coeficienteC

    @property
    def coeficienteA(self):
        return self.__coeficienteA

    @coeficienteA.setter
    def coeficienteA(self, coeficienteA):
        self.__coeficienteA = coeficienteA

    @property
    def coeficienteB(self):
        return self.__coeficienteB

    @coeficienteB.setter
    def coeficienteB(self, coeficienteB):
        self.__coeficienteB = coeficienteB

    @property
    def coeficienteC(self):
        return self.__coeficienteC

    @coeficienteC.setter
    def coeficienteC(self, coeficienteC):
        self.__coeficienteC = coeficienteC
    
    def print(self):
        print(f"{self.__coeficienteA}x² + {self.__coeficienteB}x + {self.__coeficienteC}")

    def calculo(self):
        
        
        #(-b±√(b²-4ac))/(2a) .

    def raizes(self):
        pass
