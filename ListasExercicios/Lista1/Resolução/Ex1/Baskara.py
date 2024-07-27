import math

class Baskara:
    def __init__(self, coeficienteA:int=1, coeficienteB:int=0, coeficienteC:int=0):
        self.__coeficienteA = coeficienteA
        self.__coeficienteB = coeficienteB
        self.__coeficienteC = coeficienteC
        self.__raizes = []

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
    
    @property
    def raizes(self):
        return self.__raizes
    
    def calculo(self):
        
        delta = ((self.__coeficienteB**2) - (4*(self.__coeficienteA * self.__coeficienteC)))
       
        if delta < 0:
            return "raiz negativa"
        
        else: 
            raiz_delta = math.sqrt(delta)

            x_um = (-(self.__coeficienteB) + raiz_delta)/(2*self.__coeficienteA)
            x_dois = (-(self.__coeficienteB) - raiz_delta)/(2*self.__coeficienteA)
            
            raiz_um = round(x_um, 2)
            raiz_dois = round(x_dois, 2)

            self.__raizes.extend([raiz_um, raiz_dois])
            
            print(f"O valor de X1 e :{raiz_um} e o valor de X2 e :{raiz_dois}")
        
    def raiz(self):
        for i in self.__raizes:
            j = round(i, 2)
            print(f"{j}")

    def print_equacao(self):
        print(f"{self.__coeficienteA}x² + {self.__coeficienteB}x + {self.__coeficienteC}")

    def __str__(self):
        raizes_str = ', '.join(map(str, self.__raizes)) if self.__raizes else "Nenhuma raiz calculada"
        return (f"Equação: {self.__coeficienteA}x² + {self.__coeficienteB}x + {self.__coeficienteC}\n"
                f"Raízes: {raizes_str}")