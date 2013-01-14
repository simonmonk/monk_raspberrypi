#04_06_hangman_get_guess

import random

words = ['chicken', 'dog', 'cat', 'mouse', 'frog']
lives_remaining = 14

def play():
	word = pick_a_word()
	while True:
		guess = get_guess(word)
		if process_guess(guess, word):
			print('You win! Well Done!')
			break
		if lives_remaining == 0:
			print('You are Hung!')
			print('The word was: ' + word)
			break

def pick_a_word():
	word_position = random.randint(0, len(words) - 1)
	return words[word_position]
	
def get_guess(word):
	print_word_with_blanks(word)
	print('Lives Remaining: ' + str(lives_remaining))
	guess = input(' Guess a letter or whole word?')
	return guess

def process_guess(guess, word):
	global lives_remaining
	lives_remaining = lives_remaining -1
	return False
	
def print_word_with_blanks(word):
	print('print_word_with_blanks: not done yet')
	
play()