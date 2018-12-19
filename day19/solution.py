# https://adventofcode.com/2018/day/19

import re

with open("input") as f:
	lines = f.read().splitlines()
	ip_reg = int(re.findall('\d+', lines[0])[0])

	# Copied from day16
	commands = {
		"addr": lambda r, a, b : r[a]  + r[b],
		"addi": lambda r, a, b : r[a]  + int(b),
		"mulr": lambda r, a, b : r[a]  * r[b],
		"muli": lambda r, a, b : r[a]  * int(b),
		"banr": lambda r, a, b : r[a]  & r[b],
		"bani": lambda r, a, b : r[a]  & int(b),
		"borr": lambda r, a, b : r[a]  | r[b],
		"bori": lambda r, a, b : r[a]  | int(b),
		"setr": lambda r, a, b : int(r[a]),
		"seti": lambda r, a, b : int(a),
		"gtir": lambda r, a, b : int(int(a) > r[b]),
		"gtri": lambda r, a, b : int(r[a] > int(b)),
		"gtrr": lambda r, a, b : int(r[a] > r[b]),
		"eqir": lambda r, a, b : int(int(a) == r[b]),
		"eqri": lambda r, a, b : int(r[a] == int(b)),
		"eqrr": lambda r, a, b : int(r[a] == r[b])
	}

	instructions = []
	for line in lines[1:]:
		instructions.append(tuple(line.split(" ")))

	def run(r0_start):
		registers = [r0_start, 0,0,0,0,0]

		while registers[ip_reg] in range(len(instructions)):
			instr = instructions[registers[ip_reg]]
		
			if registers[ip_reg] == 1: # When the program reaches this point, register 2 contanins a number whose prime factors are summed up to get the final result
				return sum([x for x in range(1, registers[2]+1) if registers[2] % x == 0])
				
			registers[int(instr[3])] = commands[instr[0]](registers, int(instr[1]), int(instr[2]))
			registers[ip_reg] += 1


print("A", run(0))
print("B", run(1))