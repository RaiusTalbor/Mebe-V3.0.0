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

## Detaillierte Funktionsweise der Module