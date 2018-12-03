import itertools

with open('input') as f:
	numbers = list(map(int, f.readlines()))

	print("A", sum(numbers))

	seen = set([]) # set is about 16.000 times faster in this case
	for a in itertools.accumulate(itertools.cycle(numbers)):
		if a not in seen:
			seen.add(a)
		else:
			print("B", a)
			break		