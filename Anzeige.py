# Motorsportmeisterschaftsberechner
# Mebe V3.0.0

#START DES PROGRAMMS
#Anzeige wird geladen, da steckt die komplette GUI drin. Dadurch, dass sie beim ersten Laden immer direkt ausgeführt wird, wird dabei auch das Objekt prozess erstellt, welches dadurch global zugreifbar gemacht wird - womit ich nicht immer alle Objekte oder Callbacks übergeben muss und so direkt auf die Methoden zugreifen kann.
#nicht mit MebeV3.py zusammenführbar, da sonst durch die Imports ein Zyklus entsteht und ein Fehler erfolgt

import random
from tkinter import *
import Daten    #Lesen, Schreiben von Dateien
import time
import os

from Aussehen import *

class Fenster:
    #Blueprint für jedes Fenster, welches existiert

    def __init__(self):
        self.start = 0
        self.hauptmenuebuttons = []

        #Alle Buttons, die in MebeV3.py erstellt werden, solange start=0 ist, werden permanent in die Liste hauptmenübuttons geschrieben. Nach erstmaligen (und damit letztmaligen Durchlaufen) von MebeV3.py wird start auf 1 gesetzt (für immer), damit keine weiteren Hauptmenübuttons hinzugefügt werden können. Alle anderen Buttons werden demnach normal behandelt.

        self.fenster = Tk()
        self.fenster.title("Mebe V3.0.0")
        self.fenster.geometry("900x600")
        self.fenster.configure(**aussehenFenster)

        self.labelTitel = Label(**aussehenLabelÜberschrift, master=self.fenster, text="Mebe V3.0.0")
        self.labelTitel.pack()

        self.frameButtons = Frame(**aussehenFrame, master=self.fenster)
        self.frameButtons.pack()

        self.frameAnzeigeInhalt = Frame(**aussehenFrame, master=self.fenster) #Hält den ContentFrame fest, da dieser nur relativ existiert
        self.frameAnzeigeInhalt.pack(fill="both", expand=True)

        #Canvas, um die Scrollbar darin festzuhalten --> Zwischenschicht zwischen frameAnzeigeInhalt und frameAnzeige, in der die Scrollbar den inneren Frame scrollen kann
        self.canvasScrollbar = Canvas(**aussehenCanvas, master=self.frameAnzeigeInhalt)
        self.scrollbar = Scrollbar(**aussehenScrollbar, master=self.frameAnzeigeInhalt, orient=VERTICAL, command=self.canvasScrollbar.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvasScrollbar.pack(side=LEFT, fill=BOTH, expand=True)

        self.frameAnzeige = Frame(**aussehenFrame, master=self.canvasScrollbar) #Standard-Anzeige
        #self.frameAnzeige.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.canvasScrollbar.bind("<Configure>", lambda e: self.canvasScrollbar.itemconfig(self.canvasFrame, width=e.width)) #übernimmt die Funktion von vorher
        self.canvasFrame = self.canvasScrollbar.create_window((0, 0), window=self.frameAnzeige, anchor=NW)
        self.frameAnzeige.bind("<Configure>", lambda e: self.canvasScrollbar.configure(scrollregion=self.canvasScrollbar.bbox("all")))
        self.canvasScrollbar.configure(yscrollcommand=self.scrollbar.set)
        self.fenster.bind("<MouseWheel>", lambda e: self.canvasScrollbar.yview_scroll(int(-1*(e.delta/120)), "units")) #damit Mausrad scrollt

        self.aktuelleAnzeige = self.frameAnzeige #speichert die aktuelle Anzeige, die gerade angezeigt wird (ganz oben liegt) --> einfacher händeln als Liste

        self.alleAnzeigen = [] #dazu da, um die Reihenfolge der Anzeigen besser zu managen und wenn eine Anzeige gelöscht wird, dass die nächsttiefere wieder angesprochen werden kann
        self.alleAnzeigen.append(self.aktuelleAnzeige)

        #für die geteilte Anzeige - werden noch nicht gepackt --> nicht sichtbar --> Ausgelagert zu zeige2frames(); ist an Checkpoint-Logik gescheitert, da sie ja die Frames immer übereinander lagern; aktiviert man aber die 2-Fenster-Logik wieder, dann werden sie ins allererste Fenster und nicht oberste Fenster eingetragen
        #self.frameAnzeige1 = Frame(master=self.aktuelleAnzeige)
        #self.frameAnzeige2 = Frame(master=self.aktuelleAnzeige)

        self.frameInfo = Frame(**aussehenFrame, master=self.fenster)
        self.frameInfo.pack()

        self.labelInfo = Label(**aussehenLabelGroß, master=self.frameInfo, text="", wraplength = 800)
        self.labelInfo.pack()

        self.listebuttons=[] #aktuellen Buttons
        self.gespeicherteButtons=[] #für Checkpoint, da alle Buttons drin, die für vorigen Checkpoint benötigt werden

        #self.checkpoint = [self.frameAnzeige, self.gespeicherteButtons] #speichert einen Frame, damit er wiederhergestellt werden kann

    def beenden(self):

        self.setInfo('Mebe V3.0.0 wird beendet! Auf Wiedersehen!')

        #löscht den Ordner mit temporären Dateien; Pfad setzen, Elemente heraussuchen, einzeln zerstören
        pfad = "temporäre Dateien"
        liste = os.listdir(pfad)
        for i in range(0, len(liste)):
            os.remove(str(pfad + "/" + liste[i]))

        time.sleep(1)
        self.fenster.destroy()

    #Info -----------------------------------
    def setInfo(self, info):
        self.info = info 
        self.labelInfo.config(text=info, font=('', 15), wraplength = 800)
        self.labelInfo.lift()  # legt das Label über alle anderen Widgets
        self.labelInfo.update_idletasks()

    def löscheInfo(self):
        self.info = '' 
        self.labelInfo.config(text=self.info)
        self.labelInfo.update_idletasks()

    #Buttons ----------------------------------
    def löscheButtons(self):
        for i in self.listebuttons:
            i.pack_forget()
            #mögliche Optimierung Issue #14
            #if i.kategorie != "Hauptmenü":
            #    i.destroy()
            #else:
            #    i.pack_forget() #alle mit dieser Kategorie werden versteckt, nicht zerstört

        self.listebuttons = []

    def hinzufügenButton(self, textübergabe, commandübergabe):
        button = Button(**aussehenButton, master=self.frameButtons, text=textübergabe, command=commandübergabe)
        button.pack(side=LEFT, anchor=N, padx= 20, pady = 20)
        #button.kategorie = "Button" #mögliche Optimierung Issue #14
        self.listebuttons.append(button)

        #Sonderbehandlung Buttons aus MebeV3.py
        if self.start == 0:
            self.hauptmenuebuttons.append(button)
            #button.kategorie = "Hauptmenü" #mögliche Optimierung Issue #14

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
        self.setTitelFrame("Mebe V3.0.0")
        
        self.löscheframeInhalt() #wichtig, weil sonst aktuellen Inhalte nicht entfernt werden

        #self.zeige1frame() #sollte der gerade in Zwei-Fenster-Modus hängen --> geht nicht, da evtl. nicht initialisiert

        for frame in self.alleAnzeigen[1:]:
            frame.destroy()

        self.aktuelleAnzeige = self.alleAnzeigen[0]      # Hauptmenüframe wieder aktuell setzen
        self.alleAnzeigen = [] #zurücksetzen des Anzeigenspeichers, um Checkpoints sauber zu laden
        self.alleAnzeigen.append(self.aktuelleAnzeige)   # wieder an alleAnzeigen anfügen, sonst leer!

        #wieder hinzufügen der Buttons
        for i in self.hauptmenuebuttons:
            i.pack(side=LEFT, anchor=N, padx= 20, pady = 20)
            self.listebuttons.append(i)

    #Anzeige ----------------------------------------
    def löscheframeInhalt(self):
        for widget in self.aktuelleAnzeige.winfo_children():
            widget.pack_forget() #kein destroy, da sonst große Probleme

        self.aktuelleAnzeige.update_idletasks()

    def zeige2frames(self):
        #um die geteilte Anzeige zu nutzen, muss sie explizit aktiviert und deaktiviert werden
        self.frameAnzeige1 = Frame(**aussehenFrame, master=self.aktuelleAnzeige) #werden dynamisch erstellt, damit immer oben 
        self.frameAnzeige2 = Frame(**aussehenFrame, master=self.aktuelleAnzeige)

        self.frameAnzeige1.pack(fill=BOTH, expand=True, side=LEFT)
        self.frameAnzeige2.pack(fill=BOTH, expand=True, side=LEFT)

    def zeige1frame(self):
        self.frameAnzeige1.pack_forget()
        self.frameAnzeige2.pack_forget()
        self.frameAnzeige1.update_idletasks()
        self.frameAnzeige2.update_idletasks()

    def speicherCheckpoint(self):
        #speichert Checkpoint und übergibt Buttons und Frame frei

        #erstellt Frame, den er auf frameAnzeige legt --> der ist nun der aktuelle Frame
        neuerFrame = Frame(**aussehenFrame, master=self.frameAnzeige) #Standard-Anzeige, legt den Frame über die anderen Frames | frameAnzeige --> für Scrollbar-Logik ; davor: frameAnzeigeInhalt
        neuerFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.aktuelleAnzeige = neuerFrame #aktuelleAnzeige wird gesetzt
        self.alleAnzeigen.append(neuerFrame) #Liste wird richtig gepflegt

        self.canvasScrollbar.yview_moveto(0)  # Scrollbar springt ganz nach oben

        #Buttonmanagement
        self.gespeicherteButtons.append(self.listebuttons[:]) #speichert alle aktuellen Buttons

        self.löscheButtons()

    def wiederherstellenCheckpoint(self):
        self.aktuelleAnzeige.destroy() #aktuelle Anzeige wird gelöscht und soll nicht mehr behalten werden
        self.alleAnzeigen.remove(self.aktuelleAnzeige) #löscht die Anzeige aus der Liste
        self.aktuelleAnzeige = self.alleAnzeigen[-1] #setzt die aktuelle Anzeige nun auf die letzte Anzeige, die vor der letzten gespeichert wurde

        #da alle die ganze Zeit existieren, sind die Anzeigen nie weg, sondern nur unsichtbar zum Zeitpunkt

        self.canvasScrollbar.yview_moveto(0)  # Scrollbar springt ganz nach oben

        #Buttonmanagement
        self.löscheButtons() #löscht alle erstellten Buttons

        buttons = self.gespeicherteButtons[-1]

        for i in buttons:
            i.pack(side=LEFT, anchor=N, padx= 20, pady = 20)
            self.listebuttons.append(i)

        self.gespeicherteButtons.pop(-1) #löscht den letzten Eintrag (die eben gesetzten Buttons)

    #scrollbar...

    def hinzufügenLabel(self, text):
        label = Label(**aussehenLabel, master = self.aktuelleAnzeige, text = text)
        label.pack()

    def wurdeGespeichert(self, pfad):
        #kann von einem Objekt benutzt werden, um zu prüfen, ob eine Speicherung erfolgreich war
        try:
            Daten.lesen(pfad)
            self.setInfo("Speichern erfolgreich: " + pfad)
        except:
            self.setInfo("Ein unbekannter Fehler beim Speichern ist aufgetreten: " + pfad)

        #time.sleep(1)
        self.fenster.after(3000,self.löscheInfo) #nach 3000 ms führt prozess.fenster diese Aktion aus

prozess = Fenster()