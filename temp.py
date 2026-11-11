import time
from machine import I2C, Pin, PWM, RTC
import ahtx0, mois
from servo import SERVO
from ldr import LDR



## Configuré les delai de mesure ( minute * convertion )
INTERNAL_RUN = 0.5 * 60000
INTERNAL_STOP = 0.5 * 60000

## Initialiser l'horloge a temps reel de l'esp
rtc = RTC()

## Config des états
start_time = time.ticks_ms()
est_mesuré = True

## créer object servomoteur
sMoteur = SERVO(3, 50)

## Broche du relai
relay = Pin(20, Pin.OUT)


## Créer tableau pour faire une moyen des mesures
donnee = []

## Nombre de donnée
NB_DONNEE = 10


def RTCtemps():
    global rtc, tempdelajourné, Journé
    ## Recevoir le temps
    rtc.datetime()
     
    ## Mettre des variables pour les données de temps reçus
    Tempsreel = rtc.datetime()
    moiss = Tempsreel[1]
    jours = Tempsreel[2]
    heure = Tempsreel[4]
    minute = Tempsreel[5]
    seconde = Tempsreel[6]
    
    ## Convertion pour affiché les mois avec des noms
    vmois = mois.convertMois(moiss)
    
    ## Etat du jour
    if 18 < heure or heure < 6:
        Journé = 0
    if 6 < heure or heure < 18:
        Journé = 1
    #print(Journé)
    
    
    ## affiché temps dans la console
    print(f"{jours} {vmois}, {heure}:{minute}:{seconde}\n")

def Ampoule(lumiere):
    global Journé
    if Journé == 1:
        relay.value(1)
        print(lumiere)
        print("Ampoule Alumé")
        if lumiere < 25000:
            relay.value(0)
            print("Ampoule Éteinte")
    else:
        relay.value(0)
        print("Fermer")
            
def Moyen_Donnee():
    global donnee, NB_DONNEE
    ## donnée valeur de la temperature
    valeur = temperature(1)
    ## ajouté temperature au tableau
    donnee.append(valeur)
    
    if len(donnee) > NB_DONNEE:
        donnee.pop(0)
        
    somme = sum(donnee)
    taille = len(donnee)
    moyenne = somme / taille
    
    return moyenne

## Configuré I2C
i2c = I2C(scl=Pin(5), sda=Pin(4))

## Initialisé le capteur aht20
aht20 = ahtx0.AHT20(i2c)

def temperature(valeur):
    global Temperature, Humidité
    Temperature = aht20.temperature
    Humidité = aht20.relative_humidity
    if valeur == 1:
        return Temperature
    elif valeur == 2:
        return Humidité
    elif valeur == 3:
        return Temperature, Humidité
    
def tempaffichee():
    global Humidité
    print("Humidité: %0.2f %%" % Humidité)
    

def mesure():
    global est_mesuré, start_time, last_sample, tempdelajourné, Journé
    temps_mtn = time.ticks_ms()
    if est_mesuré:
        if time.ticks_diff(temps_mtn, start_time) >= INTERNAL_RUN:
            est_mesuré = False
            start_time = temps_mtn
            print("Fin de lecture de température")
    else:
        
        if time.ticks_diff(temps_mtn, start_time) >= INTERNAL_STOP:
            est_mesuré = True
            start_time = temps_mtn
            print("Lecture de la température")
    if est_mesuré:
        #temperature()
        if not 'last_sample' in locals() or time.ticks_diff(temps_mtn, last_simple) >= 500:
            last_sample = temps_mtn
            print("Humidité: %0.2f %%" % temperature(2))
            print("Moyenne : {:.2f}".format(Moyen_Donnee()))
            if sMoteur.logique(Journé, Moyen_Donnee()):
                sMoteur.ouvert()
            else:
                sMoteur.fermer()
            
