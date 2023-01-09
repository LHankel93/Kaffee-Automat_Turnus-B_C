# LH Nötige Imports sollte nur RezeptTeil sein laut UML
import RezeptTeil

# LH Angebot Klasse
class Angebot:
    # LH Konstruktor für Angebot Klasse
    def __init__(self, bezeichner, rezept=[]):
        self.__bezeichner = bezeichner
        # RezeptTeile einpflegen in Liste Rezept
        """ 
        Espresso:
        1 x Espresso
        o Espresso macchiato:
        1 x Espresso + 1 x Milchschaum
        o Cappuccino:
        1 x Espresso + 1 x heiße Milch
        + 2 x Milchschaum
        o Café Latte:
        2 x heiße Milch + 1 x Milchschaum
        + 1 x Espresso
        """
        match bezeichner.upper():
            case "ESPRESSO":
                self.__rezept.append(RezeptTeil().__init__("ESPRESSO"))
                pass
            case "ESPRESSO MACCHIATO":
                self.__rezept.append(RezeptTeil().__init__("ESPRESSO"))
                self.__rezept.append(RezeptTeil().__init__("MILCHSCHAUM"))
                pass
            case "CAPPUCCINO":
                self.__rezept.append(RezeptTeil().__init__("ESPRESSO"))
                self.__rezept.append(RezeptTeil().__init__("HEISSE MILCH"))
                self.__rezept.append(RezeptTeil().__init__("MILCHSCHAUM"))
                self.__rezept.append(RezeptTeil().__init__("MILCHSCHAUM"))
                pass
            case "CAFE LATTE":
                self.__rezept.append(RezeptTeil().__init__("HEISSE MILCH"))
                self.__rezept.append(RezeptTeil().__init__("HEISSE MILCH"))
                self.__rezept.append(RezeptTeil().__init__("MILCHSCHAUM"))
                self.__rezept.append(RezeptTeil().__init__("ESPRESSO"))
                pass

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
