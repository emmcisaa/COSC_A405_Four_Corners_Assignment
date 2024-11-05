from fourCornerProblem import Problem
from problemGraphics import pacmanGraphic
import time

def run_medium_corners_search(search_algorithm):
    # Initialize the problem instance from mediumCorners.txt
    filename = 'mediumCorners.txt'
    problem = Problem('mediumCorners.txt')
    
    # Initialize Pacman graphics
    pacman_graphic = pacmanGraphic()

    # Select and execute the search algorithm
    start_time = time.time()
    if search_algorithm == "BFS":
        plan = bfs(problem)
        plan_length = len(plan)
    elif search_algorithm == "UCS":
        cost, plan = ucs(problem)
        plan_length = len(plan)
    elif search_algorithm == "A*":
        cost, plan = AStar(problem)
        plan_length = len(plan)
    else:
        raise ValueError("Unsupported search algorithm.")
    end_time = time.time()

    # Display plan details
    print(f"{search_algorithm} plan for mediumCorners.txt:", plan)
    print(f"{search_algorithm} plan length:", plan_length)
    print(f"{search_algorithm} Time:", (end_time - start_time) * 1000, "ms")

    # Display the maze and run the plan in graphics
    pacman_graphic.setup(problem)
    pacman_graphic.runPlan(problem, plan)

# Example usage for mediumCorners.txt with A*
run_medium_corners_search('A*')
