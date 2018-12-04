# https://adventofcode.com/2018/day/4

from collections import defaultdict
import operator

with open('input') as f:
	lines = f.read().splitlines()

	# date format is nice (big time unit -> small time unit: year-month-day hour:minute) => normal sort is enough
	lines.sort()

	sleep_per_minute = defaultdict(lambda : defaultdict(int))

	guard_id = -1
	sleepstart = -1

	for line in lines:
		firstpart	= line.split("] ")[0]
		lastpart	= line.split("] ")[1]
		time 		= firstpart.split(" ")[1]
		minute		= int(time.split(":")[1])		

		if lastpart.startswith("Guard #"): # new guard will be processed
			guard_id = int(lastpart.split(" ")[1][1:])
		elif lastpart.startswith("wakes"): # last seen guard wakes up
			for m in range(sleepstart, minute):
				sleep_per_minute[guard_id][m] += 1
		else: # last seen guard falls asleep
			sleepstart = minute

	sum_per_guard = [(guard, sum(minutes.values())) for guard, minutes in sleep_per_minute.items()]
	guard = int(max(sum_per_guard, key=operator.itemgetter(1))[0])
	max_minute = max(sleep_per_minute[guard].items(), key=operator.itemgetter(1))[0]
	print("A", guard * max_minute)

	gid = None
	max_min_val = None
	max_min = None

	for guard, minutes in sleep_per_minute.items():
		for minute, value in minutes.items():
			if max_min_val is None or value > max_min_val:
				max_min_val = value
				gid = int(guard)
				max_min = minute

	print("B", gid * max_min)