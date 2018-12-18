# https://adventofcode.com/2018/day/18

from collections import Counter
OPEN = "."
TREES = "|"
LUMBERYARD = "#"

def get_neighbors(x,y):
	ans = []
	for _x in range(x-1, x+2):
		for _y in range(y-1, y+2):
			if (_x,_y) != (x,y) and _x in range(0,50) and _y in range(0,50):
				ans.append((_x,_y))
	return ans

def get_types(grid, coords):
	ans = []
	for x,y in coords:
		ans.append(grid[y][x])
	return ans

def get_counts(elems):
	c = Counter(elems)
	return c[OPEN], c[TREES], c[LUMBERYARD]

def convert(grid, x,y):
	nbrs = get_types(grid, get_neighbors(x,y))
	n_open, n_trees, n_lumberyard = get_counts(nbrs)

	if grid[y][x] == OPEN:
		if n_trees >= 3:
			return TREES
	elif grid[y][x] == TREES:
		if n_lumberyard >= 3:
			return LUMBERYARD
	elif grid[y][x] == LUMBERYARD:
		if n_trees < 1 or n_lumberyard < 1:
			return OPEN
	return grid[y][x]

mapgrid = lambda grid: [[convert(grid,x,y) for x in range(50)] for y in range(50)]

def part1():
	with open('input') as f:
		grid = list(map(list, f.read().splitlines()))
		for _ in range(10):
			grid = mapgrid(grid)
			
		_, n_trees, n_lumberyard = get_counts(sum(grid, []))
		return n_trees*n_lumberyard

def part2():
	seen = []
	lastlen = 0
	
	with open('input') as f:
		grid = list(map(list, f.read().splitlines()))
		repeating = False

		t = 0
		offset = 0
		while not repeating:
			t += 1
			grid = mapgrid(grid)			
			_, wood, lumb = get_counts(sum(grid, []))
			v = wood*lumb

			if v in seen:
				if len(seen) == lastlen:
					repeating = True
					tmpv = v
				else:
					offset = t
				lastlen = len(seen)
			else:
				seen.append(v)

		period = False
		periodic_values = {}
		while not period:
			t += 1
			grid = mapgrid(grid)			
			_, wood, lumb = get_counts(sum(grid, []))
			v = wood*lumb
			if v == tmpv:
				period = True
				period_length = t-offset-1
			periodic_values[t] = v

		periodic_values = {(t-offset)%period_length:v for t,v in periodic_values.items()}

		return periodic_values[(1000000000-offset)%period_length]

print("Part 1", part1())
print("Part 2", part2())