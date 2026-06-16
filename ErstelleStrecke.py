# Motorsportmeisterschaftsberechner
# Mebe V3.0.0
# erstellt nur eine Strecke

from tkinter import *

import Erstellen
from Anzeige import prozess #das Objekt wird global importiert und für alle jederzeit zugreifbar gemacht
import Strecke
import Daten

from Aussehen import *

def speichern():
    global strecke, entryName, entryRekordhalterAuswählen, streckentyp, scaleSchwierigkeit

    #Informationen aus Widgets holen

    erstellen = 0 #um herauszufinden, ob erstellt oder bearbeitet wird

    if entryName != None:
        strecke.name = entryName.get()
        erstellen = 1   

    strecke.rekordhalter = entryRekordhalterAuswählen.get()

    strecke.streckentyp = int(streckentyp.get())

    strecke.schwierigkeit = scaleSchwierigkeit.get()

    strecke.speichern()

    prozess.wiederherstellenCheckpoint() #zurück an Hauptprozess

    if erstellen == 1: #geht nicht wie oben, da Checkpoint schon wieder hergestellt wird, sonst setzt er die Radios auf den dann löschenden Frame
        Erstellen.aktualisiereFenster() #nur, wenn erstellt wird --> sonst Falle für Bearbeiten

def erstellen(name):
    #erstellen und bearbeiten einer Strecke
    global strecke, entryName, entryRekordhalterAuswählen, streckentyp, scaleSchwierigkeit

    #Radios
    global kurvig
    global ausgeglichen
    global schnell

    #Fenster initialisieren
    prozess.speicherCheckpoint()

    prozess.hinzufügenButton("Abbrechen", prozess.wiederherstellenCheckpoint)
    prozess.hinzufügenButton("Speichern", speichern)
    
    #Auswahl, ob bearbeiten oder nicht
    if name == "":
        strecke = Strecke.Strecke()

        prozess.hinzufügenLabel("Name der Strecke:")

        entryName = Entry(**aussehenEntry, master = prozess.aktuelleAnzeige)
        entryName.pack()
    else:
        strecke = Strecke.Strecke()
        strecke.ladenName(name)

        entryName = None #für Überprüfung, onb Bearbeitet wurde oder nicht

    #Parameter GUI
    prozess.hinzufügenLabel("Wer ist der Rekordhalter?")

    entryRekordhalterAuswählen = Entry(**aussehenEntry, master = prozess.aktuelleAnzeige)
    entryRekordhalterAuswählen.pack()

    entryRekordhalterAuswählen.delete(0, END)
    entryRekordhalterAuswählen.insert(0, strecke.rekordhalter)
    entryRekordhalterAuswählen.update_idletasks()

    prozess.hinzufügenLabel("") #Platzhalter, damit der Button Abstand hält
    
    buttonAuswählen = Button(**aussehenButton, master = prozess.aktuelleAnzeige, text = "Fahrer aus Datenbank auswählen...", command = FahrerAuswählen)
    buttonAuswählen.pack()

    prozess.hinzufügenLabel("") #Platzhalter, damit der Button Abstand hält

    prozess.hinzufügenLabel("Auswahl des Streckentps:")

    streckentyp = StringVar()
    kurvig = Radiobutton(**aussehenRadio, master = prozess.aktuelleAnzeige, text = "Kurvige Strecke", value = 1, variable = streckentyp)
    ausgeglichen = Radiobutton(**aussehenRadio, master = prozess.aktuelleAnzeige, text = "Ausgeglichene Strecke", value = 2, variable = streckentyp)
    schnell = Radiobutton(**aussehenRadio, master = prozess.aktuelleAnzeige, text = "Schnelle Strecke", value = 3, variable = streckentyp)
    kurvig.pack()
    ausgeglichen.pack()
    schnell.pack()

    if strecke.streckentyp == 1:
        kurvig.select()
    elif strecke.streckentyp == 2:
        ausgeglichen.select()
    else:
        schnell.select()

    prozess.hinzufügenLabel("Auswahl der Schwierigkeit:")

    scaleSchwierigkeit = Scale(**aussehenScale, master = prozess.aktuelleAnzeige, from_= 1, to = 10, orient=HORIZONTAL)
    scaleSchwierigkeit.pack()

    scaleSchwierigkeit.set(strecke.schwierigkeit)

# fügt Fahrer in Entry aus fahrerAuswahl ein --> Name ist definitiv richtig; gibt checkpoint wieder zurück
def fügeFahrerein():
    global Fahrer, strecke,entryRekordhalterAuswählen

    #vielleicht vorher leeren
    entryRekordhalterAuswählen.insert(0, Fahrer.get())
    strecke.setrekordhalter = Fahrer.get()

    prozess.wiederherstellenCheckpoint()

# alle Fahrer angezeigen. Mit Radiobuttons Auswahl des Fahrers aus Datenbank möglich
def FahrerAuswählen():
    global Fahrer, strecke

    prozess.speicherCheckpoint()

    listeFahrer = Daten.listeNamen("Fahrer")

    prozess.hinzufügenButton("Fahrer auswählen", fügeFahrerein)

    Fahrer = StringVar()
    #für jedes Element der Liste (also alle Fahrer) wird ein Radiobutton erzeugt
    for i in range(0, len(listeFahrer)):
        radioFahrer = Radiobutton(**aussehenRadio, master = prozess.aktuelleAnzeige, text = listeFahrer[i], value = str(listeFahrer[i]), variable = Fahrer)
        radioFahrer.pack()

    Fahrer.set(strecke.rekordhalter)