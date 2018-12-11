import numpy as np
inpt = 3463
#inpt = 18

grid = np.zeros((300,300), dtype=np.int) #coord 1 to 300

def get_power_level(x,y):
	rid = x+10
	tmp = (rid* y + inpt)*rid
	return (tmp//100)%10 - 5


for x in range(300):
	for y in range(300):
		grid[x,y] = get_power_level(x+1, y+1)



def find_best(minsize, maxsize):
	biggest = None
	bestx, besty = -1, -1
	bestsize = -1

	for size in range(minsize,maxsize+1):
		tmpbiggest = None
		for x in range(300-size):
			for y in range(300-size):		
				subcell = grid[x:x+size,y:y+size]
				v = np.sum(subcell)
				if tmpbiggest is None or v > tmpbiggest:
					tmpbiggest = v
				if tmpbiggest < 0:
					break
				if biggest is None or tmpbiggest > biggest:
					biggest = tmpbiggest
					bestx, besty = x+1,y+1
					bestsize = size
					#print(">", bestx, besty, bestsize, biggest)

	#print()
	return (bestx, besty, bestsize, biggest)

print("Part 1", find_best(3,3)[:2])
print("Part 2", find_best(1,300)[:3])