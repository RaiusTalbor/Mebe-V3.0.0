# Motorsportmeisterschaftsberechner
# Mebe V3.0.0
# erstellt nur einen Fahrer

from tkinter import *

import Erstellen
from Anzeige import prozess #das Objekt wird global importiert und für alle jederzeit zugreifbar gemacht
import Fahrzeug
import ErstelleFahrer

def speichern():
    global fahrzeug, entryName, leistung, wendigkeit

    #Informationen aus Widgets holen

    erstellen = 0 #um herauszufinden, ob erstellt oder bearbeitet wird

    if entryName.winfo_exists():
        fahrzeug.name = entryName.get()
        erstellen = 1   

    #Daten sammeln

    fahrzeug.leistung = leistung.get()
    fahrzeug.wendigkeit = wendigkeit.get()

    #Fahrer speichern

    fahrzeug.speichern()

    prozess.wiederherstellenCheckpoint() #zurück an Fahrzeugauswahl

    if erstellen == 1: #geht nicht wie oben, da Checkpoint schon wieder hergestellt wird, sonst setzt er die Radios auf den dann löschenden Frame
        #nur, wenn erstellt wird --> sonst Falle für Bearbeiten
        prozess.wiederherstellenCheckpoint() #zurück zur Fahrerbearbeitung
        ErstelleFahrer.FahrzeugAuswählen() #nochmal aufrufen Fahrzeugauswahl, damit neues Fahrzeug erscheint

def erstellen(name):
    #erstellen und bearbeiten einer Strecke
    global fahrzeug, entryName, leistung, wendigkeit

    #Fenster initialisieren
    prozess.speicherCheckpoint()

    prozess.zurückButton() #TODO nochmal überlegen
    prozess.hinzufügenButton("Speichern", speichern)
    
    #Auswahl, ob bearbeiten oder nicht
    if name == "":
        fahrzeug = Fahrzeug.Fahrzeug()

        prozess.hinzufügenLabel("Name des Fahrzeugs:")

        entryName = Entry(master = prozess.aktuelleAnzeige)
        entryName.pack()
    else:
        fahrzeug = Fahrzeug.Fahrzeug()
        fahrzeug.ladenName(name)

    #Parameter GUI
    prozess.hinzufügenLabel("Wie viel Leistung hat das Fahrzeug im Vergleich zu den anderen in der Meisterschaft?")

    leistung = StringVar()
    wenig = Radiobutton(master = prozess.aktuelleAnzeige, text = "Wenig", value = 1, variable = leistung)
    mittel = Radiobutton(master = prozess.aktuelleAnzeige, text = "Ausgeglichen", value = 2, variable = leistung)
    viel = Radiobutton(master = prozess.aktuelleAnzeige, text = "Viel", value = 3, variable = leistung)
    wenig.pack()
    mittel.pack()
    viel.pack()
    wenig.select()

    prozess.hinzufügenLabel("Wie wendig ist das Fahrzeug im Vergleich zu den anderen der Meisterschaft?")

    wendigkeit = StringVar()
    schnell = Radiobutton(master = prozess.aktuelleAnzeige, text = "Schnell", value = 1, variable = wendigkeit)
    ausgeglichen = Radiobutton(master = prozess.aktuelleAnzeige, text = "Ausgeglichen", value = 2, variable = wendigkeit)
    wendig = Radiobutton(master = prozess.aktuelleAnzeige, text = "Wendig", value = 3, variable = wendigkeit)
    schnell.pack()
    ausgeglichen.pack()
    wendig.pack()
    schnell.select()