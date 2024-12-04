import random as r
class Lua():

    def __init__(self):

        # dinheiro minimo, maximo, nivel_de_dificuldade

        stats_lua = {"Experimentation": (160, 220, 1), 
                    "Assurance": (260, 300, 1),  
                    "Vow": (240, 280, 1), 
                    "Offense": (280, 340, 2), 
                    "March": (260, 320, 2), 
                    "Adamance": (320, 360, 2), 
                    "Rend": (360, 500, 3), 
                    "Dine": (440, 500, 3), 
                    "Titan": (560, 620, 3)}
        
        self.nome_lua = "Experimentation"
        self.din_minimo, self.din_maximo, self.dificuldade = stats_lua[self.nome_lua]

    
    def get_range_scan(self):
        return (self.din_minimo, self.din_maximo)
    

    def set_lua(self, nome_lua):
        stats_lua = {"Experimentation": (160, 220, 1), 
                    "Assurance": (260, 300, 1),  
                    "Vow": (240, 280, 1), 
                    "Offense": (280, 340, 2), 
                    "March": (260, 320, 2), 
                    "Adamance": (320, 360, 2), 
                    "Rend": (360, 500, 3), 
                    "Dine": (440, 500, 3), 
                    "Titan": (560, 620, 3)}
        
        self.nome_lua = nome_lua
        self.din_minimo, self.din_maximo, self.dificuldade = stats_lua[self.nome_lua]

    
    def status_scan(self):
        match self.dificuldade:
            case 1:
                fator = 2
            case 2:
                fator = 3
            case 3:
                fator = 4
        
        return not bool(r.randint(1, 10) in range(fator))
    
    def fazer_scan(self, din_max, din_min) -> int:
        return r.randint(din_min, din_max)

    

    def __str__(self):
        return f"Lua: {self.nome_lua}, dificuldade: {self.dificuldade}, dinheiro: {self.din_minimo} -- {self.din_maximo}"

