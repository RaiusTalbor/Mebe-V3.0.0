# Motorsportmeisterschaftsberechner
# Mebe V3.0.0
# basierend auf Mebe V2.0.0 Stand 05.01.2025
# teilweise neu gebaut zur Verbesserung der Struktur

#Mebe-Module und Funktionen
#import Erstellen
#import Bearbeiten
import Berechnen

#START DES PROGRAMMS
#Anzeige wird geladen, da steckt die komplette GUI drin. Dadurch, dass sie beim ersten Laden immer direkt ausgeführt wird, wird dabei auch das Objekt prozess erstellt, welches dadurch global zugreifbar gemacht wird - womit ich nicht immer alle Objekte oder Callbacks übergeben muss und so direkt auf die Methoden zugreifen kann.
#nicht mit Anzeige.py zusammenführbar, da sonst durch die Imports ein Zyklus entsteht und ein Fehler erfolgt

from Anzeige import prozess

# ----------pass für Testzwecke

def test():
    pass   

# ----------View

# Hauptmenü - Steuereinheit Mebe V3 ------------------------------------------

# alle ansehen und bearbeiten, Serien hinzufügen?
# Mebe 2 hat Mebe 1 implementiert, was bedeutet, dass Mebe 1 in Mebe 2 integriert und unabhängig funktioniert - Feature wurde entfernt wegen fehlenden Mehrwert - Mebe 3 basiert von der Berechnung auf M1

prozess.hinzufügenButton("Erstellen", test) #erstellen einer Meisterschaft

prozess.hinzufügenButton("Bearbeiten", test)

prozess.hinzufügenButton("Berechnen", Berechnen.berechnen) #berechnen einer Meisterschaft

prozess.hinzufügenButton("Hilfe", test) #Hilfe zu Mebe

prozess.hinzufügenButton("Beenden", prozess.beenden) #Programm beenden

prozess.start = 1

prozess.fenster.mainloop() #hier, da sonst beim Laden fest hängt