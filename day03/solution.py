import numpy as np

with open("input") as inputfile:
	lines = inputfile.read().splitlines()
	rectangles = []

	max_x = 0
	max_y = 0
	for line in lines:
		parts  = line.split(" ")
		_id    = int(parts[0][1:])
		left   = int(parts[2].split(",")[0])
		top    = int(parts[2].split(",")[1][:-1])
		width  = int(parts[3].split("x")[0])
		height = int(parts[3].split("x")[1])
		max_x  = max(max_x, left+width)
		max_y  = max(max_y, top+height)

		rectangles.append((left, top, width, height, _id))

	leftover = list(range(len(rectangles)))
	
	field = np.zeros((max_x+1, max_y+1), dtype=np.int)

	for rect in rectangles:
		for x in range(rect[0], rect[0]+rect[2]):
			for y in range(rect[1], rect[1]+rect[3]):
				field[x,y] += 1

				if field[x,y] > 1:
					for i in leftover:
						r = rectangles[i]
						if x in range(r[0], r[0]+r[2]) and y in range(r[1], r[1]+r[3]):
							leftover = [a for a in leftover if a != i]

	n = 0
	for row in field:
		for cell in row:
			if cell > 1:
				n += 1

	print("A", n)

	print("B", [rectangles[i] for i in leftover])