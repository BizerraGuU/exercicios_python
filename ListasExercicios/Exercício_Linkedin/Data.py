from datetime import date

class Data:
    def __init__(self, data_inicial, data_final):
        self.__data_inicial = data_inicial
        self.__data_final = data_final
    
    @property
    def data_inicial(self):
        return self.__data_inicial

    @data_inicial.setter
    def data_inicial(self, data_inicial):
        self.__data_inicial = data_inicial
    
    @property
    def data_final(self):
        return self.__data_final
    
    @data_final.setter
    def data_final(self, data_final):
        self.__data_final = data_final
    
    def verifica(self):
        self.datal_inicial = date(input('Digite a data inicial: '))
       
        if not self.datal_inicial:
            print('Você prosseguirá sem data definida')
        else:
            self.data_final = date(input('Digite a data final: '))
        
        self.data_final = date(input('Digite a data final: '))

        if not self.data_final:
            print('você processeguirá sem data definida')
        else:
            self.inicial = date(input('Digite a data final: '))
        
        