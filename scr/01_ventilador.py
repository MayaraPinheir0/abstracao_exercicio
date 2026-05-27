
# algoritimo da modelagem do ventilador

class Ventilador:
    def __init__(self, estado=False, velocidade=0, consumo_kw=0.0, potencia=0.0):
        self.estado = estado
        self.velocidade = velocidade
        self.consumo_kw = consumo_kw
        self.potencia = potencia
        
    def ligar(self):
        self.estado = True
        self.velocidade = 1
        print("Ventilador ligado.")
    
    def desligar(self):
        self.estado = False
        self.velocidade = 0
        print("Ventilador desligado.")
    

    def velocidade_baixa(self):
        self.velocidade = 1
        print("Velocidade baixa selecionada.")


    def velocidade_media(self):
        self.velocidade = 2
        print("Velocidade média selecionada.")
    
    def velocidade_alta(self):
        self.velocidade = 3
        print("Velocidade alta selecionada.")
    
    def calcular_consumo(self):
        if self.velocidade == 1:
            self.consumo_kw = self.potencia * 0.5
            
        elif self.velocidade == 2:
            self.consumo_kw = self.potencia * 0.75
            
        elif self.velocidade == 3:
            self.consumo_kw = self.potencia
            
        else:
            self.consumo_kw = 0.0
            
        print(f"Consumo de energia: {self.consumo_kw} kW.")
    

# Exemplo de uso
ventilador = Ventilador(estado=False, velocidade=0, consumo_kw=0.0, potencia=100.0) # Criando um ventilador com potência de 100 kW
ventilador.ligar() # Ligando o ventilador
ventilador.velocidade_media() # Selecionando velocidade média
ventilador.calcular_consumo() # Calculando o consumo de energia
ventilador.velocidade_alta() # Selecionando velocidade alta
ventilador.calcular_consumo() # Calculando o consumo de energia
ventilador.desligar() # Desligando o ventilador