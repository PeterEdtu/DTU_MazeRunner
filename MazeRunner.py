from enum import Enum

class PythonBot():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.moveList = []
        self.matrix = []
        self.found = False
        
        for pos in board.maze:
            print(str(pos))
            
    def primarySearch(self, dest):
            
            if board.maze[dest.y][dest.x - 1] != "#" and board.maze[dest.y][dest.x - 1]!= "*":
                print("0 R")
                self.moveList.append("0 R") #need to go Right                
                newDest = Point(dest.x - 1, dest.y)
                self.secondarySearch(newDest)
                
            self.moveList=[]
                
            if board.maze[dest.y + 1][dest.x] != "#" and board.maze[dest.y + 1][dest.x]!= "*":
                print("0 U")                
                self.moveList.append("0 U") #need to go Up
                newDest = Point(dest.x, dest.y + 1)
                self.secondarySearch(newDest)
                
            self.moveList=[]
                
            if board.maze[dest.y][dest.x + 1] != "#"and board.maze[dest.y][dest.x + 1]!= "*":
                print("0 L")                
                self.moveList.append("0 L") #need to go Left
                newDest = Point(dest.x + 1, dest.y)
                self.secondarySearch(newDest)
            
            self.moveList=[]
                
            if board.maze[dest.y - 1][dest.x] != "#" and board.maze[dest.y - 1][dest.x]!= "*":
                print("0 D")                
                self.moveList.append("0 D") #need to go Down
                newDest = Point(dest.x, dest.y - 1)
                self.secondarySearch(newDest)
                
            print("Done !!!")
            
    def secondarySearch(self, dest):
        right = False
        left = False
        up = False
        down = False
        
        if board.maze[dest.y][dest.x] == "0":
            print("I find a way : " + str(self.moveList))
            self.matrix.append(self.moveList.copy())
            return
        
        else:
            board.maze[dest.y][dest.x]= "*"
            
        for n in range(0,4):
              
            print("Searching : " +  board.maze[dest.y][dest.x] + " / " + str(dest.x) + "," + str(dest.y))
            
            if board.maze[dest.y][dest.x - 1] != "#" and board.maze[dest.y][dest.x - 1]!= "*" and right == False:
                print("0 R")
                self.moveList.append("0 R") #need to go Right                
                newDest = Point(dest.x - 1, dest.y)
                self.secondarySearch(newDest)
                print("Remove : " + str(self.moveList.pop(len(self.moveList)-1)))
                right = True
                
                
            if board.maze[dest.y + 1][dest.x] != "#" and board.maze[dest.y + 1][dest.x]!= "*" and up == False:
                print("0 U")                
                self.moveList.append("0 U") #need to go Up
                newDest = Point(dest.x, dest.y + 1)
                self.secondarySearch(newDest)
                print("Remove : " + str(self.moveList.pop(len(self.moveList)-1)))
                up = True
                
                
            if board.maze[dest.y][dest.x + 1] != "#"and board.maze[dest.y][dest.x + 1]!= "*" and left == False:
                print("0 L")                
                self.moveList.append("0 L") #need to go Left
                newDest = Point(dest.x + 1, dest.y)
                self.secondarySearch(newDest)
                print("Remove : " + str(self.moveList.pop(len(self.moveList)-1)))
                left = True
                
                
            if board.maze[dest.y - 1][dest.x] != "#" and board.maze[dest.y - 1][dest.x]!= "*" and down == False:
                print("0 D")                
                self.moveList.append("0 D") #need to go Down
                newDest = Point(dest.x, dest.y - 1)
                self.secondarySearch(newDest)
                print("Remove : " + str(self.moveList.pop(len(self.moveList)-1)))
                down = True
                
        
            self.removePreviousGraphicMove(dest);
            
    def removePreviousGraphicMove(self,dest):
            if board.maze[dest.y][dest.x]== "*":
                board.maze[dest.y][dest.x]= " "

                
    def showMoves(self):
        for listE in self.matrix:
            print(str(listE))
            

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def __repr__(self):
		return self.__str__();
		
	def __str__(self):
		return "Point: { x: " + str(self.x) + " y: " + str(self.y) + " }"
		
class Direction(Enum):
	Up, Down, Left, Right = range(4)
	
	def __str__(self):
		return self.name[0]
		
class Board:
	def __init__(self, robots, maze):
		self.robots = robots
		self.maze = maze
		
	def __str__(self):
		s = ""
		for i in range(len(maze[0])):
			for j in range(len(maze)):
				s += maze[j][i]
			s += "\n"
		return s
		
EMPTY_CHAR = ' '
WALL_CHAR = '#'
GOAL_CHAR = '!'
BOT_CHAR = "0"

goal = None
# Switches and the walls, which they affect
toggle_switches = {}
hold_switches = {}

board = None

def compute_solution(Matrix):
	# TODO: Implement really clever stuff here!
	# For now - just output a couple of moves:
    for list_ in Matrix:
        print(str(list_))
        
class Node():
    def __init__(self, pos, parent, nexts):
        self.pos = pos
        self.parent = parent
        self.nexts = nexts

def parse():
	# TODO:
	# This template was intended for Python 2.
	# If using Python 3, simply change raw_input() to input()
	
	#dims = input().split(' ')
     dims = "7 7".split(' ')
	#width = int(dims[0])
     width = int(dims[0])
     #height = int(dims[1])
     height = int(dims[1])
	
     #no_of_Robots = int(input())
     no_of_Robots = int(1)
     
     robots = [None] * no_of_Robots
		
	#switches = input().split(' ')
     switches = "0 0".split(' ')
     no_of_toggle_switches = int(switches[0])
     no_of_hold_switches = int(switches[1])
 
     maze = []
     for i in range(0,height):
         #line = input()
         if i == 0:
             line = "#######"
        
         elif i == 1:
             line = "#  # !#"
             
         elif i == 2:
             line = "#    ##"
             
         elif i == 3:
             line = "#     #"
        
         elif i == 4:
             line = "# ## 0#"
         elif i == 5:
             line = "#######"
         elif i == 6:
             line = "#######"
             
         row = []
         for j in range(width):
             if line[j] == GOAL_CHAR:
                 goal = Point(j, i)
             elif line[j].isdigit():
                 robots[int(line[j])] = Point(j, i)
             if line[j] == BOT_CHAR:
                    global bot
                    bot= Point(j, i)
                    
             if line[j] != EMPTY_CHAR and line[j] != WALL_CHAR and not line[j].isalpha() and line[j] != BOT_CHAR and line[j] != GOAL_CHAR:
                 print ("Error: Unknown character '" + str(line[j]) + "' on line " + str(i+1) + ", column " + str(j+1))
			
             row.append(line[j])
			
         maze.append(row)
			
     for i in range(no_of_toggle_switches):
         switch = raw_input().split(' ')
         toggle_switches[switch[0]] = Point(int(switch[1]), int(switch[2]))
			
     for i in range(no_of_hold_switches):
         switch = raw_input().split(' ')
         hold_switches[switch[0]] = Point(int(switch[1]), int(switch[2]))
		
     if goal is None:
         print ("Error: No goal found on board")
  
     global board
		
  
     board = Board(robots, maze)
 
     return goal
 


dest = parse()
 
"""
My bot
"""
print(str(bot.x) + " " + str(bot.y))

print(str(board.maze[bot.y][bot.x]))

print(str(board.maze[bot.y - 1][bot.x]))

print("GOAL : " + str(dest.x) + ", " + str(dest.y))

myBot = PythonBot(bot.x, bot.y)

myBot.primarySearch(dest)

#myBot.showMoves()

compute_solution(myBot.matrix)
