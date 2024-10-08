print("GuessTheNumber Game")
print ("The Server will pick a number and you have to guess that number, the server will hint you when you will reach that number and also will tell you that the number which you guessed is greater than server number or not.")
print ("Total Score is 100. The higher score means the better score")
print ("Guess The number between 1 and 100\n")
print ("The Server will give you the hint:-\n1. close: Your number is withing +-5 of that number\n2. very close: Your number is within +-3 of that number.\n\n\n")

import random

#server number
server = random.randint(1,100)
#print (server)
guess=1
win_stats = 0

def check_status():
	if (you > server):
		return ("greater than the number")
	else:
		return ("lesser than the number")

def Score():
	score=100
	if (win_stats==1):
		print ("Your Score is ",score-(4*guess),"by attempting ",guess,"guess")
	else:
		print ("Your Score is 0")
		
		

while ((win_stats!=1) and (guess<26)):
    #your number
    global you
    you = int(input("Enter Your Number: "))

    if (you == server):
	    print ("Congrats! You Guessed that Number")
	    if guess==1:
	    	guess=0
	    win_stats = 1
	    Score()
    elif you in range(server-3, server+4):
    	print ("You are very close and ",check_status())
    	guess+=1
    elif you in range(server-5, server+6):
    	print("You are close and ",check_status())
    	guess+=1
    else:
    	print("Take another Guess! ","You are ",check_status())
    	guess+=1
    	
    if (guess==26):
    	print ("Oops! You are out of our guesses")
    	Score()

