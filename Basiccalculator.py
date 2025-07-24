def add(n1,n2):
	return n1 +n2	

def subtract(n1,n2):
	return n1 - n2

def multiply(n1,n2):
	return n1*n2	

def div(n1,n2):
	return n1/n2
	
operations={"+":add,"-":subtract,"*":multiply,"/":div}
def again():
	num1 = float(input("what is the first number? "))
	should_continue=True
	while should_continue:
		for i in operations:
			print(i)
		symbol=input("which operation you would like to do? ")
		num2=float(input("what is the next number?"))
		answer=operations[symbol](num1,num2)
		print(f"{num1} {symbol} {num2}={answer}")
		choice=input("enter 'y' to continue with {answer}.enter 'n' to end :")
		
		
		if choice=="y":
			num1=answer
		else:
			should_continue=False
			print("\n"*100)
			again()
		
again()



	










		