'''
This is a basic black jack game. The player can only hit or stand.
'''
import random
import time
import os


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    
class Deck:
    
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))
        self.shuffle()
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        random.shuffle(self.all_cards)
        
    def deal(self):
        try:
            return self.all_cards.pop()
        except IndexError:
            self = Deck()
            return self.all_cards.pop()


class Hand:

    def __init__(self):
        self.cards = []
        self.raw_value = 0
        self.adjusted_value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.raw_value += card.value
        self.adjusted_value = self.raw_value
        if card.rank == 'Ace':
            self.aces += 1
            self.adjust_for_ace()
        
    def adjust_for_ace(self):
        if self.aces > 0 and self.raw_value > 21:
            for i in range(0, self.aces):
                if (self.raw_value - (i+1)*10) <= 21:
                    self.adjusted_value = self.raw_value - (i+1)*10
                    break

    def print_hand(self):
        for card in self.cards:
            print(card)
        print(f"Value: {self.adjusted_value}")

    def print_hand_dealer(self):
        print("????")
        print(self.cards[1])

    def is_bust(self):
        if self.adjusted_value > 21:
            return True
        else:
            return False
    
class Chips:

    def __init__(self):
        self.total = 1000
        self.bet = 0
    
    def set_bet(self, amount):
        if amount > self.total:
            return False
        else:
            self.bet = amount
            return True
            
    def win_bet(self):
        self.total += self.bet
        
        
    def lose_bet(self):
        self.total -= self.bet
        

def bet(chips):
    while True:
        try:
            amount = int(input("How much would you like to bet?\n"))
        except ValueError:
            print("Please enter a number.")
            continue
        else:
            if amount <= 0:
                print("Your bet must be greater than 0.")
                continue
            elif chips.set_bet(amount):
                break
            else:
                print("That's more than you have.")
                continue

def hit(hand, deck):
    hand.add_card(deck.deal())

def print_hands(playerHand, dealerHand):
    print("Dealer's hand:")
    dealerHand.print_hand_dealer()
    print("\nYour hand:")
    playerHand.print_hand()
    print("")
    
def print_hands_dealer_turn(playerHand, dealerHand):
    print("Dealer's hand:")
    dealerHand.print_hand()
    print("\nYour hand:")
    playerHand.print_hand()
    print("")
    

def hit_or_stand():
    while True:
        
        try:
            hitOrStand = int(input("1: Hit\n2: Stand\n"))
        except ValueError:
            print("Enter 1 to hit or 2 to stand.")
            continue
        else:
            if hitOrStand == 1:
                answer = "Hit"
                break
            elif hitOrStand == 2:
                answer = "Stand"
                break
            else:
                print("Enter 1 to hit or 2 to stand.")
                continue
    return answer

playerChips = Chips()

gameDeck = Deck()

while playerChips.total > 0:
    os.system('cls')
    playerHand = Hand()
    dealerHand = Hand()
    #Player enters his bet
    print(f"Total chips: {playerChips.total}")
    bet(playerChips)
    print("")
    
    #The initial deal
    hit(playerHand, gameDeck)
    hit(dealerHand, gameDeck)
    hit(playerHand, gameDeck)
    hit(dealerHand, gameDeck)
    
    #Display both player's hands
    print_hands(playerHand, dealerHand)
    
    #Check for Black Jack
    if playerHand.adjusted_value == 21:
        playerChips.win_bet()
        input("Black Jack! Enter anything to continue.\n")
        continue
    
    #Player's turn
    while True:
        
        answer = hit_or_stand()
        if answer == "Hit":
            hit(playerHand, gameDeck)
            os.system('cls')
            print_hands(playerHand, dealerHand)
            if playerHand.adjusted_value > 21:
                break
        else:
            break

    #Check if the player is bust
    if playerHand.adjusted_value > 21:
        playerChips.lose_bet()
        input("Bust! Enter anything to continue.\n")
        continue
    
    #Dealer's turn
    while True:
        os.system('cls')
        print_hands_dealer_turn(playerHand, dealerHand)
        time.sleep(1)
        #Hit until 17 or higher
        if dealerHand.adjusted_value >= 17:
            break
        else:
            hit(dealerHand, gameDeck)
            time.sleep(1)
            
    
    #Calculate final result
    if dealerHand.adjusted_value > 21:
        print("The dealer busts!")
        playerChips.win_bet()
    elif dealerHand.adjusted_value > playerHand.adjusted_value:
        print("You lost this hand, better luck next round!")
        playerChips.lose_bet()
    elif dealerHand.adjusted_value < playerHand.adjusted_value:
        print("You won! Enter anything to continue.")
        playerChips.win_bet()
    else:
        print("Draw! Enter anything to continue.")
     
    #Check if the player still has checks left to bet
    if playerChips.total == 0:
        break
        
    #Ask the player if s/he wants to continue playing
    while True:
        try:
            play = int(input("Continue playing?\n1: Yes\n2: No\n"))
        except TypeError:
            print("Enter 1 to continue or 2 to quit.")
        else:
            if not(play == 1 or play == 2):
                print("Enter 1 to continue or 2 to quit.")
                continue
            else:
                break
    
    if play == 1:
        continue
    else:
        break
    
print(f"Game over. You walk away with {playerChips.total}.")