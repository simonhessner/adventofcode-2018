# https://adventofcode.com/2018/day/13

from collections import defaultdict

class Crash(Exception):
	def __init__(self,x,y):
		self.x = x
		self.y = y
		super(Crash, self).__init__("Crash at (%d,%d)" %(x,y))

class Map(object):
	def __init__(self, source):
		with open(source, 'r') as f: 
			self.grid = list(map(list,f.read().splitlines()))

		self.carts = {}
		self.cart_crossed = defaultdict(int)

		mapping = {
			">" : "-",
			"<" : "-",
			"v" : "|",
			"^" : "|"
		}

		for y in range(len(self.grid)):
			for x in range(len(self.grid[y])):
				if self.grid[y][x] in "<>v^":
					self.carts[(x,y)] = (len(self.carts.keys()), self.grid[y][x])
					self.grid[y][x] = mapping[self.grid[y][x]]

	def print(self,carts=True):
		print()
		for y in range(len(self.grid)):
			for x in range(len(self.grid[y])):
				if carts and (x,y) in self.carts:
					print(self.carts[(x,y)][1], end='')
				else:
					print(self.grid[y][x], end='')
			print()
		print()

	def get_carts_in_order(self):
		carts = []
		for y in range(len(self.grid)):
			for x in range(len(self.grid[y])):
				if (x,y) in self.carts:
					carts.append((x,y))
		return carts

	def move(self, handle_crashes=False):
		movement = {
			">" : (1,0),
			"<" : (-1,0),
			"v" : (0,1),
			"^" : (0,-1)
		}

		for x,y in self.get_carts_in_order():
			if (x,y) not in self.carts:
				continue
			cid, direction = self.carts[(x,y)]
			dx, dy = movement[direction]
			del self.carts[(x,y)]

			nx, ny = x+dx, y+dy	
			if (nx,ny) in self.carts:
				del self.carts[(nx,ny)]
				if not handle_crashes:
					raise Crash(nx,ny)
				else:
					print("Crash: (%d,%d), \t%d carts left" % (nx,ny, len(self.carts.keys())))
					continue

			if self.grid[ny][nx] == "+":
				times = self.cart_crossed[cid]
				
				if direction == "v":
					newdir = [">", direction, "<"][times % 3]
				elif direction == "^":
					newdir = ["<", direction, ">"][times % 3]
				elif direction == "<":
					newdir = ["v", direction, "^"][times % 3]
				else:
					newdir = ["^", direction, "v"][times % 3]

				self.cart_crossed[cid] += 1
			elif self.grid[ny][nx] == "\\":
				if direction == ">":
					newdir = "v"
				elif direction == "^":
					newdir = "<"
				elif direction == "v":
					newdir = ">"
				else:
					newdir = "^"
			elif self.grid[ny][nx] == "/":
				if direction == ">":
					newdir = "^"
				elif direction == "^":
					newdir = ">"
				elif direction == "v":
					newdir = "<"
				else:
					newdir = "v"
			else:
				newdir = direction

			self.carts[(nx,ny)] = cid, newdir

	def get_first_crash(self):
		while True:
			try:
				self.move()
			except Crash as c:
				return c.x, c.y

	def get_last_car(self):
		while len(self.carts.keys()) > 1:
			self.move(handle_crashes=True)
		return list(self.carts.keys())[0]

print("Part 1", Map('input').get_first_crash())
print("Part 2", Map('input').get_last_car())