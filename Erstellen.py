# Motorsportmeisterschaftsberechner
# Mebe V3.0.0
# kümmert sich darum, dass die richtigen Seiten zum Erstellen einer Meisterschaft geöffnet werden --> händelt es quasi

from tkinter import *

from Anzeige import prozess #das Objekt wird global importiert und für alle jederzeit zugreifbar 
import Daten
import Meisterschaft
import Strecke
import ErstelleStrecke
import Fahrer
import Fahrzeug #notwendig hier?

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
#Achtung: varweiter ist eins höher, weil varweiter in weiter() um 1 erhöht wird, wenn es durchläuft

def sammeln():
    #sammelt bei vaweiter die Eingaben ein und speichert die zwischen

    global entryJahrMeisterschaft, entryNameMeisterschaft, rennkalenderListe, fahrerliste

    global meisterschaft #globalen Objekte zum Speichern

    if varweiter == 1: #Meisterschaft
        meisterschaft = Meisterschaft.meisterschaft()

        name = entryNameMeisterschaft.get()
        name = name + entryJahrMeisterschaft.get()

        meisterschaft.setname(name)
        meisterschaft.setPfade()

        #Initialisieren der globalen Listen für Rennkalender und Speicherliste, weil ich sonst immer weitere globals definieren muss und davon will ich weg
        rennkalenderListe = []
        fahrerliste = []

    elif varweiter == 2: #Strecken hinzufügen
        prozess.zeige1frame() #Zwei-Fenster-Anzeige deaktiviert

        meisterschaft.setRennkalenderName(rennkalenderListe)

    elif varweiter == 3: #Fahrer hinzufügen
        prozess.zeige1frame() #Zwei-Fenster-Anzeige deaktiviert

        meisterschaft.setfahrerlisteName(fahrerliste)

    elif varweiter == 4: #Speichern und erstellen beenden
        pass
    else:
        pass


def meisterschaftdefinieren():
    global entryJahrMeisterschaft, entryNameMeisterschaft

    prozess.hinzufügenLabel("Name der Meisterschaft:")

    entryNameMeisterschaft = Entry(master = prozess.frameAnzeige)
    entryNameMeisterschaft.pack()

    prozess.hinzufügenLabel("Jahr der Meisterschaft:")

    entryJahrMeisterschaft = Entry(master = prozess.frameAnzeige)
    entryJahrMeisterschaft = Entry(master = prozess.frameAnzeige)
    entryNameMeisterschaft.pack()

def auswählen():
    #Knopf-Funktion, um aktuelle Radioauswahl der Liste hinzuzufügen
    global radioAuswahl
    global rennkalenderListe, fahrerliste

    #holt sich die Daten und speichert sie zwischen
    if varweiter == 1:
        rennkalenderListe.append(radioAuswahl.get())
    
    if varweiter == 2:
        fahrerliste.append(radioAuswahl.get())

    aktualisiereFenster() #aus Liste links weg, zu Liste rechts hin

def rennkalendereinfügen():
    #zeigt die Streckenauswahl an
    global radioAuswahl

    prozess.zeige2frames() #Zwei-Fenster-Anzeige aktiviert

    prozess.hinzufügenButton("Neue Strecke erstellen", ErstelleStrecke.erstellen)

    prozess.hinzufügenButton("Strecke auswählen", auswählen) #nimmt ausgewählte Strecke und fügt sie dem Kalender und der zweiten Anzeige hinzu

    listeStrecken = Daten.listeNamen("Strecken")

    radioAuswahl = StringVar()
    for i in range(len(listeStrecken)):
        radioStrecken = Radiobutton(master=prozess.frameAnzeige1, text=listeStrecken[i], value=listeStrecken[i], variable=radioAuswahl)
        radioStrecken.pack(anchor='w')
    radioAuswahl.set(listeStrecken[0])

def fahrereinfügen():
    #zeigt die Fahrerauswahl an
    global radioAuswahl

    prozess.zeige2frames() #Zwei-Fenster-Anzeige aktiviert

    prozess.hinzufügenButton("Neuer Fahrer erstellen", ErstelleFahrer.erstellen)

    prozess.hinzufügenButton("Fahrer auswählen", auswählen) #nimmt ausgewählten Fahrer und fügt sie der Liste und der zweiten Anzeige hinzu

    listeFahrer = Daten.listeNamen("Fahrer")

    radioAuswahl = StringVar()
    for i in range(len(listeFahrer)):
        radioStrecken = Radiobutton(master=prozess.frameAnzeige1, text=listeFahrer[i], value=listeFahrer[i], variable=radioAuswahl)
        radioStrecken.pack(anchor='w')
    radioAuswahl.set(listeFahrer[0])