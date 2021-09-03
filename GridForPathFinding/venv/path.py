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


class Node:
    def __init__(self, weight, pos):
        self.weight = weight
        self.pos = pos

    def set_weight(self, w):
        self.weight = w

    def set_pos(self, p):
        self.pos = p

    def get_weight(self):
        return self.weight

    def get_pos(self):
        return self.pos


neighbours = []


"""class Node:
    def __init__(self, weight, pos):
        self.weight = weight
        self.pos = pos

    def set_weight(self, w):
        self.weight = w

    def set_pos(self, p):
        self.pos = p

    def get_weight(self):
        return self.weight

    def get_pos(self):
        return self.pos
"""
"""def get_node_by_pos(pos, list_of_nodes):
    node_1 = Node(200, (200, 200))
    for x in range(len(list_of_nodes)):
        node_1 = list_of_nodes[x]
        node_pos = pos
        if node_1.get_pos() == node_pos:
            return node_1"""


def smallest(shortest,
             node):  # a function to determine if the node currently is a shorter weight than what we have right now
    # shortest = np.Infinity
    shortest_point = (0, 0)
    if node.get_weight() < shortest:
        shortest = node.get_weight()
        shortest_point = node.get_pos()
        return node
    else:
        return False


"""def smallest_from_list(shortest, list_of_nodes):
    weight = 1000
    smallest_node = Node(1000, (100, 100))
    for i in range(len(list_of_nodes)):
        cur_n = list_of_nodes[i]
        weight = cur_n.get_weight()
        if weight < shortest:  # then we store the current node as the shortest node
            smallest_node = cur_n
    return smallest_node
"""

def smallest_in_list(shortest, list_of_nodes):
    smallest_node = Node(200,(200,200))
    node_one = Node(101,(101,101))
    for i in range(len(list_of_nodes)):
        node_one = list_of_nodes[i]
        if node_one.get_weight() < shortest:
            shortest = node_one.get_weight()
            smallest_node = node_one
    return smallest_node

"""def get_node_by_pos(pos,list_of_nodes_withaddon):  # we will use this to find the specific node e.g. the smallest and remove it from our list
    removable = Node(200, (300,300))
    node_pos = pos
    for x in range(len(list_of_nodes_withaddon)):
        removable = list_of_nodes_withaddon[x]
        #pos_of_node = list_of_nodes_withaddon[x]
        if removable.get_pos() == node_pos:
            return removable"""
def get_node_by_pos(pos, list_of_nodes):
    node_one = Node(101,(101,101))
    for x in range(len(list_of_nodes)):
        node_one = list_of_nodes[x]
        print("pos = " + str(list_of_nodes[x].get_pos()))
        node_pos = pos
        if node_one.get_pos() == node_pos:      # ok so reason we cant call this with list_of_nodes_withaddon is that list is just weights
                                                # would be a good idea to create one with updated nodes and weights and their pos
            return node_one

def create_list_withaddons(addon,list_of_nodes):
    cur_node = Node(0, (20,20))
    nodes_withaddon = []
    pos_for_node = (20,20)
    for i in range(len(list_of_nodes)):
        cur_w = list_of_nodes[i].get_weight()
        new_w = cur_w + addon
        pos_for_node = list_of_nodes[i].get_pos()
        new_node = Node(new_w,pos_for_node)
        nodes_withaddon.append(new_node)
    return nodes_withaddon

def result(distance):
    print("Path was found with a distance of %d" % distance) # could maybe update this function to say path from (start pos) to (dest pos) was found with distance of..

# want to almost create the list of nodes with add on then after each iteration but set the weights by finding the node by pos and setting its weight = to addon value weight

def shortest_path(start_pos, dest_for_final):  # take in start point in the for (x,y) and end point also in the form (x,y)
    """for example and testing purposes we will start at (0,0) and dest will be (1,2)"""
    # we will also keep track of number of moves left or right and up or down it takes
    """lets make a grid for testing with 4x4 [1,4,5,7]
                                             [1,3,6,8]      
                                             [1,2,4,1]
                                             [1,1,1,1]"""
    max_val = 10
    visited = np.zeros((max_val, max_val), dtype=bool)
    current_shortest = 10000
    #grid = [[1,1,1,1], [4,3,2,1], [5,6,4,1], [7,8,1,1]]
    grid = np.random.randint(1, 20, size=(max_val, max_val))
    visited = np.zeros((max_val, max_val), dtype=bool)
    #visited = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    """grid[0][0] = 1
    grid[1][0] = 4
    grid[2][0] = 5
    grid[3][0] = 7
    grid[0][1] = 1
    grid[1][1] = 3
    grid[2][1] = 6
    grid[3][1] = 8
    grid[0][2] = 2
    grid[1][2] = 2
    grid[2][2] = 4
    grid[3][2] = 1
    grid[0][3] = 1
    grid[1][3] = 1
    grid[2][3] = 1
    grid[3][3] = 1
"""
    #grid = np.random.randint(1, 20, size=(4, 4))
    start = grid[0][0]
    dest = grid[1][2]
    #start_pos = (0,0)
    #dest_for_final = (3  , 0 )  # the one above is the value at the grid for pos (1,2) not the actual position (1,2)
    visited[0][0] = 0
    visited[2][3] = 0
    dist_travelled = 0
    list_of_vals = []  # will be the list of values throughout our path
    weights_and_points = {}  # will store the weights and points in a dictionary format
    x, y = 0, 0  # np.int(0),np.int(0)
    finished = False
    distmap = np.ones((max_val, max_val), dtype=int) * np.Infinity
    distmap[0, 0] = 0
    current_distance = 0  # np.Infinity
    print("dist map = " + str(distmap))
    print("grid =  " + str(grid))
    print("grid val @  " + str(grid[3][1]))
    print("grid val @  " + str(grid[1][0]))
    print("grid val @  " + str(grid[1][2]))
    print("grid val @  " + str(grid[3][2]))
    print("Start pos = " + str(x) + "," + str(y))
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
    shortest_point = (0, 0)
    smallest_node = Node(np.Infinity, (100, 100))
    counter = 0
    small_weight_toaddon = 0
    list_of_nodes_withaddon = []
    vals = []  # just a list for all the values of the visisted parts of the grid to be stored
    shortest = 200
    remove_node = Node(np.Infinity,(100,100))
    nodes_with_addons = []
    path_size = 0
    sh_to_node = 0

    for i in range(10):
        for j in range(10):
            print("%d" % grid[i][j])

    while not finished:

        # remember shortest should be set to a high value after each iteration so that after we remove the smallest val after adding on to the nodes around it
        # we can then keep fining the next values and repeating the process
        #final_shortest = smallest_node.get_weight()
        ''''the small vals to add on after each loop i should keep running total for them till we reach dest
        as that will be the total path travelled i hope :D'''
        shortest = 200
        if counter == 0:
            visited[0][0] = 1 # this should only be here for the starting point so we should set the starting point to visited upon startup of the program
        if counter > 0:
            smallest_node = smallest_in_list(shortest,nodes_with_addons)
            #smallest_node = smallest_in_list(shortest,list_of_nodes)
            small_weight_toaddon = smallest_node.get_weight()
            path_size += small_weight_toaddon
            print("small val to add on = %d" % small_weight_toaddon)
            x = smallest_node.get_pos()[0]
            y = smallest_node.get_pos()[1]
            print("new starting pos = " + str(smallest_node.get_pos()))
            #nodes_with_addons = create_list_withaddons(small_weight_toaddon,list_of_nodes)# this just keeps recreating the same list with smallest after it has been removed
            for i in range(len(nodes_with_addons)):
                print("w = %d" % nodes_with_addons[i].get_weight())
            remove_node = get_node_by_pos(smallest_node.get_pos(),nodes_with_addons)
            print("weight being removed is -> " + str(remove_node.get_pos()))
            print("weight being removed is -> %d" % remove_node.get_weight())
            nodes_with_addons.remove(remove_node)
            #list_of_nodes.remove(remove_node)
            for i in range(len(nodes_with_addons)):
                print("w after removal = %d" % nodes_with_addons[i].get_weight())
            for i in range(len(list_of_nodes)):
                print("normal weights without addons = %d" % list_of_nodes[i].get_weight())
            """for i in range(len(list_of_nodes_withaddon)):
                print("w = %d" % list_of_nodes_withaddon[i])
            remove_node = get_node_by_pos(smallest_node.get_pos(),list_of_nodes) # remove smallest node from add on list
            for i in range(len(list_of_nodes_withaddon)):
                print("w after remove = %d" % list_of_nodes_withaddon[i])"""

            # we also need to remove the smallest node from the list each iteration
        """first_time_round = False
        done = 1
        x = smallest_node.get_pos()[0]
        y = smallest_node.get_pos()[1]
        print("SMALLEST RN %d" % shortest_path)
        print("smallest pos = " + str(smallest_node.get_pos()))"""

        if x <= max_val - 1:
            if visited[x + 1][y] != True:
                node_right = Node(grid[x+1][y],(x+1,y))
                print("x = " + str(x))
                print("node RIGHT POS = " + str(node_right.get_pos()[0]) + ","  + str(node_right.get_pos()[1]))
                print("dest for final[0] = " + str(dest_for_final[0]) + " dest for final[1] = " + str(dest_for_final[1]))
                if (node_right.get_pos()[0] == dest_for_final[0]) & (node_right.get_pos()[1] == dest_for_final[1]):
                    sh_to_node = small_weight_toaddon+node_right.get_weight()
                    result(sh_to_node)
                    break
                    #print("sh at right = " + str(sh_to_node))
                node_right_addon = Node(grid[x+1][y]+small_weight_toaddon,(x+1,y))
                list_of_nodes.append(node_right)    # just to keep a total list of all the nodes we pass through
                list_of_nodes_withaddon.append(node_right.get_weight()+small_weight_toaddon) # keep a list of all the weights with the add_on from the distance travelled so far
                visited[x+1][y] = 1
                nodes_with_addons.append(node_right_addon)
                print("len of list = after righy move %d" % len(list_of_nodes))
                print("val after move RIGHT = %d" % grid[x+1][y])

                """if smallest(shortest_path, node) != False:
                    smallest_node = smallest(shortest_path, node)
                    shortest_path = smallest_node.get_weight()
                    node_to_remove = smallest_node.get_pos()
                    print("current smallest weight = %d " % smallest_node.get_weight())"""

        if y <= max_val - 1:
            if visited[x][y+1] != True:
                node_up = Node(grid[x][y+1], (x,y+1))
                if (node_up.get_pos()[0] == dest_for_final[0]) & (node_up.get_pos()[1] == dest_for_final[1]):
                    sh_to_node = small_weight_toaddon+node_up.get_weight()
                    result(sh_to_node)
                    break
                    #print("sh at up = " + str(sh_to_node))
                node_up_addon = Node(grid[x][y+1]+small_weight_toaddon,(x,y+1))
                list_of_nodes.append(node_up)
                list_of_nodes_withaddon.append(node_up.get_weight()+small_weight_toaddon)
                visited[x][y+1] = 1
                nodes_with_addons.append(node_up_addon)
                print("len of list = after up move %d" % len(list_of_nodes))
                print("val after move UP = %d" % grid[x][y+1])
                """if smallest(shortest_path, node) != False:
                    smallest_node = smallest(shortest_path, node)
                    shortest_path = smallest_node.get_weight()
                    node_to_remove = smallest_node.get_pos()
                    print("current smallest weight = %d " % smallest_node.get_weight())"""

        if x > 0:
            if visited[x - 1][y] != True:
                node_left = Node(grid[x-1][y], (x-1,y))
                if (node_left.get_pos()[0] == dest_for_final[0]) & (node_left.get_pos()[1] == dest_for_final[1]):
                    sh_to_node = small_weight_toaddon+node_left.get_weight()
                    result(sh_to_node)
                    break
                    #print("sh at left = " + str(sh_to_node))
                node_left_addon = Node(grid[x-1][y]+small_weight_toaddon, (x-1,y))
                list_of_nodes.append(node_left)
                list_of_nodes_withaddon.append(node_left.get_weight()+small_weight_toaddon)
                visited[x-1][y] = 1
                nodes_with_addons.append(node_left_addon)
                print("len of list = after left move %d" % len(list_of_nodes))
                print("val after move LEFT = %d" % grid[x-1][y])

                """if smallest(shortest_path, node) != False:
                    smallest_node = smallest(shortest_path, node)
                    shortest_path = smallest_node.get_weight()
                    node_to_remove = smallest_node.get_pos()
                    print("current smallest weight = %d " % smallest_node.get_weight())"""


        if y > 0:
            if visited[x][y - 1] != True:
                node_down = Node(grid[x][y-1], (x,y-1))
                if (node_down.get_pos()[0] == dest_for_final[0]) & (node_down.get_pos()[1] == dest_for_final[1]):
                    sh_to_node = small_weight_toaddon+node_down.get_weight()
                    result(sh_to_node)
                    break
                    #print("sh at down = " + str(sh_to_node))
                node_down_addon = Node(grid[x][y-1]+small_weight_toaddon, (x,y-1))
                list_of_nodes.append(node_down)
                list_of_nodes_withaddon.append(node_down.get_weight()+small_weight_toaddon)
                visited[x][y-1] = 1
                nodes_with_addons.append(node_down_addon)
                print("len of list = after down move %d" % len(list_of_nodes))
                print("val after move DOWN = %d" % grid[x][y-1])

        #if smallest_node.get_pos()[0] == dest_for_final[0] & smallest_node.get_pos()[1] == dest_for_final[1]:
        #if counter == 3:
        for j in range(len(list_of_nodes)):
            print("weight of node = %d" % list_of_nodes[j].get_weight())
        print("WELL DONE!!!")
        print("shortest path to " + str(dest_for_final) + " was " + str(sh_to_node))
        #print("shortest path to " + str(dest_for_final) + " was "  + str(path_size))
        #break
        counter += 1

        """if smallest(shortest_path, node) != False:
            smallest_node = smallest(shortest_path, node)
            shortest_path = smallest_node.get_weight()
            node_to_remove = smallest_node.get_pos()
            print("current smallest weight = %d " % smallest_node.get_weight())"""

        """if smallest_node.get_pos()[0] == dest_for_final[0] & smallest_node.get_pos()[1] == dest_for_final[1]:
            print("point found")
            break"""




#shortest_path((0,0), (1,2))

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
# initial start point (red dot upon startup)
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
# create a counter to determine what user click is for the start pos
# and what user click is for the destination pos
first_click = 0
start = (20, 20)  # Node(100,(0,0))
dest = (100, 100)  # Node(100,(10,10))
while not done:
    #first_click = 0 # help to indentify first click for starting pos
    # declare start and pos outside the loop so that they dont reset each click of the grid

    #start = (0,0) -- make these two nodes instead of just a position
    #dest = (10,10)
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
            if first_click == 0:
                start = (column,row)
                print("start pos = " + str(start))
                #start[0] = column
                #start[1] = row
                 #start.get_pos()[0] = pos[0]
                #start.get_pos()[1] = pos[1]
                first_click = 1 # not first click so the next click will be our destination point
            elif first_click == 1:  # what we can do is set first_click = -1 within here to signal if start and dest have been picked then call the method
                dest = (column,row)
                print("dest pos = " + str(dest))
                first_click = -1    # signalling we have choose start pos and dest pos
                if first_click == -1:  # SEEMS TO REQUIRE 2 CLICK FOR DEST BEFORE CALLING SHORTSEST_PATH FUNCTION??
                    shortest_path(start, dest)
                    print("start pos = " + str(start))
                    print("dest pos = " + str(dest))
                #print("first click val = %d " % first_click)
                #dest = pos
                #dest.get_pos()[0] = pos[0]
                #dest.get_pos()[1] = pos[1]

            """elif first_click == -1: #SEEMS TO REQUIRE 2 CLICK FOR DEST BEFORE CALLING SHORTSEST_PATH FUNCTION??
                shortest_path(start,dest)
                print("start pos = " + str(start))
                print("dest pos = " + str(dest))"""

            #print("start pos = " + str(start))
            #print("dest pos = " + str(dest))
    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            num = grid[row][column]
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

