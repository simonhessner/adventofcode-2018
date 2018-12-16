# https://adventofcode.com/2018/day/15
#
#	Note: since day 15 was way more time-consuming than the others and I
#	do not want to spend 4+ hours on this, I will skip day 15.
#

def attack_or_move(grid, x, y):
	targets = []
	for _y in len(grid):
		for _x in len(grid[_y]):
			if _y != y and _x != x:
				if grid[_y][_x] in ["E", "G"] and grid[_y][_x] != field:
					targets.append((_x,_y))
	squares_in_range = []
	for _x, _y in targets:
		if (abs(x-_x)+abs(y-_y)) == 1: # in reach => attack
			pass # TODO
	
	if len(targets) == 0:
		candidates = [(_x-1,_y), (_x+1,_y), (_x,_y-1), (_x,_y+1)]:
		closest = None
		distance = 1000000
		for __x,__y in candidates:
			if grid[__y][__x] == ".":
				squares_in_range.append((__x,__y))
				dist = abs(__x-x)+abs(__y-y)
				if dist < distance:
					distance = dist
					closest = (__x,__y)
		if not closest: # next round
			return
		else:
			__x,__y = closest
			grid[__y][__x] = grid[y][x]
			grid[y][x] = "."


with open('input') as f:
	lines = f.read().splitlines()
	grid = [list(x) for x in lines]

	while True:
		for y,row in enumerate(grid):
			for x,field in enumerate(row):
				if field in ["E", "G"]:
					attack_or_move(grid, x, y)				



		exit()