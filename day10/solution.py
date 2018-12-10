#https://adventofcode.com/2018/day/10
import re

with open('input') as f:
	lines = f.read().splitlines()

	xs, ys, sxs, sys  = [], [], [], []
	for line in lines:
		x,y, sx, sy = [int(s) for s in re.findall(r'-?\d+', line)]
		xs.append(x)
		ys.append(y)
		sxs.append(sx)
		sys.append(sy)

	smallest_bb = None
	optimal_t = None
	t = 0
	while True:
		bb = (max(xs)-min(xs))*(max(ys)-min(ys))
		if smallest_bb is None or bb <= smallest_bb:
			smallest_bb = bb
			optimal_t = t			
		else:
			break
		t += 1
		xs = [xs[i]+sxs[i] for i in range(len(xs))]
		ys = [ys[i]+sys[i] for i in range(len(ys))]


	xs = [xs[i]-sxs[i] for i in range(len(xs))]
	ys = [ys[i]-sys[i] for i in range(len(ys))]
	
	points = list(zip(xs, ys))
	
	for y in range(min(ys), max(ys)+1):
		for x in range(min(xs), max(xs)+1):
			if (x,y) in points:
				print("#", end='')
			else:
				print(" ", end='')
		print()

	print(optimal_t)