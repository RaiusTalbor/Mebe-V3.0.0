# Motorsportmeisterschaftsberechner
# Mebe V3.0.0

import Daten

class Strecke:
    
    #Variablen
    pfad = ""
    name= ""
    rekordhalter = ""
    pfadrekordhalter = ""
    streckentyp = 0
    schwierigkeit = 0

    def __init__(self):
        self.pfad = ""
        self.name= ""
        self.rekordhalter = ""
        self.pfadrekordhalter = ""
        self.streckentyp = 0
        self.schwierigkeit = 0

    def __init__(self, name):
        self.name= name
        self.pfad = "Datenbank/Strecken/" + name + ".dat"
        self.laden()

    def __init__(self, pfadübergabe):
        self.pfad = pfadübergabe
        pfadübergabe = pfadübergabe.replace("Datenbank/Strecken/", "")
        pfadübergabe = pfadübergabe.replace(".dat", "")
        self.name = pfadübergabe
        self.laden()

    def __init__(self, name, rekordhalter, streckentyp, schwierigkeit):
        self.name= name
        self.pfad = "Datenbank/Strecken/" + name + ".dat"
        self.rekordhalter = rekordhalter
        self.pfadrekordhalter = "Datenbank/Fahrer/" + rekordhalter + ".dat"
        self.streckentyp = streckentyp
        self.schwierigkeit = schwierigkeit

    #getter

    #setter
    def setpfad(self, name):
        self.pfad = "Datenbank/Strecken/" + name + ".dat"

    def setrekordhalter(self, übergabe):
        self.rekordhalter = übergabe
        self.pfadrekordhalter = "Datenbank/Fahrer/" + übergabe + ".dat"

    #speichern
    def speichern(self):
        Daten.schreiben(self.pfad, [self.rekordhalter, self.streckentyp, self.schwierigkeit])
        #PRÜFEN, OB REKORDHALTER ALS NAME ODER ALS PFAD

    #laden
    def laden(self):
        attributliste = Daten.lesen(self.pfad)
        self.rekordhalter = attributliste[0]
        self.pfadrekordhalter = "Datenbank/Fahrer/" + self.rekordhalter + ".dat"
        self.streckentyp = attributliste[1]
        self.schwierigkeit = attributliste[2]