# LH & GD
class Zutatart:
    def __init__(self, bezeichner: str = "Beispielzutart", preis: float = 0.0, bestand: int = 0):
        self.__bezeichner = bezeichner
        self.__preis = preis
        self.__bestand = bestand

    # LH Setter Bezeichner
    def set_bezeichner(self, bezeichner: str):
        if bezeichner.len() > 0:
            self.__bezeichner = bezeichner
        else:
            print("Bezeichnung ist zu kurz. Bitte eine längere wählen.")

    # LH Getter Bezeichner
    def get_bezeichner(self):
        return self.__bezeichner

    # LH Setter preis
    def set_preis(self, preis):
        if preis >= 0.00:
            self.__preis = preis
        else:
            print("Preis ist zu niedrig, Preis kann nicht niedriger als 0.00 sein.")

    # LH Getter preis
    def get_preis(self):
        return self.__preis

    # LH Setter bestand
    def set_bestand(self, bestand):
        if bestand >= 0:
            self.__bestand = bestand
        else:
            print("Bestand ist zu niedrig, Bestand kann nicht unter 0 gestellt werden.")

    def get_bestand(self):
        return self.__bestand