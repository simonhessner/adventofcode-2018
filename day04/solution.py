import datetime
import operator

with open('input') as f:
	lines = f.read().splitlines()

	guards = {}
	guard = -1
	sleepstart = -1
	sleepend = -1

	lines = sorted(lines, key=lambda x: datetime.datetime.strptime(x.split("] ")[0][1:], "%Y-%m-%d %H:%M").timestamp())

	for line in lines:
		firstpart = line.split("] ")[0]
		lastpart = line.split("] ")[1]

		date = firstpart.split(" ")[0]
		time = firstpart.split(" ")[1]

		year = int(date.split("-")[0][1:])
		month = int(date.split("-")[1])
		day = int(date.split("-")[2])

		hour = int(time.split(":")[0])
		minute = int(time.split(":")[1])

		if lastpart.startswith("Guard #"):
			guard = int(lastpart.split(" ")[1][1:])			
			if guard not in guards:
				guards[guard] = [0 for _ in range(60)]
		elif lastpart.startswith("wakes"):
			sleepend = minute
			for m in range(sleepstart, sleepend):
				guards[guard][m] += 1
			sleepstart = -1
			sleepend = -1
		elif lastpart.startswith("falls"):
			if sleepstart != -1:
				print("ERROR")
			sleepstart = minute

	minutes_asleep = {guard : sum(sl) for guard, sl in guards.items()}
	_id, minsum = max(minutes_asleep.items(), key=operator.itemgetter(1))
	print(_id * [i for i in range(60) if guards[_id][i] == max(guards[_id])][0])

	max_per_min = {guard : max(sl) for guard, sl in guards.items()}
	print(max_per_min)
	_id, amount = max(max_per_min.items(), key=operator.itemgetter(1))
	m = guards[_id].index(amount)
	print(_id * m)