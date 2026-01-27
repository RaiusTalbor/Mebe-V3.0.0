# Motorsportmeisterschaftsberechner
# Mebe V3.0.0
# Untermenü bearbeiten - Meisterschaften, Strecken, Fahrer, Fahrzeuge editieren

from tkinter import *

#---
import Erstellen
import ErstelleStrecke
import ErstelleFahrer
import ErstelleFahrzeug

from Anzeige import prozess

def bearbeiten():
    prozess.hinzufügenButton("Bearbeiten - bitte Auswählen")

    prozess.hinzufügenButton("Meisterschaft bearbeiten". Erstellen.bearbeiten)
    prozess.hinzufügenButton("Strecke bearbeiten". Erstellen.bearbeiten)
    prozess.hinzufügenButton("Fahrer bearbeiten". ErstelleFahrer.bearbeiten)
    prozess.hinzufügenButton("Fahrzeug bearbeiten". ErstelleFahrzeug.bearbeiten)