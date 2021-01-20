# FourInARow
## 4 Gewinnt, auf lässig

Das Spiel 4 gewinnt soll mithilfe von TCP/IP-Sockets implementiert werde. Die Steuerung des Spieles übernimmt ein Server-Prozess. Der erste sich verbindende Prozess übernimmt den Spieler 1 und bekommt das Symbol Kreuz (X). Der 2. Sich verbindende Prozess übernimmt den Spieler 2 und das Symbol Kreis (O). Mit Spieler 1 beginnend wird nun abwechselnd eine Spalte gewählt in der ein Stein platziert werden soll. Der Spieler der zuerst 4 Steine in eine Reihe bringt gewinnt. Nach jedem Spielzug soll das Spielfeld in der Konsole ausgegeben werden. Sollte das Spielfeld voll sein ohne, dass jemand 4 Steine in einer Reihe hat, geht die Runde unentschieden aus. Nutzereingaben werden direkt an den Server geschickt, der diese auswertet.
Nach Beendung der Verbindung zum Client soll auf eine neue Verbindung gewartet werden.
Das Spielfeld besteht aus 6 Zeilen und 7 Spalten. Aus ASCII Zeichen soll ein symbolischer Spielplan aufgezeichnet werden. Die Nutzer Eingabe erfolgt über eine Zahl von 1-7 welche je für eine Spalte steht, in welcher der Stein auf den untersten freien Slot platziert wird.

## Anforderungen:

1. Es sollen mehrere Spiele parallel stattfinde können.
2. Legen Sie fest wie Spieler zugeordnet werden, wenn mehrere Spiele statfinden.
3. Die Anzahl an gleichzeitig stattfindenden Spilen wir am Ende jeden Spiels neben dem Spielausgang auch angezeigt
4. Es soll eine Maximalzeit geben, um einen Zug durchzuführen, ansonsten hat der Spieler verloren.
5. Der Sieger wird erst nach einer vorgegebenen Anzahl von Spielen bestimmt.
6. Zwischen den Spielen muss eine maximale Zeit für den nächsten ersten Zug eingehalten werden, ansonsten wird das Spiel abgebrochen.


## Die Applikation sollen wie folgt ausgeführt werden können:
fourinarow_server [-p PORT][-n NUMBER_OF_GAMES]
fourinarow_client [-p PORT[-i IP]

