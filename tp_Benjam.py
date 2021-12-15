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
#print(card.Display())

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
#while True:
#    cards.piocher()

# III. Game

class Game:

    def __init__(self):
        self.listcardJoueur1    = []
        self.listcardJoueur2    = []
        self.listcardCroupier   = []

        self.player = "J1"

        Game.distribution_j(self)
        Game.distribution_c(self)
        Game.distribution_j(self)

    def distribution_j(self):
        new_card_1 = random.randint(1, 11)
        new_card_2 = random.randint(1, 11)
        if self.player == "J1":
            self.listcardJoueur1.append(new_card_1)
            self.listcardJoueur1.append(new_card_2)
            print("Voici les nouvelles cartes du joueur 1 " \
                + str(new_card_1) + " " \
                + str(new_card_2))
            self.player = "C"
        elif self.player == "J2":
            self.listcardJoueur2.append(new_card_1)
            self.listcardJoueur2.append(new_card_2)
            print("Voici les nouvelles cartes du joueur 2 " \
                + str(new_card_1) + " "\
                + str(new_card_2))
            self.player = "J1"
        
    def distribution_c(self):
        new_card = random.randint(1, 11)
        if self.player == "C":
            self.listcardCroupier.append(new_card)
            print("Voici les nouvelles cartes du Croupier " \
                + str(new_card))
            self.player = "J2"


    def pioche(self):
        new_card    = 0

        new_card = random.randint(1, 11)
        if self.player == "J1":
            self.listcardJoueur1.append(new_card)
            print(new_card)
            if sum(self.listcardJoueur1) > 21:
                self.listcardJoueur1.clear()
                print("dégage")
        elif self.player == "J2":
            self.listcardJoueur2.append(new_card)
            print(new_card)
            if sum(self.listcardJoueur1) > 21:
                self.listcardJoueur1.clear()
                print("dégage")
        elif self.player == "C":
            self.listcardCroupier.append(new_card)
            print(new_card)
            if sum(self.listcardJoueur1) > 21:
                self.listcardJoueur1.clear()
                print("dégage")
    
    def play(self):

        print(self.player)
        instruction = input("Que voulez vous faire ? |piocher|stop|")

        if self.player == "J1":
            print(self.listcardJoueur1)
            while sum(self.listcardJoueur1) <= 21:
                if instruction == "piocher" :
                    Game.pioche(self)
                    print(self.listcardJoueur1)
                elif instruction == "stop":
                    self.player = "J2"
                    break
                if instruction == "somme":
                    print(str(sum(self.listcardJoueur1)))
                elif sum(self.listcardJoueur1) == 21:
                    print("You win !")
                    self.player = "J2"
                    break
                elif sum(self.listcardJoueur1) > 21:
                    print("You're out")
                    self.player = "J2"
                    self.listcardJoueur1.clear()
                    break   

game = Game()
while True:
    game.play()


