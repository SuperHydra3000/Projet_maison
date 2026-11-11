from machine import Pin,PWM
import time


class SERVO:
    def __init__(self, pin, freq):
        global servo
        self.pin = pin
        self.freq = freq
        servo = PWM(Pin(pin, mode=Pin.OUT))
        servo.freq(freq)
        
    def logique(self, jour, temps):
        global servo
        if jour == 1:
            if temps < 27:
                return False
                print("Fermeture fenetre")
            if temps > 27:
                return True
                print("Ouverture Fenetre")
        else:
            return False
    def ouvert(self):
        servo.duty(100)
        
    def fermer(self):
        servo.duty(15)
    
