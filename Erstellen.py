# Motorsportmeisterschaftsberechner
# Mebe V3.0.0
# kümmert sich darum, dass die richtigen Seiten zum Erstellen einer Meisterschaft geöffnet werden --> händelt es quasi

from Anzeige import prozess #das Objekt wird global importiert und für alle jederzeit zugreifbar gemacht

global varweiter

def erstellen():
    global varweiter

    #Fenster initialisieren
    prozess.löscheframeInhalt()
    prozess.löscheButtons()
    prozess.zurückButton()

    prozess.setTitelFrame("Erstellen einer Meisterschaft")

    prozess.hinzufügenButton("Weiter", weiter)

    varweiter=0

    weiter() #damit es nicht hier mit drin steht

def weiter():
    #übernimmt die Daten und gibt das nächste Fenster durch
    
    if varweiter == 0: #Meisterschaft
        ErstellenMeisterschaft.erstellen("leer") #umbenennen!!
        #sammeln Befehl, der aber in ErstellenXXX ausgeführt wird
    elif varweiter == 1: #Strecken hinzufügen
        ErstellenStrecken.erstellen("leer")
    elif varweiter == 2: #Fahrer hinzufügen
        ErstellenFahrer.erstellen("leer")
    elif varweiter == 3: #Speichern und erstellen beenden
        pass

    varweiter += 1

#einem speziellen Erstellen-Code wird immer ein Wert übergeben: ein entsprechender Pfad oder "leer". Bei leer wird etwas neues erstellt, mit Pfad wird dieser geladen und die Werte von dem Ding gespeichert