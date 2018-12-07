#https://adventofcode.com/2018/day/6
# There was a bug in the AOC system which caused many users to fai:
# https://www.reddit.com/r/adventofcode/comments/a3kr4r/2018_day_6_solutions/

# My code is very hacky and also part A is not correct. The correct result is
# not the max in line 50 but the second max in line 51. Will try to find the
# problem tomorrow

from collections import defaultdict

def manhattan(a, b):
	return abs(a[0]-b[0]) + abs(a[1]-b[1])

with open('testinput') as f:
	lines = f.read().splitlines()
	coords = []
	xs = []
	ys = []
	for line in lines:		
		coords.append(tuple((map(int, line.split(",")))))
		xs.append(coords[-1][0])
		ys.append(coords[-1][1])

	minx, maxx = min(xs), max(xs)
	miny, maxy = min(ys), max(ys)

	def find_closest(x,y):
		points_with_dist = defaultdict(list)

		for c in coords:						
				d = manhattan((x,y), c)
				points_with_dist[d].append(c)

		md = min(dict(points_with_dist).keys())
		if len(points_with_dist[md]) > 1:
			return None
		return points_with_dist[md][0]

	def is_on_border(cl):
		return cl[0] in [minx, maxx] or cl[1] in [miny, maxy]

	is_closest = defaultdict(int)

	for y in range(miny, maxy):
		for x in range(minx, maxx):
			cl = find_closest(x,y)
			if cl is not None:# and not is_on_border(cl):
				is_closest[cl] += 1

	is_closest = {k :v for k,v in is_closest.items() if not is_on_border(k) }

	print("A", max(dict(is_closest).values()))
	print(sorted(dict(is_closest).values()))

	def get_sum(x,y):
		s = 0
		for coord in coords:
			s += manhattan((x,y), coord)
		return s

	n = 0

	for y in range(miny, maxy):
		for x in range(minx, maxx):
			if get_sum(x,y) < 10000:
				n += 1

	print("B", n)