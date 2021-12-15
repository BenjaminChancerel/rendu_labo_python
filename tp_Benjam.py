import random
# I Card
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

# II Cards

class Cards:

    def __init__(self):
        self.listCard       = []
        self.counterCard    = 0

    def piocher(self):
        new_card    = 0
        verif       = input("piocher une carte ?")

        if verif == "yes":
            new_card            = random.randint(1, 52)
            self.counterCard    += 1
            self.listCard.append(new_card)
            print("Vos cartes : " + str(self.listCard))
            print("Votre nombre de carte : " + str(self.counterCard))
        else:
            print("bah dégage alors")

cards = Cards()
while True:
    cards.piocher()