# Motorsportmeisterschaftsberechner
# Mebe V3.0.0

import Daten

class Fahrer:
    
    #Variablen
    pfad = ""
    name= ""
    gebjahr = 1970
    erstesrennen = 1988
    aggressivität = 0
    geschicklichkeit = 0
    grundkönnen = 0
    vorliebe = 0
    durchschnittlicheplatzierung = 20
    fahrzeug = ""
    fahrzeugpfad = ""
    seitWannFahrzeug = 1988

    def __init__(self):
        self.pfad = ""
        self.name= ""
        self.gebjahr = 1970
        self.erstesrennen = 1988
        self.aggressivität = 0
        self.geschicklichkeit = 0
        self.grundkönnen = 0
        self.vorliebe = 0
        self.durchschnittlicheplatzierung = 20
        self.fahrzeug = ""
        self.fahrzeugpfad = ""
        self.seitWannFahrzeug = 1988

    def __init__(self, name):
        self.name= name
        self.pfad = "Datenbank/Fahrer/" + name + ".dat"
        self.gebjahr = 1970
        self.erstesrennen = 1988
        self.aggressivität = 0
        self.geschicklichkeit = 0
        self.grundkönnen = 0
        self.vorliebe = 0
        self.durchschnittlicheplatzierung = 20
        self.fahrzeug = ""
        self.fahrzeugpfad = ""
        self.seitWannFahrzeug = 1988

    def __init__(self, name, gebjahr, erstesrennen, aggressivität, geschicklichkeit, grundkönnen, vorliebe, durchschnittlicheplatzierung, fahrzeug, seitWannFahrzeug):
        self.name= name
        self.pfad = "Datenbank/Fahrer/" + name + ".dat"
        self.gebjahr = gebjahr
        self.erstesrennen = erstesrennen
        self.aggressivität = aggressivität
        self.geschicklichkeit = geschicklichkeit
        self.grundkönnen = grundkönnen
        self.vorliebe = vorliebe
        self.durchschnittlicheplatzierung = durchschnittlicheplatzierung
        self.fahrzeug = fahrzeug
        self.fahrzeugpfad = "Datenbank/Fahrzeuge/" + fahrzeug + ".dat"
        self.seitWannFahrzeug = seitWannFahrzeug

    #getter
    #setter
    def setpfad(self, name):
        self.pfad = "Datenbank/Fahrzeuge/" + name + ".dat"

    def setpfadFahrzeug(self, übergabe):
        self.fahrzeugpfadpfad = "Datenbank/Fahrzeuge/" + übergabe + ".dat"

    #speichern
    def speichern(self):
        Daten.schreiben(self.pfad, [self.gebjahr, self.erstesrennen, self.aggressivität, self.geschicklichkeit, self.grundkönnen, self.vorliebe, self.durchschnittlicheplatzierung, self.fahrzeug, self.seitWannFahrzeug])

    #laden
    def laden(self):
        attributliste = Daten.lesen(self.pfad)
        self.gebjahr = attributliste[0]
        self.erstesrennen = attributliste[1]
        self.aggressivität = attributliste[2]
        self.geschicklichkeit = attributliste[3]
        self.grundkönnen = attributliste[4]
        self.vorliebe = attributliste[5]
        self.durchschnittlicheplatzierung = attributliste[5]
        self.fahrzeug = attributliste[6]
        self.fahrzeugpfad = "Datenbank/Fahrzeuge/" + self.fahrzeug + ".dat"
        self.seitWannFahrzeug = attributliste[7]