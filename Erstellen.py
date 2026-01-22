# Motorsportmeisterschaftsberechner
# Mebe V3.0.0
# kümmert sich darum, dass die richtigen Seiten zum Erstellen einer Meisterschaft geöffnet werden --> händelt es quasi

from tkinter import *

from Anzeige import prozess #das Objekt wird global importiert und für alle jederzeit zugreifbar 
import Daten
import Meisterschaft
import Strecke
import ErstelleStrecke
import Fahrer
import Fahrzeug #notwendig hier?

global varweiter

def erstellen():
    global varweiter

    varweiter=0

    weiter() #damit es nicht hier mit drin steht

def weiter():
    #übernimmt die Daten und gibt das nächste Fenster durch

    global varweiter

    sammeln() #speichert die Informationen zwischen --> aber wie??

    #immer Fenster neu initialisieren --> die Unterdinger müssen sich nicht darum kümmern
    prozess.löscheframeInhalt()
    prozess.löscheButtons()

    prozess.setTitelFrame("Erstellen einer Meisterschaft")

    prozess.hinzufügenButton("Abbrechen", prozess.hauptmenü) #geändert, um weniger verwirrend

    prozess.hinzufügenButton("Weiter", weiter)

    varweiter += 1 #vorher erhöht, um überall gleiche Zahlen stehen zu haben (läuft ja durch)

    if varweiter == 1: #Meisterschaft
        meisterschaftdefinieren()
    elif varweiter == 2: #Strecken hinzufügen
        rennkalendereinfügen()
    elif varweiter == 3: #Fahrer hinzufügen
        fahrereinfügen()
    elif varweiter == 4: #Speichern und erstellen beenden
        prozess.hauptmenü() #da sonst diese Funktion weiter und er hängt fest  

#einem speziellen Erstellen-Code wird immer ein Wert übergeben: ein entsprechender Pfad oder "leer". Bei leer wird etwas neues erstellt, mit Pfad wird dieser geladen und die Werte von dem Ding gespeichert

def sammeln():
    #sammelt bei vaweiter die Eingaben ein und speichert die zwischen

    global entryJahrMeisterschaft, entryNameMeisterschaft, rennkalenderListe, fahrerliste

    global meisterschaft #globalen Objekte zum Speichern

    if varweiter == 1: #Meisterschaft
        meisterschaft = Meisterschaft.Meisterschaft()

        name = entryNameMeisterschaft.get()
        name = name + entryJahrMeisterschaft.get()

        meisterschaft.setname(name)
        meisterschaft.setPfade()

        #Initialisieren der globalen Listen für Rennkalender und Speicherliste, weil ich sonst immer weitere globals definieren muss und davon will ich weg
        rennkalenderListe = []
        fahrerliste = []

    elif varweiter == 2: #Strecken hinzufügen
        prozess.zeige1frame() #Zwei-Fenster-Anzeige deaktiviert

        meisterschaft.setrennkalenderName(rennkalenderListe)

    elif varweiter == 3: #Fahrer hinzufügen
        prozess.zeige1frame() #Zwei-Fenster-Anzeige deaktiviert

        meisterschaft.setfahrerlisteName(fahrerliste)

    elif varweiter == 4: #Speichern und erstellen beenden
        meisterschaft.speichern()
        print("Speicherst Du?")

    else:
        pass

def meisterschaftdefinieren():
    global entryJahrMeisterschaft, entryNameMeisterschaft

    prozess.hinzufügenLabel("Name der Meisterschaft:")

    entryNameMeisterschaft = Entry(master = prozess.aktuelleAnzeige)
    entryNameMeisterschaft.pack()

    prozess.hinzufügenLabel("Jahr der Meisterschaft:")

    entryJahrMeisterschaft = Entry(master = prozess.aktuelleAnzeige)
    entryJahrMeisterschaft = Entry(master = prozess.aktuelleAnzeige)
    entryJahrMeisterschaft.pack()

def auswählen():
    #Knopf-Funktion, um aktuelle Radioauswahl der Liste hinzuzufügen
    global radioAuswahl
    global rennkalenderListe, fahrerliste

    #holt sich die Daten und speichert sie zwischen
    if varweiter == 2:
        rennkalenderListe.append(radioAuswahl.get())
    
    if varweiter == 3:
        fahrerliste.append(radioAuswahl.get())

    aktualisiereFenster()

def entfernen():
    #Knopf-Funktion, um aktuelle Radioauswahl aus der Liste zu entfernen
    global radioAuswahlRechts
    global rennkalenderListe, fahrerliste

    #holt sich die Daten und speichert sie zwischen
    if varweiter == 2:
        rennkalenderListe.remove(radioAuswahlRechts.get())
    
    if varweiter == 3:
        fahrerliste.remove(radioAuswahlRechts.get())

    aktualisiereFenster()

def aktualisiereFenster():
    #Funktion, um im Zwei-Fenster-Modus die linke Anzeige, sowohl als auch die rechte Anzeige zu aktualisieren (bei Hinzufügen wie auch entfernen und hinzufügen Strecke)
    #aus Liste links weg, zu Liste rechts hin

    global radioAuswahl, radioAuswahlRechts
    global rennkalenderListe, fahrerliste

    #zuerst den linken Frame löschen, wiederherstellen, aber mit veränderter Liste -- effizienter?
    for widget in prozess.frameAnzeige1.winfo_children():
        widget.pack_forget()
    for widget in prozess.frameAnzeige2.winfo_children():
        widget.pack_forget()

    if varweiter == 2:
        liste = Daten.listeNamen("Strecken")
        listeRechts = rennkalenderListe
    else:
        liste = Daten.listeNamen("Fahrer")
        listeRechts = fahrerliste
        
        #entfernt alle Inhalte, die rechts schon vorkommen
        for i in fahrerliste:
            liste.remove(i)

    #alle Radios links hinzufügen
    radioAuswahl = StringVar()
    for i in range(len(liste)):
        radio = Radiobutton(master=prozess.frameAnzeige1, text=liste[i], value=liste[i], variable=radioAuswahl)
        radio.pack(anchor='w')
    radioAuswahl.set(liste[0])

    #alle Elemente rechts hinzufügen, aber nur wenn in Liste was drin
    if listeRechts:
        radioAuswahlRechts = StringVar()
        for i in range(len(listeRechts)):
            radioStrecken = Radiobutton(master=prozess.frameAnzeige2, text=listeRechts[i], value=listeRechts[i], variable=radioAuswahlRechts)
            radioStrecken.pack(anchor='w')
        radioAuswahlRechts.set(listeRechts[0])

    prozess.frameAnzeige1.update_idletasks()
    prozess.frameAnzeige2.update_idletasks()

def rennkalendereinfügen():
    #zeigt die Streckenauswahl an
    global radioAuswahl, radioAuswahlRechts
    global rennkalenderListe

    prozess.zeige2frames() #Zwei-Fenster-Anzeige aktiviert

    prozess.hinzufügenButton("Neue Strecke erstellen", erstelleElement)

    prozess.hinzufügenButton("Strecke auswählen", auswählen) #nimmt ausgewählte Strecke und fügt sie dem Kalender und der zweiten Anzeige hinzu

    prozess.hinzufügenButton("Strecke entfernen", entfernen) #nimmt ausgewählte Strecke und entfernt sie aus dem Kalender und der zweiten Anzeige

    listeStrecken = Daten.listeNamen("Strecken")

    radioAuswahl = StringVar()
    for i in range(len(listeStrecken)):
        radioStrecken = Radiobutton(master=prozess.frameAnzeige1, text=listeStrecken[i], value=listeStrecken[i], variable=radioAuswahl)
        radioStrecken.pack(anchor='w')
    radioAuswahl.set(listeStrecken[0])

    if rennkalenderListe:
        radioAuswahlRechts = StringVar()
        for i in range(len(rennkalenderListe)):
            radioStrecken = Radiobutton(master=prozess.frameAnzeige2, text=rennkalenderListe[i], value=rennkalenderListe[i], variable=radioAuswahlRechts)
            radioStrecken.pack(anchor='w')
        radioAuswahlRechts.set(rennkalenderListe[0])

def fahrereinfügen():
    #zeigt die Fahrerauswahl an
    global radioAuswahl, radioAuswahlRechts
    global fahrerliste

    prozess.zeige2frames() #Zwei-Fenster-Anzeige aktiviert

    prozess.hinzufügenButton("Neuer Fahrer erstellen", erstelleElement)

    prozess.hinzufügenButton("Fahrer auswählen", auswählen) #nimmt ausgewählten Fahrer und fügt sie der Liste und der zweiten Anzeige hinzu

    prozess.hinzufügenButton("Fahrer entfernen", entfernen) #nimmt ausgewählten Fahrer und entfernt sie aus dem Kalender und der zweiten Anzeige

    listeFahrer = Daten.listeNamen("Fahrer")

    radioAuswahl = StringVar()
    for i in range(len(listeFahrer)):
        radioFahrer = Radiobutton(master=prozess.frameAnzeige1, text=listeFahrer[i], value=listeFahrer[i], variable=radioAuswahl)
        radioFahrer.pack(anchor='w')
    radioAuswahl.set(listeFahrer[0])

    if fahrerliste:
        radioAuswahlRechts = StringVar()
        for i in range(len(fahrerliste)):
            radioStrecken = Radiobutton(master=prozess.frameAnzeige2, text=fahrerliste[i], value=fahrerliste[i], variable=radioAuswahlRechts)
            radioStrecken.pack(anchor='w')
        radioAuswahlRechts.set(fahrerliste[0])

    aktualisiereFenster() #warum keine Ahnung, aber sonst werden die falschen Radiobuttons angezeigt

def erstelleElement():
    global varweiter

    if varweiter == 2:
        ErstelleStrecke.erstellen("")
    if varweiter == 3:
        ErstelleFahrer.erstellen()

    aktualisiereFenster() #sonst würde nicht aktualisiert werden