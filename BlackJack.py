import random
#global variables
suits = ['Hearts','Diamonds','Spades','Clubs']
ranks = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True
default = 100

#Class Definition
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += card.__str__() + '\n'
        return 'The deck has: \n' + deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = 0
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.ace +=1
    def adjust_for_ace(self):
        while self.value > 21 and self.ace:
                self.value -= 10
                self.ace -= 1

class Chips:
    def __init__(self,defalut):
        self.total= default #default 100
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

#Function Definition
def take_bet(chips):
    while True:
        try:
            bet = int(input("\nHow many chips would you like to bet?: "))
            if bet > 0:
                chips.bet = bet
            else:
                print("It must be a positive number!")
                continue
        except ValueError:
            print("Sorry, a bet must be a integer!")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, your bet can't exceed! You have total chips: {chips.total}")
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input("\nWould you like to hit or stand? Enter 'h' or 's': ").strip()
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            playing = False
        else:
            print('Sorry, please try agian.')
            continue
        break

def show_some(dealer,player):
    print('Dealer Card:\n<hidden card>')
    print(dealer.cards[1],)
    print('------------------')
    print('Player Card: ',*player.cards,sep='\n')

def show_all(dealer,player):
    print('\nShowing all card and value now:')
    print('Dealer Card: ',*dealer.cards,sep='\n')
    print('Dealer Value: ',dealer.value)
    print('------------------')
    print('Player Card: ',*player.cards,sep='\n')
    print('Player Value: ',player.value)

def player_busts(player,dealer,chips):
    print('\nPlayer Busts!')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('\nPlayer Wins!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('\nDealer Busts!')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('\nDealer Wins!')
    chips.lose_bet()

def push(player,dealer):
    print('\nPlayer ad Player tie, Push!')

#GamePlay!!!
while True:
    #Game instruction
    print(f"**Welcome to BlackJack! You have {default} chips! Get as closer to 21 as you can without going over! \n\
    Dealer hits untill she reaches 17. Aces conut as 1 or 11! **")

    #shuffled deck ready
    deck = Deck()
    deck.shuffle()

    #player, dealer with 2 card
    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    
    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())

    #chips ready
    player_chips = Chips(default)

    #bet ready
    take_bet(player_chips)

    #show some card
    show_some(dealer,player)

    #asking player: hit or stand
    while playing: #stop when player stands
        hit_or_stand(deck,player)
        show_some(dealer,player)
        if player.value > 21:
            player_busts(player,dealer,player_chips)
            break
        
    if player.value <= 21:
        #show dealer card, check if it is smaller than 17
        show_all(dealer,player)

        #if dealer have to add more card if it is smaller than 17
        print('\nDealer keeps hitting unitll the value is greater than 16!')
        while dealer.value < 17:
            hit(deck,dealer)
            print(f'Adding {dealer.cards[-1]}')
        
        #show all
        show_all(dealer,player)

        #checking the results
        if dealer.value > 21:
            dealer_busts(dealer,player,player_chips)
        elif dealer.value > player.value:
            dealer_wins(dealer,player,player_chips)
        elif player.value > dealer.value:
            player_wins(dealer,player,player_chips)
        else:
            push(dealer,player)

    default = player_chips.total
    print(f"\nYou have {player_chips.total}")

    #asking player to play agian
    new_game = input("\nDo you want to play agian? Enter 'y' or 'n': ").strip().lower()
    if new_game[0] == 'y':
        playing = True
        continue
    else:
        print('\nThanks for playing again!')
        break
        
        
        
            
        
        

    









    
    












        
