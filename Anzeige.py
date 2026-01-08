# Motorsportmeisterschaftsberechner
# Mebe V3.0.0

#START DES PROGRAMMS
#Anzeige wird geladen, da steckt die komplette GUI drin. Dadurch, dass sie beim ersten Laden immer direkt ausgeführt wird, wird dabei auch das Objekt prozess erstellt, welches dadurch global zugreifbar gemacht wird - womit ich nicht immer alle Objekte oder Callbacks übergeben muss und so direkt auf die Methoden zugreifen kann.
#nicht mit MebeV3.py zusammenführbar, da sonst durch die Imports ein Zyklus entsteht und ein Fehler erfolgt

import random
from tkinter import *
import Daten    #Lesen, Schreiben von Dateien
import time

class Fenster:
    #Blueprint für jedes Fenster, welches existiert

    def __init__(self):
        self.fenster = Tk()
        self.fenster.title("Mebe V3.0.0")
        self.fenster.geometry("800x600")

        self.labelTitel = Label(master=self.fenster,
                        text="Mebe V3.0.0",
                        font=('', 18))
        self.labelTitel.pack()

        self.frameButtons = Frame(master=self.fenster)
        self.frameButtons.pack()

        self.frameAnzeige = Frame(master=self.fenster)
        self.frameAnzeige.pack()

        self.frameInfo = Frame(master=self.fenster)
        self.frameInfo.pack()

        self.labelInfo = Label(self.frameInfo, text="", font=('', 15), wraplength = 800)
        self.labelInfo.pack()

    def beenden(self):
        self.setInfo('Mebe V3.0.0 wird beendet! Auf Wiedersehen!')
        time.sleep(1)
        self.fenster.destroy()

    def neuesFenster(self, titel):
        #sollte auf das alte System zurückgesprungen werden müssen, aber bitte möglichst nicht verwenden

        self.fenster = Tk()
        self.fenster.title(titel)
        self.fenster.geometry("800x600")

        self.labelTitel = Label(master=self.fenster,
                        text=titel,
                        font=('', 18))
        self.labelTitel.pack()

        self.frameButtons = Frame(master=self.fenster)
        self.frameButtons.pack()

        self.frameAnzeige = Frame(master=self.fenster)
        self.frameAnzeige.pack()

        self.frameInfo = Frame(master=self.fenster)
        self.frameInfo.pack()

        self.labelInfo = Label(self.frameInfo, text="", font=('', 15))
        self.labelInfo.pack()

        self.listebuttons=[]
        self.übergebeneFrames=[]

    #managen der Buttons
    def löscheButtons(self):
        for i in self.listebuttons:
            i.destroy()
            self.listebuttons.remove(i)

    def hinzufügenButton(self, textübergabe, commandübergabe):
        button = Button(master=self.frameButtons, text=textübergabe, command=commandübergabe)
        button.pack(side=LEFT, anchor=N, padx= 20, pady = 20)
        self.listebuttons.append(button)
        button.update_idletasks()

    def setTitelFrame(self, übergabe):
        self.labelTitel.config(text=übergabe)
        self.labelTitel.update_idletasks()

    #managen der Info 
    def setInfo(self, info):
        self.info = info 
        self.labelInfo.config(text=info)
        self.labelInfo.update_idletasks()

    def löscheInfo(self):
        self.info = '' 
        self.labelInfo.config(text=self.info)
        self.labelInfo.update_idletasks()

    #managen des Anzeigefelds
    #ACHTUNG NICHT TRIVIAL!!!
    def zeige(self, frame):
        #fügt Frame zur Frameliste hinzu
        self.übergebeneFrames.append(frame)

    def aktualisiereFenster(self):
        for i in self.übergebeneFrames:
            i.config(master=self.frameAnzeige)
            i.pack()
        self.fenster.update_idletasks()

prozess = Fenster()