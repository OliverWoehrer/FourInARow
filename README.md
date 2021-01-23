# FourInARow

## 4 Gewinnt, auf lässig
Das Spiel 4 gewinnt soll mithilfe von TCP/IP-Sockets implementiert werde. Die Steuerung des Spieles übernimmt ein Server-Prozess. Der erste sich verbindende Prozess übernimmt den Spieler 1 und bekommt das Symbol Kreuz (X). Der 2. Sich verbindende Prozess übernimmt den Spieler 2 und das Symbol Kreis (O). Mit Spieler 1 beginnend wird nun abwechselnd eine Spalte gewählt in der ein Stein platziert werden soll. Der Spieler der zuerst 4 Steine in eine Reihe bringt gewinnt. Nach jedem Spielzug soll das Spielfeld in der Konsole ausgegeben werden. Sollte das Spielfeld voll sein ohne, dass jemand 4 Steine in einer Reihe hat, geht die Runde unentschieden aus. Nutzereingaben werden direkt an den Server geschickt, der diese auswertet.\
Nach Beendung der Verbindung zum Client soll auf eine neue Verbindung gewartet werden.\
Das Spielfeld besteht aus 6 Zeilen und 7 Spalten. Aus ASCII Zeichen soll ein symbolischer Spielplan aufgezeichnet werden. Die Nutzer Eingabe erfolgt über eine Zahl von 1-7 welche je für eine Spalte steht, in welcher der Stein auf den untersten freien Slot platziert wird.

## Anforderungen:
1. Es sollen mehrere Spiele parallel stattfinde können.
2. Legen Sie fest wie Spieler zugeordnet werden, wenn mehrere Spiele statfinden.
3. Die Anzahl an gleichzeitig stattfindenden Spilen wir am Ende jeden Spiels neben dem Spielausgang auch angezeigt
4. Es soll eine Maximalzeit geben, um einen Zug durchzuführen, ansonsten hat der Spieler verloren.
5. Der Sieger wird erst nach einer vorgegebenen Anzahl von Spielen bestimmt.
6. Zwischen den Spielen muss eine maximale Zeit für den nächsten ersten Zug eingehalten werden, ansonsten wird das Spiel abgebrochen.
7. Nutzerprofile anlegen. Die Information über die zuletzt gespielte Spielsequenz (Name des Gegners, Anzahl der Spiele, Spielstand am Ende) wird für jeden Spieler nach Anmeldung automatisch angezeigt (sofern er bereits einmal gespielt hat).


## Die Applikation sollen wie folgt ausgeführt werden können:
* fourinarow_server [-p PORT] [-n NUMBER_OF_GAMES]
* fourinarow_client [-p PORT] [-i IP]

Der Parameter für die -p-Option gibt den UDP-Port des Sockets an, über den kommuniziert werden soll, die -n-Option gibt die Anzahl der durchzuführenden Spiele an. Der Server soll auf allen möglichen Schnittstellen/IPs lauschen. Beim Client soll zusätzlich mittels -i Parameter die IP-Adresse des Servers angeben werden können. Sollte dies fehlen wird 127.0.0.1 verwendet. Wird kein port übergeben, soll ein passender, vordefinierter Port verwendet werden, der in Server und Client gleich ist (z.B. die User-ID eines Autors). Sollten ungültige Parameter übergeben werden, soll zumindest eine usage message aussgegeben werden.
