from collections import defaultdict

def run(workers):
	missing_jobs = set()
	delay = 60

	with open('input') as f:
		lines = f.read().splitlines()
		requirements = defaultdict(set)
		for line in lines:
			parts = line.split(" ")
			requirements[parts[-3]].add(parts[1])
			missing_jobs.add(parts[1])
			missing_jobs.add(parts[-3])

		waittimes = [0] * workers
		step_agent = [None] * workers
		
		a = []
		duration = 0
		while len(missing_jobs) > 0:
			for i in range(workers):
				if waittimes[i] == 0:
					job_finished = step_agent[i]
					step_agent[i] = None
					if job_finished is not None:
						a.append(job_finished)
						missing_jobs = missing_jobs - set([job_finished])
						requirements = {s : r-set([job_finished]) for s,r in requirements.items()}

					possible = [st for st in missing_jobs if len(requirements[st]) == 0 and st not in step_agent]
					possible.sort()

					if len(possible) > 0:
						nextstep = possible[0]				
						
						waittimes[i] = delay + 1 + ord(nextstep) - ord('A')
						step_agent[i] = nextstep

			waittimes = [max(0, x-1) for x in waittimes]
					
			if len(missing_jobs) > 0:
				duration += 1


		return (duration, "".join(a))			

result1 = run(1)
print("Part 1\t", result1[1])

result2 = run(5)
print("Part 2\t", result2[0])