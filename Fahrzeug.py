# Motorsportmeisterschaftsberechner
# Mebe V3.0.0

import Daten

class Fahrzeug:
    
    #Variablen
    pfad = ""
    name= ""
    leistung = 0
    wendigkeit = 0

    def __init__(self):
        self.pfad = ""
        self.name= ""
        self.leistung = 0
        self.wendigkeit = 0

    def __init__(self, name):
        self.name = name
        self.pfad = "Datenbank/Fahrzeuge/" + name + ".dat"
        self.leistung = 0
        self.wendigkeit = 0

    def __init__(self, name, leistung, wendigkeit):
        self.name = name
        self.pfad = "Datenbank/Fahrzeuge/" + name + ".dat"
        self.leistung = leistung
        self.wendigkeit = wendigkeit

    #getter
    #setter
    def setpfad(self, name):
        self.pfad = "Datenbank/Fahrzeuge/" + name + ".dat"

    #speichern
    def speichern(self):
        Daten.schreiben(self.pfad, [self.leistung, self.wendigkeit])

    #laden
    def laden(self):
        attributliste = Daten.lesen(self.pfad)
        self.leistung = attributliste[0]
        self.wendigkeit = attributliste[1]
