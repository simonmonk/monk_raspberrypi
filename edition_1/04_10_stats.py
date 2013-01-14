#04_09_stats
def stats(numbers):
	numbers.sort()
	return (numbers[0], numbers[-1])

list = [5, 45, 12, 1, 78]
min, max = stats(list)
print(min)
print(max)