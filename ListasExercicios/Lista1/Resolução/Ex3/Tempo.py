class Tempo:
    def __init__(self, hora=00, minuto=00, segundo=00):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo
    
    @property
    def hora(self):
        return self.__hora
    
    @hora.setter
    def hora(self, hora):
        self.__hora = hora

    @property
    def minuto(self):
        return self.__minuto
    
    @minuto.setter
    def minuto(self, minuto):
        self.__minuto = minuto

    @property
    def segundo(self):
        return self.__segundo
    
    @segundo.setter
    def segundo(self, segundo):
        self.__segundo = segundo
    
    def print_horario(self):
        print(f"{self.__hora}:{self.__minuto}:{self.__segundo}")
    
    def segundos_total(self):

        if self.__hora < 0 or self.__minuto < 0 or self.__segundo < 0:
            return "horário inválido"
        else:
            total_segundos = (self.__hora*3600) + (self.__minuto*60) + (self.__segundo)
        
        print(f"o total do tempo em segundos é: {total_segundos}")
    
    def pega_maior_horario(self, horario1:'Tempo', horario2:'Tempo'):

        if horario1 == horario2:
            return "os horarios são iguais"

        elif (horario1.__hora > horario2.__hora 
            or horario1.__minuto > horario2.__minuto 
            or horario1.__segundo > horario2.__segundo):
            return "o horario 1 é maior"
        else:
            return "o horario 2 é maior"
        
    def segundos_comparacao(self, horario1:'Tempo', horario2:'Tempo'):


        if horario1.__hora < 0 or horario1.__minuto < 0 or horario1.__segundo < 0:
            return "horário inválido"
        else:
            total_segundos1 = (horario1.__hora*3600) + (horario1.__minuto*60) + (horario1.__segundo)
        
        if horario2.__hora < 0 or horario2.__minuto < 0 or horario2.__segundo < 0:
            return "horário inválido"
        else:
            total_segundos2 = (horario2.__hora*3600) + (horario2.__minuto*60) + (horario2.__segundo)

        if total_segundos1 == total_segundos2:
            return "os dois são iguais"
        
        elif total_segundos1 > total_segundos2:
            return "o primeiro horário é maior"
        
        else: 
            return "o segundo horário é maior"
