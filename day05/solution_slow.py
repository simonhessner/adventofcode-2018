# https://adventofcode.com/2018/day/5
# My solution runs very slow (240s), probably because of the construction of a new string everytime a reaction is found. solution_fast.py avoids this

def findIndex(inp):
	for i in range(len(inp)-1):
		if ((inp[i].isupper() and inp[i+1].islower()) or (inp[i+1].isupper() and inp[i].islower())) and inp[i].lower() == inp[i+1].lower():
			return i
	return None

def react(s):
	while True:
		i = findIndex(s)
		if i is None:
			return s
		else:
			s = "".join(s[idx] for idx in range(len(s)) if idx not in [i, i+1])
			
with open('input') as f:
	lines = f.read().splitlines()
	inp = lines[0]
	reacted = react(inp)
	print("A", len(reacted))
	
lengths = []
for ch in "abcdefghijklmnopqrstuvwxyz":
	ns = "".join(x for x in reacted if x.lower() != ch)
	r = react(ns)
	lengths.append(len(r))
print("B", min(lengths))