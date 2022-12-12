# LH & GD
class Zutatart:
    def __init__(self,bezeichner:str = "Beispiel" , preis:float =0.0, bestand:int = 0 ):
        self.__bezeichner = bezeichner
        self.__preis = preis
        self.__bestand = bestand
    
    
    # LH Setter 
    def set_bezeichner(self, bezeichner:str):
        if bezeichner.len() > 0:
            self.__bezeichner = bezeichner
        else:
            print("Bezeichnung ist zu kurz. Bitte eine längere wählen.")

    # LH Getter
    def get_bezeichner(self):
        return self.__bezeichner
    