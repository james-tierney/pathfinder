"""
 Example program to show using an array to back a grid on-screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
import numpy as np
from random import randint

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][5] = 1

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

neighbours = []

class Node:
    def __init__(self,weight,pos):
        self.weight = weight
        self.pos = pos

    def set_weight(self,w):
        self.weight = w

    def set_pos(self, p):
        self.pos = p

    def get_weight(self):
        return self.weight

    def get_pos(self):
        return self.pos

def get_node_by_pos(pos, list_of_nodes):
    node_1 = Node(200,(200,200))
    for x in range(len(list_of_nodes)):
        node_1 = list_of_nodes[x]
        node_pos = pos
        if node_1.get_pos() == node_pos:
            return node_1

def smallest(shortest,node):    # a function to determine if the node currently is a shorter weight than what we have right now
    #shortest = np.Infinity
    shortest_point = (0,0)
    if node.get_weight() < shortest:
        shortest = node.get_weight()
        shortest_point = node.get_pos()
        return node
    else: return False

def smallest_from_list(shortest,list_of_nodes):
    weight = 1000
    smallest_node = Node(1000, (100,100))
    for i in range(len(list_of_nodes)):
        cur_n = list_of_nodes[i]
        weight = cur_n.get_weight()
        if weight < shortest:   # then we store the current node as the shortest node
            smallest_node = cur_n
    return smallest_node



max_val = 10

def add_neighbours(grid):
    if x < max_val-1:
        neighbours.append(grid[x+1][y])
    if x > 0:
        neighbours.append(grid[x-1][y])
    if y < max_val-1:
        neighbours.append(grid[x][y+1])
    if y > 0:
        neighbours.append(grid[x][y-1])

def neighbours_for_point():
    for i in range(max_val):
        for j in range(max_val):
            grid[i][j].add_neighbours(grid)


def shortest_path(start, dest): # take in start point in the for (x,y) and end point also in the form (x,y)
    """for example and testing purposes we will start at (0,0) and dest will be (1,2)"""
    # we will also keep track of number of moves left or right and up or down it takes
    max_val = 10
    visited = np.zeros((max_val, max_val), dtype=bool)
    current_shortest = 10000
    grid = np.random.randint(1, 20, size=(10, 10))
    start = grid[0][0]
    dest = grid[1][2]
    dest_for_final = (1,2)  # the one above is the value at the grid for pos (1,2) not the actual position (1,2)
    visited[0][0] = 1
    visited[1][2] = 1
    dist_travelled = 0
    list_of_vals = []           # will be the list of values throughout our path
    weights_and_points = {}      # will store the weights and points in a dictionary format
    x,y = 0,0 #np.int(0),np.int(0)
    finished = False
    distmap = np.ones((max_val, max_val), dtype=int) * np.Infinity
    distmap[0, 0] = 0
    current_distance = 0 #np.Infinity
    print("dist map = " + str(distmap))
    x_start = 0
    y_start = 0
    # x & y will = cordinates of starting point but for simplicity rn lets make them 0 & 0
    #x,y = 1,1
    first_time_round = True
    smallest_val = 0
    key_list = []
    done = 0
    list_of_nodes = []
    shortest_path = np.Infinity
    shortest_point = (0,0)
    smallest_node = Node(np.Infinity, (100,100))
    counter = 0
    small_weight_toaddon = 0
    list_of_nodes_withaddon = []
    vals = [] # just a list for all the values of the visisted parts of the grid to be stored
    while not finished:
        #if smallest_node.getpos() != dest then we need to set the smallest to a big value again and add every point around the smallests weight + 2 to the list of weights
        #if smallest_node.get_pos() != dest:
        print("SMALLEST NODES POS ======= " + str(smallest_node.get_pos()))
        if counter > 0:
            node_to_remove = smallest_node.get_pos()
            new_node_remove = get_node_by_pos(node_to_remove, list_of_nodes)
            print("weight of node removed %d " % new_node_remove.get_weight())
            for i in range(len(list_of_nodes)):
                print("list of node WEIGHT before ==== %d" % list_of_nodes[i].get_weight())
            list_of_nodes.remove(new_node_remove)
            for i in range(len(list_of_nodes)):
                print("list of node WEIGHT after #### %d" % list_of_nodes[i].get_weight())
            for i in range(len(list_of_vals)):
                print("list of the nodes throughout =-> %d" % list_of_vals[i])
            for i in range(len(list_of_nodes_withaddon)):
                print("node after add on %d" % list_of_nodes_withaddon[i])
            new_smallest_node = smallest_from_list(100,list_of_nodes)        #keep something like 100 because we want smallest from the whole list everytime??
            print("new smallest nodes weight = %d" % new_smallest_node.get_weight())
            # some of the smaller values are missing from the lists now making it hard for me to see what is going on i should keep a list
            # with all the values for the poins we visit from the grid
        if len(list_of_vals) != 0:

            small_weight_toaddon = smallest_node.get_weight()
            print("smallest weight TO ADD ON === %d" % small_weight_toaddon)
            smallest_node.weight = 100
            shortest_path = 200

#find the smallest value and his pos and remove the node from the list of vals with that pos
            ###KEEP ITS WEIGHT TO ADD BUT REMOVE IT AND JUST KEEP THE POINTS AROUND IT PLUS ITS WEIGHT IN THE LIST
            ###WE SHOULD TRY REMOVING THE SMALLEST NODE AFTER WE USE IT SO FIND THE NODE BY ITS POS AND REMOVE IT FROM OUR LIST AND ITS WEIGHT TOO
            
            first_time_round = False
            done = 1
            x = smallest_node.get_pos()[0]
            y = smallest_node.get_pos()[1]
            print("SMALLEST RN %d" % shortest_path )
            print("smallest pos = " + str(smallest_node.get_pos()))


        if x < max_val-1:
            if visited[x+1][y] != True:
            #if grid[x+1][y] is not visited[x+1][y]:
                node = Node(grid[x+1][y],(x+1,y))
                print("NODE GET WEIGHT OF %d " % node.get_weight())
                list_of_nodes.append(node)
                vals.append(node)

                list_of_vals.append(grid[x+1][y])
                list_of_nodes_withaddon.append(grid[x + 1][y] + small_weight_toaddon)
                visited[x+1][y] = 1
                new_weights_and_points = {(x+1,y) : grid[x+1][y]}
                weights_and_points.update(new_weights_and_points)   # updates the dictionary with the new point and weight

                if smallest(shortest_path,node) != False:
                    smallest_node = smallest(shortest_path,node)
                    shortest_path = smallest_node.get_weight()
                    node_to_remove = smallest_node.get_pos()
                    print("current smallest weight = %d " % smallest_node.get_weight())

        if y < max_val-1:
            if visited[x][y+1] != True:
            #if grid[x][y+1] is not visited[x][y+1]:
                node = Node(grid[x][y+1], (x,y+1))
                list_of_nodes.append(node)
                vals.append(node)
                list_of_vals.append(grid[x][y+1])
                list_of_nodes_withaddon.append(grid[x][y + 1] + small_weight_toaddon)
                visited[x][y+1] = 1
                new_weights_and_points = {(x,y+1) : grid[x][y+1]}
                weights_and_points.update(new_weights_and_points)
                if smallest(shortest_path,node) != False:
                    smallest_node = smallest(shortest_path,node)
                    shortest_path = smallest_node.get_weight()
                    print("current smallest weight = %d " % smallest_node.get_weight())

        if x > 0:
            if visited[x-1][y] != True:
            #if grid[x-1][y] is not visited[x-1][y]:
                node = Node(grid[x-1][y], (x-1,y))
                list_of_nodes.append(node)
                vals.append(node)
                list_of_vals.append(grid[x-1][y])
                list_of_nodes_withaddon.append(grid[x - 1][y] + small_weight_toaddon)
                visited[x-1][y] = 1
                new_weights_and_points = {(x-1,y) : grid[x-1][y]}
                weights_and_points.update(new_weights_and_points)
                if smallest(shortest_path,node) != False:
                    smallest_node = smallest(shortest_path,node)
                    shortest_path = smallest_node.get_weight()
                    print("current smallest weight = %d " % smallest_node.get_weight())

                #ok so we could do some finding max were we add each nodes weight to the list and then we check if it is shortest and if it is
                #then we store the nodes position as shortest node and every time we add we do this so we can keep the shortest point
                #we could also add the points to a list in order shortest point to biggest and then just use indexing after sorting them in ascending
                #order based on weights
                #anther thing we could loop through our list of objects and get their weights and positions have them in parallel arrays??
                #like how we have printed out the weight and pos we can store shortest weight and point and compare it each time after we explore a new node
                #and if the weight is shorter than the existing one then we can update the shortespoint to that currentnode.get_pos()

                #now after finding the weight of shortest node when it goes to repeat itself we should get the current_shortest node value
                #and append that value + up's weight + down weight etc..
        if y > 0:
            #if grid[x][y-1] is not visited[x][y-1]:
            if visited[x][y - 1] != True:
                node = Node(grid[x][y-1], (x,y-1))
                list_of_nodes.append(node)
                vals.append(node)
                list_of_vals.append(grid[x][y-1])    #if not visted add it add that part in???? dont want same value being added a multitude of times
                list_of_nodes_withaddon.append(grid[x] [y - 1] + small_weight_toaddon)
                visited[x][y-1] = 1
                new_weights_and_points = {(x,y-1) : grid[x][y-1]}
                weights_and_points.update(new_weights_and_points)
                if smallest(shortest_path,node) != False:
                    smallest_node = smallest(shortest_path,node)
                    shortest_path = smallest_node.get_weight()
                    print("current smallest weight = %d " % smallest_node.get_weight())
                #counter += 1
                '''if counter == 2:
                    print("ALL WEIGHTS")
                    for i in range(len(list_of_nodes)):
                        node_w = list_of_nodes[i]
                        print("w %d" % (node_w.get_weight()))
                        #print("w %d" % (node_w))
                    print("FINAL SMALLEST WEIGHT ==== %d " % smallest_node.get_weight())
                    #print("FINAL SMALLEST WEIGHT.P2 ==== %d " % small_weight_toaddon)
                    print("node weights with addon")
                    for i in range(len(list_of_nodes_withaddon)):
                        node_we = list_of_nodes_withaddon[i]
                        print(str("after add on %d " % (node_we)))
                        #node.weight = list_of_nodes_withaddon[i]
                        #print(str(node.get_weight()))
                    for i in range(len(vals)):
                        node_cur = vals[i]
                        print("each val visisted of grid %d" % node_cur.get_weight())
                    for i in range(len(vals)):
                        print("VALS = %d" % vals[i].get_weight())
                    break'''
                if smallest_node.get_pos()[0] == dest_for_final[0] & smallest_node.get_pos()[1] == dest_for_final[1]:
                    print("point found")
                    break
                #OK ADD IN PART TO PRINT OUT THE SMALLEST NODES POS AFTER EACH ITERARION WE SEEM TO BE IN AN ITERNAL LOOP SOMEHTING GOING WRONG???
            counter += 1
#break
#print("vals after moving right, up, left, down %d, %d, %d, %d" % (list_of_vals[0], list_of_vals[1], list_of_vals[2], list_of_vals[3]))
#print("weights and points = " + str(weights_and_points))
"""if done == 1:
break"""

# so we take the first smallest value from all around the starting point we get that val
# then once we are at that val we want all the values around it again
# we can get the dict value and the point and add that value to the new points and then append the new values to the list
# this should be done for every step after the first step
# then we keep checking around the smallest value in the list until one of the values around it is the destination
#  if x > 0:
# = current_shortest

#what if we make a node object which stores a weight and a (x,y) point with the node object being the grid indexes
#if we create a list of nodes and then choose the nodes points  with the min weight from the list
def test():
    l = [4,56,7,2,3,1]
    l1 = [4, 56, 7, 2, 3, 44]
    l2 = [4, 56, 7, 2, 3, 0]
    np.unravel_index([5, 10, 15], (7, 6))
    #(array([3, 6, 6]), array([4, 5, 1]))
    dismaptemp = grid
    minpost = np.unravel_index(np.argmin(dismaptemp), np.shape(dismaptemp))
    print("Min post = " + str(minpost))
    print(np.unravel_index(np.argmin([min(l),min(l1),min(l2)]), np.shape(grid)))
    #print(np.unravel_index(np.argmin([(2,1),(1,1),(4,5)]), np.shape(grid)))
    print(np.unravel_index([1,1], (10, 10)))

test()
shortest_path(0,0)

"""so we need to get the values surrounding the current point on the grid we are at so up down left right"""
""" we then need to add the weights of these points and there (x,y) value into a dictionary"""
"""then we need to add all the weights to a list find the smallest go to that (x,y) val """
"""and repeat this process until we reach our destination"""
# we want to set grid[x,y] = to the val from the dict of the shortest weight each time then get the surrouding weights of that current position

"""        if x < max_val-1:
            if start + grid[x+1,y] < distmap[x+1,y] and not visited[x+1,y]:
                visited[x+1,y] = 1  #true
                current_distance = start + grid[x+1,y]
                if current_distance < current_shortest:
                    current_shortest = current_distance     
        
if x > 0:
"""

"""if x < max_val-1:
    if grid[x+1,y] + dist_travelled < distmap[x+1,y] and not visited[x+1,y]:
    #if start + grid[x+1,y] + dist_travelled < distmap[x+1,y] and not visited[x+1,y]: # will not work every time start value only needs to be considered once fix that
        visited[x+1,y] = 1  #true
        current_distance += grid[x+1,y] + dist_travelled
        if current_distance < current_shortest:
            current_shortest = current_distance     # need to do what we have done for moving right for moving up down and left aswell
            dist_travelled = current_shortest
            # dist_travelled will be 0 upon first time then updated as we go along
if x > 0:
    if grid[x-1,y] + dist_travelled < distmap[x-1,y] and not visited[x-1,y]:
    #if start + grid[x-1,y] + dist_travelled < distmap[x-1,y] and not visited[x-1,y]:
        visisted[x-1,y] = 1
        current_distance += grid[x-1,y] + dist_travelled
        if current_distance < current_shortest:
            current_shortest = current_distance
            dist_travelled = current_shortest"""