# https://adventofcode.com/2018/day/8

# This was the hardest problem so far in AOC2018.

def parse_subtree(unexplored):
	n_childs, n_meta = unexplored[:2]
	unexplored = unexplored[2:]

	metas = []
	child_values = []

	for c in range(n_childs):
		child_metas, unexplored, child_value = parse_subtree(unexplored)
		metas += child_metas
		child_values.append(child_value)
	
	local_metas = unexplored[:n_meta]

	metas += unexplored[:n_meta]

	if n_childs == 0:
		return metas, unexplored[n_meta:], sum(local_metas)

	value = 0
	for ref in local_metas:
		print(local_metas)
		if ref in range(1, len(child_values)+1):
			value += child_values[ref-1]
	return metas, unexplored[n_meta:], value


with open('input') as f:
	unexplored = [int(x) for x in f.read().splitlines()[0].split()]
	metas, _, value = parse_subtree(unexplored)
	print(sum(metas), value)