import re
from collections import defaultdict

class Grid(object):
	SAND 	= "."
	CLAY 	= "#"
	SPRING 	= "+"
	FLOW	= "|"
	SETTLED = "~"

	def __init__(self, source):
		self.grid = defaultdict(lambda : Grid.SAND)
		self.grid[(500,0)] = Grid.SPRING

		with open(source) as f:
			lines = f.read().splitlines()
			for line in lines:
				if line[0] == "x":
					x, yl, yh = [int(x) for x in re.findall(r'\d+', line)]
					for y in range(yl, yh+1):
						self.grid[(x,y)] = Grid.CLAY
				else:
					y, xl, xh = [int(x) for x in re.findall(r'\d+', line)]
					for x in range(xl, xh+1):
						self.grid[(x,y)] = Grid.CLAY

			self.xmin = min([x[0] for x in self.grid.keys()])
			self.xmax = max([x[0] for x in self.grid.keys()])
			self.ymin = min([x[1] for x in self.grid.keys()])
			self.ymax = max([x[1] for x in self.grid.keys()])

	def print(self):
		for y in range(self.ymin, self.ymax+1):
			for x in range(self.xmin, self.xmax+1):
				print(self.grid[(x,y)], end='')
			print()
		print()

	def find_borders(self,x,y):
		lx = x
		rx = x

		while self.grid[(lx,y)] != Grid.CLAY:
			lx -= 1

		while self.grid[(rx,y)] != Grid.CLAY:
			rx += 1

		return lx+1, rx-1

	def is_flooded(self,lx,rx,y):
		for x in range(lx,rx+1):
			if self.grid[(x,y)] != Grid.FLOW:
				return False
		return True

	def settle(self,lx,rx,y):
		for x in range(lx,rx+1):
			self.grid[(x,y)] = Grid.SETTLED

	def fill(self, x, y, dx, dy):
		#print(x,y,dx,dy)
		while self.grid[(x,y)] == Grid.SAND and y in range(self.ymin, self.ymax+1):
			self.grid[(x,y)] = Grid.FLOW
			x += dx
			y += dy
			#if (x,y) != (0,1):
			#	if self.grid[(x,y+1)] == Grid.SAND:
			#		self.print()
			#		self.fill(x,y,0,1)
			#print(x,y, self.grid[(x,y)])
			#print(dx,dy)
			#self.print()

		x -= dx
		y -= dy
		#print(x,y, self.grid[(x,y)])

		if self.grid[(x-1, y)] == Grid.SAND:
			self.fill(x-1, y, -1, 0)

		if self.grid[(x+1, y)] == Grid.SAND:
			self.fill(x+1, y, 1, 0)

		lx,rx = self.find_borders(x,y)
		if self.is_flooded(lx,rx,y):
			self.settle(lx,rx,y)
			self.fill(x,y-1,-1,0)
			self.fill(x,y-1,1,0)
		else:
			self.print()
			if self.grid[(lx,y)] == Grid.SAND:
				pritn("left")
				self.fill(x-1,y,0,1)
			if self.grid[(rx,y)] == Grid.SAND:
				self.print()
				print("right", self.grid[(x-1,y)], self.grid[(x,y)], self.grid[(x+1,y)])
				self.fill(x+1,y,0,1)



	def solve(self):
		self.fill(500,self.ymin+1,0,1)


g = Grid('example')
g.print()
g.solve()
g.print()