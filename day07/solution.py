from collections import defaultdict

def run(workers):
	requirements = defaultdict(set)
	missing_steps = set()
	finish_order = []

	waittimes = [0] * workers
	works_on = [None] * workers

	with open('input') as f:		
		for line in f.read().splitlines():
			parts = line.split(" ")
			requirements[parts[-3]].add(parts[1])
			missing_steps |= set([parts[1], parts[-3]])		
		
	duration = 0
	while len(missing_steps) > 0:
		for i in range(workers):
			if waittimes[i] == 0:
				job_finished = works_on[i]
				if job_finished is not None:
					finish_order.append(job_finished)
					missing_steps = missing_steps - set([job_finished])
					requirements = {step : reqs-set([job_finished]) for step,reqs in requirements.items()}
				works_on[i] = None

				possible = sorted([step for step in missing_steps if len(requirements[step]) == 0 and step not in works_on])

				if len(possible) > 0:
					works_on[i] = possible[0]					
					waittimes[i] = 60 + ord(works_on[i]) - ord('A') + 1
					

		waittimes = [max(0, x-1) for x in waittimes]
				
		if len(missing_steps) > 0:
			duration += 1

	return (duration, "".join(finish_order))			

_, job_order = run(1)
print("Part 1\t", job_order)

duration, _ = run(5)
print("Part 2\t", duration)