# https://adventofcode.com/2018/day/5
# My solution runs very slow (240s), probably because of the construction of a new string everytime a reaction is found. solution_fast.py avoids this

import string

def findIndex(inp):
	for i in range(len(inp)-1):
		if ((inp[i].isupper() and inp[i+1].islower()) or (inp[i+1].isupper() and inp[i].islower())) and inp[i].lower() == inp[i+1].lower():
			return i
	return None

def react(s):
	while True: # This is also not very optimal
		i = findIndex(s)
		if i is None:
			return s
		else:
			s = "".join(s[idx] for idx in range(len(s)) if idx not in [i, i+1]) # I guess this is the problematic part that slows down everything
			
with open('input') as f:
	reacted = react(f.read().splitlines()[0])
	print("A", len(reacted))
	
lengths = []
for ch in string.ascii_lowercase:
	lengths.append(react("".join(x for x in reacted if x.lower() != ch)))
print("B", min(lengths))