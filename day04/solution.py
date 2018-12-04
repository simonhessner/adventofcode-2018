# https://adventofcode.com/2018/day/4

from collections import defaultdict
from collections import Counter

with open('input') as f:
	lines = f.read().splitlines()

	guards = defaultdict(lambda : Counter({ minute : 0 for minute in range(60) }))
	guard_id = -1
	sleepstart = -1

	# I just realized that you do not have to do the date conversion since the format is already nice (big time unit -> small time unit: year-month-day hour:minute)
	# Thus, you do not need this:
	# lines = sorted(lines, key=lambda x: datetime.datetime.strptime(x[x.index("[")+1:x.index("]")], "%Y-%m-%d %H:%M").timestamp())
	# This is enough (string sort):
	lines.sort()

	for line in lines:
		firstpart	= line.split("] ")[0]
		lastpart	= line.split("] ")[1]
		time 		= firstpart.split(" ")[1]
		minute		= int(time.split(":")[1])		

		if lastpart.startswith("Guard #"): # new guard will be processed
			guard_id = int(lastpart.split(" ")[1][1:])
		elif lastpart.startswith("wakes"): # last seen guard wakes up
			guards[guard_id].update({_min : 1 for _min in range(sleepstart, minute)})
		else: # last seen guard falls asleep
			sleepstart = minute

	gid_max_sum = -1
	max_sum = -1
	max_minute_p1 = -1
	gid_max_minute = -1
	max_minute_val = -1
	max_minute_p2 = -1

	for guard_id, sleep_count in guards.items():
		sleep_count = list(dict(sleep_count).values())
		if sum(sleep_count) > max_sum:
			max_sum = sum(sleep_count)
			gid_max_sum = guard_id
			max_minute_p1 = sleep_count.index(max(sleep_count))

		if max(sleep_count) > max_minute_val:
			gid_max_minute = guard_id
			max_minute_val = max(sleep_count)
			max_minute_p2 = sleep_count.index(max_minute_val)

	print("A", gid_max_sum * max_minute_p1)
	print("B", gid_max_minute * max_minute_p2)