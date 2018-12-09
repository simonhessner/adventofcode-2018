# https://adventofcode.com/2018/day/9
# Runtime ~ 17s for both parts (~8 times slower than deque solution)

class Marble(object): # Own implementation of a simple double-linked list
	def __init__(self, number):
		self.number = number
		self.prev = self
		self.next = self

	def remove(self): # Removes itself from the list
		self.prev.next = self.next
		self.next.prev = self.prev

	def insert(self, marble):
		marble.prev = self
		marble.next = self.next
		self.next.prev = marble
		self.next = marble

def run(players, last_marble):
	current_marble = Marble(0)
	scores = [0]*players
	next_marble = 1

	for next_marble in range(1, last_marble+1):
		if next_marble % 23 == 0:
			for i in range(7):
				current_marble = current_marble.prev
			scores[next_marble % players] += current_marble.number + next_marble
			current_marble.remove()
			current_marble = current_marble.next
		else:
			current_marble = current_marble.next
			current_marble.insert(Marble(next_marble))
			current_marble = current_marble.next

	return max(scores)

print("Part 1", run(459, 72103))
print("Part 2", run(459, 72103 * 100))