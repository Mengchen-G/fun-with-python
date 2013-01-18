import sys

guesses = 0
range_low = 0
range_high = 101
answers = ['S', 'H', 'L']

print '''To play this game, please choose any number between 1 and 100.
I will try to guess it in the least amount of guesses.'''

def graceful_exit():
	print "Thanks for playing!"
	sys.exit(0)

while True:
	guess = int((range_high + range_low) / 2)
	guesses += 1

	while True:
		print "My guess is {guess}. Is your number the same (S), higher (H), or is it lower (L)?".format(guess = guess)
		try:
			hilo = raw_input()
			hilo = hilo.strip()
		except KeyboardInterrupt:
			graceful_exit()

		if hilo in answers:
			if hilo.upper() == "S":
				print "Hooray! It only took me {guesses} guesses to find the answer!".format(guesses = guesses)
				graceful_exit()
			elif hilo.upper() == "H":
				range_low = guess
			elif hilo.upper() == "L":
				range_high = guess
			
			break