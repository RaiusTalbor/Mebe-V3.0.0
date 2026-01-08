# Motorsportmeisterschaftsberechner
# Mebe V3.0.0
# basierend auf Mebe V2.0.0 Stand 05.01.2025
# teilweise neu gebaut zur Verbesserung der Struktur

import pickle
import random
from tkinter import *
import Daten    #Lesen, Schreiben von Dateien

#Mebe-Module und Funktionen
#import Erstellen
#import Bearbeiten
import Berechnen

#Mebe Prozesse
import Fenster

# ----------Knopffunktionen

#beendet das Program sauber
def beenden():
    prozess.beenden()

# ----------pass für Testzwecke

def test():
    pass   

# ----------View

prozess = Fenster.Fenster()

# Hauptmenü - Steuereinheit Mebe V2 ------------------------------------------

#buttonSerien = Button(master=fenster,
#                      text="Serien",
#                      command=test)
#buttonSerien.pack()

# alle ansehen und bearbeiten
#buttonMeisterschaften = Button(master=fenster,
#                               text="Meisterschaften",
#                               command=test)
#buttonMeisterschaften.pack()

#buttonStrecken = Button(master=fenster,
#                        text="Strecken",
#                        command=test)
#buttonStrecken.pack()

#buttonFahrzeuge = Button(master=fenster,
#                         text="Fahrzeuge",
#                         command=test)
#buttonFahrzeuge.pack()

#buttonFahrer = Button(master=fenster,
#                      text="Fahrer",
#                      command=test)
#buttonFahrer.pack()

#erstellen einer Meisterschaft
prozess.hinzufügenButton("Erstellen", test)

prozess.hinzufügenButton("Bearbeiten", test)

#berechnen einer Meisterschaft
prozess.hinzufügenButton("Berechnen", Berechnen.berechnen)

#Hilfe zu Mebe
prozess.hinzufügenButton("Hilfe", test)

# Mebe 2 hat Mebe 1 implementiert, was bedeutet, dass Mebe 1 in Mebe 2 integriert und unabhängig funktioniert
# die alten Daten und das vereinfachte Programm können verwendet werden
#buttonMebe1 = Button(master=frameButtons,
#                       text="Mebe 1",
#                       command=M1.RunMebe)
#buttonMebe1.pack(side=LEFT, anchor=N, padx= 20, pady = 20)

#Programm beenden
prozess.hinzufügenButton("Beenden", beenden)

prozess.fenster.mainloop()