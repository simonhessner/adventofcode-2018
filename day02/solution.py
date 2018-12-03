from collections import Counter

with open("input") as inputfile:
	lines = inputfile.read().splitlines()

	relevant_frequencies = [2,3]
	counter = Counter({freq : 0 for freq in relevant_frequencies})	

	for line in lines:
		freqs = dict(Counter(line)).values()
		counter.update({freq : int(freq in freqs) for freq in relevant_frequencies})

	print("A", counter[2] * counter[3])

	sorted_lines = sorted(lines)
	for i in range(len(sorted_lines)-1):
		str1 = sorted_lines[i]
		str2 = sorted_lines[i+1]
		is_equal = list(map(lambda x : x[0] == x[1], list(zip(str1, str2))))
		if Counter(is_equal)[False] == 1:
			print("B", "".join(str1[j] if is_equal[j] else "" for j in range(len(str1))))
			break