import random
from data import *
current_score = 0
print("------------HIGHER OR LOWER---------------")

acc_A=random.choice(data)
acc_B=random.choice(data)

def higher_lower():
	global current_score 
	global acc_A 
	global acc_B
	acc_A = acc_B
	acc_B=random.choice(data)
	if acc_A == acc_B:
	    higher_lower()
	print("Choice A:")
	acc_name_A=acc_A["name"]
	acc_desc_A=acc_A["description"]
	acc_country_A=acc_A["country"]
	print(f"{acc_name_A} , a {acc_desc_A} , from {acc_country_A}")
	print("-----------------VS-----------------")
	print("Choice B:")
	acc_name_B=acc_B["name"]
	acc_desc_B=acc_B["description"]
	acc_country_B=acc_B["country"]
	print(f"{acc_name_B} , a {acc_desc_B} , from {acc_country_B}")
	
	
	guess=input("Who has more followers ? Type 'A' or 'B'  :").lower()
	print("\n" * 100)
	if guess=="a":
		if acc_A["follower_count"]>acc_B["follower_count"]:
			current_score+=1
			print(f"You're right .Current score: {current_score}")
			higher_lower()
		else:
			print(f"Sorry that's wrong. final score={current_score}")
	else:
		if acc_A["follower_count"]<acc_B["follower_count"]:
			current_score+=1
			print(f"You're right .Current score: {current_score}")
			higher_lower()
		else:
			print(f"Sorry that's wrong. final score={current_score}")
higher_lower()		