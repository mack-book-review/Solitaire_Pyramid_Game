import pygame
from pygame.locals import *
import random
from card import Card

class Deck:

    def __init__(self,suits=("Clubs","Spades","Diamond","Hearts")):
        self.cards = []
        for suit in suits:
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)
        self.shuffle()

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            idx = random.randint(0,i-1)
            temp = self.cards[idx]
            self.cards[idx] = self.cards[i]
            self.cards[i] = temp

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()

    def add_cards(self,new_cards):
        for card in new_cards:
            if card.faceup:
                card.flip()
            self.cards.insert(0,card)