# Motorsportmeisterschaftsberechner
# Mebe V3.0.0
# erstellt nur eine Strecke

from tkinter import *

from Anzeige import prozess #das Objekt wird global importiert und für alle jederzeit zugreifbar gemacht
import Strecke
import Daten

def speichern():
    global strecke, entryName, entryRekordhalterAuswählen, streckentyp, scaleSchwierigkeit

    #Radios
    global kurvig
    global ausgeglichen
    global schnell

    #Informationen aus Widgets holen

    if entryName.winfo_exists():
        strecke.name = entryName.get()   

    strecke.rekordhalter = entryRekordhalterAuswählen.get()

    strecke.streckentyp = int(streckentyp.get())

    strecke.schwierigkeit = scaleSchwierigkeit.get()

    strecke.speichern()

    prozess.wiederherstellenCheckpoint() #zurück an Hauptprozess

def erstellen(name):
    #erstellen und bearbeiten einer Strecke
    global strecke, entryName, entryRekordhalterAuswählen, streckentyp, scaleSchwierigkeit

    #Radios
    global kurvig
    global ausgeglichen
    global schnell

    #Fenster initialisieren
    prozess.speicherCheckpoint()

    prozess.zurückButton() #TODO nochmal überlegen
    prozess.hinzufügenButton("Speichern", speichern)
    
    #Auswahl, ob bearbeiten oder nicht
    if name == "":
        strecke = Strecke.Strecke()

        prozess.hinzufügenLabel("Name der Strecke:")

        entryName = Entry(master = prozess.frameAnzeige)
        entryName.pack()
    else:
        strecke = Strecke.Strecke()
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

# fügt Fahrer in Entry aus fahrerAuswahl ein --> Name ist definitiv richtig; gibt checkpoint wieder zurück
def fügeFahrerein():
    global Fahrer, strecke,entryRekordhalterAuswählen

    #vielleicht vorher leeren
    entryRekordhalterAuswählen.insert(0, Fahrer.get())
    strecke.setrekordhalter = Fahrer.get()

    prozess.wiederherstellenCheckpoint()

# alle Fahrer angezeigen. Mit Radiobuttons Auswahl des Fahrers aus Datenbank möglich
def FahrerAuswählen():
    global Fahrer, strecke

    prozess.speicherCheckpoint()

    listeFahrer = Daten.listeNamen("Fahrer")

    prozess.hinzufügenButton("Fahrer auswählen", fügeFahrerein)

    Fahrer = StringVar()
    #für jedes Element der Liste (also alle Fahrer) wird ein Radiobutton erzeugt
    for i in range(0, len(listeFahrer)):

        #formated String in Radiobutton wird gesetzt
        textFahrer = listeFahrer[i]

        radioFahrer = Radiobutton(master = prozess.frameAnzeige, text = listeFahrer[i], value = str(listeFahrer[i]), variable = Fahrer)
        radioFahrer.pack()

    Fahrer.set(strecke.rekordhalter)