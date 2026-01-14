# Motorsportmeisterschaftsberechner
# Mebe V3.0.0

import Daten

class Meisterschaft:
    #stellt eine Meisterschaft dar - zur einfacheren und zentraleren Verwaltung der Meisterschaften

    #Initialisieren mit Standardwerten
    def __init__(self):
        self.name = ''
        self.pfad = 'Datenbank/' + '' + '.dat'
        self.pfadRennkalender = 'Datenbank/' + '' + 'Strecken.dat'
        self.pfadFahrer = 'Datenbank/' + '' + 'Fahrer.dat'
        self.rennkalender = []
        self.fahrerliste = []
    
    #wenn Name geg., Objekt kann eindeutig und vollständig richtig aus Datei geladen werden (mit richtigen Attributen für Objekt)
    def ladenName(self, name):
        self.name= name
        self.pfad = 'Datenbank/' + name + '.dat'
        self.laden()

    #wenn Pfad geg., Objekt kann eindeutig und vollständig richtig aus Datei geladen werden (mit richtigen Attributen für Objekt)
    def ladenPfad(self, pfadübergabe):
        #kann auch die zugeordneten Pfade verarbeiten
        if (pfadübergabe.endswith('Fahrer.dat')):
             pfadübergabe = pfadübergabe.replace('Fahrer.dat', '')  
        if (pfadübergabe.endswith('Strecken.dat')):
             pfadübergabe = pfadübergabe.replace('Strecken.dat', '') 

        self.pfad = pfadübergabe
        pfadübergabe = pfadübergabe.replace('Datenbank/', '')
        pfadübergabe = pfadübergabe.replace('.dat', '')
        self.name = pfadübergabe
        self.laden()

    #wenn Parameter übergeben werden, kann neue Meisterschaft erstellt werden --> es existiert aber nur lokal
    def erstellen(self, name, rennkalender, fahrerliste):
        #Variablen
        self.name = name
        self.pfad = 'Datenbank/' + name + '.dat'
        self.pfadRennkalender = 'Datenbank/' + name + 'Strecken.dat'
        self.pfadFahrer = 'Datenbank/' + name + 'Fahrer.dat'
        self.rennkalender = rennkalender
        self.fahrerliste = fahrerliste

    #getter
    def getname(self):
        return self.name

    def getpfad(self):
        return self.pfad

    def getpfadRennkalender(self):
        return self.pfadRennkalender

    def getpfadFahrer(self):
        return self.pfadFahrer

    def getrennkalender(self):
        return self.rennkalender

    def getfahrerliste(self):
        return self.fahrerliste

    #setter
    def setname(self, übergabe):
        self.name = übergabe

    def setpfad(self, übergabe):
        self.pfad = 'Datenbank/' + übergabe + '.dat'

    def setpfadRennkalender(self, übergabe):
        self.pfadRennkalender = 'Datenbank/' + übergabe + 'Strecken.dat'

    def setpfadFahrer(self, übergabe):
        self.pfadFahrer = 'Datenbank/' + übergabe + 'Fahrer.dat'

    #wenn Liste mit Namen übergeben wird, wird ins richtige Speicherformat (in Pfade überführt) gebracht
    def setrennkalenderName(self, übergabe):
        for i in range(0, len(übergabe)):
            übergabe[i] = 'Datenbank/Strecke/' + übergabe[i] + '.dat'

        self.rennkalender = übergabe      

    #setzt Rennkalender aus Pfadliste
    def setrennkalenderPfad(self, übergabe):
        self.rennkalender = übergabe     

    #wenn Liste mit Namen übergeben wird, wird ins richtige Speicherformat (in Pfade überführt) gebracht
    def setfahrerlisteName(self, übergabe):
        for i in range(0, len(übergabe)):
            übergabe[i] = 'Datenbank/Fahrer/' + übergabe[i] + '.dat'
        
        self.fahrerliste = übergabe

    #setzt Fahrerliste aus Pfadliste
    def setfahrerlistePfad(self, übergabe):
        self.fahrerliste = übergabe

    def setPfade(self):
        #setzt alle nötigen Pfade selbst über seinen Namen
        self.setpfad(self.name)
        self.setpfadFahrer(self.name)
        self.setpfadRennkalender(self.name)

    #speichern
    def speichern(self):
        Daten.schreiben(self.pfadFahrer, self.fahrerliste)
        Daten.schreiben(self.pfadRennkalender, self.rennkalender)
        Daten.schreiben(self.pfad, [self.pfadRennkalender, self.pfadFahrer])

    #laden aus Datei
    def laden(self):
        self.setpfad(self.name)
        self.setpfadFahrer(self.name)
        self.setpfadRennkalender(self.name)

        self.rennkalender = Daten.lesen(self.pfadRennkalender)
        self.fahrerliste = Daten.lesen(self.pfadFahrer)