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
        self.start = 0
        self.hauptmenuebuttons = []
        #Hauptmenübuttons sind besondere Buttons, die sich in button.kategorie unterscheiden. Sie haben die Kategorie "Hauptmenü".
        #Alle Buttons, die in MebeV3.py erstellt werden, bekommen diese Kategorie, da beim Laden dieses Moduls prozess.start=0 ist. Dadurch wird beim Hinzufügen der Buttons, solange start=0, diese Eigenschaft zugewiesen und permanent in die Liste hauptmenübuttons geschrieben. Nach erstmaligen (und damit letztmaligen Durchlaufen) von MebeV3.py wird start auf 1 gesetzt (für immer), damit keine weiteren Hauptmenübuttons hinzugefügt werden können. Alle anderen Buttons werden demnach normal behandelt.
        #Alle Buttons mit dieser speziellen Kategorie werden nie gelöscht, sondern nur versteckt. So kann man (über die Liste geht der Zugriff nicht verloren) sie immer wieder hinzufügen, wenn sie benötigt werden (destroy vernichtet sie für immer).

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

        #für die geteilte Anzeige - werden noch nicht gepackt --> nicht sichtbar
        self.frameAnzeige1 = Frame(master=self.frameAnzeige)
        self.frameAnzeige2 = Frame(master=self.frameAnzeige)

        self.frameInfo = Frame(master=self.fenster)
        self.frameInfo.pack()

        self.labelInfo = Label(self.frameInfo, text="", font=('', 15), wraplength = 800)
        self.labelInfo.pack()

        self.listebuttons=[]
        self.übergebeneFrames=[]
        self.gespeicherteButtons=[]

        self.checkpoint = [self.frameAnzeige, self.gespeicherteButtons] #speichert einen Frame, damit er wiederhergestellt werden kann

    def beenden(self):
        self.setInfo('Mebe V3.0.0 wird beendet! Auf Wiedersehen!')
        time.sleep(1)
        self.fenster.destroy()

    #Info -----------------------------------
    def setInfo(self, info):
        self.info = info 
        self.labelInfo.config(text=info, font=('', 15), wraplength = 800)
        self.labelInfo.update_idletasks()

    def löscheInfo(self):
        self.info = '' 
        self.labelInfo.config(text=self.info)
        self.labelInfo.update_idletasks()

    #Buttons ----------------------------------
    def löscheButtons(self):
        for i in self.listebuttons:
            if i.kategorie != "Hauptmenü":
                i.destroy()
            else:
                i.pack_forget() #alle mit dieser Kategorie werden versteckt, nicht zerstört

        self.listebuttons = []

    def hinzufügenButton(self, textübergabe, commandübergabe):
        button = Button(master=self.frameButtons, text=textübergabe, command=commandübergabe)
        button.pack(side=LEFT, anchor=N, padx= 20, pady = 20)
        button.kategorie = "Button"
        self.listebuttons.append(button)

        #Sonderbehandlung Buttons aus MebeV3.py
        if self.start == 0:
            self.hauptmenuebuttons.append(button)
            button.kategorie = "Hauptmenü"

    def setTitelFrame(self, übergabe):
        self.labelTitel.config(text=übergabe)
        self.labelTitel.update_idletasks()

    def zurückButton(self):
        #globaler Zurück-Button, da immer dasselbe
        prozess.hinzufügenButton("Zurück zum Hauptmenü", prozess.hauptmenü)

    #noch einen, um zum Frame davor zurückzukehren

    def hauptmenü(self):
        self.löscheButtons()
        self.löscheInfo()
        self.löscheframeInhalt()

        #wieder hinzufügen der Buttons
        for i in self.hauptmenuebuttons:
            i.pack(side=LEFT, anchor=N, padx= 20, pady = 20)
            self.listebuttons.append(i)

    #Anzeige ----------------------------------------
    def löscheframeInhalt(self):
        for widget in self.frameAnzeige.winfo_children():
            widget.destroy()

        self.frameAnzeige.update_idletasks()

    def zeige2frames(self):
        #um die geteilte Anzeige zu nutzen, muss sie explizit aktiviert und deaktiviert werden
        self.frameAnzeige1.pack(fill=BOTH, expand=True, side=LEFT)
        self.frameAnzeige2.pack(fill=BOTH, expand=True, side=RIGHT)

    def zeige1frame(self):
        self.frameAnzeige1.pack_forget()
        self.frameAnzeige2.pack_forget()
        self.frameAnzeige1.update_idletasks()
        self.frameAnzeige2.update_idletasks()

    def speicherCheckpoint(self):
        #speichert Checkpoint und übergibt Buttons und Frame frei

        self.checkpoint = [self.frameAnzeige, self.listeButtons]

        self.frameAnzeige.pack_forget()

        for i in self.listebuttons:
            i.pack_forget()

    def wiederherstellenCheckpoint(self):
        self.löscheframeInhalt()
        self.löscheButtons()
        self.löscheInfo()

        self.frameAnzeige = self.checkpoint[0]

        buttons = self.checkpoint[1]
        
        for i in buttons:
            i.pack(side=LEFT, anchor=N, padx= 20, pady = 20)
            self.listebuttons.append(i)

    #scrollbar...

    def hinzufügenLabel(self, text):
        label = Label(master = self.frameAnzeige, text = text)
        label.pack()

prozess = Fenster()