from machine import RTC

def convertMois(mois):
    if mois == 1:
        mois = "jan"
    if mois == 2:
        mois = "fev"
    if mois == 3:
        mois = "mar"
    if mois == 4:
        mois = "avr"
    if mois == 5:
        mois = "mai"
    if mois == 6:
        mois = "juin"
    if mois == 7:
        mois = "juil"
    if mois == 8:
        mois = "aout"
    if mois == 9:
        mois = "sep"
    if mois == 10:
        mois = "oct"
    if mois == 11:
        mois = "nov"
    if mois == 12:
        mois = "dec"
    return mois


