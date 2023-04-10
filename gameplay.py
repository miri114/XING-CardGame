from time import sleep
from deck import Deck
from hand import Hand

### creating a deck ######
deck = Deck()

### This block creates 4 players to play the game
hands = []
for i in range(1,5):
    hands.append(Hand(f'P{i}'))
#### end block #######


#### This block is for drwaing last 4 deck-cards in game field #### 
def cards_in_field():
    field_cards = []
    for i in range(4):
        field_cards.append(deck.indexed_pop(-1))
    return field_cards
##### end block ######


###### Function : This block is for giving each player by 4 cards ######
def spread_cards():
    for i in range(4):
        for hand in hands:
            hand.add_card(deck.pop_card())
####### end block #####################

played_cards = []              ### declaring a list of played_cards

field_cards = cards_in_field()   ######  creating a variable of function cards_in_field

collected_cards = { 'P1':[], 'P2':[] , 'P3':[], 'P4':[]}    ##### This dictionary is for storing each card collected by each player (hand)

####################################################################################################################
### ## ################ ################## One round function start ################################################


def game_round():

    spread_cards()
    
    ############### In this piece of code, each player has its turn to drop a card #################
    print("\n")
    print("Card to Match :")
    print(field_cards[-1])

    print("\n")
    ## This first for loop is to have 4 rounds of card drop since each player has 4 cards
    for i in range(len(hands)):
        ## This second loop is to give each player the turn to drop a card
        for hand in hands:
            print(hand)
            my_turn = int(input(f"Player {hand.label}, your turn to drop a card: "))
            card_dropped = hand.indexed_pop(my_turn)
            print(card_dropped.only_rank())
            played_cards.append(card_dropped)

######################### end here ##########################################

###############################    Some game logic here ##################################
            
            if(len(field_cards) != 0):

                print("\n")
                print("****Card to Match****:")
                print(f"**** {card_dropped} ****")
                print("\n")
####################  This if is to check if the card droped is the same as last card in field ##################
                if (card_dropped.only_rank() == field_cards[-1].only_rank()):
                    print(f'***Player {hand.label}, COLLECT YOUR CARDS***')
                    ############ If there is only one card in field ############ THAN XING - XING ############## 
                    if len(field_cards) ==  1:
                        print(f"XING-XING-XING --> {hand.xing_win_count()}")
                        
                    field_cards.append(card_dropped)

                    collected_cards[hand.label] += field_cards
                    print(f"{hand.label} : {[str(card) for card in field_cards]}")

                    field_cards.clear()
                    print("\n")
                    print("Field is Empty, drop a card")
                    print("\n")

                elif card_dropped.only_rank() == 'F':
                    print(f'***Player {hand.label}, COLLECT YOUR CARDS***')

                    field_cards.append(card_dropped)
                    collected_cards[hand.label] += field_cards
                    print(f"{hand.label} : {[str(card) for card in field_cards]}")
                    field_cards.clear()
                    print("\n")
                    print("Field is Empty, drop a card")
                    print("\n")
                else:
                    field_cards.append(card_dropped)
            else:
                field_cards.append(card_dropped)
    
    
def start_game():
    for i in range(3):
        if i < 2:
            print("Deliver next round cards")
            game_round()
            sleep(1)
        else:
            print("Last round cards")
            sleep(3)
            game_round()



############### After the end of the game, we need to print some results #############################
################ ############  RESULTS ################## #######################
def results():
    score_list = []
    for player, cards in collected_cards.items():
        # print(f"{player} : {[str(card) for card in cards]}")

        score = 0
        for card in cards:
            my_card = card.only_rank()
            if my_card == 'A':
                my_card = '11'
            elif my_card == 'F':
                my_card = '12'
            elif my_card == 'Q':
                my_card = '13'
            elif my_card == 'K':
                my_card = '14'
            
            if int(my_card) > 9 or str(card) == '2♣':
                score += 1
            if str(card) == '10♦':
                score += 1
        print (f"{player} : {score}")
        score_list.append(score)

    print("\n")
    print(" ******** MaxScore Below *************** ")
    print (f"Congrats P{score_list.index(max(score_list)) + 1}, you the winner with score : {max(score_list)} ")
###################################################################################
#################################################################################### 


########## This function is to attach last round cards in field ##########
########## to the last hand that took the cards #########################

