class Card:

    def __init__(self, value, color):
        self.value = value
        self.color = color

    def getClasses(self) :
        return self.value, self.color

    def Display(self):
        print("Valeur de la carte : " + self.value \
            + ", Couleur de la carte : " + self.color)
    
card = Card("4", "red")
print(card.Display())