class Card:

    suits = ['\u2666', '\u2665','\u2663','\u2660' ]
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'F' , 'Q', 'K', 'A']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    ## This function is used to have a string representation of Card class objects
    def __str__(self):
        return f"{Card.ranks[self.rank]}{Card.suits[self.suit]}"


    def only_rank(self):
        my_rank = str(Card.ranks[self.rank])
        return f"{my_rank}"
        
    def only_suit(self):
        my_suit = str(Card.suits[self.suit])
        return f"{my_suit}"