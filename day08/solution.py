# https://adventofcode.com/2018/day/8
# This was the hardest problem so far in AOC2018.

# For a nicer solution, check solution_with_generators.py

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
	metas += local_metas

	if n_childs == 0:
		value = sum(local_metas)
	else:
		value = sum(child_values[ref-1] for ref in local_metas if ref-1 in range(n_childs))
	return metas, unexplored[n_meta:], value

unexplored = [int(x) for x in open('input').read().splitlines()[0].split()]
metas, _, value = parse_subtree(unexplored)
print("Part 1", sum(metas))
print("Part 2", value)