# -*- coding: utf-8 -*- #
""" #
Create an automated card dealer for a Texas Hold’em application. #
It should be able to handle Deck objects, consisting of Cards. #
Cards can be added or removed from Decks, and Decks can be shuffled and sorted. #
When dealing cards, each Player receives a Hand consisting of 2 Cards. #
After all cards are dealt, the Dealer should draw the table Hand of 5 Cards #
""" #
from random import shuffle as rshuffle #

class Card(object): #

    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] #
    colors = ['clubs', 'diamonds', 'hearts', 'spades'] #

    def __init__(self, value, color): #
        self._value = value #
        self._color = color #

    def get_value(self): #
        return self._value #

    def get_color(self): #
        return self._color #

    def get_item(self): #
        return (self._color, self._value) #

    def __str__(self): #
        return '({0:>2},{1:>8})'.format(self._value, self._color) #

class Deck(object): #

    def __init__(self): #
        self._deck = [] #

    def add_card(self, card): #
        self._deck.append(card) #

    def extend_deck(self, deck): #
        self._deck.extend(deck.get_cards()) #

    def get_cards(self): #
        return self._deck #

    def pop_card(self): #
        return self._deck.pop() #

    def remove_card(self, card): #
        self._deck.remove(card) #

    def shuffle(self): #
        rshuffle(self._deck) #

    def sort(self): #
        self._deck.sort(key=lambda x:x.get_value()) #

    @classmethod #
    def build_deck(cls): #
        d = Deck() #
        for color in Card.colors: #
            for value in Card.values: #
                d.add_card(Card(value, color)) #
        #d.sort() #
        return d; #

    def __str__(self): #
        result = '[' #
        for card in self._deck: #
            result+=card.__str__()+'\n' #
        result+=']' #
        return result #


class Player(object): #

    def __init__(self, name): #
        self._name = name #
        self._cards = [] #

    def get_name(self): #
        return self._name #

    def set_cards(self, cards): #
        self._cards = cards #

    def get_cards(self): #
        return self._cards #

    def __str__(self): #
        result = '[' #
        for card in self._cards: #
            result+=card.__str__()+',' #
        result+=']' #
        return '{0:20} | {1}'.format(self._name, result) #

class Dealer(Player): #
    _deck = Deck() #the large deck #

    def __init__(self, name, total_decks): #
        super(Dealer, self).__init__(name) #
        for i in range(total_decks): #
            d = Deck.build_deck() #
            Dealer._deck.extend_deck(d) #
        #print Dealer._deck #

    def deal(self, players): #
        Dealer._deck.shuffle() #
        for player in players: #
            cards = [] #
            for i in range(2): #
                cards.append(Dealer._deck.pop_card()) #
            player.set_cards(cards) #
        cards = [] #
        for i in range(5): #
            cards.append(Dealer._deck.pop_card()) #
        self.set_cards(cards) #

players = [Player('Paul'), Player('Zoli'), Player('Bogdan'), Player('Radu'), Player('Marcom')] #
dealer = Dealer('Za Dealer', 3) #
dealer.deal(players) #
print '-'*40 #
print dealer #
print '-'*40 #
for player in players: #
    print player #
print '-'*40 #