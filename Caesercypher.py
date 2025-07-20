alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(original_text,shift_amount,direction):
	cipher_text=""
	if direction=="decode":
		shift_amount*=-1
		
	for letter in original_text:
		if letter not in alphabets:
			cipher_text+=letter
		else:
			shifted_position=alphabets.index(letter)+shift_amount
			shifted_position%=len(alphabets)
			cipher_text+=alphabets[shifted_position]
	print(f"here is the encoded result: {cipher_text}")
	
should_continue=True
while should_continue:
		direction=input("type 'encode' to encrypt . type 'decode'' to decrypt\n").lower()
		text=input("type your message:\n").lower()
		shift=int(input("enter the shift number:\n"))
		
		caeser(text,shift,direction)
		
		restart=input("type 'yes' to continue. type 'no' to end\n")
		if restart=="no":
			should_continue=False
			print("Goodbye")
		