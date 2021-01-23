'''
Establishes dealer and any necesseary actions
'''

from blackjack_card import Card

class Dealer():

	def __init__(self):
		self.hand = []
		self.hand_val = 0
		self.early_blackjack = False
		self.dealer_bust = False

	def receive_card(self, card):
			self.hand.append(card)

	def calc_hand_val(self):
		self.hand_val = 0

		ace = 0

		for ele in self.hand:
			
			if ele.rank == "A":
				ace += 1
			else: 
				self.hand_val = self.hand_val + ele.value

		ct = 1

		while ct <= ace:
			self.hand_val = self.hand_val + 11
			
			if self.hand_val <= 21:
				pass
			elif self.hand_val > 21:
				self.hand_val = self.hand_val - 11 + 1
			
			ct +=1	

	def clear_hand(self):
		self.hand = []
		self.hand_val = 0
		self.early_blackjack = False
		self.dealer_bust = False

	def check_early_blackjack(self):
		if self.hand[1].value == 10 or self.hand[1].value == 11:
			if self.hand[1].value +self.hand[0].value == 21:
				self.early_blackjack = True
				return True
			else:
				return False

	def dealer_bust_trigger(self):
		self.dealer_bust = True

		