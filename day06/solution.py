# https://adventofcode.com/2018/day/6
# There was a bug in the AOC system which caused many users to fail:
# https://www.reddit.com/r/adventofcode/comments/a3kr4r/2018_day_6_solutions/

from collections import defaultdict, Counter

def manhattan(a, b):
	return abs(a[0]-b[0]) + abs(a[1]-b[1])

with open('input') as f:
	coords, xs, ys = [], [], []
	for line in f.read().splitlines():		
		coords.append(tuple((map(int, line.split(",")))))
		xs.append(coords[-1][0])
		ys.append(coords[-1][1])

	minx, maxx = min(xs), max(xs)
	miny, maxy = min(ys), max(ys)		

	field = defaultdict(tuple)

	for y in range(miny, maxy+1):
		for x in range(minx, maxx+1):
			points_with_dist = defaultdict(list)
			for c in coords:
				d = manhattan((x,y), c)
				points_with_dist[d].append(c)

			closest = points_with_dist[min(dict(points_with_dist).keys())]
			field[(x,y)] = closest[0] if len(closest) == 1 else None

	# Every point that is closest to one border point is part of a infinite area
	inf_points = set([None]) # This is technically not an infinite point, but a point that has more than one closes points
	for x in range(minx, maxx):
		inf_points.add(field[(x,miny)])
		inf_points.add(field[(x,maxy)])

	for y in range(miny, maxy):
		inf_points.add(field[(minx,y)])
		inf_points.add(field[(maxx,y)])

	c = Counter(field.values())
	biggest_area = [count for p,count in c.most_common() if p not in inf_points][0]
	print("Part 1", biggest_area)

	def get_sum(x,y):
		return sum(manhattan((x,y), coord) for coord in coords)

	n = 0
	for y in range(miny, maxy):
		for x in range(minx, maxx):
			if get_sum(x,y) < 10000:
				n += 1

	print("Part 2", n)