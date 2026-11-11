
import mois, network, ahtx0
from machine import RTC, I2C, Pin, Counter, ADC, PWM
from time import sleep
import temp
from ldr import LDR
import ssd1306


#import MQTTsetup
SSID = "TGE-IOT"
MDP = "iOTN3t$$"

## LDR
Ldr = LDR(1)



## Ouvrir interface WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

## Établir une connection Wifi
if not wlan.isconnected():
  print("Connecting to network...")
  wlan.connect(SSID, MDP)
  while not wlan.isconnected():
      pass
    
    
print("Connected! Network config:", wlan.ifconfig())
#initMQTT()

while True:

    temp.RTCtemps()
    
    ## Attendre 1sec pour sauvé de la memoires
    sleep(1)
    
    ## appeler la fonction mesure de la librairie "temp" pour recevoir les donner chaque 5min
    temp.mesure()
    
    ## Lire capteur LDR
    value = Ldr.lecture()
    envi = Ldr.clartee(value)
    temp.Ampoule(value)
    print(f"Lumiere : {envi}")
    
    
    
