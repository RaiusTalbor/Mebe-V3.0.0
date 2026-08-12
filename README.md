# MEBE V3.0.0

# 1. Vorwort und Historie
Mebe ist ein Motorsport-Meisterschaftsberechnungsprogramm. Ein Tool, um Ergebnisse von fiktiven Motorsportmeisterschaften ausgeben zu lassen.  
Es ist komplett in Python 3 entwickelt worden.  
Mebe V1 ist der Vorläufer und ist als Konsolenedition voll funktionsfähig. Aufgrund der umständlichen und fehleranfälligen Bedienung in der Konsole wurde Mebe V2 entwickelt, welches den Vorgänger ablöste und grundsätzlich denselben Funktionsumfang aufwies, wie die erste Version. Version 2 ergänzte dabei die Möglichkeit, Objekte zu bearbeiten.  
Aufgrund mehrerer Probleme bei Zugriffen und Speicherungen wurde die Plattform neu konzipiert und Mebe V3 entwickelt. Viele Funktionen wurden aus Mebe V2.0.0 (Stand 05.01.2026 - https://github.com/RaiusTalbor/Mebe-V2.0.0) aber übernommen.  
Alle Versionen, V1, V2 und V3, sind aber zueinander kompatibel. Die Datenbank, Rechenergebnisse und andere gespeicherte Daten können ohne Anpassung übernommen und migriert werden. Auch die Pfade mussten nicht angepasst werden.

# 2. Grundfunktionen
Mebe kann Meisterschaften erstellen. Zu diesen Meisterschaften können Strecken und Fahrer hinzugefügt werden, die an dieser Meisterschaft teilnehmen.  
Wird eine Meisterschaft berechnet, so wird jedes einzelne Rennergebnis ermittelt. Dabei werden die Parameter jedes einzelnen Objekts gegeneinander nach bestimmten Kriterien aufgewogen und eine Rangfolge ermittelt. Zufallswerte ermöglichen eine unvorhersehbare Berechnung des Ergebnisses.  
Man kann eine Meisterschaft beliebig oft berechnen lassen.  
Eine Meisterschaft (nicht die Ergebnisse) oder auch jedes einzelne Objekt kann auch nachträglich bearbeitet werden. So ist es möglich, die Parameter über einen längeren Zeitraum anzupassen.

# 3. Bedienung
## 3.1 Hauptmenü
Im Hauptmenü hat man Zugang zu sämtlichen Grundfunktionen des Programms: Erstellen, Bearbeiten und Berechnen. Außerdem kann man hier die Dokumentation aufrufen.

## 3.2 Erstellen
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

## 3.3 Bearbeiten
Bearbeiten ist sehr ähnlich dem Erstellungsprozess.  
Im Zwischenmenü kann man zunächst auswählen, welche Art von Objekt man bearbeiten möchte. Entscheidet man sich für eine Art, wird man in ein weiteres Untermenü weitergeleitet, bei dem man entscheiden kann, welches konkrete Objekt man bearbeiten. Möchte. Auch hier erfolgt die Auswahl über Radiobuttons und dem Knopf "Auswählen".  
Nach der Auswahl sieht man dieselbe Oberfläche, wie man sie aus der "Erstellen"-Ansicht kennt, mit dem Unterschied, dass der Name nicht mehr editierbar ist. Dieser bleibt unveränderlich.

## 3.4 Berechnen
Als Hauptaufgabe besitzt Mebe, Meisterschaften zu berechnen. Dies kann man über den dritten Menüpunkt "Berechnen" tun.  
Im Untermenü kann man sich dann noch für eine Meisterschaft entscheiden, mit "Meisterschaft auswählen" wird die Berechnung gestartet. Die Ausgabe erfolgt am unteren Rand des Bildschirms. Eine Berechnung kann dabei beliebig oft gestartet werden.  
Die Rennergebnisse werden als DAT-Datei gespeichert, werden aber derzeit noch nicht weiterverarbeitet oder sind zugänglich.  
Den Kern bildet der Berechnungsalgorithmus aus Mebe V1 (MebeAl1). Angepasst wurden entsprechende Ausgaben, Anzeigen und Zugriffe, die Logik aber ist unverändert. Dementsprechend ist auch die gesamte Datenbank, gespeicherte Daten und Ergebnisse mit Mebe V1 und Mebe V2 rückwärts als auch vorwärts kompatibel.

## 3.5 Hilfe
Über den Hilfe-Button im Hauptmenü gelangt man zu dieser Dokumentation, welche sich im Standard-PDF-Viewer öffnet.

## 3.6 Beenden
Mit diesen Button wird das Programm sicher beendet. Dabei werden auch alle Daten aus dem temporären Ordner entfernt.

# 4 Bedeutung der Parameter der Objekte

Für die Berechnung sind vier Objekte wichtig: Die Meisterschaft, Fahrer, Fahrzeuge und Strecken.
Die Meisterschaft dient lediglich zur eindeutigen Identifizierung einer Zusammenstellung der übrigen drei Objekte.

Jedes Objekt beeinflusst das Ergebnis einer Meisterschaft. Objekte unterscheiden sich anhand von Parametern, die individuell festgelegt werden können.
Jedes Objekt hat einen eindeutigen Namen, über den das Objekt identifiziert wird.
Da jedes Objekt mit einer .dat-Datei repräsentiert wird, sind doppelte Namen ausgeschlossen.

Für detailiertere Einblicke: siehe mehr in der Berechnungsmechanik.

## 4.1 Strecken
Strecken sind diejenigen Objekte, an denen ein Ergebnis gebunden wird.
Jedes Ergebnis wird pro Strecke erstellt. Ein Meisterschaftsergebnis besteht aus der Summe aller Streckenergebnisse.

Der Rennkalender einer Meisterschaft definiert dabei, welche Strecken in welcher Reihenfolge in der Meisterschaft absolviert werden.

Parameter:
- Rekordhalter: Sollte der Rekordhalter in einer Meisterschaft mit teilnehmen, so erhält dieser bei der Platzierung einen Vorteil.
- Streckentyp: Eine Strecke kann kurvig (Streckentyp 1), schnell (Streckentyp 3) oder ausgeglichen (Streckentyp 2) sein. Je nach Eigenschaften des gefahrenen Fahrzeugs des Fahrers erhält dieser einen Vorteil oder Nachteil. Passt außerdem die Vorliebe des Fahrers zum Streckentyp, so verbessert sich das Ergebnis.
- Schwierigkeit: Gibt an, wie anspruchsvoll eine Strecke im Vergleich zu den anderen (der Meisterschaft bspw.) ist. Dabei können Werte von 1 bis 10 angegeben werden, je höher die Zahl, desto schwieriger ist die Strecke. Die Schwierigkeit erhöht die Unfallwahrscheinlichkeit eines Fahrers in einem Rennen.

## 4.2 Fahrer
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

## 4.3 Fahrzeug
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

# 5 Detaillierte Funktionsweise der Objekte

## 5.1 Meisterschaft
Eine Meisterschaft hat zwei Listen. Die Liste "Rennkalender", wo alle Strecken in der richtigen Reihenfolge gespeichert sind und die Liste "Fahrerliste", wo alle Fahrer gespeichert sind, die an dieser Meisterschaft teilnehmen.  
Gespeichert wird eine Meisterschaft im Ordner Datenbank und beinhaltet zwei Werte, abgespeichert als Array. Als erster Wert ist der Dateiname zum Rennkalender und als zweiter Wert der Dateiname zur Fahrerliste gespeichert, denn beide Listen werden noch mal extra als Datei im Ordner Datenbank gespeichert.  
Mit anderen Worten besteht eine Meisterschaft aus drei Dateien:  
- NAME_MEISTERSCHAFT.dat --> bestehend aus [Rennkalenderpfad, Fahrerlistepfad]
- NAME_MEISTERSCHAFTStrecken.dat --> beinhaltet den Rennkalender, jede Strecke ebenfalls als Pfad
- NAME_MEISTERSCHAFTFahrer.dat --> beinhaltet die Fahrerliste, jeden Fahrer ebenfalls als Pfad abgespeichert

Das Objekt "Meisterschaft" wird dazu verwendet, um das Datenhandling um das Objekt möglichst einfach zu gestalten, was sich im Bezug auf die Erstellung bewährt hat. Entsprechend wurden auch verschiedene Methoden implementiert, um sämtliche Funktionen zu unterstützen.  

### 5.1.1 ladenName und ladenPfad
Wenn ein Objekt aufgefordert wird, gespeicherte Daten aus der Datenbank zu laden, so kann das Objekt dies mithilfe des Pfades oder mithilfe des übergebenen Namens tun. Mit der Angabe kann die Methode laden aufgerufen werden. 

### 5.1.2 erstellen
Das Objekt kann all seine eigenen Parameter festlegen, wenn es den eigenen Namen, den Rennkalender und die Fahrerliste übergeben bekommt. Dadurch werden sämtliche notwendigen Pfade gebaut, die das Objekt benötigt, um die Fahrerliste und den Rennkalender anschließend zu speichern.

### 5.1.3 getRennkalenderNamen
Manchmal ist es notwendig, den Rennkalender zu laden und dabei nur die Streckennamen herauszufiltern. Diese Methode gibt sämtliche Strecken in der richtigen Reihenfolge zurück, aber nicht als Pfad, wie es abgespeichert ist, sondern nur den Streckennamen.

### 5.1.4 getFahrerNamen
Analog wie bei Rennkalendern, nur für Fahrer.

### 5.1.5 setRennkalenderNamen
Mit Angabe aller Fahrer kann das Objekt Meisterschaft sich den Rennkalender selbst so zusammenbauen, wie es für die Abspeicherung anschließend benötigt wird.

### 5.1.6 setfahrerlisteName
Analog wie bei Rennkalendern, nur für Fahrer.

### 5.1.7 setPfade
Für eine erfolgreiche Speicherung hat die Meisterschaft die Pfade aller Dateien als Attribute. Da sich alle Dateinamen vom Namen der Meisterschaft ableiten lassen, wurde diese Methode implementiert, die genau das tut.

### 5.1.8 speichern
Speichert alle drei Dateien ab. Im Anschluss wird geprüft, ob die Meisterschaft gespeichert wurde und man kommt eine entsprechende Meldung zurück.

### 5.1.9 laden
Lädt die Meisterschaft anhand seines Namens. Zuerst werden alle drei Pfade ermittelt und danach alle drei Dateien eingelesen, die dann als Attributwerte im Objekt gespeichert werden und zur Verfügung stehen.

## 5.2 Fahrer
Das Objekt "Fahrer" wird dazu verwendet, um das Datenhandling um das Objekt möglichst einfach zu gestalten, was sich im Bezug auf die Erstellung bewährt hat. Entsprechend wurden auch verschiedene Methoden implementiert, um sämtliche Funktionen zu unterstützen. 

Speicherwerte: gebjahr, erstesrennen, aggressivität, geschicklichkeit, grundkönnen, vorliebe, durchschnittlicheplatzierung, fahrzeug, seitWannFahrzeug

### 5.2.1 ladenName und ladenPfad
Wenn ein Objekt aufgefordert wird, gespeicherte Daten aus der Datenbank zu laden, so kann das Objekt dies mithilfe des Pfades oder mithilfe des übergebenen Namens tun. Mit der Angabe kann die Methode laden aufgerufen werden. 

### 5.2.2 erstellen
Mit erstellen() und der Übergabe aller Parameter wird ein Objekt Fahrer instanziiert.
Parameter: name, gebjahr, erstesrennen, aggressivität, geschicklichkeit, grundkönnen, vorliebe, durchschnittlicheplatzierung, fahrzeug, seitWannFahrzeug

### 5.2.3 setPfad
Setzt seinen eigenen Pfad.
Fahrer sind unter /Datenbank/Fahrer gespeichert.

### 5.2.4 setPfadFahrzeug
Setzt den Pfad des Fahrzeugs (s. da).

### 5.2.5 speichern
Speichert das Objekt "Fahrer" ab. Anschließend wird geprüft, ob die Speicherung erfolgreich war und gibt eine entsprechende Meldung zurück.

### 5.2.6 laden
Lädt einen Fahrer aus einer Datei und überträgt die gespeicherten Daten ins Objekt.
Es ist zwingend erforderlich, dass ein Fahrer bereits einen Namen hat. Dies ist zum Bearbeiten dieser Datei gedacht.


## 5.3 Strecke
Das Objekt "Strecke" wird dazu verwendet, um das Datenhandling um das Objekt möglichst einfach zu gestalten, was sich im Bezug auf die Erstellung bewährt hat. Entsprechend wurden auch verschiedene Methoden implementiert, um sämtliche Funktionen zu unterstützen. 

Speicherwerte: rekordhalter, streckentyp, schwierigkeit

### 5.3.1 ladenName und ladenPfad
Wenn ein Objekt aufgefordert wird, gespeicherte Daten aus der Datenbank zu laden, so kann das Objekt dies mithilfe des Pfades oder mithilfe des übergebenen Namens tun. Mit der Angabe kann die Methode laden aufgerufen werden. 

### 5.3.2 erstellen
Mit erstellen() und der Übergabe aller Parameter wird ein Objekt Strecke instanziiert.
Parameter: name, rekordhalter, streckentyp, schwierigkeit

### 5.3.2 setPfad
Setzt seinen eigenen Pfad.
Strecken sind unter /Datenbank/Strecken gespeichert.

### 5.3.3 setPfadRekordhalter
Setzt den Pfad des Rekordhalters, ein Fahrer (s. da).

### 5.3.4 speichern
Speichert das Objekt "Strecke" ab. Anschließend wird geprüft, ob die Speicherung erfolgreich war und gibt eine entsprechende Meldung zurück.

### 5.3.5 laden
Lädt eine Strecke aus einer Datei und überträgt die gespeicherten Daten ins Objekt.
Es ist zwingend erforderlich, dass eine Strecke bereits einen Namen hat. Dies ist zum Bearbeiten dieser Datei gedacht.

## 5.4 Fahrzeug
Das Objekt "Fahrzeug" wird dazu verwendet, um das Datenhandling um das Objekt möglichst einfach zu gestalten, was sich im Bezug auf die Erstellung bewährt hat. Entsprechend wurden auch verschiedene Methoden implementiert, um sämtliche Funktionen zu unterstützen. 

Speicherwerte: leistung, wendigkeit

### 5.4.1 ladenName und ladenPfad
Wenn ein Objekt aufgefordert wird, gespeicherte Daten aus der Datenbank zu laden, so kann das Objekt dies mithilfe des Pfades oder mithilfe des übergebenen Namens tun. Mit der Angabe kann die Methode laden aufgerufen werden. 

### 5.4.2 erstellen
Mit erstellen() und der Übergabe aller Parameter wird ein Objekt Fahrzeug instanziiert.
Parameter: name, rekordhalter, leistung, wendigkeit

### 5.4.3 setPfad
Setzt seinen eigenen Pfad.
Fahrzeuge sind unter /Datenbank/Fahrzeuge gespeichert.

### 5.4.4 speichern
Speichert das Objekt "Fahrzeug" ab. Anschließend wird geprüft, ob die Speicherung erfolgreich war und gibt eine entsprechende Meldung zurück.

### 5.4.5 laden
Lädt ein Fahrzeug aus einer Datei und überträgt die gespeicherten Daten ins Objekt.
Es ist zwingend erforderlich, dass ein Fahrzeug bereits einen Namen hat. Dies ist zum Bearbeiten dieser Datei gedacht.

# 6. Datenspeicherung

Mebe V3 speichert Daten permanent. Dafür werden Binär-Dateien mit der Dateiendung ".dat" im Ordner "Datenbanken" angelegt.
Zwischengespeicherte Daten, die während der Berechnung benötigt werden, werden im Ordner "temporäre Dateien" gespeichert und nach Programmende, wenn das Programm sauber verlassen wird, gelöscht. Auch das sind binärer DAT-Dateien.

Im Ordner "Datenbank" befinden sich alle Meisterschaftsdateien (beschrieben zum Objekt "Meisterschaft") und vier weitere Ordner: "Fahrer", "Fahrzeuge", "Strecken" und "Meisterschaften".
Die ersten drei Ordner beinhalten alle gespeicherten, gleichnamigen Objekte (bspw. Fahrer XYZ im Ordner Fahrer). Alle gespeicherten Parameter des Objekts sind dabei als Array in der DAT-Datei abgespeichert. Der Name der Datei ohne Dateiendung entspricht dabei den Namen des Objekts.

Eine Ausnahme bildet der Ordner "Meisterschaften". In diesem Ordner sind alle Ergebnisse gespeichert, die Mebe V3 jemals berechnet hatte, ebenfalls als DAT-Datei. Damit war geplant, die Rennergebnisse zurückzuverfolgen und nachvollziehbar zu machen, auch wenn die Berechnung selbst schon lang zurückliegt.
Derzeit werden die Ergebnisse allerdings nicht weiterverwendet und nur abgespeichert. 

Meisterschaftsgesamtergebnisse haben dabei folgende Namenskonvention: [Meisterschaftsname][Nummer des Durchlaufs]Meisterschaftsergebnisse.dat
Einzelne Streckenergebnisse erkennt man so: [Meisterschaftsname][Nummer des Durchlaufs]Rennergebnisse[Name der Strecke].dat

## 6.1 Modul Daten - Objekt- und Datenhandling
Das Modul "Daten.py" ist eine ausgelagerte Konsolidierung von Methoden, die die Handhabung von Daten vereinfachen soll.
Vorrangig ist das Modul dazu zuständig, dass die Daten gelesen und geschrieben werden können und dass Informationen über Objekte aus der Datenbank herausgeholt werden können.

### 6.1.1 lesen
In einem Stream werden die binären Daten gelesen und direkt zurückgegeben.

### 6.1.2 schreiben
Als Parameter wird der Pfad übergeben und die Daten, die dann als binäre Daten gespeichert werden.
Es wird nicht automatisch die Dateiendung .dat angefügt.

### 6.1.3 listeMeisterschaftspfade
Diese Methode gibt alle Pfade zurück, die auf eine Meisterschaft zeigen.

Funktionsweise:
Zuallererst werden alle Objekte im Datenbank-Ordner in eine Liste zwischengespeichert.
Für jedes dieses Element wird dann eine Prüfung gemacht. Es handelt sich um eine Meisterschaftsdatei, wenn...
- Wenn es nicht mit "Fahrer.dat" endet (Fahrerliste)
- Wenn es nicht mit "Strecken.dat" endet (Rennkalender)
- Wenn es auf ".dat" endet (andere Ordner)
Alle Objekte des Ordners Datenbank, die durch den Filter gekommen sind, sind Meisterschaftsdateien. Diese werden mit dem Präfix "Datenbank/" erweitert, wodurch dann der vollständige relative Pfad fertig erstellt ist.

Dieser wird dann in einer weiteren Liste zwischengespeichert. Ist die Liste vollständig, dann wird sie wieder zurück ans aufrufende Modul übergeben.

### 6.1.4 listeMeisterschaftsnamen
Diese Methode liefert alle existierenden Meisterschaften als Liste.

Funktionsweise:
Sie nutzt listeMeisterschaftspfade, um die Meisterschaften herauszunehmen. In einer weiteren Schleife wird jedem Element der Präfix und die Dateiendung entfernt, sodass nur noch der reine Meisterschaftsname übrig bleibt.

### 6.1.5 listePfade
Diese Methode dient dazu, eine Liste mit Pfaden von existierenden Objekten (Fahrer, Strecken oder Fahrzeuge) zu erstellen.
Meisterschaften müssen anders wiedergegeben werden, deshalb müssen existierende Meisterschaften anders ermittelt werden.

Als Übergabeparameter wird der Objekttyp erfordert. Erlaubt sind dabei "Strecken", "Fahrer" und "Fahrzeuge", was den Ordnernamen im Ordner "Datenbank" entspricht.

Funktionsweise:
Zuallererst wird der Pfad ermittelt, aus dem die Objekte herausgelesen werden sollen. Dazu wird der übergebene Parameter mit dem Präfix "Datenbank" kombiniert, sodass der korrekte relative Pfad zwischengespeichert werden kann.

Innerhalb dieses Pfades werden dann alle Objekte in einer Liste gespeichert.
Für jedes Objekt dieser Liste wird dann der gesamte korrekte relative Pfad zusammengebaut, indem der Ordnerpfad von eben mit einem "/" versehen wird und dann der Name der Datei ergänzt wird.

Zurückgegeben wird die Liste mit allen relativen Pfaden der angefragten Objekte.

### 6.1.6 listeNamen
Diese Methode dient dazu, eine Liste von existierenden Objekten (Fahrer, Strecken oder Fahrzeuge) zu erstellen.
Meisterschaften müssen anders wiedergegeben werden, deshalb müssen existierende Meisterschaften anders ermittelt werden.

Als Übergabeparameter wird der Objekttyp erfordert. Erlaubt sind dabei "Strecken", "Fahrer" und "Fahrzeuge", was den Ordnernamen im Ordner "Datenbank" entspricht.

Funktionsweise:
Zuallererst wird der Pfad ermittelt, aus dem die Objekte herausgelesen werden sollen. Dazu wird der übergebene Parameter mit dem Präfix "Datenbank" kombiniert, sodass der korrekte relative Pfad zwischengespeichert werden kann.

Innerhalb dieses Pfades werden dann alle Objekte in einer Liste gespeichert.
Für jedes Objekt dieser Liste wird dann die Dateiendung entfernt, sodass nur noch der Name des Objekts über bleibt.

Zurückgegeben wird die Liste mit allen Namen der angefragten Objekte.

# 7 Technische Betrachtung Erstellen.py
Ein Erstellungsprozess ist zwingend notwendig, um Daten berechnen zu können. Dieser ist allerdings auch sehr komplex.

In diesem Kapitel soll chronologisch aufgeführt werden, welchen Ablauf das Modul durchläuft.

## 7.1 Erstellen()

Vom Hauptmenü aus, wenn man "Erstellen" auswählt, wird diese Methode ausgeführt.

Es müssen zwei Variablen gesetzt werden:
- Die Variable "varweiter" muss initialisiert werden: 0. Das sagt aus, dass der Prozess beginnt.
- Die Variable "bearbeitungsmodus" mit dem Wert 0 zeigt an, dass sich das Programm aktuell eine Meisterschaft erstellt und nicht bearbeitet.

Im nächsten Schritt wird ein Objekt "Meisterschaft" initialisiert.
Das Objekt hilft, die Daten zu händeln.

Nachdem der Bildtitel gesetzt wurde, wird weiter() ausgeführt.

## 7.2 MeisterschaftBearbeiten

Meisterschaften können aber auch bearbeitet werden. In diesem Fall unterscheidet sich die Methode von erstellen() nur sofern, dass neben der Objektinstanziierung das Objekt noch geladen wird.
Außerdem werden die Variablen "bearbeitungsmodus" und "varweiter" auf 1 gesetzt, um zu kennzeichnen, dass es ein Berbeitungsprozess ist.
Was varweiter macht, ist im nächsten Kapitel ersichtlich.

## 7.3 sammeln() in weiter()

Als allererstes in weiter() wird sammeln() ausgeführt. sammeln() dient dazu, die eingegebenen Informationen aufzugreifen und zwischenzuspeichern, sodass sie weiter genutzt werden können.

Vor jeder Aktion wird die aktuelle Statusmeldung gelöscht, da es sein kann, dass Infomeldungen erscheinen - die dann nicht weg gehen.

Je nachdem, welchen Wert varweiter hat, werden andere Informationen abgerufen.

### 7.3.1 Keine Aktion: varweiter == 0
Wenn die Meisterschaft erstellt wird, so gibt es im allerersten Durchlauf keine Benutzerinteraktion, weshalb der Fall varweiter == 0 nicht näher definiert ist und keine Aktion ausführt.

### 7.3.2 Meisterschaftsdaten sammeln: varweiter == 1
Es wird direkt geprüft, ob der Bearbeitungsmodus (1) an ist. Wenn nicht (0), dann wird eine Meisterschaft erstellt. Wenn nicht, dann werden die meisten Aktionen übersprungen und dem Objekt Meisterschaft, was im ersten Schritt erstellt worden ist, die Werte zugeordnet, die in der Datei gespeichert sind.

Wird eine Meisterschaft erstellt, sind noch weitere Schritte notwendig.
1. Es wird der Name aus dem Eingabefeld herausgenommen. Daraufhin wird er mit dem Jahr, welches ebenso eingegeben werden soll, kombiniert. Daraufhin wird dem Objekt Meisterschaft der Wert zugeordnet und es erstellt seine Pfade.
2. Anschließend wird geprüft, ob der Name der Meisterschaft leer ist. Wenn ja, wird eine Infomeldung gesendet, varweiter auf 0 gesetzt, damit das ganze Modul wieder von vorne beginnt und dann wird return ausgeführt, damit die Methode an der Stelle abbricht.
3. Sollte die erste Prüfung erfolgreich im Sinne des Fortschritts sein, dann wird die Liste aller existierenden Meisterschaften gelesen. Befindet sich der eingegebene Name bereits in der Liste der existierenden Meisterschaften, so wird auch hier eine Meldung gesendet und der Prozess abgebrochen. Andernfalls könnte es sein, dass die bestehende Meisterschaft überschrieben wird.
4. Erst, wenn die Überprüfung des Namens erfolgreich wird, werden zwei Arrays initialisiert, die die Fahrerliste und den Rennkalender lokal zwischenspeichern. Sie sind an der Stelle, um weitere globale Variablen zu vermeiden. An dieser Stelle geht das Programm aber mitunter als Erstes durch.

### 7.3.3 Strecken hinzufügen: varweiter == 2
Zuallererst wird die Zwei-Fenster-Anzeige beendet. Durch die Funktionsweise der anderen Module muss es an der Stelle erfolgen, da sonst eine unsaubere Anzeige erscheint.
Als Nächstes wird der Rennkalender der Meisterschaft zugewiesen.

### 7.3.4 Fahrer hinzufügen: varweiter == 3
Zuallererst wird die Zwei-Fenster-Anzeige beendet. Durch die Funktionsweise der anderen Module muss es an der Stelle erfolgen, da sonst eine unsaubere Anzeige erscheint.
Als Letztes wird die Fahrerliste der Meisterschaft zugewiesen.

### 7.3.5 varweiter > 3 || varweiter < 0
Diese Fälle werden abgefangen und es passiert nichts, weil es nicht definiert ist.

## 7.4 weiter()
Nach sammeln() springt das Programm zurück in weiter().
Weiter wird auch dann aufgerufen, wenn der Button "Weiter" bzw. "Meisterschaft erstellen" aufgerufen wird.

Dabei wird der Frameinhalt geleert und die Buttons zurückgesetzt, bevor es wieder befüllt wird.
Danach wird varweiter um eins erhöht - bevor etwas anderes passiert ist. So ist es einfacher, die verschiedenen Programmzustände nachzuvollziehen.

Als nächstes wird der Weiter-Knopf noch angepasst. Ist varweiter ungleich drei, so wird der Knopf "Weiter" genannt, ansonsten "Meisterschaft erstellen".
Das soll für weniger Verwirrung im letzten Bildschirm sorgen.

Erst jetzt wird unterschieden, im welchen Zustand sich das Programm jetzt befinden soll. Nach diesem Aufruf ist weiter() beendet.

### 7.4.1 Meisterschaftsnamen definieren: varweiter == 1
Der Meisterschaftsname wird festgelegt.
Es wird meisterschaftdefinieren() aufgerufen.

### 7.4.2 Rennkalender einfügen: varweiter == 2
Der Rennkalender wird bearbeitet.
Es wird rennkalendereinfügen() aufgerufen.

### 7.4.3 Fahrerliste einfügen: varweiter == 3
Die Fahrerliste wird bearbeitet.
Es wird fahrereinfügen() aufgerufen.

### 7.4.4 varweiter == 4
Nachdem im letzten Bildschirm auf "Meisterschaft erstellen" geklickt wurde (der Weiter-Knopf wurde in diesem Bildschirm modifiziert!), dann wird das Hauptmenü aufgerufen und das Objekt Meisterschaft, welches über den gesamten Prozess hinweg existierte, gespeichert.

## 7.5 meisterschaftdefinieren()
meisterschaftdefinieren() wird in weiter() aufgerufen.
Das Fenster wird mit einem Label, darunter einem Eingabefenster, noch einem Label und noch einem Fenster ausgemschmückt.
Im zweiten Eingabefenster, wo das Jahr eingegeben werden soll, wird das aktuelle Jahr ermittelt und als Standardwert dort eingetragen.
Danach ist diese Methode vorbei und das Programm wartet auf eine Aktion des Nutzenden.

## 7.6 rennkalendereinfügen() und fahrereinfügen()
Beide Methoden sind sich fast identisch.

Zuerst wird der Anzeigemodus umgestellt, auf die Zwei-Fenster-Anzeige. Danach werden alle nötigen Buttons eingefügt, einer der ein neues Element erstellen kann, einer, der ein Element auswählt und einer, der ein Element entfernen kann.

Anschließend wird über Daten.py die jeweilige Liste geladen, die benötigt wird. Entweder die Liste aller existierenden Fahrer oder die Liste aller existierenden Strecken.

Danach wird im linken Fenster in einer For-Schleife für jedes Element ein Radiobutton erstellt. Als Text bekommt es den Namen des Elements, als Wert ebenso.
Anschließend wird das allererste Element ausgewählt.

Wenn die Fahrerliste bzw. Rennkalenderliste nicht leer ist, so wird der Vorgang für das rechte Fenster wiederholt, allerdings mit den Elementen aus der Fahrer- bzw. Rennkalenderliste und als Wert nur die Indexnummer (Int, kein String) in der Liste. So kann eindeutig sichergestellt werden, dass der richtige Wert gewählt wird, da Strecken auch doppelt vorkommen können. Bei der Auswahlseite (links) ist es nicht notwendig, da jedes Element eindeutig sein muss.

Über die rennkalenderliste und die fahrerliste können andere Meisterschaften bearbeitet werden. Diese Listen ermöglichen es auch, während des Erstellen-Prozesses zum vorigen Fenster zurückzukehren oder den Frame neu zu laden (aktualisiereFenster oder bei Checkpoints), ohne dass die Werte verloren gehen.

Anders als in rennkalendereinfügen() muss in fahrereinfügen() abschließend aktualisiereFenster() ausgeführt werden, weil sonst falsche Radiobuttons angezeigt werden. Der Grund ist aber ungeklärt.

Je nachdem, welcher Button gedrückt wird, geht das Programm weiter

## 7.7 erstelleElement()
Wird der Knopf "Fahrer erstellen" oder "Strecke erstellen" gedrückt, so wird die Funktion erstelleElement() aufgerufen. Je nach Wert von varweiter kann die Methode herausfinden, ob gerade ein Fahrer oder eine Strecke erstellt werden muss. Entsprechendes Modul wird anschließend aufgerufen. Wenn dieses Modul beendet wird, wird aktualisiereFenster() aufgerufen und erstelleElement terminiert.

## 7.8 auswählen()
Wird der Knopf "auswählen" gedrückt, wird diese Funktion ausgeführt. Auch diese Methode kann über varweiter herausfinden, ob die Rennkalenderliste oder die Fahrerliste bearbeitet werden muss.
Entsprechend wird append() auf die jeweilige Liste ausgeführt und der Wert des gewählten Radiobuttons auf der linken Seite (Auswahl) zur Liste hinzugefügt.

Abschließend wird aktualisiereFenster() aufgerufen. 

## 7.9 entfernen()
Wird der Knopf "Entfernen" gedrückt, wird diese Funktion ausgeführt. Auch diese Methode kann über varweiter herausfinden, ob die Rennkalenderliste oder die Fahrerliste bearbeitet werden muss.
Entsprechend wird pop() auf die jeweilige Liste ausgeführt und der Wert (der Index!) des gewählten Radiobuttons auf der rechten Seite (für Meisterschaft ausgewählt) von der Liste entfernt. Durch den Index ist nun jedes Element eindeutig.

Abschließend wird aktualisiereFenster() aufgerufen. 

## 7.10 aktualisiereFenster()
Diese Methode hilft im Zwei-Fenster-Modus beide Listen zu aktualisieren, um die Radiobuttons mit den neuen bzw. gelöschten Elementen zu ergänzen.

Zuerst werden sowohl die linke als auch die rechte Anzeige zurückgesetzt (Forget).

Danach wird über varweiter herausgefunden, ob die Rennkalender- oder Fahrerliste bearbeitet werden soll.

Über listeNamen aus Daten.py wird die entsprechende Liste aller existierenden Elemente neu gesetzt. Auch die rechte Liste wird wieder neu gesetzt.
Da Fahrer aber eindeutig ist und entweder rechts oder links vorkommen kann, müssen noch alle Elemente auf der linken Seite entfernt werden, die schon rechts sind.

Anschließend werden die Radiobuttons wieder neu gesetzt, wie sie in den anderen Methoden erstellt worden sind.

Ganz zum Schluss wird tkinter geupdatet.

# 8 Weitere Erstell-Module
## 8.1 Gemeinsames
Der Erstell-Prozess ist recht komplex. Um ihn ein bisschen aufzuteilen, wurde für jedes Objekt ein Modul gebaut, um die Erstellung zu vereinfachen.
Sie sind sich auch sehr ähnlich, weshalb in den spezifischen Abschnitten nur auf die unterscheidenden Merkmale eingegangen wird. Sie bestehen alle aus mind. zwei Modulen: speichern() und erstellen(name).

### 8.1.1 speichern()
Wie der Name schon sagt, ist diese Methode dazu da, das entsprechende Objekt zu speichern. Dem vorangegangen werden Prüfungen gemacht, ob die Erstellung vollständig erfolgt ist bzw. ob das Objekt schon existiert. Mit der Objektmethode .speichern() im Objekt werden alle Angaben gespeichert, bevor angewiesen wird, den Erstell-Prozess zu beenden.
Da Erstellen-Module als Checkpoint aufgerufen werden, muss dieser nun zerstört und der alte wiederhergestellt werden (mehr zur Mechanik später mehr).
Da Erstellen-Module auch dazu gebaut sind, Objekte zu bearbeiten, muss zum Abschluss auch geprüft werden, ob bearbeitet oder erstellt wurde. Denn wenn ein Objekt erstellt wurde, muss das Fenster noch einmal aktualisiert werden (s. aktualisiereFenster).

### 8.1.2 erstellen(name)
Zuerst muss ein neuer Checkpoint (s. da) erstellt werden, damit der Erstell-Prozess richtig angezeigt werden kann.
Hier werden jetzt sämtliche grafischen Elemente definiert, die angezeigt werden sollen, um das Objekt zu bearbeiten. Ausgelesen werden die Werte dann speichern().

### 8.1.3 Bearbeitung
Auch der Bearbeitungsprozess wird hier abgehandelt. Dazu wird der Methode erstellen() ein Parameter übergeben.
Da das Modul nur eine bestimmte Art von Objekt bearbeiten (Fahrzeug, Fahrer, Strecke) kann, kann alleine anhand des Namens das Objekt geladen werden und in das temporäre Objekt geladen werden. In die grafischen Elemente werden dann die gespeicherten Werte als Startwerte festgelegt.
Im weiteren Verlauf wird das Objekt behandelt, als wäre es ein neues Objekt, mit dem Unterschied, dass der Name nicht bearbeitet werden kann.
Wenn das Objekt gespeichert, wird das alte Objekt vom neuen Objekt überschrieben.
Anhand des fehlenden Eingabefelds wird auch erkannt, ob es sich um ein Erstellen- oder Bearbeitungs-Prozess handelt. Dies ist lediglich für den Ausgang aus dem Modul und die Zurückführung zum aufrufenden Modul wichtig.

### 8.1.4 Kontrollen
Es gibt einen Wert, der geprüft wird, um die Erstellung erfolgreich abzuschließen. Ist der Wert im Eingabefeld leer (also kein Name eingegeben), so wird nicht gespeichert.
Des Weiteren wird geprüft, ob das Objekt schon existiert. Dafür wird aus Daten.py die Liste gezogen, welche Objekte dieser Art überhaupt existieren. Kommt der Name in dieser Liste vor, dann wird eine Warnung ausgegeben und die Variable "namekontrolle" auf 1 gesetzt. Wird wieder das Objekt gespeichert, so erscheint die Warnung nicht (weil namekontrolle auf 0 steht) und das existierende Objekt wird überschrieben, wenn die Namen immer noch gleich sind.

Alle weiteren Kontrollen werden so gelöst, indem alle Widgets, wo Daten erwartet werden, ausgelesen und in das temporäre Objekt geladen werden.
Auf diese Attribute wird geprüft, ob sie bspw. leer sind oder andere ungültige Werte enthalten. Ist dies der Fall, so wird eine Info gesetzt und der Speichern-Prozess abgebrochen.

## 8.2 Technische Betrachtung ErstelleFahrzeug.py 
ErstelleFahrzeug unterscheidet sich nur unwesentlich vom Blueprint.
Der einzige Unterschied befindet sich in der Übergabe und der Wiederherstellung des Checkpoints. Da ErstelleFahrzeuge aus der Fahrzeugauswahl aufgerufen wird, aber wieder zurück an ErstelleFahrer übergeben werden muss, muss der Checkpoint zwei Mal wiederhergestellt werden, da sonst die Widgets des Fahrers in den zu löschenden Frame gesetzt werden.
Anschließend muss ErstelleFahrer.FahrzeugAuswählen() erneut aufgerufen werden, damit die Fahrzeugauswahl neu geladen werden kann und das neu erstellte Fahrzeug erscheint.

### 8.2.1 Voraussetzungen zum Speichern
- Name muss angegeben werden
- Das Fahrzeug darf noch nicht existieren.
Die Kontrolle funktioniert nach Blueprint.

## 8.3 Technische Betrachtung ErstelleFahrer.py 
ErstelleFahrer.py ist der umfangreichste Erstellprozess neben den Meisterschaften, weil er am meisten Attribute enthält. Die Komplexität wurde allerdings nur geringfügig erweitert.

### 8.3.1 Fahrzeugauswahl
Der wesentliche Unterschied zu anderen Erstellprozessen ist, dass jedem Fahrer ein Fahrzeug zugeordnet werden muss. Dafür wird ein einfacher String ins Objekt geschrieben. Doch bis dahin, sind weitere Schritte notwendig.

1. Es kann kein freier Name gewählt werden, um sicherzustellen, dass das Fahrzeug auch wirklich existiert. Es muss also ein existierendes Fahrzeug aus der Datenbank herausgesucht werden. Dafür muss man den Button "Fahrzeug auswählen" klicken.
2. Es wird ein Checkpoint (s. da) erstellt.
3. Die Liste aller Fahrzeuge wird über das Modul "Daten" ausgelesen.
4. Es werden die benötigten Buttons hinzugefügt.
5. Es wird die Fahrzeugkontrollvariable gesetzt (siehe Kontrollen)
6. Für jedes Element (also jedes Fahrzeug-Element) wird ein Radiobutton erstellt, welcher dann ausgewählt werden kann.
7. Klickt man nun auf "Neues Fahrzeug erstellen", dann wird neuesFahrzeug() ausgeführt. Dieser Zwischenschritt ist notwendig, damit "ErstelleFahrzeug.py" nicht direkt bei der Erstellung des Buttons ausgeführt wird, da das Argument eines leeren Strings mitgegeben werden muss, um nicht den Bearbeiten-Prozess auszulösen.
8. Wenn das Fahrzeug erstellt wurde, erscheint es nun als Auswahlmöglichkeit, da der Checkpoint wiederhergestellt wird, also die Radiobuttons neu erstellt werden.
9. Man wählt ein Fahrzeug und klickt auf "Fahrzeug auswählen". fügeFahrzeugein() wird ausgeführt.
10. Das Label, was den Namen des Fahrzeugs anzeigt, wird umbenannt, sodass der richtige Name angezeigt wird. Dieser Wert wird dann beim Objekt "Fahrer" gespeichert.

### 8.3.2 Voraussetzungen zum Speichern
- Fahrzeug muss zugeordnet sein
    - Wenn gar nicht erst der Button zur Fahrzeugauswahl gedrückt wurde, kann ausgeschlossen werden, dass ein Fahrzeug ausgewählt wurde. Daher wird in der Funktion die Variable "fahrzeugkontrolle" auf 1 gesetzt. Wenn in speichern() geprüft wird, ob ein Fahrzeug ausgewählt wurde, muss die Variable 1 sein.
    - Bei Bearbeitungen kann es allerdings sein, dass ein Fahrzeug nicht geändert werden muss. Daher ist diese Kontrolle nicht möglich. Stattdessen wird kontrolliert, ob der standardmäßige Text "[Kein Fahrzeug ausgewählt]" ins Objekt geschrieben wurde. So kann ausgeschlossen werden, dass ein Fahrzeug ausgewählt wurde.
    - Sobald eine Bedingung falsch ist, also der Button geklickt wurde ODER ein anderes Fahrzeug im Objekt gespeichert wurde, erst dann ist ein Speichern möglich. Sind beide Bedingungen wahr, so wird ein Fehler geworfen.

- Name muss angegeben werden
- Das Geburtsdatum muss eine Zahl sein.
    - fahrer.gebjahr.isnumeric()
    - Wenn das Geburtsjahr nicht angegeben wurde oder keine Zahl ist, wird falsch zurückgegeben.
    - Durch die Negation wird die Verzweigung ausgelöst und der Fehler ausgegeben.
    - Analog zu den anderen Integer-Prüfungen.
- Das Jahr des ersten Rennens muss eine Zahl sein.
- Das Jahr des ersten Rennens darf nicht weniger als 10 Jahre nach dem Geburtsjahr liegen --> der Fahrer darf frühestens im zehnten Lebensjahr mit dem Motorsport beginnen.
    - int(fahrer.gebjahr)+10 > int(fahrer.erstesrennen)
    - Wenn der Zahlwert addiert mit 10 von dem Geburtsjahr größer ist als das Jahr des ersten Rennens, wird der Fehler ausgegeben.
- Die Angabe der Durschnitssplatzierung muss eine Zahl sein.
- Jahr mit der Fahrt des aktuellen Fahrzeugs muss eine Zahl sein.
- Jahr mit der Fahrt des aktuellen Fahrzeugs darf nicht weniger als 10 Jahre nach dem Geburtsjahr liegen.
- Fahrer darf noch nicht existieren

## 8.4 Technische Betrachtung ErstelleStrecke.py
HIER WEITER. 8.1 beachten.

# 9 Technische Betrachtung Bearbeiten

# 10 Berechnungsmechanik (MebeAl1)

# 11 Anzeige
(Programmstart, Prozess, Aufgaben und Aussehen, Checkpoint)

# 12 Hilfsmodul Z-Hilfe-Leser (HiLe1)