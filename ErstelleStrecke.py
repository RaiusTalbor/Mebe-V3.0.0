# Motorsportmeisterschaftsberechner
# Mebe V3.0.0
# erstellt nur eine Strecke

from tkinter import *

from Anzeige import prozess #das Objekt wird global importiert und für alle jederzeit zugreifbar gemacht
import Strecke

def speichern():
    pass

def erstellen(name):
    #erstellen und bearbeiten einer Strecke

    #Fenster initialisiren
    prozess.löscheButtons()
    prozess.zurückButton() #TODO nochmal überlegen
    prozess.hinzufügenButton("Speichern", speichern)

    prozess.löscheframeInhalt()
    
    #Auswahl, ob bearbeiten oder nicht
    if name == "":
        strecke = Strecke()
    else:
        strecke = Strecke()
        strecke.ladenName(name)

    prozess.hinzufügenLabel("Wer ist der Rekordhater?")

    entryRekordhalterAuswählen = Entry(master = prozess.frameAnzeige)
    entryRekordhalterAuswählen.pack()

    entryRekordhalterAuswählen.delete(0, END)
    entryRekordhalterAuswählen.insert(0, name)
    entryRekordhalterAuswählen.update_idletasks()
    
    buttonAuswählen = Button(master = prozess.frameAnzeige, text = "Fahrer aus Datenbank auswählen...", command = FahrerAuswählen)
    buttonAuswählen.pack()

    prozess.hinzufügenLabel("Auswahl des Streckentps:")

    streckentyp = StringVar()
    kurvig = Radiobutton(master = prozess.frameAnzeige, text = "Kurvige Strecke", value = 1, variable = streckentyp)
    ausgeglichen = Radiobutton(master = prozess.frameAnzeige, text = "Ausgeglichene Strecke", value = 2, variable = streckentyp)
    schnell = Radiobutton(master = prozess.frameAnzeige, text = "Schnelle Strecke", value = 3, variable = streckentyp)
    kurvig.select()

    kurvig.pack()
    ausgeglichen.pack()
    schnell.pack()

    if strecke.streckentyp == 1:
        kurvig.select()
    elif strecke.streckentyp == 2:
        ausgeglichen.select()
    else:
        schnell.select()

    kurvig.update_idletasks()
    ausgeglichen.update_idletasks()
    schnell.update_idletasks()

    prozess.hinzufügenLabel("Auswahl der Schwierigkeit:")

    scaleSchwierigkeit = Scale(master = prozess.frameAnzeige, from_= 1, to = 10, orient=HORIZONTAL)
    scaleSchwierigkeit.pack()

    scaleSchwierigkeit.set(strecke.schwierigkeit)
    scaleSchwierigkeit.update_idletasks()