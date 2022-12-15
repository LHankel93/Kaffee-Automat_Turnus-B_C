# import <Dateiname ohne Endung>
# Bei Zutatart bin ich mir nicht 100% sicher, aber laut UML ist's wohl nötig. LH
import Angebot, Kasse, Zutatart
# Aufruf von fremder Datei-Methode mit <Dateiname Ohne Endung>.<Methodenname>
# Kurze Verschiebung von KaffeeautomatSim zu dieser Klasse nach eingehender Betrachtung des UML Diagramms.

# LH Kaffeeautomat Klasse
class Kaffeeautomat:
    # LH Konstruktor für Kaffeeautomat
    def __init__(self, angebote, kasse) -> None:
        self.__angebote = angebote
        self.__kasse = kasse
    
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