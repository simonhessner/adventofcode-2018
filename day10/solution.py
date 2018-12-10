#https://adventofcode.com/2018/day/10
import re

with open('input') as f:
	xs, ys, speedxs, speedys  = [], [], [], []
	for line in f.read().splitlines():
		x,y, sx, sy = tuple(int(s) for s in re.findall(r'-?\d+', line))
		xs.append(x)
		ys.append(y)
		speedxs.append(sx)
		speedys.append(sy)

	smallest_bb = None
	optimal_t = None
	t = 0
	while True:		
		xs = [xs[i]+speedxs[i] for i in range(len(xs))]
		ys = [ys[i]+speedys[i] for i in range(len(ys))]
		bb = (max(xs)-min(xs))*(max(ys)-min(ys))
		t += 1
		if smallest_bb is None or bb <= smallest_bb:
			smallest_bb = bb
			optimal_t = t
		else:
			# In this case the BB increases again, so the LAST point
			# positions were correct => move back and cancel
			xs = [xs[i]-speedxs[i] for i in range(len(xs))]
			ys = [ys[i]-speedys[i] for i in range(len(ys))]
			break

	points = list(zip(xs, ys))
	
	for y in range(min(ys), max(ys)+1):
		for x in range(min(xs), max(xs)+1):
			if (x,y) in points:
				print("#", end='')
			else:
				print(" ", end='')
		print()

	print(optimal_t)