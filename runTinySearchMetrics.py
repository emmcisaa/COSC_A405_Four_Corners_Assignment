from fourCornerProblem import Problem, bfs, ucs, AStar
from problemGraphics import pacmanGraphic
import time

def collect_metrics(search_algorithm, problem):
    start_time = time.time()

    # Run the specified search algorithm and collect metrics
    if search_algorithm == "BFS":
        plan, nodes_explored = bfs(problem)
    elif search_algorithm == "UCS":
        cost, plan, nodes_explored = ucs(problem)
    elif search_algorithm == "A*":
        cost, plan, nodes_explored = AStar(problem)
    else:
        raise ValueError("Unsupported search algorithm.")

    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    plan_length = len(plan)

    return nodes_explored, execution_time, plan_length, plan

def run_part_2():
    filename = 'tinySearch.txt'
    problem = Problem(filename)
    pacman_graphic = pacmanGraphic()

    # Collect metrics for BFS
    bfs_nodes, bfs_time, bfs_length, bfs_plan = collect_metrics("BFS", problem)
    print("BFS Results:")
    print(f"  Nodes Explored: {bfs_nodes}")
    print(f"  Execution Time: {bfs_time} ms")
    print(f"  Plan Length: {bfs_length}")

    # Collect metrics for UCS
    ucs_nodes, ucs_time, ucs_length, ucs_plan = collect_metrics("UCS", problem)
    print("\nUCS Results:")
    print(f"  Nodes Explored: {ucs_nodes}")
    print(f"  Execution Time: {ucs_time} ms")
    print(f"  Plan Length: {ucs_length}")

    # Collect metrics for A*
    a_star_nodes, a_star_time, a_star_length, a_star_plan = collect_metrics("A*", problem)
    print("\nA* Results:")
    print(f"  Nodes Explored: {a_star_nodes}")
    print(f"  Execution Time: {a_star_time} ms")
    print(f"  Plan Length: {a_star_length}")

    # Display the maze and run the A* plan in graphics
    pacman_graphic.setup(problem)
    pacman_graphic.runPlan(problem, a_star_plan)

# Run Part 2
run_part_2()
