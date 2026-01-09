# Motorsportmeisterschaftsberechner
# Mebe V3.0.0
# Lesen, Schreiben von Dateien

import pickle
import os

# Daten werden gelesen
def lesen(pfad):
    f = open(pfad, mode = 'rb')
    daten = pickle.load(f)
    f.close()
    return daten

# Daten werden geschrieben
def schreiben(pfad, daten):
    f = open(pfad, mode = 'wb')
    pickle.dump(daten, f)
    f.close()

def listeMeisterschaftspfade():
    #listet alle Pfade, die sich in "Datenbank" befinden

    VerzeichnisMeisterschaftenohnefilter = os.listdir('Datenbank')
    VerzeichnisMeisterschaftenPfade = []

    #für alle Dateien, die nicht auf 'Strecken.dat' oder 'Fahrer.dat', aber auf '.dat' enden, wird zur Liste hinzugefügt
    for i in range(0, len(VerzeichnisMeisterschaftenohnefilter)):
        if (not VerzeichnisMeisterschaftenohnefilter[i].endswith('Fahrer.dat') 
            and not VerzeichnisMeisterschaftenohnefilter[i].endswith('Strecken.dat') 
            and VerzeichnisMeisterschaftenohnefilter[i].endswith('.dat')):

            VerzeichnisMeisterschaftenPfade.append('Datenbank/' + VerzeichnisMeisterschaftenohnefilter[i])
    
    return VerzeichnisMeisterschaftenPfade

def listeMeisterschaftsnamen():
    liste = listeMeisterschaftspfade()

    for i in range(0, len(liste)):
        liste[i] = liste[i].replace('Datenbank/', '')
        liste[i] = liste[i].replace('.dat', '')
    
    return liste

def listePfade(objekt):
    #listet alle Pfade, die sich in Datenbank unter dem übergebenen Unterordner befinden befinden

    pfad = "Datenbank/" + objekt

    liste = os.listdir(pfad)

    for i in range(0, len(liste)):
        liste[i] = str(pfad + "/" + liste[i])

    return liste

def listeNamen(objekt):
    pfad = "Datenbank/" + objekt

    liste = os.listdir(pfad)

    for i in range(0, len(liste)):
        liste[i] = liste[i].replace('.dat', '')

    return liste