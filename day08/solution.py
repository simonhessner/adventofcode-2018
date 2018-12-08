from collections import defaultdict

def parse(unprocessed_data):
	n_childs, n_meta = unprocessed_data[:2]
	unprocessed_data = unprocessed_data[2:]

	metas = []
	child_values = []

	for c in range(n_childs):
		child_metas, unprocessed_data, child_value = parse(unprocessed_data)
		metas += child_metas
		child_values.append(child_value)
	
	local_metas = unprocessed_data[:n_meta]

	metas += unprocessed_data[:n_meta]

	if n_childs == 0:
		return metas, unprocessed_data[n_meta:], sum(local_metas)

	value = 0
	for ref in local_metas:
		print(local_metas)
		if ref in range(1, len(child_values)+1):
			value += child_values[ref-1]
	return metas, unprocessed_data[n_meta:], value


with open('input') as f:
	unprocessed_data = [int(x) for x in f.read().splitlines()[0].split()]
	metas, _, value = parse(unprocessed_data)
	print(sum(metas), value)