import copy
from collections import deque

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

	def __eq__(self,other):
		if (other.cells == self.cells):
			return True
		return False

	def cost(self):
		retval = 9
		if (self.cells[0] == 0):
			retval = retval - 1
		if (self.cells[1] == 1):
			retval = retval - 1
		if (self.cells[2] == 2):
			retval = retval - 1
		if (self.cells[3] == 3):
			retval = retval - 1
		if (self.cells[4] == 4):
			retval = retval - 1
		if (self.cells[5] == 5):
			retval = retval - 1
		if (self.cells[6] == 6):
			retval = retval - 1
		if (self.cells[7] == 7):
			retval = retval - 1
		if (self.cells[8] == 8):
			retval = retval - 1
		return retval


	def prn(self):
		return "[" + str(self.cells[0]) + "," + str(self.cells[1]) + "," + str(self.cells[2]) + "," + str(self.cells[3]) + "," + str(self.cells[4]) + "," + str(self.cells[5]) + "," + str(self.cells[6]) + "," + str(self.cells[7]) + "," + str(self.cells[8]) + "]"

class State():
        puzzle = Puzzle([0,1,2,3,4,5,6,7,8])
        path = []

        def __init__(self,puzzle,path):
                self.puzzle = puzzle
                self.path = path

        def is_solution(self):
                return self.puzzle.is_solution()

        def branches(self):
                retval = []

                blank_position = self.puzzle.zero_position()
                blankx = blank_position % 3
                blanky = int(blank_position / 3)

		retval.append(self.branch_check(self.puzzle,self.path,Dirs.UP))
		retval.append(self.branch_check(self.puzzle,self.path,Dirs.RIGHT))
		retval.append(self.branch_check(self.puzzle,self.path,Dirs.DOWN))
		retval.append(self.branch_check(self.puzzle,self.path,Dirs.LEFT))

		retval[:] = (value for value in retval if value != False)

                return retval

	def __eq__(self,other):
		if (self.puzzle.cost() > other.puzzle.cost()):
			return 1
		if (self.puzzle.cost() == other.puzzle.cost()):
			return 0
		if (self.puzzle.cost() < other.puzzle.cost()):
			return -1

	def branch_check(self,puzzle,path,dir):
                blank_position = self.puzzle.zero_position()
                blankx = blank_position % 3
                blanky = int(blank_position / 3)
#		print("blankp = " + str(blank_position) + " , blankx = " + str(blankx) + " , blanky = " + str(blanky))

		if (dir == Dirs.UP):
	                if (blanky > 0):
				tmp = copy.deepcopy(self.puzzle)
				tmp2 = copy.deepcopy(self.path)
				tmp.swap_index(blank_position - 3)
				tmp2.append("up")
				return State(tmp,tmp2)

		if (dir == Dirs.RIGHT):
	                if (blankx < 2):
				tmp = copy.deepcopy(self.puzzle)
				tmp2 = copy.deepcopy(self.path)
				tmp.swap_index(blank_position + 1)
				tmp2.append("right")
				return State(tmp,tmp2)

		if (dir == Dirs.DOWN):
	                if (blanky < 2):
				tmp = copy.deepcopy(self.puzzle)
				tmp2 = copy.deepcopy(self.path)
				tmp.swap_index(blank_position + 3)
				tmp2.append("down")
				return State(tmp,tmp2)

		if (dir == Dirs.LEFT):
	                if (blankx > 0):
				tmp = copy.deepcopy(self.puzzle)
				tmp2 = copy.deepcopy(self.path)
				tmp.swap_index(blank_position - 1)
				tmp2.append("left")
				return State(tmp,tmp2)

		return False


visited = []
frontier = []

def search(state):
	tmp = state.branches()
	for item in tmp:
		try:
			loc = visited.index(item)
		except ValueError:
			frontier.append(item)
#			print(item.puzzle.prn() + " , " + str(item.path))

#	tmp[:] = (value for value in tmp if visited.count(value) == 0)
#	frontier.extend(tmp)
	visited.append(state)
#	for item in tmp:
#		print(item.puzzle.prn() + " , " + str(item.path))

def solve(puzzle):
	state = State(puzzle,[])
	while (True):
#		foo = raw_input("enter")
		if (state.is_solution()):
			break;
		search(state)
		frontier.sort()
		print(str(len(frontier)) + " , " + str(len(visited)))
		state = frontier.pop(0)
#		print("Current = " + state.puzzle.prn())
	return state

#solve(Puzzle([3,1,2,0,4,5,6,7,8]))

#jason = Puzzle([3,1,2,0,4,5,6,7,8])
#print(jason.cells)
#print(jason.is_solution())
#print(jason.zero_position())
#print(jason.swap_index(0))
#print(jason.is_solution())
#print(jason.cells)
#print("----")

ed = Puzzle([1,4,2,3,0,5,6,7,8])
#ed = Puzzle([1,2,3,4,5,6,7,8,0])
#ed = Puzzle([7,6,2,5,3,1,0,4,8])
print(ed.prn())
print(ed.is_solution())
soln = solve(ed)
print(soln.path)

