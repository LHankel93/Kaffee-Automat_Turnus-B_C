# LH Nötige Imports sollte nur RezeptTeil sein laut UML
import RezeptTeil

# LH Angebot Klasse
class Angebot:
    # LH Konstruktor für Angebot Klasse
    def __init__(self, bezeichner, rezept):
        self.__bezeichner = bezeichner
        self.__rezept = rezept

    # LH Setter für bezeichner
    def set_bezeichner(self, bezeichner):
        if bezeichner.len() > 0:
            self.__bezeichner = bezeichner
        else:
            print("Bezeichner ist zu kurz.")

    # LH Getter für Bezeichner
    def get_bezeichner(self):
        return self.__bezeichner

    # LH Setter für rezept
    def set_rezept(self, rezept):
        self.__rezept = rezept

    # LH Getter für rezept
    def get_rezept(self):
        return self.__rezept
