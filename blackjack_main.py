'''
Blackjack Game
'''

#Import classes
from blackjack_deck import Deck
from blackjack_dealer import Dealer
from blackjack_player import Player

#Helper Functions
def register_players():

	add_players = True
	players = []

	while add_players == True:
		player_name = input('What is your name: ')
		print('\n')
		
		while True:
			try:
				player_acct = int(input('How much are you playing with today? '))
			except:
				print('Please input an integer value')
			else:
				break

		new_player = Player(player_name,player_acct)

		players.append(new_player)

		print('\n')

		if input('Anyone else playing? (Y/N):').upper() == 'Y':
			print('\n')
			add_players = True
		else:
			add_players = False
			print("Great, let's play\n")
			time.sleep(0.5)

	return players
	print('\n')

def check_bust(hand_value):
	if hand_value <= 21:
		return False
	else:
		return True

def player_input(player, option_num = 2):
	
	print(f'{player.name} choose:\n')

	if option_num == 1:
		option = ['H']
		
		invalid = True
		while invalid:
			
			move = input("Hit = 'H'").upper()
						
			if move in option:
				invalid = False
			else:
				invalid = True

	elif option_num == 2:
		option = ['H','S']
		
		invalid = True
		while invalid:
			move = input("Hit = 'H', Stay = 'S'").upper()

			if move in option:
				invalid = False
			else:
				invalid = True

	return move

def player_move(player):

	move = player_input(player,2)

	print('\n')

	while player.stay_status == False:
			
		if move == 'H':
			hit(player)
			if player.stay_status == True:
				time.sleep(1)
			else:
				print(f'Dealer showing {dealer1.hand[1].value}:\n')
				move = player_input(player,2)

		elif move == 'S':
			player.calc_hand_val()
			player.player_stay_status()
			print(f'{player.name} stays\n at {player.hand_val}')
			print('----------\n')
			time.sleep(1)

def hit(player):
	
	print(f'{player.name} hit')
	time.sleep(0.5)
	hit_card = gamedeck.deal()
	print(f'{hit_card}\n')
	time.sleep(0.5)				
	player.receive_card(hit_card)
	player.calc_hand_val()
	print(f'{player.name} has {player.hand_val}\n')

	if check_bust(player.hand_val):
		player.player_status(-1)
		player.player_stay_status()
		print(f"Sorry {player.name}, Bust.")
		print('\n')

	else:
		pass

#Welcome Message
import time
print('Welcome to Blackjack\n')
time.sleep(0.2)

#Register Players for testing
#playerlist, num_of_players = register_players()
time.sleep(2)
playerlist = register_players()
dealer1 = Dealer()

#Game Play

#Build Deck
gamedeck = Deck(6)

game_on = True

while game_on == True:

	#Collect player bets
	for player in playerlist:

		valid = False
		x = 0

		while valid == False:
			
			try:
				x = int(input(f'{player.name}, Place your bet: '))
			except:
				print('Please enter an integer only')

			if type(x) == int and x > 0 and x < player.acct:
				valid = True
			else:
				print('Please enter a positive integer that is less than the amount you are playing with')

		player.bet(x)
		print(f'{player.name} bets {player.bet_amt}')
		print('\n')
		time.sleep(1)

	#Deal Cards
	print("Let's deal\n")
	time.sleep(1)

	ct = 1

	while ct <= 2:

		for player in playerlist:
			player.receive_card(gamedeck.deal())
		dealer1.receive_card(gamedeck.deal())
		ct += 1

	#Show Dealer Top Card & Player Cards
	print(f'Dealer showing {dealer1.hand[1].value}:')
	print(dealer1.hand[1])
	print('\n')

	for player in playerlist:
		player.calc_hand_val()
		print(f'{player.name} has {player.hand_val}:')
		for card in player.hand:
			print(card)
		print('\n')
	print('----------\n')
	input('Press Enter to Continue')

	#Blackjack Win
	if dealer1.check_early_blackjack():
		print("Sorry, Dealer Blackjack")
		print('\n')
		time.sleep(1)
		for player in playerlist:
			if player.calc_hand_val() == 21:
				player.player_status(0)
			else:
				player.player_status(-1)
				
	else:
		pass

	#Normal player hands
	if dealer1.early_blackjack == False:

		#Loop through available players
		for player in playerlist:
			
			if len(playerlist) > 1:
				print(f'Dealer showing {dealer1.hand[1].value}:\n')
				print(f'{player.name} has {player.hand_val}:')
				for card in player.hand:
					print(card)
				print('\n')

			player_move(player)

	#Dealer hand
	dealer1.calc_hand_val()
	print(f'Dealer has {dealer1.hand_val}')
	for card in dealer1.hand:
		print(card)
	print('\n')
	time.sleep(2)

	while dealer1.hand_val < 17:

		print('Dealer hit')
		hit_card = gamedeck.deal()
		print('\n')
		time.sleep(1)
		print(hit_card)
		time.sleep(1)
					
		dealer1.receive_card(hit_card)
		dealer1.calc_hand_val()
		print(f'Dealer has {dealer1.hand_val}:\n')

		if check_bust(dealer1.hand_val):
			dealer1.dealer_bust_trigger()
			print('Dealer Bust\n')

		time.sleep(1)

	if not dealer1.dealer_bust_trigger:
		print('Dealer stay\n')

	time.sleep(3)

	#Determine hand results
	for player in playerlist:

		if dealer1.dealer_bust == True and player.status != -1:
			player.player_status(1)

		elif dealer1.dealer_bust == False:

			if player.hand_val > dealer1.hand_val and player.status != -1:
				player.player_status(1)

			elif player.hand_val < dealer1.hand_val and player.status != -1:
				player.player_status(-1)

			elif player.hand_val == dealer1.hand_val and player.status != -1:
				player.player_status(0)
				player.payout(player.bet_amt)

		if player.status == 1:

			if player.hand_val == 21:
				player.payout(player.bet_amt * 2.5)
			else:
				player.payout(player.bet_amt * 2)

	#Print hand results
	print("Let's see how the table did\n")
	for player in playerlist:
			
		if player.status == 0:
			print(f'{player.name} bet {player.bet_amt} and Pushed with {player.hand_val}')
			time.sleep(0.5)

		if player.status == 1:
			print(f'{player.name} bet {player.bet_amt} and Won with {player.hand_val}')
			time.sleep(0.5)

		if player.status == -1:
			print(f'{player.name} bet {player.bet_amt} and Lost with {player.hand_val}')
			time.sleep(0.5)

		print(f'{player.name} now has {player.acct}\n')

		time.sleep(1)

	if input('Keep playing (Y/N)?:').upper() == 'Y':
		game_on = True
		dealer1.clear_hand()
		for player in playerlist:
			player.clear_hand()
	else:
		game_on = False
