# Motorsportmeisterschaftsberechner
# Mebe V3.0.0
# Untermenü bearbeiten - Meisterschaften, Strecken, Fahrer, Fahrzeuge editieren

from tkinter import *
import time

#---
import Erstellen
import ErstelleStrecke
import ErstelleFahrer
import ErstelleFahrzeug

import Daten

from Anzeige import prozess

def bearbeiten():
    prozess.löscheframeInhalt()
    prozess.löscheButtons()
    prozess.zurückButton()

    prozess.setTitelFrame("Bearbeiten von Objekten")

    prozess.hinzufügenLabel("Bearbeiten - bitte auswählen")

    prozess.hinzufügenButton("Meisterschaft bearbeiten", bearbeiteMeisterschaft)
    prozess.hinzufügenButton("Strecke bearbeiten", bearbeiteStrecke)
    prozess.hinzufügenButton("Fahrer bearbeiten", bearbeiteFahrer)
    prozess.hinzufügenButton("Fahrzeug bearbeiten", bearbeiteFahrzeug)

def auswählen():
    global radioAuswahl, ausgewählteAktion

    ausgewähltesObjekt = radioAuswahl.get()

    if ausgewählteAktion == 1: #Meisterschaft
        pass
    elif ausgewählteAktion == 2: #Strecke
        ErstelleStrecke.erstellen(str(ausgewähltesObjekt))
    elif ausgewählteAktion == 3: #Fahrer
        ErstelleFahrer.erstellen(str(ausgewähltesObjekt))
    elif ausgewählteAktion == 4: #Fahrzeug
        ErstelleFahrzeug.erstellen(str(ausgewähltesObjekt))
    else:
        prozess.setInfo("Es ist ein Fehler aufgetreten!")
        time.sleep(3)
        prozess.setInfo("")

def auswahl(objekt):
    global radioAuswahl

    prozess.setTitelFrame("")

    prozess.löscheButtons()
    prozess.zurückButton()

    prozess.hinzufügenButton("Auswählen", auswählen)

    if objekt == "Meisterschaft":
        liste = Daten.listeMeisterschaftsnamen
    else:
        liste = Daten.listeNamen(objekt)

    radioAuswahl = StringVar()
    for i in range(len(liste)):
        radio = Radiobutton(master=prozess.frameAnzeige, text=liste[i], value=liste[i], variable=radioAuswahl)
        radio.pack()
    radioAuswahl.set(liste[0])

def bearbeiteMeisterschaft():
    global ausgewählteAktion
    ausgewählteAktion = 1

    auswahl("Meisterschaft")

def bearbeiteStrecke():
    global ausgewählteAktion
    ausgewählteAktion = 2

    auswahl("Strecken")

def bearbeiteFahrer():
    global ausgewählteAktion
    ausgewählteAktion = 3

    auswahl("Fahrer")

def bearbeiteFahrzeug():
    global ausgewählteAktion
    ausgewählteAktion = 4

    auswahl("Fahrzeuge")