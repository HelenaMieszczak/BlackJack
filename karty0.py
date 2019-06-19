import random


class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    ''' Trefl - Clubs (c),
        Karo - Diamonds (d),
        Kier - Hearts (h), 
        Pik - Spades (s)'''

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + ""
        else:
            rep = "<pusta>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Nie mogę dalej rozdawać. Zabrakło kart!")

class Unprintable_Card(Card):
    def __str__(self):
        return "<utajniona>"


class Positionable_Card(Card):
    def __init__(self, rank, suit, face_up=True):
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up

# card1 = Card(rank = "A", suit= "c")
# print('Wyświetlam obiekt karty (klasy "Card"):')
# print(card1)
# card2 = Card(rank='2', suit='c')
# card3 = Card(rank='3', suit='c')
# card4 = Card(rank='4', suit='c')
# card5 = Card(rank='5', suit='c')
# print('\nWyświetlam resztę obiektów po jednym na raz:')
# print(card2)
# print(card3)
# print(card4)
# print(card5)

# my_hand = Hand()
# print('\nWyświetlam zawartość mojej ręki przed dodaniem jakichkolwiek kart:')
# print(my_hand)
# my_hand.add(card1)
# my_hand.add(card2)
# my_hand.add(card3)
# my_hand.add(card4)
# my_hand.add(card5)
# print('\nWyświetlam zawartość mojej ręki po dodaniu 5 kart:')
# print(my_hand)

# your_hand = Hand()
# my_hand.give(card1, your_hand)
# my_hand.give(card2, your_hand)
# print("\nPrzekazuję pierwsze dwie karty z mojej ręki do Twojej.")
# print("----------------------------------")
# print("Twoja ręka:")
# print(your_hand)
# print("Moja ręka:")
# print(my_hand)
#
# my_hand.clear()
# print("\nMoja ręka po usunięciu z niej kart:")
# print(my_hand)
# input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

# deck1 = Deck()
# print("Utworzono nową talię.")
# print("Talia:")
# print(deck1)
# deck1.populate()
# print("\nDodałem do talii komplet kart.")
# print("Talia:")
# print(deck1)
# deck1.shuffle()
# print("\nPotasowałem talię kart.")
# print("Talia:")
# print(deck1)
# my_hand = Hand()
# your_hand = Hand()
# hands = [my_hand, your_hand]
# deck1.deal(hands, per_hand = 5)
# print("\nRozdałem sobie i Tobie po 5 kart.")
# print("Moja ręka:")
# print(my_hand)
# print("Twoja ręka:")
# print(your_hand)
# print("Talia:")
# print(deck1)
# deck1.clear()
# print("\nUsunąłem zawartość talii.")
# print("Talia:", deck1)
# input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

# card1 = Card("A", "c")
# card2 = Unprintable_Card("A", "d")
# card3 = Positionable_Card("A", "h")
# print("Wyświetlenie obiektu klasy Card:")
# print(card1)
# print("\nWyświetlenie obiektu klasy Unprintable_Card:")
# print(card2)
# print("\nWyświetlenie obiektu klasy Positionable_Card:")
# print(card3)
# print("Odwrócenie stanu obiektu klasy ``Positionable_Card`` (odkrycie-zakrycie karty).")
# card3.flip()
# print("Wyświetlenie obiektu klasy ``Positionable_Card``:")
# print(card3)

# input("\n\nAby zakończyć program, naciśnij klawisz Enter.")