#06_03_file_readline
words_file = 'hangman_words.txt'
try:
	f = open(words_file)
	line = f.readline()
	while line != '':
		if line == 'elephant\n':
			print('There is an elephant in the file')
			break
		line = f.readline()
	f.close()	
except IOError:
	print("Cannot find file: " + words_file)
