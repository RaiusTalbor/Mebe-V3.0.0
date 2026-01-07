# Motorsportmeisterschaftsberechner
# Mebe V3.0.0

from tkinter import *
import time

class Fenster:
    #Blueprint für jedes Fenster, welches existiert

    fenster = Tk()
    fenster.title("Mebe V3.0.0")
    fenster.geometry("800x600")

    labelTitel = Label(master=fenster,
                    text="Mebe V3.0.0",
                    font=('', 18))
    labelTitel.pack()

    frameButtons = Frame(master=fenster)
    frameButtons.pack()

    frameAnzeige = Frame(master=fenster)
    frameAnzeige.pack()

    frameInfo = Frame(master=fenster)
    frameInfo.pack()

    titel = ''
    buttons = []
    übergebeneFrames = []
    info = ''

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

        self.labelInfo = Label(self.frameInfo, text="", font=('', 15))
        self.labelInfo.pack()

        self.fenster.mainloop()

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

    #managen der Buttons
    def löscheButtons(self):
        for i in self.buttons:
            i.destroy()

    def hinzufügenButton(self, button):
        button.config(master = self.frameButtons)
        button.pack(side=LEFT, anchor=N, padx= 20, pady = 20)
        #update_idletasks() nötig?

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