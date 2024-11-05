from fourCornerProblem import Problem
from tkinter import *
import time
from itertools import combinations
from problemGraphics import pacmanGraphic
import heapq
import time

def construct_path(node, visited):
    path = []
    while node:
        food = tuple(node[1])
        node, action = visited[(node[0], food)]
        if action != None:
            if type(action) == list: path = action + path
            else: path = [action] + path
    return path

def bfs(p):
    start = p.startState()
    frontier = [(start, None, None)]
    visited = {}
    count = 0
    while frontier:
        node, parent, action = frontier.pop(0)
        food = tuple(node[1])
        if (node[0], food) in visited: continue
        visited[(node[0], food)] = (parent, action)
        if p.isGoal(node):
            print ('BFS number of nodes explored: ', count)
            return construct_path(node, visited)
        count += 1
        neighbors = p.transition(node)
        for n, a, c in neighbors:
            food = tuple(n[1])
            if (n, node, a) not in frontier and (n[0], food) not in visited:
                frontier.append ((n, node, a))
    return []

def ucs(p):
    pq = [(0, p.startState(), None, None)]
    visited = {}
    count = 0
    while pq:
        gCost, node, parent, action = heapq.heappop(pq)
        food = tuple(node[1])
        if (node[0], food) in visited: continue
        visited[(node[0], food)] = (parent, action)
        if p.isGoal(node):
            print ('UCS number of nodes explored: ', count)
            return gCost, construct_path(node, visited)
        count += 1
        neighbors = p.nextStates(node)
        for stepCost, n, a in neighbors:
            food = tuple(n[1])
            newState = (stepCost + gCost, n, node, a)
            heapq.heappush(pq, newState)
    return None

def AStar(p):
    start = p.startState()  # Get the start state from the Problem
    pq = [(p.h(start), 0, start, None, None)]
    visited = {}
    count = 0
    while pq:
        fCost, gCost, node, parent, action = heapq.heappop(pq)
        food = tuple(node[1])
        if (node[0], food) in visited: continue
        visited[(node[0], food)] = (parent, action)
        if p.isGoal(node):
            print ('A* number of nodes explored: ', count)
            return gCost, construct_path(node, visited)
        count += 1
        neighbors = p.nextStates(node)  # Get the neighbors of the current node
        for step_cost, neighbor, a in neighbors:
            f = gCost + step_cost + p.h(neighbor)
            newState = (f, gCost + step_cost, neighbor, node, a)
            heapq.heappush(pq, newState)  # Insert newState into the priority queue
    return None, None

filename = 'tinyCorners.txt'

# Initialize the Problem instance
p = Problem(filename)

# -------------------------------------------------------
# BFS:
# -------------------------------------------------------

startTime = time.time()
plan = bfs(p)
endTime = time.time()
print(plan)
print('BFS plan length:', len(plan))
print('BFS Time:', (endTime - startTime) * 10**3, "ms")
print('------------------------')

pac = pacmanGraphic(1300, 700)
pac.setup(p)
pac.runPlan(p, plan)

# -------------------------------------------------------
# UCS:
# -------------------------------------------------------

p = Problem(filename)
startTime = time.time()
p.compute_distances()
cost, plan = ucs(p)
endTime = time.time()
print('UCS cost:', cost)
print(plan)
print('UCS plan length:', len(plan))
print('UCS Time:', (endTime - startTime) * 10**3, "ms")

pac = pacmanGraphic(1300, 700)
pac.setup(p)
pac.runPlan(p, plan)

# -------------------------------------------------------
# A*:
# -------------------------------------------------------

p = Problem(filename)  # Initialize a new instance of the Problem
startTime = time.time()
p.compute_distances()  # Compute distances for A*
cost, plan = AStar(p)  # Run A* search on the problem instance
endTime = time.time()
print('A* cost:', cost)
print(plan)
print('A* plan length:', len(plan))
print('A* Time:', (endTime - startTime) * 10**3, "ms")

# Execute plan using Pacman graphics
pac = pacmanGraphic(1300, 700)
pac.setup(p)
pac.runPlan(p, plan)