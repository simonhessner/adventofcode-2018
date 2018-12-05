# https://adventofcode.com/2018/day/
# This runs about 800 times faster than solution_slow.py (reason: react() only adds and removes elements at the end of the new string and not at arbitrary positions)

import string

def reacts(a, b):
	return a.isupper() != b.isupper() and a.lower() == b.lower()

def react(original):
	stack = []
	for c in original:
		if len(stack) == 0 or not reacts(c, stack[-1]):
			stack.append(c)
		else:
			stack.pop()
	return "".join(stack)
			
with open('input') as f:
	reacted = react(f.read().splitlines()[0])
	print("A", len(reacted))
	
lengths = []
for char in string.ascii_lowercase:
	lengths.append(len(react("".join(x for x in reacted if x.lower() != char))))
print("B", min(lengths))