import random

def game():
	comp_num = random.randint(1,10)
	score = 1
	win = False
	
	while win == False:
		guess = int(raw_input(player + ", make your guess: "))
		if guess == comp_num:
			if score == 1: print "You win!  It only took you 1 guess."
			else: print "You win!  It only took you " + str(score) + " guesses."
			win = True
			again = raw_input("Play again (y/n)? ")
			if again == "y": game()
		elif guess > comp_num: print "Too high!"
		else: print "Too low!"
		score += 1

player = raw_input("Please enter your name: ")
game()
