# Motorsportmeisterschaftsberechner
# Mebe V3.0.0
# erstellt nur einen Fahrer

from tkinter import *

import Erstellen
from Anzeige import prozess #das Objekt wird global importiert und für alle jederzeit zugreifbar gemacht
import Fahrzeug
import ErstelleFahrer
import Daten

from Aussehen import *

def speichern():
    global fahrzeug, entryName, leistung, wendigkeit, namekontrolle

    #Informationen aus Widgets holen

    erstellen = 0 #um herauszufinden, ob erstellt (0) oder bearbeitet wird (1)

    if entryName != None:
        fahrzeug.name = entryName.get()
        erstellen = 1  

    #Daten sammeln

    fahrzeug.leistung = leistung.get()
    fahrzeug.wendigkeit = wendigkeit.get()

    if fahrzeug.name == '': #wenn kein Name vergeben wurde
        prozess.setInfo("Das Fahrzeug wurde noch nicht benannt!")
        return 
    
    #prüft, ob Fahrzeug schon existiert
    liste = Daten.listeNamen("Fahrzeuge")
    if erstellen == 0 and fahrzeug.name in liste:
        prozess.setInfo("Das Fahrzeug existiert bereits. Die Werte werden beim Speichern überschrieben!")
        namekontrolle = 1 #wenn Objekt schon in Datenbank existiert, wird auf 1 gesetzt. Beim zweiten Mal speichern wird das Objekt überschrieben

    #Fahrer speichern

    fahrzeug.speichern()

    prozess.wiederherstellenCheckpoint() #zurück an Fahrzeugauswahl

    if erstellen == 1: #geht nicht wie oben, da Checkpoint schon wieder hergestellt wird, sonst setzt er die Radios auf den dann löschenden Frame
        #nur, wenn erstellt wird --> sonst Falle für Bearbeiten
        prozess.wiederherstellenCheckpoint() #zurück zur Fahrerbearbeitung
        ErstelleFahrer.FahrzeugAuswählen() #nochmal aufrufen Fahrzeugauswahl, damit neues Fahrzeug erscheint

def erstellen(name):
    #erstellen und bearbeiten einer Strecke
    global fahrzeug, entryName, leistung, wendigkeit, namekontrolle

    namekontrolle = 0 #wenn Objekt schon in Datenbank existiert, wird auf 1 gesetzt. Beim zweiten Mal speichern wird das Objekt überschrieben

    #Fenster initialisieren
    prozess.speicherCheckpoint()

    prozess.hinzufügenButton("Abbrechen", prozess.wiederherstellenCheckpoint)
    prozess.hinzufügenButton("Speichern", speichern)
    
    #Auswahl, ob bearbeiten oder nicht
    if name == "":
        fahrzeug = Fahrzeug.Fahrzeug()

        prozess.hinzufügenLabel("Name des Fahrzeugs:")

        entryName = Entry(**aussehenEntry, master = prozess.aktuelleAnzeige)
        entryName.pack()
    else:
        fahrzeug = Fahrzeug.Fahrzeug()
        fahrzeug.ladenName(name)
        entryName = None #für Überprüfung, onb Bearbeitet wurde oder nicht

    #Parameter GUI
    prozess.hinzufügenLabel("Wie viel Leistung hat das Fahrzeug im Vergleich zu den anderen in der Meisterschaft?")

    leistung = StringVar()
    wenig = Radiobutton(**aussehenRadio, master = prozess.aktuelleAnzeige, text = "Wenig", value = 1, variable = leistung)
    mittel = Radiobutton(**aussehenRadio, master = prozess.aktuelleAnzeige, text = "Ausgeglichen", value = 2, variable = leistung)
    viel = Radiobutton(**aussehenRadio, master = prozess.aktuelleAnzeige, text = "Viel", value = 3, variable = leistung)
    wenig.pack()
    mittel.pack()
    viel.pack()
    
    if fahrzeug.leistung == 1:
        wenig.select()
    elif fahrzeug.leistung == 2:
        mittel.select()
    else:
        viel.select()

    prozess.hinzufügenLabel("Wie wendig ist das Fahrzeug im Vergleich zu den anderen der Meisterschaft?")

    wendigkeit = StringVar()
    schnell = Radiobutton(**aussehenRadio, master = prozess.aktuelleAnzeige, text = "Schnell", value = 1, variable = wendigkeit)
    ausgeglichen = Radiobutton(**aussehenRadio, master = prozess.aktuelleAnzeige, text = "Ausgeglichen", value = 2, variable = wendigkeit)
    wendig = Radiobutton(**aussehenRadio, master = prozess.aktuelleAnzeige, text = "Wendig", value = 3, variable = wendigkeit)
    schnell.pack()
    ausgeglichen.pack()
    wendig.pack()
    
    if fahrzeug.wendigkeit == 1:
        schnell.select()
    elif fahrzeug.wendigkeit == 2:
        ausgeglichen.select()
    else:
        wendig.select()