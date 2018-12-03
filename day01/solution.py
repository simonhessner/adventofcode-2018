import itertools

with open('input') as f:
	numbers = list(map(int, f.readlines()))

	print("A", sum(numbers))

	seen = []
	for a in itertools.accumulate(itertools.cycle(numbers)):
		if a not in seen:
			seen.append(a)
		else:
			print("B", a)
			break		