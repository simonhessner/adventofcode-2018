# https://adventofcode.com/2018/day/9
# Alternative solution inspired by https://www.reddit.com/r/adventofcode/comments/a4i97s/2018_day_9_solutions/
# Runtime ~2s for both parts

from collections import deque # double-ended queue

def run(players, last_marble):
	marbles = deque([0])
	scores = [0]*players

	for marble in range(1, last_marble+1):
		if marble % 23 == 0:
			marbles.rotate(7) # Move head left
			scores[marble%players] += marble + marbles.pop() # remove element at current pointer
			marbles.rotate(-1) # Move head right
		else:
			marbles.rotate(-1) # Rotate one element to the left, this means the head is moved one right
			marbles.append(marble) # Inserts the element right from the current pointer

	return max(scores)

print("Part 1", run(459, 72103))
print("Part 2", run(459, 72103 * 100))