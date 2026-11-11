from machine import ADC, Pin


class LDR:
    def __init__(self, pin):
        global adc
        self.pin = pin
        adc = ADC(Pin(pin))
        
    def lecture(self):
        global adc
        valeur = adc.read_u16()
        return valeur
    
    def clartee(self, lumière):
        description = ""
        ## détecté si il fait noir ou lumineux
        if lumière < 8000:
            description = "Noir"
        elif lumière < 25000:
            description = "Sombre"
        elif lumière < 55800:
            description = "Lumineux"
        else:
            description = "Soleil"
            
        return description
