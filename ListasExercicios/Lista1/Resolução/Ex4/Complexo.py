class Complexo:
    def __init__(self, a=0, b=0):
        self.__a = a
        self.__b = b

    @property
    def a(self):
        return self.__a
    
    @a.setter
    def a(self, a):
        self.__a = a
    
    @property
    def b(self):
        return self.__b

    @b.setter    
    def b(self, b):
        self.__b = b
        
    def atribui_valor_a(self, valor):
        self.__a = valor
        self.__b = 0

    def imprime_equacao(self):
        print(f"{self.__a} + {self.__b}i")