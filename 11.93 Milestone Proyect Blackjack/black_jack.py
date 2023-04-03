""" BlackJack card play
Considerations for this game:
Dealer: CPU
Player: Human, only one player
Cards: standard deck of 52 cards

Game Rules:
    _Player Goal,  is to get a hand total of closer to 21 than the dealer without going over 21 (busting).
    _Player start te game.
    _Ignore actions like: Insurance, Split, DoubleDown.
    _Jack,Queen,King value is 10
    _Ace is 11, unless the hand > 21, in which case it is 1.
    _Total of 21 on the first two cards is a "natural" or "blackjack".
    _A blackjack beats any hand that is not a blackjack, even one with a value of 21.
    _When the cut card is reached this indicates the final deal of the game before the cards are shuffled.
    _Select number of decks (1,2,4,6,8)
    _https://www.pagat.com/banking/blackjack.html
 """

from random import shuffle
import os

card_ranks = {'A':11,'K':10,'Q':10,'J':10,10:10,9:9,8:8,7:7,6:6,5:5,4:4,3:3,2:2}
card_ranks_21 = {'K':10,'Q':10,'J':10,10:10,9:9,8:8,7:7,6:6,5:5,4:4,3:3,2:2,'A':1}
card_suits = {'H':'Heart','D':'Diamond','C':'Clover','P':'Pikes'}

class Card():
    """  """
    def __init__(self,rank,suit) -> None:
        self.rank = rank
        self.suit = suit
    def __str__(self) -> str:
        if self.rank == "??" or self.suit == "?????":
            return f'{str(self.rank):3}{str(self.suit):8}'
        else:
            return f'{str(self.rank):3}{card_suits[self.suit]:8}'


class Dealer():
    """  """
    def __init__(self,number_decks,chips_bank) -> None:
        self.number_decks = number_decks
        self.chips_bank = chips_bank
        self.deck = []
        self.player_cards = []
        self.dealer_cards = []
        self.control_card = 'CC'
        self.player_card_sum = 0
        self.dealer_card_sum = 0
        self.player_card_bj = False
        self.dealer_card_bj = False
    
    def deck_create(self):
        for n in range(self.number_decks):
            for rank in card_ranks:
                for suit in card_suits:
                    self.deck.append(Card(rank,suit))
    def deck_shuffle(self):
        shuffle(self.deck)
    def deck_add_cut_card(self):
        self.deck.append(Card('??','?????'))
    def deck_add_played_cards(self):
        self.deck.extend(self.player_cards)
        self.deck.extend(self.dealer_cards)
    def deck_control_cut_card(self,index):
        if (self.deck[index].rank) == "??":
            self.deck.pop(index)
            self.deck_shuffle()
            self.deck_add_cut_card()
        pass
    def game_start(self):
        self.player_cards = []
        self.dealer_cards = []
        self.deck_control_cut_card(0)
        self.player_cards.append(self.deck[0])
        self.deck.pop(0)
        self.deck_control_cut_card(1)
        self.dealer_cards.append(self.deck[1])
        self.deck.pop(1)
        self.deck_control_cut_card(2)
        self.player_cards.append(self.deck[2])
        self.deck.pop(2)
        self.deck_control_cut_card(3)
        self.dealer_cards.append(self.deck[3])
        self.deck.pop(3)
    def game_hit_player(self):
        self.deck_control_cut_card(0)
        self.player_cards.append(self.deck.pop(0))
    def game_hit_dealer(self):
        self.deck_control_cut_card(0)
        self.dealer_cards.append(self.deck.pop(0))
    def game_player_control(self):
        #In case of Blackjack
        self.player_card_bj = False
        self.player_card_sum = ((card_ranks[self.player_cards[0].rank] + card_ranks[self.player_cards[1].rank]))
        if self.player_card_sum == 21:
            self.player_card_bj = True
            return False
        #Check if sum of cards > 21
        self.player_card_sum = sum(map(lambda c:card_ranks[c.rank],self.player_cards))
        if self.player_card_sum > 21:
            #Check if A value is 11 or 1
            self.player_card_sum = sum(map(lambda c:card_ranks_21[c.rank],self.player_cards))
            if self.player_card_sum > 21:
                return False
            return True
        return True
    
    def game_dealer_control(self):
        #Check if player loose
        if self.game_player_control() == False:
            return False
        #In case of Blackjack
        self.dealer_card_bj = False
        self.dealer_card_sum = ((card_ranks[self.dealer_cards[0].rank] + card_ranks[self.dealer_cards[1].rank]))
        if self.dealer_card_sum == 21:
            self.dealer_card_bj = True
            return False
        #Check Soft 17
        self.dealer_card_sum = sum(map(lambda c:card_ranks[c.rank],self.dealer_cards))
        if self.dealer_card_sum > 17:
            #Check if A value is 11 or 1
            self.dealer_card_sum = sum(map(lambda c:card_ranks_21[c.rank],self.dealer_cards))
            if self.dealer_card_sum > 17:
                return False
            return True
        return True

    def print_player(self,p_name):
        print(f'Cards of {p_name:10}: ',end="")
        for n in self.player_cards:
            print(n, end="")
        print("")
    def print_dealer_start(self):
        print('Cards of House     : ',end="")
        unknow = Card("??","?????")
        print(unknow,end="")
        print(self.dealer_cards[1], end="")
        print("")
    def print_dealer(self):
        print('Cards of House     : ',end="")
        for n in self.dealer_cards:
            print(n, end="")
        print("")

    
class Player():
    """ Player() """
    def __init__(self,p_name,chips_account) -> None:
        self.p_name = p_name
        self.chips_account = chips_account
        self.beat = 0
        self.card_sum = 0

    def chips_beat(self):
        if self.chips_account <= 0:
            print("You don't have enought chips to continue playing. END of the game")
            return False
        cls()
        print(self)
        if input_control('YoN','Do you want to play a round?, selec Y or N') == "Y":
            while True:
                self.beat = 0
                self.beat = input_control('INT','How much do you want to beat?')
                if self.beat <= self.chips_account:
                    self.chips_account -= self.beat
                    return True
                else:
                    print(f"Problem!. The amount to beat is grater than your chips: ${self.chips_account}")

    def __str__(self) -> str:
        return f'Player {self.p_name} has: $ {self.chips_account}'

# """ ---------------------------------- """
def cls():
    """ cls() """
    #print("\n")
    os.system('cls' if os.name=='nt' else 'clear')

def input_control(input_type,message):
    """
    Control de requiered imput.
    input_type:
    INT:    for a integer number -> return int
    YoN:    for Yes or No -> return Y or N
    STR:    any string -> return the string
    message: str to show in the input.
    """
    
    while True:
        try:
            keyboard_input = input(f'{message} ->: ')

            if input_type.upper() == ("INT"):
                return int(keyboard_input)
            
            elif (input_type.upper() == ("YON")) and (keyboard_input.upper() in ('Y','N')):
                return keyboard_input.upper()
            
            elif input_type.upper() == ("STR"):
                return keyboard_input
            
            else:
                raise ValueError
            
        except ValueError:
            cls()
            print("The input value is worg or incorrect.")

def game_win_control(dealer,player):
    if dealer.player_card_bj == True:
        if dealer.dealer_card_bj == True:
            player.chips_account += player.beat
            print ('Dual BlackJack!!!. Is a Tie')
        else:
            player.chips_account += (player.beat)*2.5
            dealer.chips_bank -= player.beat*1.5
            print ('BlackJack!!!. Player Win!')
    elif dealer.dealer_card_bj == True:
        dealer.chips_bank += player.beat
        print ('BlackJack!!!. House Win!')
    elif dealer.player_card_sum > 21:
        dealer.chips_bank += player.beat
        print ('Player Bust. The House Win!')
    elif dealer.dealer_card_sum > 21:
        player.chips_account += (player.beat)*2
        dealer.chips_bank -= player.beat
        print ('House Bust. The Player Win!')
    elif dealer.player_card_sum == dealer.dealer_card_sum:
        player.chips_account += player.beat
        print ('Same Values. Is a Tie')
    elif dealer.player_card_sum > dealer.dealer_card_sum:
        player.chips_account += (player.beat)*2
        dealer.chips_bank -= player.beat
        print ('The Player Win!')
    else:
        dealer.chips_bank += player.beat
        print ('The House Win!')
    player.beat = 0

# """ ---------------------------------- """

def game_play():
    """  """
    dealer = Dealer(1,100000)
    player = Player('Facundo',1000)
    #dealer = Dealer(input_control('INT','Please select the number of deck (1 to 8)'),100000)
    #player = Player(input_control('STR','Please input the player name'),input_control('INT','Please select the amount to play'))
    dealer.deck_create()
    dealer.deck_shuffle()
    dealer.deck_add_cut_card()
    i = 0
    

    while player.chips_beat():
        j = 0
        k = 0
        dealer.game_start()
        cls()
        dealer.print_player(player.p_name)
        dealer.print_dealer_start()

        while dealer.game_player_control():
            if (input_control("YoN","Please input Y if you want to Hit another cadd, else input N")) == "Y":
                dealer.game_hit_player()
            else:
                break
            cls()
            dealer.print_player(player.p_name)
            dealer.print_dealer_start()
            j += 1

        #print(f'\nThe counter j is: {j}')
        #print('----------------------')

        while dealer.game_dealer_control():
            dealer.game_hit_dealer()
            cls()
            dealer.print_player(player.p_name)
            dealer.print_dealer()
            k += 1

        #print(f'\nThe counter k is: {k}')
        #print('--------------------------------------------')
        
        dealer.deck_add_played_cards()
            
        game_win_control(dealer,player)

        cls()
        print(player)
        dealer.print_player(player.p_name)
        print(dealer.player_card_bj)
        print(dealer.player_card_sum)

        dealer.print_dealer()
        print(dealer.dealer_card_bj)
        print(dealer.dealer_card_sum)

        i += 1
        #print(f'\nThe counter i is: {i}')

        print("-------------")
        for n in dealer.deck:
            print(n, end=" ")
        print(f'\nthe lenght is {len(dealer.deck)}')
        print('------------------------------------------------------------------')

        
        




    
    cls()
    dealer.print_player(player.p_name)
    print(dealer.player_card_sum)
    dealer.print_dealer()
    print(dealer.dealer_card_sum)
     
    


    #s1 = sum(map(lambda c:card_ranks[c],dealer.player_cards))
    #print(s1)
    

    print("-------------")
    for n in dealer.deck:
        print(n, end=" ")
    print(f'\nthe lenght is {len(dealer.deck)}')



# """ ---------------------------------- """

game_play()

