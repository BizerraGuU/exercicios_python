class Computador:
    def __init__(self, frequencia_clock=0, tamanho_hd=0, nome_processador=''):
        self.__frequencia_clock = frequencia_clock
        self.__tamanho_hd = tamanho_hd
        self.__nome_processador = nome_processador

    @property
    def frequencia_clock(self):
        return self.__frequencia_clock
    
    @frequencia_clock.setter
    def frequencia_clock(self, frequencia_clock):
        self.__frequencia_clock = frequencia_clock
    
    @property
    def tamanho_hd(self):
        return self.__tamanho_hd

    @frequencia_clock.setter
    def tamanho_hd(self, tamanho_hd):
        self.__tamanho_hd = tamanho_hd
    
    @property
    def nome_processador(self):
        return self.__nome_processador
    
    @nome_processador.setter
    def nome_processador(self, nome_processador):
        self.__nome_processador = nome_processador
    

    def print_dados(self):
        pass

    def compara_igualdade(self, computador:Computador):
        pass

    def compara_hd_ou_clock(self, computador:Computador, comparacao:char):
        pass

    

