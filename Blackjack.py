import random

def deal_card():
	cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
	card=random.choice(cards)
	return card
	
def calculate_score(cards):
	if sum(cards)==21 and len(cards)==2:
		return 0
	if 11 in cards and sum(cards)>21:
		cards.remove(11)
		cards.append(1)
		
	return sum(cards)
	
def compare(u_score,c_score):
	if u_score==c_score:
		return "Draw"
	elif c_score==0 :
		return "You lost"
	elif u_score==0 :
		return "You won"
	elif c_score>21:
		return "You won"
	elif u_score>21:
		return "You lost"
	elif u_score>c_score:
		return "You won"
	else:
		return "You lost"

def play_game():		
	user_card=[]
	computer_card=[]
	is_game_over=False
	
	for _ in range(2):
		user_card.append(deal_card())
		computer_card.append(deal_card())
	
	
	while not is_game_over:
	           user_score=calculate_score(user_card)
	           computer_score =calculate_score(computer_card)
	           print(f" your card={user_card} : computer card={computer_card[0]}")
	           print(f"computer's first card : {computer_card[0]}")
	           if computer_score==0 or user_score==0 or user_score>21:
	           	is_game_over=True
	           else:
	           	resume=input("you wanna draw another card? type 'y' to draw or type 'n' to pass:")
	           	if resume=="y":
	           		user_card.append(deal_card())
	           	else:
	           		is_game_over=True
	           		
	while computer_score!=0 and computer_score<17:
		computer_card.append(deal_card())
		computer_score =calculate_score(computer_card)
		
	print(f"Your card:{user_card} , current_score:{user_score}")
	print(f"Computer first card:{computer_card[0]}, final score:{computer_score}")
	
	
	print(compare(user_score,computer_score))
	
while input("Do you wanna play a game of blackjack? enter 'yes' or 'no' : ") == "yes":
		print("\n" * 100)
		play_game()

	




