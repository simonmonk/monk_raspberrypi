#04_04_hangman_words
import random

words = ['chicken', 'dog', 'cat', 'mouse', 'frog']

def pick_a_word():
	word_position = random.randint(0, len(words) - 1)
	return words[word_position]

print(pick_a_word())