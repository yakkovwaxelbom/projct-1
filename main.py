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
        if self.__suit == other.__suit:
            return self.__rank < other.__rank
        raise NotImplementedError()

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

    def __len__(self):
        return len(self.hand)


class Game:
    def __init__(self, player_1='player_1', player_2='player_2'):
        self.deck = Deck()
        self.player_1 = Player(player_1, hand=self.deck.deal_hand(26))
        self.player_2 = Player(player_2, hand=self.deck.deal_hand(26))


# x = Deck()
a = Game()
# print(len(a.player_1))
x = a.player_1.hand[0]
print(x)
# print(x.deal_hand(26))
# print(x[0].get_rank)
# x.sort_by_suit()
# print(x.get_deck())
# x.sort_by_rank()
# print(x.get_deck())
# print(x.deal_hand(5))
# print(x.count_cards())
# print(type(x.deck[0]))
# def set_suit(self, suit):
#     self.__suit = suit
# x.draw()
# print(x.count_cards())
# def set_data(slf, data):
#     self.__data = data
#
# def get_data(self):
#     return self.__data
#
# def get_next(self):
#     return self.__next
