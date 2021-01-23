'''
Generates player class to use in blackjack game
'''

from blackjack_card import Card

class Player():

	def __init__(self, name, acct):

		self.name = name
		self.acct = acct
		self.hand = []
		self.hand_val = 0
		self.bet_amt = 0
		self.status = 0
		self.stay_status = False

	def __str__(self):
		return f'{self.name}: ${self.acct}'

	def bet(self,bet):
		self.acct = self.acct - bet
		self.bet_amt = bet
		return self.bet_amt

	def payout(self,payout):
		self.acct = self.acct + payout
		return payout

	def double(self):
		self.acct = self.acct - self.bet_amt
		self.double = True
		return self.bet_amt

	def receive_card(self, card):
			self.hand.append(card)

	def split(self):
			self.acct = self.acct - self.bet_amt
			return (True,self.hand.pop(0),self.bet_amt)

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
		self.bet_amt = 0
		self.status = 0
		self.insurance = False
		self.double = False
		self.stay_status = False

	def player_status(self, status = 0):
		#O if no result, 1 if win, -1 if loose
		self.status = status
		return self.status

	def player_stay_status(self):
		self.stay_status = True

		
