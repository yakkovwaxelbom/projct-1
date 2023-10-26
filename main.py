import random


class Card:
    def __init__(self, value: str, suit=None):
        # self.__name = None
        self.__rank = None
        self.__suit = None
        self.__value = None
        self.check_card(value, suit)
        self.get_card_rank(value)

    def check_card(self, value, suit):
        if value == 'Joker':
            # self.__name = 'Joker'
            self.__value = 'Joker'
            self.__suit = 'x'  # I force the joker to be at the end of the deck when I sort
        else:
            suits = ['Heart', 'Diamond', 'Club', 'Spade']
            names = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
            if value in names and suit in suits:
                # self.__name = f'{value},{suit}'
                self.__value = value
                self.__suit = suit
            # else:
            #     raise ValueError()

    def get_card_rank(self, value):
        ranks = {'A': 13, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, 'J': 10, 'Q': 11,
                 'K': 12, 'Joker': float('inf')}
        self.__rank = ranks[value]

    def get_rank(self):
        return self.__rank

    def get_suit(self):
        return self.__suit

    def get_value(self):
        return self.__value

    def __lt__(self, other):
        return self.__rank < other.__rank

    def __gt__(self, other):
        return self.__rank > other.__rank

    def __eq__(self, other):
        return self.__rank == other.__rank

    def __str__(self):
        return f'({self.__value},{self.__suit})'

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        self.__deck = []
        self.creating_a_package()
        self.shuffle()

    def creating_a_package(self):
        suits = ['Heart', 'Diamond', 'Club', 'Spade']
        names = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for name in names:
                self.__deck.append(Card(name, suit))
        self.__deck.append(Card('Joker'))
        self.__deck.append(Card('Joker'))

    def shuffle(self):
        random.shuffle(self.__deck)

    def draw(self):
        card = self.__deck[0]
        self.__deck.pop(0)
        return card

    def __len__(self):
        return len(self.__deck)

    def __getitem__(self, i):
        if self.__deck[i]:
            return self.__deck[i]

    def get_deck(self):
        return self.__deck

    def sort_by_suit(self):
        self.__deck.sort(key=lambda card: (card.get_suit(), card.get_rank()))

    def sort_by_rank(self):
        self.__deck.sort(key=lambda card: (card.get_rank(), card.get_suit()))

    def deal_hand(self, num_cards):
        hand = []
        for i in range(num_cards):
            hand.append(self.draw())
        return hand

    def count_cards(self):
        count = {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0,
                 'K': 0, 'Joker': 0}
        for i in range(len(self.__deck)):
            count[self.__deck[i].get_value()] += 1
        return count


class Player:
    def __init__(self, name, hand: list):
        self.name = name
        self.hand = hand
        self.score = 0

    def __repr__(self):
        return str(self.name)

    def __len__(self):
        return len(self.hand)


class Game:
    def __init__(self, player_1='player_1', player_2='player_2'):
        self.winner = False
        self.deck = Deck()
        self.player_1 = Player(player_1, hand=self.deck.deal_hand(26))
        self.player_2 = Player(player_2, hand=self.deck.deal_hand(26))

    def receive_and_take_cards(self, win_player_1, i=0, j=0):
        if win_player_1:
            for i in range(0, j):
                self.player_1.hand.append(self.player_2.hand.pop(0))
                self.player_1.hand.append(self.player_1.hand.pop(0))
            self.player_1.score += j
        else:
            for j in range(0, i):
                self.player_2.hand.append(self.player_1.hand.pop(0))
                self.player_2.hand.append(self.player_2.hand.pop(0))
            self.player_2.score += i

    def war(self):
        i = 3
        try:
            while self.player_1.hand[i] == self.player_2.hand[i]:
                i += 3
            self.play_round(i, i)
        except IndexError:
            if len(self.player_1.hand) - 1 > i > len(self.player_2.hand) - 1:
                self.play_round(i, len(self.player_2.hand) - 1)
            elif len(self.player_2.hand) - 1 > i > len(self.player_1.hand) - 1:
                self.play_round(len(self.player_1.hand) - 1, i)
            else:
                self.play_round(len(self.player_1.hand) - 1, len(self.player_2.hand) - 1, True)
        # self.play_round(i, i)

    def play_round(self, i=0, j=0, test=False):
        if self.player_1.hand[i].__gt__(self.player_2.hand[j]) and test is False:
            self.receive_and_take_cards(True, j=j + 1)
        elif self.player_1.hand[i].__lt__(self.player_2.hand[j]) and test is False:
            self.receive_and_take_cards(False, i=i + 1)
        elif self.player_1.hand[i].__eq__(self.player_2.hand[j]) and test is False:
            self.war()
        else:
            self.winner = True

    def get_winner(self):
        if len(self.player_1.hand) == 0 or len(self.player_2.hand) == 0:
            self.winner = True

    def play(self, i=100):
        while i > 0:
            i -= 1
            self.get_winner()
            if not self.winner:
                self.play_round()
                print(f'yakov: {self.player_1.hand}')
                print(f'shloimy: {self.player_2.hand}')
        if self.player_1.score > self.player_2.score:
            print(f'{self.player_1} is win')
        elif self.player_1.score < self.player_2.score:
            print(f'{self.player_2} is win')
        else:
            print('Draw: The motley programmer is lost on you')


a = Game('yakov', 'shloimy')
a.play(200)


# def war(array):
#     if len(array):
#         return array
#     current = []
#     for i in range(3):
#         try:
#             current.append(array.pop(0))
#         except IndexError:
#             break
#         # current.append(self.player_1.hand.pop(0))
#     try:
#         if current[len(current) - 1] == current[len(current) - 2]:
#             current += war(array)
#     except IndexError:
#         current += war(array)
#     return current
# def war_3(array_1, array_2, i):
#     for i in range(0, i):
#         array_1.append(array_2.pop(0))
#     return array_1, array_2
#
#
# def war_1(array_1, array_2, i):
#     if len(array_1) - 1 > i and len(array_2) - 1 > i:
#         if array_1[i] > array_2[i]:
#             return war_3(array_1, array_2, i + 1)
#         else:
#             return war_3(array_2, array_1, i + 1)
#     elif len(array_1) - 1 > i:
#         if array_1[i] > array_2[len(array_2) - 1]:
#             return war_3(array_1, array_2, len(array_2) - 1)
#         else:
#             return war_3(array_2, array_1, i + 1)
#     elif len(array_2) - 1 > i:
#         if array_1[len(array_1) - 1] > array_2[i]:
#             return war_3(array_1, array_2, i + 1)
#         else:
#             return war_3(array_2, array_1, len(array_1) - 1)
#     else:
#         if array_1[len(array_1) - 1] > array_2[len(array_2) - 1]:
#             return war_3(array_1, array_2, len(array_2) - 1)
#         else:
#             return war_3(array_2, array_1, len(array_1) - 1)


#
# def war_2(array_1, array_2, i):
#     if array_1[i] > array_2[i]:
#         for i in range(0, i + 1):
#             array_1.append(array_2.pop(0))
#     else:
#         for i in range(0, i + 1):
#             array_2.append(array_1.pop(0))
#     return array_1, array_2

#
def war(array_1, array_2):
    i = 3
    try:
        while array_1[i] == array_2[i]:
            i += 3
    except IndexError:
        if len(array_1) - 1 > i > len(array_2) - 1:
            return war_1(array_1, array_2, i, len(array_2) - 1)
        elif len(array_2) - 1 > i > len(array_1) - 1:
            return war_1(array_1, array_2, len(array_1) - 1, i)
        else:
            return war_1(array_1, array_2, len(array_1) - 1, len(array_2) - 1)
    return war_1(array_1, array_2, i)
#
#
# w = [1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9, 9, 1, 1, 1, 1, 1, 2, 3, 4]
# k = [5, 6]
#
#
# def war_3_1(array_1, array_2, i):
#     for i in range(0, i):
#         array_1.append(array_2.pop(0))
#     return array_1, array_2
#
#
# def war_6(array_1, array_2):
#     i, j = 3, 3
#     while array_1[i] == array_2[j]:
#         if i + 3 > len(array_1) - 1:
#             i += 3
#         else:
#             i = len(array_1) - 4
#             all_in = True
#         if j + 3 > len(array_2) - 1:
#             j += 3
#         else:
#             i = len(array_2) - 4
#             all_in = True
#     return play_round(array_1, array_2, i, j)
#     # return war_1(array_1, array_2, 4 * i - 1)
#
#
# def play_round(array_1, array_2, i=0, j=0):
#     if array_1[i] > array_2[j]:
#         return war_3(array_1, array_2, j + 1)
#     elif array_1[i] < array_2[j]:
#         return war_3_1(array_2, array_1, i + 1)
#     else:
#         return war(array_1, array_2)

#
# a_1 = [1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9, 9]
# b_2 = [1, 1, 1, 1, 1, 2, 3, 4, 5, 6, ]
# x, y = play_round(a_1, b_2)
# print(x)
# print(y)

# yakov: [(A,Club), (7,Heart), (Q,Spade), (2,Heart), (3,Heart)]
# shloimy: [(A,Heart), (2,Club), (Q,Club), (2,Spade), (K,Club), (4,Club), (9,Spade), (4,Heart), (6,Spade), (8,Spade), (8,Heart), (Q,Diamond), (6,Diamond), (Joker,x), (Joker,x), (2,Diamond), (5,Club), (4,Spade), (7,Club), (4,Diamond), (10,Diamond), (J,Heart), (K,Heart), (5,Diamond), (5,Spade), (9,Heart), (J,Spade), (5,Heart), (8,Diamond), (10,Heart), (K,Diamond), (3,Spade), (J,Club), (7,Spade), (K,Spade), (6,Heart), (7,Diamond), (3,Club), (A,Spade), (J,Diamond), (A,Diamond), (9,Diamond), (10,Spade), (9,Club), (Q,Heart), (3,Diamond), (6,Club)]
