# Motorsportmeisterschaftsberechner
# Mebe V3.0.0

import Daten

class Strecke:
    #stellt eine Strecke dar - zur einfacheren und zentraleren Verwaltung der Strecken besonders beim erstellen und speichern
    
    #Attribute
    pfad = ''
    name= ''
    rekordhalter = ''
    pfadrekordhalter = ''
    streckentyp = 0
    schwierigkeit = 0

    #Initialisieren mit Standardwerten
    def __init__(self):
        self.pfad = ''
        self.name= ''
        self.rekordhalter = ''
        self.pfadrekordhalter = ''
        self.streckentyp = 0
        self.schwierigkeit = 0

    #wenn Name geg., Objekt kann eindeutig und vollständig richtig aus Datei geladen werden (mit richtigen Attributen für Objekt)
    def ladenName(self, name):
        self.name= name
        self.pfad = 'Datenbank/Strecken/' + name + '.dat'
        self.laden()

    #wenn Pfad geg., Objekt kann eindeutig und vollständig richtig aus Datei geladen werden (mit richtigen Attributen für Objekt)
    def ladenPfad(self, pfadübergabe):
        self.pfad = pfadübergabe
        pfadübergabe = pfadübergabe.replace('Datenbank/Strecken/', '')
        pfadübergabe = pfadübergabe.replace('.dat', '')
        self.name = pfadübergabe
        self.laden()

    #wenn Parameter übergeben werden, kann neue Strecke erstellt werden --> es existiert aber nur lokal
    def erstellen(self, name, rekordhalter, streckentyp, schwierigkeit):
        self.name= name
        self.pfad = 'Datenbank/Strecken/' + name + '.dat'
        self.rekordhalter = rekordhalter
        self.pfadrekordhalter = 'Datenbank/Fahrer/' + rekordhalter + '.dat'
        self.streckentyp = streckentyp
        self.schwierigkeit = schwierigkeit

    #getter

    #setter
    def setpfad(self, name):
        self.pfad = 'Datenbank/Strecken/' + name + '.dat'

    def setrekordhalter(self, übergabe):
        self.rekordhalter = übergabe
        self.pfadrekordhalter = 'Datenbank/Fahrer/' + übergabe + '.dat'

    #speichern
    def speichern(self):
        Daten.schreiben(self.pfad, [self.rekordhalter, self.streckentyp, self.schwierigkeit])

    #laden aus Datei
    def laden(self):
        attributliste = Daten.lesen(self.pfad)
        self.rekordhalter = attributliste[0]
        self.pfadrekordhalter = 'Datenbank/Fahrer/' + self.rekordhalter + '.dat'
        self.streckentyp = attributliste[1]
        self.schwierigkeit = attributliste[2]