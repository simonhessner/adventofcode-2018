# Inspired by: 
# https://www.reddit.com/r/adventofcode/comments/a47ubw/2018_day_8_solutions/ebc82oj/

"""
The idea is to go through the input int by int. Each integer must only be read 
one time, so the runtime is O(n).

parse_tree() takes the input stream and reads the first two integers from it. 
These describe the amount of child nodes and meta values. For each child 
parse_tree is called recursively, thus the stream is read further. When there 
is no child left, the meta values of the deepest node are read and processed as 
required by the problem description. Then the recursion goes one level up and 
either continues with the next child or with the meta data of the parent node, 
and so on.
"""

def parse_tree(inp):
	n_childs, n_meta = next(inp), next(inp)
	metas = []

	child_values = []
	for _ in range(n_childs):
		child_metas, child_value = parse_tree(inp)
		metas += child_metas
		child_values.append(child_value)
	
	local_metas = [next(inp) for _ in range(n_meta)]
	metas += local_metas

	return (metas, 
		    sum(local_metas) if n_childs == 0 
		    else (
		    	  sum(child_values[ref-1] 
		    	  for ref in local_metas if ref-1 in range(n_childs))
		    	 )
		   )

it = iter([int(x) for x in open('input').read().split(" ")])
metas, value = parse_tree(it)
print("Part 1", sum(metas))
print("Part 2", value)