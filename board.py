import copy

class Dirs:
	UP=1
	RIGHT=2
	DOWN=3
	LEFT=4

class Puzzle():
	Solution = [0,1,2,3,4,5,6,7,8]
	cells = []

	def __init__(self, cells):
		self.cells = cells
	
	def is_solution(self):
		return self.Solution == self.cells

	def zero_position(self):
		return self.cells.index(0)

	def swap_index(self,swap_index):
		self.cells[self.zero_position()] = self.cells[swap_index]
		self.cells[swap_index] = 0

	def prn(self):
		return self.cells

	def val(self):
		retval = 0

		if (self.cells[0] == 0):
			retval = retval + 1

		if (self.cells[1] == 1):
			retval = retval + 1

		if (self.cells[2] == 2):
			retval = retval + 1

		if (self.cells[3] == 3):
			retval = retval + 1

		if (self.cells[4] == 4):
			retval = retval + 1

		if (self.cells[5] == 5):
			retval = retval + 1

		if (self.cells[6] == 6):
			retval = retval + 1

		if (self.cells[7] == 7):
			retval = retval + 1

		if (self.cells[8] == 8):
			retval = retval + 1

		return retval

class State():
	Puzzle = Puzzle([0,1,2,3,4,5,6,7,8])
	Path = []

	def __init__(self,puzzle,path):
		self.Puzzle = puzzle
		self.Path = path

	def __eq__(self,other):
		if ((self.Puzzle.cells) == (other.Puzzle.cells)):
			return 1
		else:
			return 0
	
	def is_solution(self):
		return self.Puzzle.is_solution()

	def branches(self):
		retval = []

		tmp = self.branch_toward(Dirs.UP)
		if (tmp):
			retval.append(tmp)

		tmp = self.branch_toward(Dirs.RIGHT)
		if (tmp):
			retval.append(tmp)

		tmp = self.branch_toward(Dirs.DOWN)
		if (tmp):
			retval.append(tmp)

		tmp = self.branch_toward(Dirs.LEFT)
		if (tmp):
			retval.append(tmp)

#		retval[:] = [x for x in retval if x != False]

		return retval

	def branch_toward(self, direction):
		blank_position = self.Puzzle.zero_position()
		blankx = blank_position % 3
		blanky = int(blank_position / 3)
#		print("= " + str(blank_position) + " , " + str(blankx) + " , " + str(blanky) + " = " + str(self.Puzzle.prn()))

		if (direction == Dirs.UP):
			if (blanky > 0):
				tmp = copy.deepcopy(self.Puzzle)
				tmp.swap_index(blank_position - 3)
				tmp2 = copy.deepcopy(self.Path)
				tmp2.append("up")
				return State(tmp,tmp2)

		if (direction == Dirs.RIGHT):
			if (blankx < 2):
				tmp = copy.deepcopy(self.Puzzle)
				tmp.swap_index(blank_position + 1)
				tmp2 = copy.deepcopy(self.Path)
				tmp2.append("right")
				return State(tmp,tmp2)

		if (direction == Dirs.DOWN):
			if (blanky < 2):
				tmp = copy.deepcopy(self.Puzzle)
				tmp.swap_index(blank_position + 3)
				tmp2 = copy.deepcopy(self.Path)
				tmp2.append("down")
				return State(tmp,tmp2)

		if (direction == Dirs.LEFT):
			if (blankx > 0):
				tmp = copy.deepcopy(self.Puzzle)
				tmp.swap_index(blank_position - 1)
				tmp2 = copy.deepcopy(self.Path)
				tmp2.append("left")
				return State(tmp,tmp2)

		return False

visited = []
frontier = []

def search(state):
	tmp = state.branches()
	visited.append(state)
	print("count = " + str(len(tmp)) + ", visited = " + str(len(visited)) + ", frontier = " + str(len(frontier)))
	tmp[:] = [x for x in tmp if visited.count(x) == 0]
	for item in tmp:
		frontier.append(item)
	sorted(frontier, key=lambda State: State.Puzzle.val())

def solve(puzzle):
	state = State(puzzle,[])
	while (True):
		if (state.is_solution()):
			break
		search(state)
		state = frontier.pop(0)
	return state

#jason = Puzzle([1,4,2,3,0,5,6,7,8])
jason = Puzzle([7,6,2,5,3,1,0,4,8])
#jason = Puzzle([7,6,2,5,3,1,0,4,8])
#print(jason.cells)
#print(jason.is_solution())
#print(jason.zero_position())
#print(jason.swap_index(0))
#print(jason.is_solution())
#print(jason.cells)
#print("----")
ed = State(jason,[])
print("init = " + str(ed.Puzzle.prn()))
solution = solve(jason)
print(solution.Puzzle.prn())
print(solution.Path)

