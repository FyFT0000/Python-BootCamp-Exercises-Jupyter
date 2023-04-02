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
card_suits = {'H':'Heart','D':'Diamond','C':'Clover','P':'Pikes'}

class Card():
    """  """
    def __init__(self,rank,suit) -> None:
        self.rank = rank
        self.suit = suit
    def __str__(self) -> str:
        return f'{str(self.rank):3}{card_suits[self.suit]:8}'


class Dealer():
    """  """
    def __init__(self,number_decks,chips_bank) -> None:
        self.number_decks = number_decks
        self.chips_bank = chips_bank
        self.deck = []
        self.control_card = 'CC'
    
    def deck_create(self):
        for n in range(self.number_decks):
            for rank in card_ranks:
                for suit in card_suits:
                    self.deck.append(Card(rank,suit))
    def deck_shuffle(self):
        shuffle(self.deck)
    def deck_add_cut_card(self):
        self.deck.append(self.control_card)
    def deck_control(self):
        pass
    def player_control(self):
        pass
    def game_start(self):
        pass
    def game_hit(self):
        pass
    def game_stay(self):
        pass

class Player():
    """ Player() """
    def __init__(self,p_name,chips_account) -> None:
        self.p_name = p_name
        self.chips_account = chips_account

    def chips_beat(self):
        pass
    def __str__(self) -> str:
        return f'Player {self.p_name} has: $ {self.chips_account}'

def cls():
    """ cls() """
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
            elif input_type.upper() == ("YoN") and keyboard_input.upper() in ('Y','N'):
                return keyboard_input
            elif input_type.upper() == ("STR"):
                return keyboard_input
            raise ValueError
        except ValueError:
            cls()
            print("The input value is worg or incorrect.")

def game_play():
    """  """
    dealer = Dealer(1,100000)
    player = Player('Facundo',1000)
    #dealer = Dealer(input_control('INT','Please select the number of deck (1 to 8)'),100000)
    #player = Player(input_control('STR','Please input the player name'),input_control('INT','Please select the amount to play'))


    while True:
        print(1)
        break





    print(player)
    print('1------')
    for n in dealer.deck:
        print(n, end=" ")
    print(f'\nthe lenght is {len(dealer.deck)}')
    print('2------')
    dealer.deck_create()
    j=0
    for n in dealer.deck:
        print(n, end=" ")
        j+=1
    print(f'\nthe lenght is {len(dealer.deck)}')
    print('3------')
    dealer.deck_shuffle()
    for n in dealer.deck:
        print(n, end=" ")
    print(f'\nthe lenght is {len(dealer.deck)}')
    print('4------')
    dealer.deck_add_cut_card()
    i=0
    for n in dealer.deck:
        print(n, end=" ")
        i += 1
    print(f'\nthe lenght is {len(dealer.deck)}')
    print(i)


game_play()


card1 = Card(1,'H')
print(card1)