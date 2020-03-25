'''
Blackjack
'''

import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self):
        # 100 is default, later make a system to make the player input an amount of starting money
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How much would you like to bet? \nAmount: '))
        except ValueError:
            print('Please input a number.')
            continue
        else:
            if chips.bet <= chips.total:
                break
            else:
                print("You don't have enough chips")

def hit(deck,hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):

    global playing

    hit_or_stand_ask = str(input('[H]it or [S]tand? '))
    hit_ans = ['h','hit','H']
    stand_ans = ['s','stand','S']

    while True:
        if hit_or_stand_ask in hit_ans:
            
            hit(deck,hand)
            break
        elif hit_or_stand_ask in stand_ans:
            playing = False
            break
        else:
            print('Type a valid answer!')
            continue

def show_some(player,dealer):

    print("\nDealers hand:")
    print(dealer.cards[0])
    print('Second card hidden\n')

    print("Players hand:")
    for card in player.cards:
        print(card)

def show_all(player,dealer):

    print("Dealers hand:")
    for card in dealer.cards:
        print(card)

    print("\nPlayers hand")
    for card in player.cards:
        print(card)

def player_busts(player,dealer,chips):

    print("\nPlayer busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):

    print("\nPlayer wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):

    print("\nDealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):

    print("\nDealer wins!")
    chips.lose_bet()

def push(player,dealer):

    print("\nDealer and Player tie! It's a push.")

playing = True

while True:

    print('Blackjack!\n')

    # Create and shuffle deck
    main_deck = Deck()
    main_deck.shuffle()

    # Set up player chips
    players_chips = Chips()

    # Place players bet
    take_bet(players_chips)

    players_hand = Hand()
    dealers_hand = Hand()

    # Deal initial cards
    players_hand.add_card(main_deck.deal())
    players_hand.add_card(main_deck.deal())

    dealers_hand.add_card(main_deck.deal())
    dealers_hand.add_card(main_deck.deal())

    # Show cards (2 for player, both shown. 2 for dealer but only one shown)
    show_some(players_hand,dealers_hand)

    while playing:

        # Player hit or stand
        hit_or_stand(main_deck,players_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(players_hand,dealers_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if players_hand.value > 21:
            player_busts(players_hand,dealers_hand,players_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if players_hand.value <= 21:
        while dealers_hand.value <= 17:
            hit(main_deck,dealers_hand)

        # Show cards
        show_all(players_hand,dealers_hand)

        # Run different winning scenarios
        if dealers_hand.value > 21:
            dealer_busts(players_hand,dealers_hand,players_chips)
        elif players_hand.value == dealers_hand.value:
            push(players_hand,dealers_hand)
        elif players_hand.value > dealers_hand.value:
            player_wins(players_hand,dealers_hand,players_chips)
        elif players_hand.value < dealers_hand.value:
            dealer_wins(players_hand,dealers_hand,players_chips)        
    
    # Inform Player of their chips total 
    print(players_chips.total)

    # Ask to play again
    replay_ask = str(input('Play again? y / n: '))

    if replay_ask == 'y':
        playing = True
        continue
    else:
        break


