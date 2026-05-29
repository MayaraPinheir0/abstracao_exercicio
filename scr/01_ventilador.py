# ventilador.py

class Ventilador:
    def __init__(self):
        self.estado = False  # Ventilador desligado por padrão
        self.velocidade = 0  # Velocidade inicial
        self.consumo_kw = 0.0  # Consumo de energia em kW
        self.potencia = 100.0  # Potência do ventilador em kW
        
    def ligar(self):
        self.estado = True
        print("Ventilador ligado.")
        
    def desligar(self):
        self.estado = False
        self.velocidade = 0
        self.consumo_kw = 0.0
        print("Ventilador desligado.")