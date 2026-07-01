# MEBE V3.0.0

# Vorwort und Historie
Mebe ist ein Motorsport-Meisterschaftsberechnungsprogramm. Ein Tool, um fiktive Motorsportmeisterschaften ausgeben zu lassen.  
Es ist komplett in Python 3 entwickelt worden.  
Mebe V1 ist der Vorläufer und ist als Konsolenedition voll funktionsfähig. Aufgrund der umständlichen und fehleranfälligen Bedienung in der Konsole, wurde Mebe V2 entwickelt, welches den Vorgänger ablöste und grundsätzlich denselben Funktionsumfang aufwies, wie die erste Version. Version 2 ergänzte dabei die Möglichkeit, Objekte zu bearbeiten.  
Aufgrund mehrerer Probleme bei Zugriffen und Speicherungen wurde die Plattform neu konzipiert und Mebe V3 entwickelt. Viele Funktionen wurden aus Mebe V2.0.0 (Stand 05.01.2026 - https://github.com/RaiusTalbor/Mebe-V2.0.0) aber übernommen.  
Alle Versionen, V1, V2 und V3, sind aber zueinander kompatibel. Die Datenbank, Rechenergebnisse und andere gespeicherte Daten können ohne Anpassung übernommen und migriert werden. Auch die Pfade mussten nicht angepasst werden.

# Grundfunktionen
Mebe kann Meisterschaften erstellen. Zu diesen Meisterschaften können Strecken und Fahrer hinzugefügt werden, die an dieser Meisterschaft teilnehmen.  
Wird eine Meisterschaft berechnet, so wird jedes einzelne Rennergebnis ermittelt. Dabei werden die Parameter jedes einzelnen Objekts gegeneinander nach bestimmten Kriterien aufgewogen und eine Rangfolge ermittelt. Zufallswerte ermöglichen eine unvorhersehbare Berechnung des Ergebnisses.  
Man kann eine Meisterschaft beliebig oft berechnen lassen.  
Eine Meisterschaft (nicht die Ergebnisse) oder auch jedes einzelne Objekt kann auch nachträglich bearbeitet werden. So ist es möglich, die Parameter über einen längeren Zeitraum anzupassen.

# Bedienung
## Hauptmenü
Im Hauptmenü hat man Zugang zu sämtlichen Grundfunktionen des Programms: Erstellen, Bearbeiten und Berechnen. Außerdem kann man hier die Dokumentation aufrufen.

## Erstellen
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

## Bearbeiten
Bearbeiten ist sehr ähnlich dem Erstellungsprozess.  
Im Zwischenmenü kann man zunächst auswählen, welche Art von Objekt man bearbeiten möchte. Entscheidet man sich für eine Art, wird man in ein weiteres Untermenü weitergeleitet, bei dem man entscheiden kann, welches konkrete Objekt man bearbeiten. Möchte. Auch hier erfolgt die Auswahl über Radiobuttons und dem Knopf "Auswählen".  
Nach der Auswahl sieht man dieselbe Oberfläche, wie man sie aus der "Erstellen"-Ansicht kennt, mit dem Unterschied, dass der Name nicht mehr editierbar ist. Dieser bleibt unveränderlich.

## Berechnen
Als Hauptaufgabe besitzt Mebe, Meisterschaften zu berechnen. Dies kann man über den dritten Menüpunkt "Berechnen" tun.  
Im Untermenü kann man sich dann noch für eine Meisterschaft entscheiden, mit "Meisterschaft auswählen" wird die Berechnung gestartet. Die Ausgabe erfolgt am unteren Rand des Bildschirms. Eine Berechnung kann dabei beliebig oft gestartet werden.  
Die Rennergebnisse werden als DAT-Datei gespeichert, werden aber derzeit noch nicht weiterverarbeitet oder sind zugänglich.  
Den Kern bildet der Berechnungsalgorithmus aus Mebe V1 (MebeAl1). Angepasst wurden entsprechende Ausgaben, Anzeigen und Zugriffe, die Logik aber ist unverändert. Dementsprechend ist auch die gesamte Datenbank, gespeicherte Daten und Ergebnisse mit Mebe V1 und Mebe V2 rückwärts als auch vorwärts kompatibel.

## Hilfe
Über den Hilfe-Button im Hauptmenü gelangt man zu dieser Dokumentation, welche sich im Standard-PDF-Viewer öffnet.

## Beenden
Mit diesen Button wird das Programm sicher beendet. Dabei werden auch alle Daten aus dem temporären Ordner entfernt.

# Bedeutung der Parameter der Objekte

Für die Berechnung sind vier Objekte wichtig: Die Meisterschaft, Fahrer, Fahrzeuge und Strecken.
Die Meisterschaft dient lediglich zur eindeutigen Identifizierung einer Zusammenstellung der übrigen drei Objekte.

Jedes Objekt beeinflusst das Ergebnis einer Meisterschaft. Objekte unterscheiden sich anhand von Parametern, die individuell festgelegt werden können.
Jedes Objekt hat einen eindeutigen Namen, über den das Objekt identifiziert wird.
Da jedes Objekt mit einer .dat-Datei repräsentiert wird, sind doppelte Namen ausgeschlossen.

Für detailiertere Einblicke: siehe mehr in der Berechnungsmechanik.

## Strecken
Strecken sind diejenigen Objekte, an denen ein Ergebnis gebunden wird.
Jedes Ergebnis wird pro Strecke erstellt. Ein Meisterschaftsergebnis besteht aus der Summe aller Streckenergebnisse.

Der Rennkalender einer Meisterschaft definiert dabei, welche Strecken in welcher Reihenfolge in der Meisterschaft absolviert werden.

Parameter:
- Rekordhalter: Sollte der Rekordhalter in einer Meisterschaft mit teilnehmen, so erhält dieser bei der Platzierung einen Vorteil.
- Streckentyp: Eine Strecke kann kurvig (Streckentyp 1), schnell (Streckentyp 3) oder ausgeglichen (Streckentyp 2) sein. Je nach Eigenschaften des gefahrenen Fahrzeugs des Fahrers erhält dieser einen Vorteil oder Nachteil. Passt außerdem die Vorliebe des Fahrers zum Streckentyp, so verbessert sich das Ergebnis.
- Schwierigkeit: Gibt an, wie anspruchsvoll eine Strecke im Vergleich zu den anderen (der Meisterschaft bspw.) ist. Dabei können Werte von 1 bis 10 angegeben werden, je höher die Zahl, desto schwieriger ist die Strecke. Die Schwierigkeit erhöht die Unfallwahrscheinlichkeit eines Fahrers in einem Rennen.

## Fahrer
Fahrer sind diejenigen Objekte, die im Ergebnis gemessen werden. Ein Fahrer kann Platzierungen erhalten und entsprechend Ergebnisse gewinnen.

Die Fahrerliste in einer Meisterschaft definiert dabei, welche Fahrer bei dieser Meisterschaft teilnehmen und Ergebnis erzielen können.

Parameter:
- Geburtsjahr: Aus dem Alter wird eine Grunderfahrung berechnet, die sich positiv auf das Ergebnis auswirkt.
- Erstes Rennen: Die Fahrerfahrung ist ein Teil der Berechnung der Grunderfahrung.
- Aggressivität: Wert von 1-10. Gibt an, wie aggressiv im Vergleich zu anderen ein Pilot fährt. Je höher die Aggressivität, desto wahrscheinlicher ist ein Unfall oder eine Strafzeit.
- Geschicklichkeit: Wert von 1-10. Gibt an, wie souverän ein Fahrer im Vergleich zu anderen in besonderen Situationen agieren kann. Je höher die Geschicklichkeit, desto geringer ist die Wahrscheinlichkeit für Dreher.
- Grundkönnen: Wert von 1-100. Gibt an, wie talentiert ein Fahrer im Vergleich zu anderen ist. Das Grundkönnen hat den größten direkten Einfluss auf das Endergebnis. Je höher das Grundkönnen, desto besser das Ergebnis.
- Vorliebe: Die Vorliebe gibt an, ob ein Fahrer eher kurvige oder schnelle Strecken beherrscht. Es gibt einen Vorteil, wenn die Vorliebe mit dem Streckentyp übereinstimmt.
- Durchschnittliche Platzierung: Die durchschnittliche Platzierung gibt an, welchen Rang ein Fahrer statistisch gesehen erreicht. In der Berechnung hat dieser Wert derzeit keinen Einfluss.
- Fahrzeug: Jedem Fahrer wird exakt ein Fahrzeug zugeordnet. Dieses Fahrzeug hat ebenso Einfluss auf das Ergebnis. Fährt ein Fahrer bei mehreren Meisterschaften mit, so ist es ggf. notwendig, mehrere Fahrerprofile zu erstellen.
- Fahrzeug wird gefahren seit: Gibt an, wie lang ein Fahrer bereits das Fahrzeug fährt und spiegelt die Erfahrung zur Funktion und Beherrschung des Fahrzeugs wider. Je länger ein Pilot ein Fahrzeug bereits gefahren ist, desto besser ist das Ergebnis.

## Fahrzeug
Fahrzeuge sind diejenigen Objekte, mit deren Einfluss Fahrer Ergebnisse erzielen.

Jedem Fahrer ist exakt einem Fahrzeug zugeordnet.

Parameter:
- Leistung: Wert von 1-3. Gibt an, wie viel Leistung das Fahrzeug im Vergleich zu anderen hat.
- Wendigkeit: Wert von 1-3. Gibt an, wie wendig ein Fahrzug im Vergleich zu anderen ist.

Auf schnellen Strecken gibt es einen Wagenvorteil für den Fahrer, wenn das Fahrzeug schnell und nicht wendig ist. Es gibt aber einen Nachteil, wenn es nicht leistungsstark und wendig ist.
Auf kurvigen Strecken gibt es einen Vorteil, wenn das Fahrzeug wendig und nicht schnell ist. Es gibt einen Nachteil, wenn es leistungsstark und nicht wendig ist.
Ausgeglichene Fahrzeuge haben weder Vor- noch Nachteile.

In der Regel sind Leistung und Wendigkeit gegensätzlich.
Andererseits gibt es auch keine Mechanik, die dies überprüft.

# Detaillierte Funktionsweise der Objekte

## Meisterschaft
Eine Meisterschaft hat zwei Listen. Die Liste "Rennkalender", wo alle Strecken in der richtigen Reihenfolge gespeichert sind und die Liste "Fahrerliste", wo alle Fahrer gespeichert sind, die an dieser Meisterschaft teilnehmen.  
Gespeichert wird eine Meisterschaft im Ordner Datenbank und beinhaltet zwei Werte, abgespeichert als Array. Als erster Wert ist der Dateiname zum Rennkalender und als zweiter Wert der Dateiname zur Fahrerliste gespeichert, denn beide Listen werden noch mal extra als Datei im Ordner Datenbank gespeichert.  
Mit anderen Worten besteht eine Meisterschaft aus drei Dateien:  
- NAME_MEISTERSCHAFT.dat --> bestehend aus [Rennkalenderpfad, Fahrerlistepfad]
- NAME_MEISTERSCHAFTStrecken.dat --> beinhaltet den Rennkalender, jede Strecke ebenfalls als Pfad
- NAME_MEISTERSCHAFTFahrer.dat --> beinhaltet die Fahrerliste, jeden Fahrer ebenfalls als Pfad abgespeichert

Das Objekt "Meisterschaft" wird dazu verwendet, um das Datenhandling um das Objekt möglichst einfach zu gestalten, was sich im Bezug auf die Erstellung bewährt hat. Entsprechend wurden auch verschiedene Methoden implementiert, um sämtliche Funktionen zu unterstützen.  

### ladenName und ladenPfad
Wenn ein Objekt aufgefordert wird, gespeicherte Daten aus der Datenbank zu laden, so kann das Objekt dies mithilfe des Pfades oder mithilfe des übergebenen Namens tun. Mit der Angabe kann die Methode laden aufgerufen werden. 

### erstellen
Das Objekt kann all seine eigenen Parameter festlegen, wenn es den eigenen Namen, den Rennkalender und die Fahrerliste übergeben bekommt. Dadurch werden sämtliche notwendigen Pfade gebaut, die das Objekt benötigt, um die Fahrerliste und den Rennkalender anschließend zu speichern.

### getRennkalenderNamen
Manchmal ist es notwendig, den Rennkalender zu laden und dabei nur die Streckennamen herauszufiltern. Diese Methode gibt sämtliche Strecken in der richtigen Reihenfolge zurück, aber nicht als Pfad, wie es abgespeichert ist, sondern nur den Streckennamen.

### getFahrerNamen
Analog wie bei Rennkalendern, nur für Fahrer.

### setRennkalenderNamen
Mit Angabe aller Fahrer kann das Objekt Meisterschaft sich den Rennkalender selbst so zusammenbauen, wie es für die Abspeicherung anschließend benötigt wird.

### setfahrerlisteName
Analog wie bei Rennkalendern, nur für Fahrer.

### setPfade
Für eine erfolgreiche Speicherung hat die Meisterschaft die Pfade aller Dateien als Attribute. Da sich alle Dateinamen vom Namen der Meisterschaft ableiten lassen, wurde diese Methode implementiert, die genau das tut.

### speichern
Speichert alle drei Dateien ab. Im Anschluss wird geprüft, ob die Meisterschaft gespeichert wurde und man kommt eine entsprechende Meldung zurück.

### laden
Lädt die Meisterschaft anhand seines Namens. Zuerst werden alle drei Pfade ermittelt und danach alle drei Dateien eingelesen, die dann als Attributwerte im Objekt gespeichert werden und zur Verfügung stehen.

## Fahrer
Das Objekt "Fahrer" wird dazu verwendet, um das Datenhandling um das Objekt möglichst einfach zu gestalten, was sich im Bezug auf die Erstellung bewährt hat. Entsprechend wurden auch verschiedene Methoden implementiert, um sämtliche Funktionen zu unterstützen. 

Speicherwerte: gebjahr, erstesrennen, aggressivität, geschicklichkeit, grundkönnen, vorliebe, durchschnittlicheplatzierung, fahrzeug, seitWannFahrzeug

### ladenName und ladenPfad
Wenn ein Objekt aufgefordert wird, gespeicherte Daten aus der Datenbank zu laden, so kann das Objekt dies mithilfe des Pfades oder mithilfe des übergebenen Namens tun. Mit der Angabe kann die Methode laden aufgerufen werden. 

### erstellen
Mit erstellen() und der Übergabe aller Parameter wird ein Objekt Fahrer instanziiert.
Parameter: name, gebjahr, erstesrennen, aggressivität, geschicklichkeit, grundkönnen, vorliebe, durchschnittlicheplatzierung, fahrzeug, seitWannFahrzeug

### setPfad
Setzt seinen eigenen Pfad.
Fahrer sind unter /Datenbank/Fahrer gespeichert.

### setPfadFahrzeug
Setzt den Pfad des Fahrzeugs (s. da).

### speichern
Speichert das Objekt "Fahrer" ab. Anschließend wird geprüft, ob die Speicherung erfolgreich war und gibt eine entsprechende Meldung zurück.

### laden
Lädt einen Fahrer aus einer Datei und überträgt die gespeicherten Daten ins Objekt.
Es ist zwingend erforderlich, dass ein Fahrer bereits einen Namen hat. Dies ist zum Bearbeiten dieser Datei gedacht.


## Strecke
Das Objekt "Strecke" wird dazu verwendet, um das Datenhandling um das Objekt möglichst einfach zu gestalten, was sich im Bezug auf die Erstellung bewährt hat. Entsprechend wurden auch verschiedene Methoden implementiert, um sämtliche Funktionen zu unterstützen. 

Speicherwerte: rekordhalter, streckentyp, schwierigkeit

### ladenName und ladenPfad
Wenn ein Objekt aufgefordert wird, gespeicherte Daten aus der Datenbank zu laden, so kann das Objekt dies mithilfe des Pfades oder mithilfe des übergebenen Namens tun. Mit der Angabe kann die Methode laden aufgerufen werden. 

### erstellen
Mit erstellen() und der Übergabe aller Parameter wird ein Objekt Strecke instanziiert.
Parameter: name, rekordhalter, streckentyp, schwierigkeit

### setPfad
Setzt seinen eigenen Pfad.
Strecken sind unter /Datenbank/Strecken gespeichert.

### setPfadRekordhalter
Setzt den Pfad des Rekordhalters, ein Fahrer (s. da).

### speichern
Speichert das Objekt "Strecke" ab. Anschließend wird geprüft, ob die Speicherung erfolgreich war und gibt eine entsprechende Meldung zurück.

### laden
Lädt eine Strecke aus einer Datei und überträgt die gespeicherten Daten ins Objekt.
Es ist zwingend erforderlich, dass eine Strecke bereits einen Namen hat. Dies ist zum Bearbeiten dieser Datei gedacht.

## Fahrzeug
Das Objekt "Fahrzeug" wird dazu verwendet, um das Datenhandling um das Objekt möglichst einfach zu gestalten, was sich im Bezug auf die Erstellung bewährt hat. Entsprechend wurden auch verschiedene Methoden implementiert, um sämtliche Funktionen zu unterstützen. 

Speicherwerte: leistung, wendigkeit

### ladenName und ladenPfad
Wenn ein Objekt aufgefordert wird, gespeicherte Daten aus der Datenbank zu laden, so kann das Objekt dies mithilfe des Pfades oder mithilfe des übergebenen Namens tun. Mit der Angabe kann die Methode laden aufgerufen werden. 

### erstellen
Mit erstellen() und der Übergabe aller Parameter wird ein Objekt Fahrzeug instanziiert.
Parameter: name, rekordhalter, leistung, wendigkeit

### setPfad
Setzt seinen eigenen Pfad.
Fahrzeuge sind unter /Datenbank/Fahrzeuge gespeichert.

### speichern
Speichert das Objekt "Fahrzeug" ab. Anschließend wird geprüft, ob die Speicherung erfolgreich war und gibt eine entsprechende Meldung zurück.

### laden
Lädt ein Fahrzeug aus einer Datei und überträgt die gespeicherten Daten ins Objekt.
Es ist zwingend erforderlich, dass ein Fahrzeug bereits einen Namen hat. Dies ist zum Bearbeiten dieser Datei gedacht.

# Datenspeicherung

Mebe V3 speichert Daten permanent. Dafür werden Binär-Dateien mit der Dateiendung ".dat" im Ordner "Datenbanken" angelegt.
Zwischengespeicherte Daten, die während der Berechnung benötigt werden, werden im Ordner "temporäre Dateien" gespeichert und nach Programmende, wenn das Programm sauber verlassen wird, gelöscht. Auch das sind binärer DAT-Dateien.

Im Ordner "Datenbank" befinden sich alle Meisterschaftsdateien (beschrieben zum Objekt "Meisterschaft") und vier weitere Ordner: "Fahrer", "Fahrzeuge", "Strecken" und "Meisterschaften".
Die ersten drei Ordner beinhalten alle gespeicherten, gleichnamigen Objekte (bspw. Fahrer XYZ im Ordner Fahrer). Alle gespeicherten Parameter des Objekts sind dabei als Array in der DAT-Datei abgespeichert. Der Name der Datei ohne Dateiendung entspricht dabei den Namen des Objekts.

Eine Ausnahme bildet der Ordner "Meisterschaften". In diesem Ordner sind alle Ergebnisse gespeichert, die Mebe V3 jemals berechnet hatte, ebenfalls als DAT-Datei. Damit war geplant, die Rennergebnisse zurückzuverfolgen und nachvollziehbar zu machen, auch wenn die Berechnung selbst schon lang zurückliegt.
Derzeit werden die Ergebnisse allerdings nicht weiterverwendet und nur abgespeichert. 

Meisterschaftsgesamtergebnisse haben dabei folgende Namenskonvention: [Meisterschaftsname][Nummer des Durchlaufs]Meisterschaftsergebnisse.dat
Einzelne Streckenergebnisse erkennt man so: [Meisterschaftsname][Nummer des Durchlaufs]Rennergebnisse[Name der Strecke].dat

## Modul Daten - Objekt- und Datenhandling
Das Modul "Daten.py" ist eine ausgelagerte Konsolidierung von Methoden, die die Handhabung von Daten vereinfachen soll.
Vorrangig ist das Modul dazu zuständig, dass die Daten gelesen und geschrieben werden können und dass Informationen über Objekte aus der Datenbank herausgeholt werden können.

### lesen
In einem Stream werden die binären Daten gelesen und direkt zurückgegeben.

### schreiben
Als Parameter wird der Pfad übergeben und die Daten, die dann als binäre Daten gespeichert werden.
Es wird nicht automatisch die Dateiendung .dat angefügt.

### listeMeisterschaftspfade
Diese Methode gibt alle Pfade zurück, die auf eine Meisterschaft zeigen.

Funktionsweise:
Zuallererst werden alle Objekte im Datenbank-Ordner in eine Liste zwischengespeichert.
Für jedes dieses Element wird dann eine Prüfung gemacht. Es handelt sich um eine Meisterschaftsdatei, wenn...
- Wenn es nicht mit "Fahrer.dat" endet (Fahrerliste)
- Wenn es nicht mit "Strecken.dat" endet (Rennkalender)
- Wenn es auf ".dat" endet (andere Ordner)
Alle Objekte des Ordners Datenbank, die durch den Filter gekommen sind, sind Meisterschaftsdateien. Diese werden mit dem Präfix "Datenbank/" erweitert, wodurch dann der vollständige relative Pfad fertig erstellt ist.

Dieser wird dann in einer weiteren Liste zwischengespeichert. Ist die Liste vollständig, dann wird sie wieder zurück ans aufrufende Modul übergeben.

### listeMeisterschaftsnamen
Diese Methode liefert alle existierenden Meisterschaften als Liste.

Funktionsweise:
Sie nutzt listeMeisterschaftspfade, um die Meisterschaften herauszunehmen. In einer weiteren Schleife wird jedem Element der Präfix und die Dateiendung entfernt, sodass nur noch der reine Meisterschaftsname übrig bleibt.

### listePfade
Diese Methode dient dazu, eine Liste mit Pfaden von existierenden Objekten (Fahrer, Strecken oder Fahrzeuge) zu erstellen.
Meisterschaften müssen anders wiedergegeben werden, deshalb müssen existierende Meisterschaften anders ermittelt werden.

Als Übergabeparameter wird der Objekttyp erfordert. Erlaubt sind dabei "Strecken", "Fahrer" und "Fahrzeuge", was den Ordnernamen im Ordner "Datenbank" entspricht.

Funktionsweise:
Zuallererst wird der Pfad ermittelt, aus dem die Objekte herausgelesen werden sollen. Dazu wird der übergebene Parameter mit dem Präfix "Datenbank" kombiniert, sodass der korrekte relative Pfad zwischengespeichert werden kann.

Innerhalb dieses Pfades werden dann alle Objekte in einer Liste gespeichert.
Für jedes Objekt dieser Liste wird dann der gesamte korrekte relative Pfad zusammengebaut, indem der Ordnerpfad von eben mit einem "/" versehen wird und dann der Name der Datei ergänzt wird.

Zurückgegeben wird die Liste mit allen relativen Pfaden der angefragten Objekte.

### listeNamen
Diese Methode dient dazu, eine Liste von existierenden Objekten (Fahrer, Strecken oder Fahrzeuge) zu erstellen.
Meisterschaften müssen anders wiedergegeben werden, deshalb müssen existierende Meisterschaften anders ermittelt werden.

Als Übergabeparameter wird der Objekttyp erfordert. Erlaubt sind dabei "Strecken", "Fahrer" und "Fahrzeuge", was den Ordnernamen im Ordner "Datenbank" entspricht.

Funktionsweise:
Zuallererst wird der Pfad ermittelt, aus dem die Objekte herausgelesen werden sollen. Dazu wird der übergebene Parameter mit dem Präfix "Datenbank" kombiniert, sodass der korrekte relative Pfad zwischengespeichert werden kann.

Innerhalb dieses Pfades werden dann alle Objekte in einer Liste gespeichert.
Für jedes Objekt dieser Liste wird dann die Dateiendung entfernt, sodass nur noch der Name des Objekts über bleibt.

Zurückgegeben wird die Liste mit allen Namen der angefragten Objekte.

# Technische Betrachtung Erstellen
Ein Erstellungsprozess ist zwingend notwendig, um Daten berechnen zu können. Dieser ist allerdings auch sehr komplex.

In diesem Kapitel soll chronologisch aufgeführt werden, welchen Ablauf das Modul durchläuft.

## 1. Erstellen()

Vom Hauptmenü aus, wenn man "Erstellen" auswählt, wird diese Methode ausgeführt.

Es müssen zwei Variablen gesetzt werden:
- Die Variable "varweiter" muss initialisiert werden: 0. Das sagt aus, dass der Prozess beginnt.
- Die Variable "bearbeitungsmodus" mit dem Wert 0 zeigt an, dass sich das Programm aktuell eine Meisterschaft erstellt und nicht bearbeitet.

Im nächsten Schritt wird ein Objekt "Meisterschaft" initialisiert.
Das Objekt hilft, die Daten zu händeln.

Nachdem der Bildtitel gesetzt wurde, wird weiter() ausgeführt.

## 1. MeisterschaftBearbeiten

Meisterschaften können aber auch bearbeitet werden. In diesem Fall unterscheidet sich die Methode von erstellen() nur sofern, dass neben der Objektinstanziierung das Objekt noch geladen wird.
Außerdem werden die Variablen "bearbeitungsmodus" und "varweiter" auf 1 gesetzt, um zu kennzeichnen, dass es ein Berbeitungsprozess ist.
Was varweiter macht, ist im nächsten Kapitel ersichtlich.

## 2. sammeln() in weiter()

Als allererstes in weiter() wird sammeln() ausgeführt. sammeln() dient dazu, die eingegebenen Informationen aufzugreifen und zwischenzuspeichern, sodass sie weiter genutzt werden können.

Vor jeder Aktion wird die aktuelle Statusmeldung gelöscht, da es sein kann, dass Infomeldungen erscheinen - die dann nicht weg gehen.

Je nachdem, welchen Wert varweiter hat, werden andere Informationen abgerufen.

### Keine Aktion: varweiter == 0
Wenn die Meisterschaft erstellt wird, so gibt es im allerersten Durchlauf keine Benutzerinteraktion, weshalb der Fall varweiter == 0 nicht näher definiert ist und keine Aktion ausführt.

### Meisterschaftsdaten sammeln: varweiter == 1
Es wird direkt geprüft, ob der Bearbeitungsmodus (1) an ist. Wenn nicht (0), dann wird eine Meisterschaft erstellt. Wenn nicht, dann werden die meisten Aktionen übersprungen und dem Objekt Meisterschaft, was im ersten Schritt erstellt worden ist, die Werte zugeordnet, die in der Datei gespeichert sind.

Wird eine Meisterschaft erstellt, sind noch weitere Schritte notwendig.
1. Es wird der Name aus dem Eingabefeld herausgenommen. Daraufhin wird er mit dem Jahr, welches ebenso eingegeben werden soll, kombiniert. Daraufhin wird dem Objekt Meisterschaft der Wert zugeordnet und es erstellt seine Pfade.
2. Anschließend wird geprüft, ob der Name der Meisterschaft leer ist. Wenn ja, wird eine Infomeldung gesendet, varweiter auf 0 gesetzt, damit das ganze Modul wieder von vorne beginnt und dann wird return ausgeführt, damit die Methode an der Stelle abbricht.
3. Sollte die erste Prüfung erfolgreich im Sinne des Fortschritts sein, dann wird die Liste aller existierenden Meisterschaften gelesen. Befindet sich der eingegebene Name bereits in der Liste der existierenden Meisterschaften, so wird auch hier eine Meldung gesendet und der Prozess abgebrochen. Andernfalls könnte es sein, dass die bestehende Meisterschaft überschrieben wird.
4. Erst, wenn die Überprüfung des Namens erfolgreich wird, werden zwei Arrays initialisiert, die die Fahrerliste und den Rennkalender lokal zwischenspeichern. Sie sind an der Stelle, um weitere globale Variablen zu vermeiden. An dieser Stelle geht das Programm aber mitunter als Erstes durch.

### Strecken hinzufügen: varweiter == 2
Zuallererst wird die Zwei-Fenster-Anzeige beendet. Durch die Funktionsweise der anderen Module muss es an der Stelle erfolgen, da sonst eine unsaubere Anzeige erscheint.
Als Nächstes wird der Rennkalender der Meisterschaft zugewiesen.

### Fahrer hinzufügen: varweiter == 3
Zuallererst wird die Zwei-Fenster-Anzeige beendet. Durch die Funktionsweise der anderen Module muss es an der Stelle erfolgen, da sonst eine unsaubere Anzeige erscheint.
Als Letztes wird die Fahrerliste der Meisterschaft zugewiesen.

### varweiter > 3 || varweiter < 0
Diese Fälle werden abgefangen und es passiert nichts, weil es nicht definiert ist.

## weiter()
Nach sammeln() springt das Programm zurück in weiter().
Weiter wird auch dann aufgerufen, wenn der Button "Weiter" bzw. "Meisterschaft erstellen" aufgerufen wird.

Dabei wird der Frameinhalt geleert und die Buttons zurückgesetzt, bevor es wieder befüllt wird.
Danach wird varweiter um eins erhöht - bevor etwas anderes passiert ist. So ist es einfacher, die verschiedenen Programmzustände nachzuvollziehen.

Als nächstes wird der Weiter-Knopf noch angepasst. Ist varweiter ungleich drei, so wird der Knopf "Weiter" genannt, ansonsten "Meisterschaft erstellen".
Das soll für weniger Verwirrung im letzten Bildschirm sorgen.

Erst jetzt wird unterschieden, im welchen Zustand sich das Programm jetzt befinden soll. Nach diesem Aufruf ist weiter() beendet.

### Meisterschaftsnamen definieren: varweiter == 1
Der Meisterschaftsname wird festgelegt.
Es wird meisterschaftdefinieren() aufgerufen.

### Rennkalender einfügen: varweiter == 2
Der Rennkalender wird bearbeitet.
Es wird rennkalendereinfügen() aufgerufen.

### Fahrerliste einfügen: varweiter == 3
Die Fahrerliste wird bearbeitet.
Es wird fahrereinfügen() aufgerufen.

### varweiter == 4
Nachdem im letzten Bildschirm auf "Meisterschaft erstellen" geklickt wurde (der Weiter-Knopf wurde in diesem Bildschirm modifiziert!), dann wird das Hauptmenü aufgerufen und das Objekt Meisterschaft, welches über den gesamten Prozess hinweg existierte, gespeichert.

## meisterschaftdefinieren()
meisterschaftdefinieren() wird in weiter() aufgerufen.
Das Fenster wird mit einem Label, darunter einem Eingabefenster, noch einem Label und noch einem Fenster ausgemschmückt.
Im zweiten Eingabefenster, wo das Jahr eingegeben werden soll, wird das aktuelle Jahr ermittelt und als Standardwert dort eingetragen.
Danach ist diese Methode vorbei und das Programm wartet auf eine Aktion des Nutzenden.

## rennkalendereinfügen() und fahrereinfügen()
Beide Methoden sind sich fast identisch.

Zuerst wird der Anzeigemodus umgestellt, auf die Zwei-Fenster-Anzeige. Danach werden alle nötigen Buttons eingefügt, einer der ein neues Element erstellen kann, einer, der ein Element auswählt und einer, der ein Element entfernen kann.

Anschließend wird über Daten.py die jeweilige Liste geladen, die benötigt wird. Entweder die Liste aller existierenden Fahrer oder die Liste aller existierenden Strecken.

Danach wird im linken Fenster in einer For-Schleife für jedes Element ein Radiobutton erstellt. Als Text bekommt es den Namen des Elements, als Wert ebenso.
Anschließend wird das allererste Element ausgewählt.

Wenn die Fahrerliste bzw. Rennkalenderliste nicht leer ist, so wird der Vorgang für das rechte Fenster wiederholt, allerdings mit den Elementen aus der Fahrer- bzw. Rennkalenderliste und als Wert nur die Indexnummer in der Liste. So kann eindeutig sichergestellt werden, dass der richtige Wert gewählt wird, da Strecken auch doppelt vorkommen können. Bei der Auswahlseite (links) ist es nicht notwendig, da jedes Element eindeutig sein muss.

Anders als in rennkalendereinfügen() muss in fahrereinfügen() abschließend aktualisiereFenster() ausgeführt werden, weil sonst falsche Radiobuttons angezeigt werden. Der Grund ist aber ungeklärt.

Je nachdem, welcher Button gedrückt wird, geht das Programm weiter

## erstelleElement()
Wird der Knopf "Fahrer erstellen" oder "Strecke erstellen" gedrückt, so wird die Funktion erstelleElement() aufgerufen. Je nach Wert von varweiter kann die Methode herausfinden, ob gerade ein Fahrer oder eine Strecke erstellt werden muss. Entsprechendes Modul wird anschließend aufgerufen. Wenn dieses Modul beendet wird, wird aktualisiereFenster() aufgerufen und erstelleElement terminiert.

## auswählen()
Wird der Knopf "auswählen" gedrückt, wird diese Funktion ausgeführt. Auch diese Methode kann über varweiter herausfinden, ob die Rennkalenderliste oder die Fahrerliste bearbeitet werden muss.
Entsprechend wird append() auf die jeweilige Liste ausgeführt und der Wert des gewählten Radiobuttons auf der linken Seite (Auswahl) zur Liste hinzugefügt.

Abschließend wird aktualisiereFenster() aufgerufen. 

## entfernen()
Wird der Knopf "Entfernen" gedrückt, wird diese Funktion ausgeführt. Auch diese Methode kann über varweiter herausfinden, ob die Rennkalenderliste oder die Fahrerliste bearbeitet werden muss.
Entsprechend wird pop() auf die jeweilige Liste ausgeführt und der Wert (der Index!) des gewählten Radiobuttons auf der rechten Seite (für Meisterschaft ausgewählt) von der Liste entfernt. Durch den Index ist nun jedes Element eindeutig.

Abschließend wird aktualisiereFenster() aufgerufen. 

## aktualisiereFenster()
Diese Methode hilft im Zwei-Fenster-Modus beide Listen zu aktualisieren, um die Radiobuttons mit den neuen bzw. gelöschten Elementen zu ergänzen.

Zuerst werden sowohl die linke als auch die rechte Anzeige zurückgesetzt (Forget).

Danach wird über varweiter herausgefunden, ob die Rennkalender- oder Fahrerliste bearbeitet werden soll.

Über listeNamen aus Daten.py wird die entsprechende Liste aller existierenden Elemente neu gesetzt. 

eihfb eslkufh  kesjhb fleshjb flkjesbs lkfjb lsk jh<fen lkjn ljkn s<lefjk<lö jkn n esmf . f  fe>>>

# Technische Betrachtung Bearbeiten

# Berechnungsmechanik (MebeAl1)

# Anzeige
(Programmstart, Prozess, Aufgaben und Aussehen)

# Hilfsmodul Daten

# Hilfsmodul Z-Hilfe-Leser (HiLe1)