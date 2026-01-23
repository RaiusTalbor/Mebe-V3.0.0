# Motorsportmeisterschaftsberechner
# Mebe V3.0.0

import Daten

class Fahrer:
    #stellt einen Fahrer dar - zur einfacheren und zentraleren Verwaltung der Fahrer besonders beim erstellen und speichern

    #Initialisieren mit Standardwerten
    def __init__(self):
        self.pfad = ''
        self.name= ''
        self.gebjahr = 1970
        self.erstesrennen = 1988
        self.aggressivität = 0
        self.geschicklichkeit = 0
        self.grundkönnen = 0
        self.vorliebe = 0
        self.durchschnittlicheplatzierung = 20
        self.fahrzeug = ''
        self.fahrzeugpfad = ''
        self.seitWannFahrzeug = 1988

    #wenn Name geg., Objekt kann eindeutig und vollständig richtig aus Datei geladen werden (mit richtigen Attributen für Objekt)
    def ladenName(self, name):
        self.name= name
        self.pfad = 'Datenbank/Fahrer/' + name + '.dat'
        self.laden()

    #wenn Pfad geg., Objekt kann eindeutig und vollständig richtig aus Datei geladen werden (mit richtigen Attributen für Objekt)
    def ladenPfad(self, pfadübergabe):
        self.pfad = pfadübergabe
        pfadübergabe = pfadübergabe.replace('Datenbank/Fahrer/', '')
        pfadübergabe = pfadübergabe.replace('.dat', '')
        self.name = pfadübergabe
        self.laden()

    #wenn Parameter übergeben werden, kann neuer Fahrer erstellt werden --> es existiert aber nur lokal
    def erstellen(self, name, gebjahr, erstesrennen, aggressivität, geschicklichkeit, grundkönnen, vorliebe, durchschnittlicheplatzierung, fahrzeug, seitWannFahrzeug):
        self.name= name
        self.pfad = 'Datenbank/Fahrer/' + name + '.dat'
        self.gebjahr = gebjahr
        self.erstesrennen = erstesrennen
        self.aggressivität = aggressivität
        self.geschicklichkeit = geschicklichkeit
        self.grundkönnen = grundkönnen
        self.vorliebe = vorliebe
        self.durchschnittlicheplatzierung = durchschnittlicheplatzierung
        self.fahrzeug = fahrzeug
        self.fahrzeugpfad = 'Datenbank/Fahrzeuge/' + fahrzeug + '.dat'
        self.seitWannFahrzeug = seitWannFahrzeug

    #getter

    #setter
    def setpfad(self, name):
        self.pfad = 'Datenbank/Fahrer/' + name + '.dat'

    def setpfadFahrzeug(self, übergabe):
        self.fahrzeugpfadpfad = 'Datenbank/Fahrzeuge/' + übergabe + '.dat'

    #speichern
    def speichern(self):
        self.setpfad(self.name)
        Daten.schreiben(self.pfad, [int(self.gebjahr), int(self.erstesrennen), int(self.aggressivität), int(self.geschicklichkeit), int(self.grundkönnen), self.vorliebe, self.durchschnittlicheplatzierung, self.fahrzeug, int(self.seitWannFahrzeug), self.name])

    #laden aus Datei
    def laden(self):
        attributliste = Daten.lesen(self.pfad)
        self.gebjahr = attributliste[0]
        self.erstesrennen = attributliste[1]
        self.aggressivität = attributliste[2]
        self.geschicklichkeit = attributliste[3]
        self.grundkönnen = attributliste[4]
        self.vorliebe = attributliste[5]
        self.durchschnittlicheplatzierung = attributliste[6]
        self.fahrzeug = attributliste[7]
        self.fahrzeugpfad = 'Datenbank/Fahrzeuge/' + self.fahrzeug + '.dat'
        self.seitWannFahrzeug = attributliste[8]