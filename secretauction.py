def highest_bidder(bidding_dictionary):
	winner=""
	highest_bid=0
	for bidder in bidding_dictionary:
		bid_amount=bidding_dictionary[bidder]
		if highest_bid<bid_amount:
			highest_bid=bid_amount
			winner=bidder
	print(f"the winner is {winner} with the bid of {bid_amount} ")
	
	


Auction={}
continue_bidder=True
while continue_bidder:
	name=input("What is your name? ")
	bid=int(input("Enter your bid amount: ₹"))
	Auction[name]=bid
	resume= input("Do u wanna continue? type 'yes' or 'no'\n").lower()
	if resume=="no":
		continue_bidder=False
		highest_bidder(Auction)
	elif resume=="yes":
		print("\n" * 100)
			
			
		
	