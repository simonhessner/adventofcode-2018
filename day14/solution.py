# https://adventofcode.com/2018/day/14

def part1_condition(recipes, puzzle_input):
	return len(recipes) >= 10 + puzzle_input

def part2_condition(recipes, puzzle_input):
	search = [int(x) for x in str(puzzle_input)]
	return recipes[-len(search):] == search

def do_until(condition, puzzle_input):
	recipes = [3,7]
	current = [0,1]

	while True:
		current_scores = [recipes[i] for i in current]
		newscore = sum(current_scores)

		for r in [int(x) for x in str(newscore)]:
			recipes.append(r)
			if condition(recipes, puzzle_input):
				return recipes

		current = [(current[i] + current_scores[i] + 1) % len(recipes) for i in range(len(current_scores))]
		

inp = 147061

recipes = do_until(part1_condition, inp)
print("".join(map(str, recipes[-10:])))
	
recipes = do_until(part2_condition, inp)
print(len(recipes)-len(str(inp)))