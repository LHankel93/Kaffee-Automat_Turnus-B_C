# LH RezeptTeil Klasse
# Nötiger Import sollte laut UML Zutatart sein.
from Zutatart import Zutatart

# LH Klasse RezeptTeil
class RezeptTeil:
    # LH Konstruktor für die Klasse RezeptTeil
    def __init__(self, zutatart, menge):
        self.__zutatart = zutatart
        self.__menge = menge

    # LH Setter für zutatart
    def set_zutatart(self, zutatart):
        self.__zutatart = zutatart

    # LH Getter für zutatart
    def get_zutatart(self):
        return self.__zutatart

    # LH Setter für menge
    def set_menge(self, menge):
        if menge >= 0:
            self.__menge = menge
        else:
            print("Menge zu gering. Menge darf nicht kleiner als 0 sein.")

    # LH Getter für menge
    def get_menge(self):
        return self.__menge
