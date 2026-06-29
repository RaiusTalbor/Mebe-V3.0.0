# MEBE V3.0.0

## Vorwort und Historie
Mebe ist ein Motorsport-Meisterschaftsberechnungsprogramm. Ein Tool, um fiktive Motorsportmeisterschaften ausgeben zu lassen.  
Es ist komplett in Python 3 entwickelt worden.  
Mebe V1 ist der Vorläufer und ist als Konsolenedition voll funktionsfähig. Aufgrund der umständlichen und fehleranfälligen Bedienung in der Konsole, wurde Mebe V2 entwickelt, welches den Vorgänger ablöste und grundsätzlich denselben Funktionsumfang aufwies, wie die erste Version. Version 2 ergänzte dabei die Möglichkeit, Objekte zu bearbeiten.  
Aufgrund mehrerer Probleme bei Zugriffen und Speicherungen wurde die Plattform neu konzipiert und Mebe V3 entwickelt. Viele Funktionen wurden aus Mebe V2.0.0 (Stand 05.01.2026 - https://github.com/RaiusTalbor/Mebe-V2.0.0) aber übernommen.  
Alle Versionen, V1, V2 und V3, sind aber zueinander kompatibel. Die Datenbank, Rechenergebnisse und andere gespeicherte Daten können ohne Anpassung übernommen und migriert werden. Auch die Pfade mussten nicht angepasst werden.

## Grundfunktionen
Mebe kann Meisterschaften erstellen. Zu diesen Meisterschaften können Strecken und Fahrer hinzugefügt werden, die an dieser Meisterschaft teilnehmen.  
Wird eine Meisterschaft berechnet, so wird jedes einzelne Rennergebnis ermittelt. Dabei werden die Parameter jedes einzelnen Objekts gegeneinander nach bestimmten Kriterien aufgewogen und eine Rangfolge ermittelt. Zufallswerte ermöglichen eine unvorhersehbare Berechnung des Ergebnisses.  
Man kann eine Meisterschaft beliebig oft berechnen lassen.  
Eine Meisterschaft (nicht die Ergebnisse) oder auch jedes einzelne Objekt kann auch nachträglich bearbeitet werden. So ist es möglich, die Parameter über einen längeren Zeitraum anzupassen.

## Bedienung
### Hauptmenü
Im Hauptmenü hat man Zugang zu sämtlichen Grundfunktionen des Programms: Erstellen, Bearbeiten und Berechnen. Außerdem kann man hier die Dokumentation aufrufen.

### Erstellen
Klickt man auf Erstellen, so kann man eine Meisterschaft erstellen.

Man kann keine Objekte einzeln erstellen, da es gedacht ist, sie in einen Meisterschaftskontext zu bringen. Um einzelne Objekte hinzuzufügen, muss also entweder eine Meisterschaft erstellt oder bearbeitet werden.

Als erster Schritt zum Erstellen einer Meisterschaft wird man gebeten, den Namen einzugeben. Dabei wird geprüft, ob der Name bereits vergeben wurde, denn es dürfen keine Meisterschaften mit identischen Namen existieren.  
Mit Weiter kommt man ins nächste Fenster, wo man aufgefordert wird, Strecken zur Meisterschaft hinzuzufügen. Dazu klickt man auf der rechten Seite die gewünschte Strecke an, der Radiobutton bestätigt die Auswahl, und mit dem Knopf "Strecke auswählen" wird sie dem Rennkalender hinzugefügt.   
Die Reihenfolge, in der man die Strecken hinzufügt und wie sie dann auf der rechten Seite von oben nach unten erscheinen, in dieser Reihenfolge findet auch die Meisterschaft statt und wird auch so berechnet. Strecken können demnach auch mehrfach hinzugefügt werden. Wenn sie auf der rechten Seite über die Radiobuttons ausgewählt wurden, so ist es auch möglich, sie über den Knopf "Strecke entfernen" wieder aus dem Rennkalender zu löschen.

Ist die gewünschte Strecke nicht vorhanden, so kann man eine neue Strecke hinzufügen. Im neu erscheinenden Fenster wählt man einen Namen, legt den Streckentyp und die Schwierigkeit fest (genaue Bedeutung siehe später). Über den Button "Fahrer aus Datenbank hinzufügen" kann als Rekordhalter ein bereits erstellter Fahrer hinzugefügt werden. Dies minimiert die Schreibfehler. Man kann sich aber auch dazu entscheiden, einen anderen Fahrer hineinzuschreiben oder sogar leer zu lassen (da fordert Mebe aber eine Bestätigung). Wenn man sich umentschieden hat, kann man den Prozess abbrechen oder man speichert die Strecke ab. Sie erscheint dann alphabetisch sortiert in der linken Liste.

Im nächsten Fenster, welches man über Weiter erreicht, kann man über selbiges Prinzip die Fahrer auswählen. Allerdings spielt die Reihenfolge nun keine Rolle mehr. Außerdem kann ein Fahrer nicht mehrfach hinzugefügt werden. Ebenso wie bei den Strecken können Fahrer erstellt werden.

Auch hier muss ein einzigartiger Name vergeben werden. Bei der Angabe des Geburtsjahrs und des Jahres, in dem der Fahrer seine Karriere gestartet hatte, ist zu beachten, dass das Geburtsjahr mindestens 10 Jahre vor dem aktiven Karrierestart liegen muss. Selbiges gilt für die Angabe, seit wann das ausgewählte Fahrzeug gefahren wird.  
Auch ohne Auswahl des Fahrzeugs kann der Fahrer nicht gespeichert werden. Dabei muss das Fahrzeug zwingend in der Datenbank vorliegen. Über den Button "Fahrzeug auswählen" wird man in einen Dialog geleitet, bei dem man über die Radiobuttons und dem Knopf "Fahrzeug auswählen" ein Fahrzeug festlegen kann, oder man kann auch hier ein neues Fahrzeug erstellen. 

Die Erstellung des Fahrzeugs ist relativ übersichtlich und verhält sich analog wie bei den anderen Objekten.

Hat man die gewünschten Strecken, Fahrer und Fahrzeuge hinzugefügt, dann kann man die Meisterschaft speichern und sie wird in der Datenbank abgelegt.  
Möchte man zwischendurch den Prozess abbrechen, so gelangt man über den Button "Abbrechen" jederzeit ins Hauptmenü.

### Bearbeiten
Bearbeiten ist sehr ähnlich dem Erstellungsprozess.  
Im Zwischenmenü kann man zunächst auswählen, welche Art von Objekt man bearbeiten möchte. Entscheidet man sich für eine Art, wird man in ein weiteres Untermenü weitergeleitet, bei dem man entscheiden kann, welches konkrete Objekt man bearbeiten. Möchte. Auch hier erfolgt die Auswahl über Radiobuttons und dem Knopf "Auswählen".  
Nach der Auswahl sieht man dieselbe Oberfläche, wie man sie aus der "Erstellen"-Ansicht kennt, mit dem Unterschied, dass der Name nicht mehr editierbar ist. Dieser bleibt unveränderlich.

### Berechnen
Als Hauptaufgabe besitzt Mebe, Meisterschaften zu berechnen. Dies kann man über den dritten Menüpunkt "Berechnen" tun.  
Im Untermenü kann man sich dann noch für eine Meisterschaft entscheiden, mit "Meisterschaft auswählen" wird die Berechnung gestartet. Die Ausgabe erfolgt am unteren Rand des Bildschirms. Eine Berechnung kann dabei beliebig oft gestartet werden.  
Die Rennergebnisse werden als DAT-Datei gespeichert, werden aber derzeit noch nicht weiterverarbeitet oder sind zugänglich.  
Den Kern bildet der Berechnungsalgorithmus aus Mebe V1 (MebeAl1). Angepasst wurden entsprechende Ausgaben, Anzeigen und Zugriffe, die Logik aber ist unverändert. Dementsprechend ist auch die gesamte Datenbank, gespeicherte Daten und Ergebnisse mit Mebe V1 und Mebe V2 rückwärts als auch vorwärts kompatibel.

### Hilfe
Über den Hilfe-Button im Hauptmenü gelangt man zu dieser Dokumentation, welche sich im Standard-PDF-Viewer öffnet.

### Beenden
Mit diesen Button wird das Programm sicher beendet. Dabei werden auch alle Daten aus dem temporären Ordner entfernt.

## Bedeutung der Parameter der Objekte

Für die Berechnung sind vier Objekte wichtig: Die Meisterschaft, Fahrer, Fahrzeuge und Strecken.
Die Meisterschaft dient lediglich zur eindeutigen Identifizierung einer Zusammenstellung der übrigen drei Objekte.

Jedes Objekt beeinflusst das Ergebnis einer Meisterschaft. Objekte unterscheiden sich anhand von Parametern, die individuell festgelegt werden können.
Jedes Objekt hat einen eindeutigen Namen, über den das Objekt identifiziert wird.
Da jedes Objekt mit einer .dat-Datei repräsentiert wird, sind doppelte Namen ausgeschlossen.

Für detailiertere Einblicke: siehe mehr in der Berechnungsmechanik.

### Strecken

Strecken sind diejenigen Objekte, an denen ein Ergebnis gebunden wird.
Jedes Ergebnis wird pro Strecke erstellt. Ein Meisterschaftsergebnis besteht aus der Summe aller Streckenergebnisse.

Der Rennkalender einer Meisterschaft definiert dabei, welche Strecken in welcher Reihenfolge in der Meisterschaft absolviert werden.

Parameter:
- Rekordhalter: Sollte der Rekordhalter in einer Meisterschaft mit teilnehmen, so erhält dieser bei der Platzierung einen Vorteil.
- Streckentyp: Eine Strecke kann kurvig (Streckentyp 1), schnell (Streckentyp 3) oder ausgeglichen (Streckentyp 2) sein. Je nach Eigenschaften des gefahrenen Fahrzeugs des Fahrers erhält dieser einen Vorteil oder Nachteil.
- Schwierigkeit: Gibt an, wie anspruchsvoll eine Strecke im Vergleich zu den anderen (der Meisterschaft bspw.) ist. Dabei können Werte von 1 bis 10 angegeben werden, je höher die Zahl, desto schwieriger ist die Strecke. Die Schwierigkeit erhöht die Unfallwahrscheinlichkeit eines Fahrers in einem Rennen.

### Fahrer
Fahrer sind diejenigen Objekte, die im Ergebnis gemessen werden. Ein Fahrer kann Platzierungen erhalten und entsprechend Ergebnisse gewinnen.

Die Fahrerliste in einer Meisterschaft definiert dabei, welche Fahrer bei dieser Meisterschaft teilnehmen und Ergebniss erzielen können.

### Strecken

## Detaillierte Funktionsweise der Module

### Meisterschaft
Eine Meisterschaft hat zwei Listen. Die Liste "Rennkalender", wo alle Strecken in der richtigen Reihenfolge gespeichert sind und die Liste "Fahrerliste", wo alle Fahrer gespeichert sind, die an dieser Meisterschaft teilnehmen.  
Gespeichert wird eine Meisterschaft im Ordner Datenbank und beinhaltet zwei Werte, abgespeichert als Array. Als erster Wert ist der Dateiname zum Rennkalender und als zweiter Wert der Dateiname zur Fahrerliste gespeichert, denn beide Listen werden noch mal extra als Datei gespeichert.  
Mit anderen Worten besteht eine Meisterschaft aus drei Dateien:  
- NAME_MEISTERSCHAFT.dat --> bestehend aus [Rennkalenderpfad, Fahrerlistepfad]
- NAME_MEISTERSCHAFTStrecken.dat --> beinhaltet den Rennkalender, jede Strecke ebenfalls als Pfad
- NAME_MEISTERSCHAFTFahrer.dat --> beinhaltet die Fahrerliste, jeden Fahrer ebenfalls als Pfad abgespeichert

Das Objekt "Meisterschaft" wird dazu verwendet, um das Datenhandling um das Objekt möglichst einfach zu gestalten, was sich im Bezug auf die Erstellung bewährt hat. Entsprechend wurden auch verschiedene Methoden implementiert, um sämtliche Funktionen zu unterstützen.  

#### ladenName und ladenPfad
Wenn ein Objekt aufgefordert wird, gespeicherte Daten aus der Datenbank zu laden, so kann das Objekt dies mithilfe des Pfades oder mithilfe des übergebenen Namens tun. Mit der Angabe kann die Methode laden aufgerufen werden. 

#### erstellen
Das Objekt kann all seine eigenen Parameter festlegen, wenn es den eigenen Namen, den Rennkalender und die Fahrerliste übergeben bekommt. Dadurch werden sämtliche notwendigen Pfade gebaut, die das Objekt benötigt, um die Fahrerliste und den Rennkalender anschließend zu speichern.

#### getRennkalenderNamen
Manchmal ist es notwendig, den Rennkalender zu laden und dabei nur die Streckennamen herauszufiltern. Diese Methode gibt sämtliche Strecken in der richtigen Reihenfolge zurück, aber nicht als Pfad, wie es abgespeichert ist, sondern nur den Streckennamen.

#### getFahrerNamen
Analog wie bei Rennkalendern, nur für Fahrer.

#### setRennkalenderNamen
Mit Angabe aller Fahrer kann das Objekt Meisterschaft sich den Rennkalender selbst so zusammenbauen, wie es für die Abspeicherung anschließend benötigt wird.

#### setfahrerlisteName
Analog wie bei Rennkalendern, nur für Fahrer.

#### setPfade
Für eine erfolgreiche Speicherung hat die Meisterschaft die Pfade aller Dateien als Attribute. Da sich alle Dateinamen vom Namen der Meisterschaft ableiten lassen, wurde diese Methode implementiert, die genau das tut.

#### speichern
Speichert alle drei Dateien ab. Im Anschluss wird geprüft, ob die Meisterschaft gespeichert wurde und man kommt eine entsprechende Meldung zurück.

#### laden
Lädt die Meisterschaft anhand seines Namens. Zuerst werden alle drei Pfade ermittelt und danach alle drei Dateien eingelesen, die dann als Attributwerte im Objekt gespeichert werden und zur Verfügung stehen.