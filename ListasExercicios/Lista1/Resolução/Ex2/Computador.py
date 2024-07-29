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
        print(f"dados computador: {self.__frequencia_clock}Hz, {self.__tamanho_hd}Gb, {self.__nome_processador}")

    def compara_igualdade(self, computador1:'Computador', computador2:'Computador'):
        if computador1 != computador2:
            return False
        else: 
            return True


    def compara_hd_ou_clock(self, computador1:'Computador', computador2:'Computador', comparacao:str):
        if computador1 == computador2:
            return "HD e Clock iguais"
        else: 
            if comparacao == 'HD':
                if computador1.tamanho_hd > computador2.tamanho_hd:
                    return "o hd do computador 1 é maior"
                else:
                    return "o hd do computador 2 é maior"
            
            if comparacao == 'CLOCK':
                if computador1.frequencia_clock > computador2.frequencia_clock:
                    return "o clock do computador 1 é maior"
                else:
                    return "o clock do computador 2 é maior"

    

