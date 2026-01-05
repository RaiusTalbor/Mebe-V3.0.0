# Motorsportmeisterschaftsberechner
# Mebe V3.0.0

#Variablen
global name, pfad, pfadFahrer, pfadRennkalender, rennkalender, fahrerliste
name = ""
pfad = "Datenbank/" + name + ".dat"
pfadRennkalender = "Datenbank/" + name + "Strecken.dat"
pfadFahrer = "Datenbank/" + name + "Fahrer.dat"
rennkalender = []
fahrerliste = []

#getter
def getname():
    return name

def getpfad():
    return pfad

def getpfadRennkalender():
    return pfadRennkalender

def getpfadFahrer():
    return pfadFahrer

def getrennkalender():
    return rennkalender

def getfahrerliste():
    return fahrerliste

#setter
def setname(übergabe):
    name = übergabe

def setpfad(übergabe):
    pfad = übergabe

def setpfadRennkalender(übergabe):
    pfadRennkalender = übergabe

def setpfadFahrer(übergabe):
    pfadFahrer = übergabe

def setrennkalender(übergabe):
    rennkalender = übergabe
    

def setfahrerliste(übergabe):
    fahrerliste = übergabe

#speichern

#laden - an die komischen Speicherlisten denken!