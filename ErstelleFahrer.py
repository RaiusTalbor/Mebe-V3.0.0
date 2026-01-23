# Motorsportmeisterschaftsberechner
# Mebe V3.0.0
# erstellt nur einen Fahrer

from tkinter import *

import Erstellen
from Anzeige import prozess #das Objekt wird global importiert und für alle jederzeit zugreifbar gemacht
import Fahrer
import ErstelleFahrzeug
import Daten

def speichern():
    global fahrer, entryName, entryGebJahr, entry1Rennen, scaleAggressivität, scaleGeschicklichkeit, scaleGrundkönnen, vorliebe, entryDurchschnittPlatzierung, labelFahrzeugAuswahl, entryFahrzeugwann, fahrzeugkontrolle

    #Informationen aus Widgets holen

    erstellen = 0 #um herauszufinden, ob erstellt oder bearbeitet wird

    if entryName.winfo_exists():
        fahrer.name = entryName.get()
        erstellen = 1   

    if fahrzeugkontrolle == 0 and fahrer.fahrzeug == '': #wenn kein Fahrzeug ausgewählt wurde und keiner im Objekt hinterlegt wurde
        prozess.setInfo("Kein Fahrzeug ausgewählt! Wähle ein Fahrzeug zum Fortfahren aus.")
        return

    #Daten sammeln

    fahrer.gebjahr = entryGebJahr.get()
    fahrer.erstesrennen = entry1Rennen.get()
    fahrer.aggressivität = scaleAggressivität.get()
    fahrer.geschicklichkeit = scaleGeschicklichkeit.get()
    fahrer.grundkönnen = scaleGrundkönnen.get()
    fahrer.vorliebe = vorliebe.get()
    fahrer.durchschnittlicheplatzierung = entryDurchschnittPlatzierung.get()
    fahrer.seitWannFahrzeug = entryFahrzeugwann.get()

    if labelFahrzeugAuswahl.cget("text") == "[Kein Fahrzeug ausgewählt]":
        fahrer.fahrzeug = ''
    else:
        fahrer.fahrzeug = labelFahrzeugAuswahl.cget("text") #Achtung!! Leerer Wert wird schlecht abgefangen

    #Fahrer speichern

    fahrer.speichern()

    prozess.wiederherstellenCheckpoint() #zurück an Hauptprozess

    if erstellen == 1: #geht nicht wie oben, da Checkpoint schon wieder hergestellt wird, sonst setzt er die Radios auf den dann löschenden Frame
        Erstellen.aktualisiereFenster() #nur, wenn erstellt wird --> sonst Falle für Bearbeiten

def erstellen(name):
    #erstellen und bearbeiten einer Strecke
    global fahrer, entryName, entryGebJahr, entry1Rennen, scaleAggressivität, scaleGeschicklichkeit, scaleGrundkönnen, vorliebe, entryDurchschnittPlatzierung, labelFahrzeugAuswahl, entryFahrzeugwann, fahrzeugkontrolle

    fahrzeugkontrolle = 0 #dazu da, dass man nur mit gesetzten Fahrzeug weiter kann --> sonst Probleme

    #Fenster initialisieren
    prozess.speicherCheckpoint()

    prozess.zurückButton() #TODO nochmal überlegen
    prozess.hinzufügenButton("Speichern", speichern)
    
    #Auswahl, ob bearbeiten oder nicht
    if name == "":
        fahrer = Fahrer.Fahrer()

        prozess.hinzufügenLabel("Name des Fahrers:")

        entryName = Entry(master = prozess.aktuelleAnzeige)
        entryName.pack()
    else:
        fahrer = Fahrer.Fahrer()
        fahrer.ladenName(name)

    #Parameter GUI
    prozess.hinzufügenLabel("Geburtsjahr des Fahrers:")
    entryGebJahr = Entry(master = prozess.aktuelleAnzeige)
    entryGebJahr.pack()

    prozess.hinzufügenLabel("Wann fuhr der Fahrer/die Fahrerin sein/ihr erstes Rennen?")
    entry1Rennen = Entry(master = prozess.aktuelleAnzeige)
    entry1Rennen.pack()

    prozess.hinzufügenLabel("Wie aggressiv fährt der Fahrer?")
    scaleAggressivität = Scale(master = prozess.aktuelleAnzeige, from_= 1, to = 10, orient=HORIZONTAL)
    scaleAggressivität.pack()

    prozess.hinzufügenLabel("Wie geschickt fährt der Fahrer?")
    scaleGeschicklichkeit = Scale(master = prozess.aktuelleAnzeige, from_= 1, to = 10, orient=HORIZONTAL)
    scaleGeschicklichkeit.pack()

    prozess.hinzufügenLabel("Wie hoch ist sein Grundkönnen?")
    scaleGrundkönnen = Scale(master = prozess.aktuelleAnzeige, from_= 1, to = 100, orient=HORIZONTAL)
    scaleGrundkönnen.pack()

    prozess.hinzufügenLabel("Welche Strecken bevorzugt der Fahrer?")

    vorliebe = StringVar()
    kurvig = Radiobutton(master = prozess.aktuelleAnzeige, text = "Kurvige Strecke", value = 1, variable = vorliebe)
    schnell = Radiobutton(master = prozess.aktuelleAnzeige, text = "Schnelle Strecke", value = 2, variable = vorliebe)
    kurvig.pack()
    schnell.pack()
    kurvig.select()

    prozess.hinzufügenLabel("Welche durchschnittliche Platzierung?") #wird die Info überhaupt benutzt?
    entryDurchschnittPlatzierung = Entry(master = prozess.aktuelleAnzeige)
    entryDurchschnittPlatzierung.pack()

    prozess.hinzufügenLabel("Welches Fahrzeug wird gefahren?")

    labelFahrzeugAuswahl = Label(master = prozess.aktuelleAnzeige, text="[Kein Fahrzeug ausgewählt]")
    labelFahrzeugAuswahl.pack()

    buttonFahrzeugAuswählen = Button(master = prozess.aktuelleAnzeige, text = "Fahrzeug auswählen...", command = FahrzeugAuswählen)
    buttonFahrzeugAuswählen.pack()

    prozess.hinzufügenLabel("Seit wann wird das Fahrzeug gefahren?")

    entryFahrzeugwann = Entry(master = prozess.aktuelleAnzeige)
    entryFahrzeugwann.pack()

# fügt Fahrer in Entry aus fahrerAuswahl ein --> Name ist definitiv richtig; gibt checkpoint wieder zurück
def fügeFahrzeugein():
    global Fahrzeug, labelFahrzeugAuswahl

    labelFahrzeugAuswahl.config(text = Fahrzeug.get())

    prozess.wiederherstellenCheckpoint()

# alle Fahrzeuge angezeigen. Mit Radiobuttons Auswahl des Fahrzeugs aus Datenbank möglich
def FahrzeugAuswählen():
    global Fahrzeug, fahrzeugkontrolle

    prozess.speicherCheckpoint()

    listeFahrzeug = Daten.listeNamen("Fahrzeuge")

    prozess.hinzufügenButton("Fahrzeug auswählen", fügeFahrzeugein)
    prozess.hinzufügenButton("Neues Fahrzeug erstellen", neuesFahrzeug)

    fahrzeugkontrolle = 1 #ab hier kann der Fahrer gespeichert werden --> weil ab hier nur noch mit Abbruch wegkann (ich möchte globals vermeiden)

    Fahrzeug = StringVar()
    #für jedes Element der Liste (also alle Fahrzeuge) wird ein Radiobutton erzeugt
    for i in range(0, len(listeFahrzeug)):
        radioFahrzeug = Radiobutton(master = prozess.aktuelleAnzeige, text = listeFahrzeug[i], value = str(listeFahrzeug[i]), variable = Fahrzeug)
        radioFahrzeug.pack()

    Fahrzeug.set(listeFahrzeug[0])

def neuesFahrzeug(): #da sonst direkt ausgeführt, weil Parameterübergabe
    global fahrer, labelFahrzeugAuswahl

    labelFahrzeugAuswahl.config(text = ErstelleFahrzeug.erstellen("")) #nimmt den Namen entgegen und setzt ihn ins Label