#04_11_except
try:
	list = [1, 2, 3, 4]
	list[4]
except IndexError, detail:
	print('Oops')
