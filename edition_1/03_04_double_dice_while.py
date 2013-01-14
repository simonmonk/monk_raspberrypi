#03_04_double_dice_while
import random
throw_1 = random.randint(1, 6)
throw_2 = random.randint(1, 6)
while not (throw_1 == 6 and throw_2 == 6):
	total = throw_1 + throw_2
	print(total)
	throw_1 = random.randint(1, 6)
	throw_2 = random.randint(1, 6)
print('Double Six thrown!')