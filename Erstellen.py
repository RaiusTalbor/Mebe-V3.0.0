# Motorsportmeisterschaftsberechner
# Mebe V3.0.0
# kümmert sich darum, dass die richtigen Seiten zum Erstellen einer Meisterschaft geöffnet werden --> händelt es quasi

from tkinter import *

from Anzeige import prozess #das Objekt wird global importiert und für alle jederzeit zugreifbar gemacht

global varweiter

def erstellen():
    global varweiter

    varweiter=0

    weiter() #damit es nicht hier mit drin steht

def weiter():
    #übernimmt die Daten und gibt das nächste Fenster durch

    global varweiter

    sammeln() #speichert die Informationen zwischen --> aber wie??

    #immer Fenster neu initialisieren --> die Unterdinger müssen sich nicht darum kümmern
    prozess.löscheframeInhalt()
    prozess.löscheButtons()
    prozess.zurückButton()

    prozess.setTitelFrame("Erstellen einer Meisterschaft")

    prozess.hinzufügenButton("Weiter", weiter)

    
    if varweiter == 0: #Meisterschaft
        meisterschaftdefinieren()
    elif varweiter == 1: #Strecken hinzufügen
        rennkalendereinfügen()
    elif varweiter == 2: #Fahrer hinzufügen
        fahrereinfügen()
    elif varweiter == 3: #Speichern und erstellen beenden
        pass

    varweiter += 1

#einem speziellen Erstellen-Code wird immer ein Wert übergeben: ein entsprechender Pfad oder "leer". Bei leer wird etwas neues erstellt, mit Pfad wird dieser geladen und die Werte von dem Ding gespeichert

def meisterschaftdefinieren():
    prozess.hinzufügenLabel("Name der Meisterschaft:")

    entryNameMeisterschaft = Entry(master = prozess.frameAnzeige)
    entryNameMeisterschaft.pack()

    prozess.hinzufügenLabel("Jahr der Meisterschaft:")

    entryJahrMeisterschaft = Entry(master = prozess.frameAnzeige)
    entryJahrMeisterschaft = Entry(master = prozess.frameAnzeige)
    entryNameMeisterschaft.pack()

def rennkalendereinfügen():
    pass

def fahrereinfügen():
    pass