from card import Card
import random 

class Deck:
    def __init__(self):
        self.deck = []
        for suit in range(4):
            for rank in range(13):
                my_Card = Card(suit, rank)
                self.deck.append(my_Card)
        self.shuffle()

    def __len__(self):
        return len(self.deck)
    
    def add_card(self, card):
        self.deck.append(card)

    def pop_card(self):
        return self.deck.pop()
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def indexed_pop(self, input):
        return self.deck.pop(input)


