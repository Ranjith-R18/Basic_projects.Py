import random

number=[]
def rock(a):
	global number
	number=random.randint(1,100)
	
rock(number)
	
print(" -----------GUESS THE NUMBER------------\n I'm thinking of a number between 1 to 100")
difficulty=input("Choose a difficulty . type 'easy' or 'hard' : ").lower()
attempts = 0
if difficulty =="easy":
	attempts+=10
	print(f"You have {attempts} attempts left to guess the number")
else:
	attempts+=5
	print(f"You have {attempts} attempts left to guess the number")

no_guesses=True
while no_guesses:
	guess=int(input("take a guess : "))
	if guess>number:
		print("Too high")
		attempts-=1
		print(f"You have {attempts} attempts left to guess the number")
		if attempts==0:
			print("you lose")
			no_guesses=False
		
	elif number>guess:
		print("Too low")
		attempts-=1
		print(f"You have {attempts} attempts left to guess the number")
		if attempts==0:
			print("You lose")
			no_guesses=False
			
	else:
		print(f"You guessed it right. it's {number} .")
		no_guesses=False
	