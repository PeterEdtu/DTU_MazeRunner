from enum import Enum
import time
import math

class PythonBot():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.moveList = []
        self.matrix = []
        self.found = False
        
        for pos in board.maze:
            print(str(pos))
            
    def primarySearch(self, dest, goal):
        
            self.found = False
            
            if board.maze[dest.y][dest.x - 1] != "#" and board.maze[dest.y][dest.x - 1]!= "*":
                self.moveList.append("0 L") #need to go Right                
                newDest = Point(dest.x - 1, dest.y)
                
                if self.secondarySearch(newDest, goal) == True:
                    return
            self.moveList = []
                
            if board.maze[dest.y][dest.x + 1] != "#"and board.maze[dest.y][dest.x + 1]!= "*":
                #print("0 R")                
                self.moveList.append("0 R") #need to go Left
                newDest = Point(dest.x + 1, dest.y)
                
                if self.secondarySearch(newDest, goal) == True:
                    return
                    
            self.moveList = []
                
            if board.maze[dest.y + 1][dest.x] != "#" and board.maze[dest.y + 1][dest.x]!= "*":
                #print("0 D")                
                self.moveList.append("0 D") #need to go Up
                newDest = Point(dest.x, dest.y + 1)
                
                if self.secondarySearch(newDest, goal) == True:
                    return
                    
            self.moveList = []
                  
            if board.maze[dest.y - 1][dest.x] != "#" and board.maze[dest.y - 1][dest.x]!= "*":
                #print("0 U")                
                self.moveList.append("0 U") #need to go Down
                newDest = Point(dest.x, dest.y - 1)
                
                if self.secondarySearch(newDest, goal) == True:
                    return
                    
                
            print("Done !!!")
            
    def secondarySearch(self, dest, goal):
        #print(len(self.matrix))        
        
        right = False
        left = False
        up = False
        down = False
        
        if board.maze[dest.y][dest.x] == "!":
            #print("I find a way : " + str(self.moveList))
            self.found = True
            self.matrix.append(self.moveList.copy())
            return True
        
        else:
            board.maze[dest.y][dest.x]= "*"
            
        if self.found == False:
              
            #print("Searching : " +  board.maze[dest.y][dest.x] + " / " + str(dest.x) + "," + str(dest.y))
            
            #print("len : " + str(len(self.moveList)))            
            distances = []  
            
            distanceLeftPoint = calculateDistance(Point(dest.x - 1, dest.y), goal)
            distanceRightPoint = calculateDistance(Point(dest.x + 1, dest.y), goal)
            distanceDownPoint = calculateDistance(Point(dest.x, dest.y + 1), goal)
            distanceUpPoint = calculateDistance(Point(dest.x, dest.y - 1),goal)
            
            
            distances.append(distanceLeftPoint)
            distances.append(distanceRightPoint)
            distances.append(distanceDownPoint)
            distances.append(distanceUpPoint)
            
            distances.sort()
            
            #print(distances)
            
            for w in range(0, len(distances)):
            
                    if distances[w] == distanceLeftPoint: #left point est plus proche
                     #print("left short")
                     try:
                         if board.maze[dest.y][dest.x - 1] != "#" and board.maze[dest.y][dest.x - 1]!= "*" and left == False:
                             self.moveList.append("0 L")             
                             newDest = Point(dest.x - 1, dest.y)
                
                             if self.secondarySearch(newDest, goal) == True:
                                 return
                
                        # print("Remove : " + str(self.moveList.pop(len(self.moveList)-1)))
                             left = True
                             self.removePreviousGraphicMove(newDest);
                     except:
                         pass

                    elif distances[w] == distanceRightPoint: #right point est plus proche
                    # print("right short")
                     try:
                         if board.maze[dest.y][dest.x + 1] != "#"and board.maze[dest.y][dest.x + 1]!= "*" and right == False:
                             self.moveList.append("0 R")
                             newDest = Point(dest.x + 1, dest.y)
                
                             if self.secondarySearch(newDest, goal) == True:
                                 return
                                
                    
                        # print("Remove : " + str(self.moveList.pop(len(self.moveList)-1)))
                             right = True
                             self.removePreviousGraphicMove(newDest);

                     except:
                         pass
                 
                    elif distances[w] == distanceDownPoint: #down point est plus proche
                     #print("down short")
                     try:                         
                         if board.maze[dest.y + 1][dest.x] != "#" and board.maze[dest.y + 1][dest.x]!= "*" and down == False:
                             self.moveList.append("0 D") #need to go down
                             newDest = Point(dest.x, dest.y + 1)
                
                             if self.secondarySearch(newDest, goal) == True:
                                 return
                    
                         #print("Remove : " + str(self.moveList.pop(len(self.moveList)-1)))
                             down = True
                             self.removePreviousGraphicMove(newDest);
                             
                     except:
                         pass
                 
                    elif distances[w] == distanceUpPoint: #up point est plus proche
                     #print("up short")                 
                     try:                         
                         if board.maze[dest.y - 1][dest.x] != "#" and board.maze[dest.y - 1][dest.x]!= "*" and up == False:
                             self.moveList.append("0 U") #need to go up
                             newDest = Point(dest.x, dest.y - 1)
                
                             if self.secondarySearch(newDest, goal) == True:
                                 return
                    
                         #print("Remove : " + str(self.moveList.pop(len(self.moveList)-1)))
                             up = True
                             self.removePreviousGraphicMove(newDest);
                     except:
                        pass
        
        #self.removePreviousGraphicMove(dest);
            
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


def calculateDistance(A,B):
    result = math.sqrt(((B.x - A.x)**2) + ((B.y - A.y)**2))
    return result

def parse():
	# TODO:
	# This template was intended for Python 2.
	# If using Python 3, simply change raw_input() to input()
	
	#dims = input().split(' ')
     #dims = "7 7".split(' ')
     dims = "10 10".split(' ')
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
             line = "#      #  "
        
         elif i == 1:
             line = "#0     #!#"
             
         elif i == 2:
             line = "#  ##     #"
             
         elif i == 3:
             line = "# ##  #  #"
        
         elif i == 4:
             line = "# #####   "
         elif i == 5:
             line = "#        #"
         elif i == 6:
             line = "#        #"
         elif i == 7:
             line = "#        #"
         elif i == 8:
             line = "# #      #"
         elif i == 9:
             line = "##########"
             
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
 
start = time.time()

dest = parse()
 
"""
My bot
"""
print(str(bot.x) + " " + str(bot.y))

print(str(board.maze[bot.y][bot.x]))

print(str(board.maze[bot.y - 1][bot.x]))

print("GOAL : " + str(dest.x) + ", " + str(dest.y))

myBot = PythonBot(bot.x, bot.y)

myBot.primarySearch(Point(bot.x, bot.y), dest)

#myBot.showMoves()

compute_solution(myBot.matrix)

end = time.time()
print ("Finished in " + str(end) + " - " + str(start) + " = " + str(end-start) + " sec")
