import copy
import threading

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

	def key(self):
		return self.cells[0]*100000000 + self.cells[1]*10000000 + self.cells[2]*1000000 + self.cells[3]*100000 + self.cells[4]*10000 + self.cells[5]*1000 + self.cells[6]*100 + self.cells[7]*10 + self.cells[8]

	def val(self):
		retval = 1

		if (self.cells[0] != 0):
			retval = retval + 1

		if (self.cells[1] != 1):
			retval = retval + 1

		if (self.cells[2] != 2):
			retval = retval + 1

		if (self.cells[3] != 3):
			retval = retval + 1

		if (self.cells[4] != 4):
			retval = retval + 1

		if (self.cells[5] != 5):
			retval = retval + 1

		if (self.cells[6] != 6):
			retval = retval + 1

		if (self.cells[7] != 7):
			retval = retval + 1

		if (self.cells[8] != 8):
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
		self.branch_toward(Dirs.UP)
		self.branch_toward(Dirs.RIGHT)
		self.branch_toward(Dirs.DOWN)
		self.branch_toward(Dirs.LEFT)

	def branch_toward(self, direction):
		blank_position = self.Puzzle.zero_position()
		blankx = blank_position % 3
		blanky = int(blank_position / 3)
		tmp3 = None

		if (direction == Dirs.UP):
			if (blanky > 0):
				tmp = copy.deepcopy(self.Puzzle)
				tmp.swap_index(blank_position - 3)
				tmp2 = copy.deepcopy(self.Path)
				tmp2.append("up")
				tmp3 = State(tmp,tmp2)

		if (direction == Dirs.RIGHT):
			if (blankx < 2):
				tmp = copy.deepcopy(self.Puzzle)
				tmp.swap_index(blank_position + 1)
				tmp2 = copy.deepcopy(self.Path)
				tmp2.append("right")
				tmp3 = State(tmp,tmp2)

		if (direction == Dirs.DOWN):
			if (blanky < 2):
				tmp = copy.deepcopy(self.Puzzle)
				tmp.swap_index(blank_position + 3)
				tmp2 = copy.deepcopy(self.Path)
				tmp2.append("down")
				tmp3 = State(tmp,tmp2)

		if (direction == Dirs.LEFT):
			if (blankx > 0):
				tmp = copy.deepcopy(self.Puzzle)
				tmp.swap_index(blank_position - 1)
				tmp2 = copy.deepcopy(self.Path)
				tmp2.append("left")
				tmp3 = State(tmp,tmp2)

		if (tmp3):
			if not (visited.get(tmp3.Puzzle.key(),False)):
				frontier.append(tmp3)
			visited[tmp3.Puzzle.key()] = 1

visited = {}
frontier = []

def compare(a,b):
	if (a.Puzzle.val() > b.Puzzle.val()):
		return 1
	if (a.Puzzle.val() == b.Puzzle.val()):
		return 0
	if (a.Puzzle.val() < b.Puzzle.val()):
		return -1

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0  
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


def solve(puzzle):
	try:
		state = State(puzzle,[])
		while (True):
			if (state.is_solution()):
				break
			threading.Thread(target=state.branches, args=()).start()
#			sorted(frontier, key=cmp_to_key(compare))
			print("visited = " + str(len(visited)) + ", frontier = " + str(len(frontier)))
			state = frontier.pop(0)
		return state
	except KeyboardInterrupt:
		for f in frontier:
			print(f.Puzzle.val())

#jason = Puzzle([1,4,2,3,0,5,6,7,8])
jason = Puzzle([7,6,2,5,3,1,0,4,8])
#jason = Puzzle([7,6,2,5,3,1,0,4,8])
ed = State(jason,[])
print("init = " + str(ed.Puzzle.prn()))
solution = solve(jason)
print(solution.Puzzle.prn())
print(solution.Path)


