# Motorsportmeisterschaftsberechner
# Mebe V3.0.0

import Daten

class Fahrzeug:
    #stellt ein Fahrzeug dar - zur einfacheren und zentraleren Verwaltung der Fahrzeugen besonders beim erstellen und speichern

    #Initialisieren mit Standardwerten
    def __init__(self):
        self.pfad = ''
        self.name= ''
        self.leistung = 0
        self.wendigkeit = 0

    #wenn Name geg., Objekt kann eindeutig und vollständig richtig aus Datei geladen werden (mit richtigen Attributen für Objekt)
    def ladenName(self, name):
        self.name = name
        self.pfad = 'Datenbank/Fahrzeuge/' + name + '.dat'
        self.laden()

    #wenn Pfad geg., Objekt kann eindeutig und vollständig richtig aus Datei geladen werden (mit richtigen Attributen für Objekt)
    def ladenPfad(self, pfadübergabe):
        self.pfad = pfadübergabe
        pfadübergabe = pfadübergabe.replace('Datenbank/Fahrzeuge/', '')
        pfadübergabe = pfadübergabe.replace('.dat', '')
        self.name = pfadübergabe
        self.laden()

    #wenn Parameter übergeben werden, kann neues Fahrzeug erstellt werden --> es existiert aber nur lokal
    def erstellen(self, name, leistung, wendigkeit):
        self.name = name
        self.pfad = 'Datenbank/Fahrzeuge/' + name + '.dat'
        self.leistung = leistung
        self.wendigkeit = wendigkeit
    
    #getter

    #setter
    def setpfad(self, name):
        self.pfad = 'Datenbank/Fahrzeuge/' + name + '.dat'

    #speichern
    def speichern(self):
        Daten.schreiben(self.pfad, [self.leistung, self.wendigkeit])

    #laden aus Datei
    def laden(self):
        attributliste = Daten.lesen(self.pfad)
        self.leistung = attributliste[0]
        self.wendigkeit = attributliste[1]
