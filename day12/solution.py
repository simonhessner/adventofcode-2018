from collections import defaultdict

def getsum(pots, first):
	s = 0
	for i,c in enumerate(pots):
		if c == "#":
			s += i - first
	return s

lines = open('input').read().splitlines()
pots = lines[0].split(": ")[1]
pots = "."*2000 + pots + "."*2000
first = 0
for i,c in enumerate(pots):
	if c == "#":
		first = i
		break
	
rules = defaultdict(lambda : ".")
for rule in lines[2:]:
	condition, replacement = rule.split(" => ")
	rules[condition] = replacement

for g in range(200):
	newpots = list(pots)
	for i in range(2, len(pots)-2):
		newpots[i] = rules[pots[i-2:i+3]]
	pots = "".join(newpots)
	s = getsum(pots, first)
	
print((50000000000-200)*87+s)