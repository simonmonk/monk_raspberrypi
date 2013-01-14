#03_05_double_dice_while_break
import random
while True:
	throw_1 = random.randint(1, 6)
	throw_2 = random.randint(1, 6)
	total = throw_1 + throw_2
	print(total)
	if throw_1 == 6 and throw_2 == 6:
		break
print('Double Six thrown!')