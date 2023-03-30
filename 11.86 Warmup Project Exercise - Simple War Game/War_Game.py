
""" Simple War Game, card game. """

import os
import random
import time

class Game():
    """ Game() calls that is used to ineritance to the classes Players and Cards """
    def __init__(self, player,turn):
        self.player = player
        self.turn = turn


class Card(Game):
    """ Card(Game) """
    def __init__(self, player, turn,rank,suits,color):
        self.player = player
        self.turn = turn
        self.rank = rank
        self.suits = suits
        self.color = color

    def __str__(self):
        print_card = self.rank
        if self.rank == 11: print_card = 'J'
        elif self.rank == 12: print_card = 'Q'
        elif self.rank == 13: print_card = 'K'
        elif self.rank == 14: print_card = 'A'
        return f'{self.player},{print_card}.{self.suits}'


class Player(Game):
    """ Player(Game) """
    def __init__(self, player, turn, packet):
        self.player = player
        self.turn = turn
        self.packet = packet

    def __str__(self):
        print_player = f'{self.player}:\n'
        for n in self.packet:
            print_player += f'{n} _ '
        print_player += f'\n{len(self.packet)}'
        return print_player


def cls():
    """ cls() """
    os.system('cls' if os.name=='nt' else 'clear')


def create_players():
    """ create_players() """
    select = "NO"
    while True:
        player1_name = input("Please enter de Player 1 name: ")
        player2_name = input("Please enter de Player 2 name: ")
        select = input(f"is the name {player1_name} and {player2_name}correct for Player 1 and Player 2?. YES / NO : ").upper()
        cls()
        if select.startswith("Y"):
            break
        else:
            print("Enter de desired name for the Player. Or YES if it is correct")
    return player1_name, player2_name


def random_cards():
    """ random_cards() """
    rank = (14,13,12,11,10,9,8,7,6,5,4,3,2)
    suits = ('Heart','Diamond','Clover','Pikes')
    color = ('Red','Black')
    packet = []

    for r in rank:
        for s in suits:
            if s in ('Heart','Diamond'):
                packet.append([r,s,'Red'])
            else:
                packet.append([r,s,'Black'])
    random.shuffle(packet)
    return packet


def deal_cards(packet,player1Name,player2Name):
    """ deal_cards(packet,player1Name,player2Name) """
    count = 0
    player1 = []
    player2 = []
    for p in packet:
        count += 1
        if count < (len(packet)+1)/2:
            player1.append(Card(player1Name,'Pile',p[0],p[1],p[2]))
        else:
            player2.append(Card(player2Name,'Pile',p[0],p[1],p[2]))
    p1 = Player(player1Name,'Pile',player1)
    p2 = Player(player2Name,'Pile',player2)
    return p1,p2


def game_win(p1,p2,i):
    """ game_win(p1,p2,i) """
    if len(p1.packet) > i and len(p2.packet) > i:
        return True
    else:
        if len(p1.packet) > len(p2.packet):
            print(f'Player {p1.player} Wins!!')
        else:
            print(f'Player {p2.player} Wins!!')
        return False


def game_battle(p1,p2,i):
    """ game_battle(p1,p2,i) """
    #time.sleep(0.01)
    print(f'{len(p1.packet):2} . {p1.packet[i].rank:2}  -  {p2.packet[i].rank:2} . {len(p2.packet):2}     {i:2}',flush=True)
    if p1.packet[i].rank > p2.packet[i].rank:
        n = 0
        while n <= i:
            p1.packet.append(p2.packet[0])
            p1.packet.append(p1.packet[0])
            p1.packet.pop(0)
            p2.packet.pop(0)
            n += 1
        return 'Battle'
    elif p1.packet[i].rank < p2.packet[i].rank:
        n = 0
        while n <= i:
            p2.packet.append(p1.packet[0])
            p2.packet.append(p2.packet[0])
            p2.packet.pop(0)
            p1.packet.pop(0)
            n += 1
        return 'Battle'
    else:
        return 'War'


def game_play():
    """ game_play() """
    turn = "Pile"

    player1_name, player2_name = create_players()
    #player1_name, player2_name = ('Ang','Fac')

    p1,p2 = deal_cards(random_cards(),player1_name,player2_name)
    print(p1)
    print(p2)
    cls()
    i = 0
    indice_battle = 0
    indice_war = 0
    indice_max_war = 0
    st = time.time()

    while game_win(p1,p2,i):
        turn = game_battle(p1,p2,i)
        if turn == "Battle":
            i = 0
            indice_battle += 1
        elif turn == 'War':
            i += 2
            indice_war += 1
            if i > indice_max_war:
                indice_max_war = i
            print('------- War -------',flush=True)
            time.sleep(0.5)

    et = time.time()

    print(f'Turns: {indice_war + indice_battle}, Battles: {indice_battle}, War: {indice_war}, Long War: {indice_max_war}')

    print('Time: ',f'{((et-st)*1000):.4f}',' miliseconds.')



game_play()
