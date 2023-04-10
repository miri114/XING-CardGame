from deck import Deck

class Hand(Deck):
    def __init__(self, label):
        self.deck = []
        self.label = label
        self.xing_count = 1
        self.point_count = 0
    def __str__(self):
        return self.label + ':' + ' '.join([str(card) for card in self.deck])
    
    def get_label(self):
        return self.label
    
    def xing_win_count(self):
        return self.xing_count
    
    def game_points(self, deck):
        my_score = 0
        for card in deck:
            if int(card.only_rank()) > 9 or str(card) == '2♣':
                my_score += 1
            if (card.only_rank) == '10♦':
                my_score += 1
        return my_score
    