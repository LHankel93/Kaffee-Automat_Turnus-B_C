# import <Dateiname ohne Endung>
# Bei Zutatart bin ich mir nicht 100% sicher, aber laut UML ist's wohl nötig. LH
from Angebot import Angebot
from Kasse import Kasse
from Zutatart import Zutatart
# Aufruf von fremder Datei-Methode mit <Dateiname Ohne Endung>.<Methodenname>
# Kurze Verschiebung von KaffeeautomatSim zu dieser Klasse nach eingehender Betrachtung des UML Diagramms.

# LH Kaffeeautomat Klasse
class Kaffeeautomat:
    espresso = Zutatart("ESPRESSO", 1.00, 100) # Standardbestand 100
    heiße_milch = Zutatart("HEISSE MILCH", 1.00, 100)
    milchschaum = Zutatart("MILCHSCHAUM", 0.50, 100)
    # LH Konstruktor für Kaffeeautomat
    def __init__(self) -> None:
        self.__angebote = Angebot()
        self.__kasse = Kasse()
    
    # LH Setter für angebote
    def set_angebote(self, angebote):
        self.__angebote = angebote
    
    # LH Getter für angebote
    def get_angebote(self):
        return self.__angebote
    
    # LH Setter für kasse
    def set_kasse(self, kasse):
        self.__kasse = kasse
    
    # LH Getter für kasse
    def get_kasse(self):
        return self.__kasse