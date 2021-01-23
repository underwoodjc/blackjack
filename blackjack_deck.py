'''
Generates blackjack deck with variable shoe length
'''
from blackjack_card import Card

from random import shuffle

class Deck():

	suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
	ranks = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')

	def __init__(self,shoe_number = 6):

		self.shoe_number = shoe_number
		self.all_cards = []

		ct = 1

		while ct <= shoe_number:
			for i in Deck.suits:
				for j in Deck.ranks:
					self.all_cards.append(Card(i,j))
			ct += 1

		shuffle(self.all_cards)

	def deal(self):
		return self.all_cards.pop(0)

	def check_zero(self):
		return len(self.all_cards) == 0
