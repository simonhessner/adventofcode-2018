from collections import defaultdict

registers = defaultdict(int)
instructions = []

commands = {
	"addr": lambda a, b : registers[a]  + registers[b],
	"addi": lambda a, b : registers[a]  + int(b),
	"mulr": lambda a, b : registers[a]  * registers[b],
	"muli": lambda a, b : registers[a]  * int(b),
	"banr": lambda a, b : registers[a]  & registers[b],
	"bani": lambda a, b : registers[a]  & int(b),
	"borr": lambda a, b : registers[a]  | registers[b],
	"bori": lambda a, b : registers[a]  | int(b),
	"setr": lambda a, b : int(registers[a]),
	"seti": lambda a, b : int(a),
	"gtir": lambda a, b : int(int(a) > registers[b]),
	"gtri": lambda a, b : int(registers[a] > int(b)),
	"gtrr": lambda a, b : int(registers[a] > registers[b]),
	"eqir": lambda a, b : int(int(a) == registers[b]),
	"eqri": lambda a, b : int(registers[a] == int(b)),
	"eqrr": lambda a, b : int(registers[a] == registers[b])
}

possible_mappings = defaultdict(set)

def parse_parts(parts):
	parsed = []
	for v in parts:
		v = v.strip()
		if len(v) < 1:
			continue
		if v[0] == "[":
			v = v[1:]
		if v[-1] == "]":
			v = v[:-1]
		if v[-1] == ",":
			v = v[:-1]
		parsed.append(int(v))
	return parsed

n = 0

with open("input") as f:
	lines = f.read().splitlines()
	for line in lines[:3353]:
		if len(line.strip()) < 1:
			continue

		parts = tuple(line.split(" "))

		if len(parts) > 1:
			if parts[0] == "Before:":
				parsed_before = parse_parts(parts[1:])
				
			elif parts[0] == "After:":
				parsed_after = parse_parts(parts[1:])
				c = 0
				for cmnd in commands:
					registers.update(enumerate(parsed_before))
					result = commands[cmnd](in1, in2)
					registers[out] = result
					if all(registers[k] == parsed_after[k] for k in registers.keys()):
						c += 1
						possible_mappings[opcode].add(cmnd)
				if c >= 3:
					n += 1

			else:
				opcode, in1, in2, out = parts
				opcode = int(opcode)
				in1 = int(in1)
				in2 = int(in2)
				out = int(out)

	print("Part 1", n)
	
	registers.clear()

	while any(len(x) > 1 for x in possible_mappings.values()):
		unique = [k for k,v in possible_mappings.items() if len(v) == 1]
		for k in unique:
			for _k in possible_mappings.keys():
				if _k != k:
					possible_mappings[_k] -= possible_mappings[k]

	for cmd in lines[3354:]:
		cmd = cmd.strip()
		if len(cmd) < 1:
			continue
		opcode, a, b, c = [int(x) for x in cmd.split(" ")]
		cmdname = list(possible_mappings[opcode])[0]
		registers[c] = commands[cmdname](a,b)

print("Part 2", registers[0])