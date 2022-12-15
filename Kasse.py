from pathlib import Path
from decimal import *

"""LH. Kasse enthält die Methoden für die Berechnung und
Verarbeitung von Wechselgeld und der Rechnung.
Für später kann hier auch das vorhandene Wechselgeld gespeichert
werden."""

# LH Kasse Klasse
class Kasse:
    # LH Konstruktor für Kasse
    def __init__(self) -> None:
        # LH Decimal Präzision auf 2 Nachkommastellen einstellen.
        self.__wechselgeld = float(0.00)

    # LH Setter für wechselgeld
    def set_wechselgeld(self, wechselgeld):
        if wechselgeld >= 0.00:
            self.__wechselgeld = wechselgeld
        else:
            print("Wechselgeld zu gering. Wechselgeld darf nicht unter 0.00 fallen.")

    # LH Getter für wechselgeld
    def get_wechselgeld(self):
        return self.__wechselgeld

    # LH eine Möglichkeit um gespeichertes Wechselgeld aufzurufen
    def lade_wechselgeld(self):
        path = Path("./wechselgeld.txt")
        if path.is_file():
            file = open(path, "r")
            w = Decimal(file.readline())
            self.__wechselgeld = float(w)
            file.close()

    # LH eine Möglichkeit um Wechselgeld zu speichern in txt Datei.
    def speicher_wechselgeld(self):
        path = Path("./wechselgeld.txt")
        file = open(path, "w")
        file.write(round(self.__wechselgeld, 2))
        file.close

# LH Beispielhafte Verwendung der Klasse
"""
a = Kasse()
a.lade_wechselgeld()
w = a.get_wechselgeld()
print(w)
a.set_wechselgeld((w - 2 )) 
print(a.get_wechselgeld())
"""