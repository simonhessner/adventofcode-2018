# My solution for https://adventofcode.com/2018/day/3

from collections import defaultdict

with open("input") as inputfile:
	lines = inputfile.read().splitlines()

	field = defaultdict(set)
	intersections = defaultdict(set)

	no_intersections = set()

	for line in lines:
		parts  = line.split(" ")
		cid    = int(parts[0][1:])
		left   = int(parts[2].split(",")[0])
		top    = int(parts[2].split(",")[1][:-1])
		width  = int(parts[3].split("x")[0])
		height = int(parts[3].split("x")[1])

		no_intersections.add(cid) # Assume this rectangle has no intersections with others
		intersections_found = set() # Every intersection that is found now will be removed from no_intersections later

		for x in range(left, left+width):
			for y in range(top, top+height):
				for other_cid in field[(x,y)]:
					intersections[cid].add(other_cid)
					intersections[other_cid].add(cid)
					intersections_found |= set([cid, other_cid])
				field[(x,y)].add(cid)

		no_intersections -= intersections_found

	print("A", sum([len(claims) >= 2 for claims in field.values()]))
	print("B", list(no_intersections)[0])