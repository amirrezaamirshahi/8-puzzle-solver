import datetime
import random
import numpy as np


def ida_star(root, goal):
    def search(path, g, bound):
        node = path[-1]
        f = g + h(node)
        if f > bound:
            return f
        if np.array_equal(node, goal):
            return 'FOUND'
        min_bound = float('inf')
        for succ in successors(node):
            if succ not in path:
                path.append(succ)
                t = search(path, g + 1, bound)
                if t == 'FOUND':
                    return 'FOUND'
                if t < min_bound:
                    min_bound = t
                path.pop()
        return min_bound

    def h(puzzle):
        # Manhattan distance heuristic
        return sum(abs((val - 1) % 3 - i % 3) + abs((val - 1) // 3 - i // 3)
                   for i, val in enumerate(puzzle) if val)

    def successors(puzzle):
        # Generate the successor states
        zero = puzzle.index(0)
        succ = []
        if zero >= 3:  # Up
            succ.append(puzzle[:zero-3] + (0,) + puzzle[zero -
                        2:zero] + (puzzle[zero-3],) + puzzle[zero+1:])
        if zero < 6:  # Down
            succ.append(puzzle[:zero] + (puzzle[zero+3],) +
                        puzzle[zero+1:zero+3] + (0,) + puzzle[zero+4:])
        if zero % 3:  # Left
            succ.append(puzzle[:zero-1] +
                        (0, puzzle[zero-1]) + puzzle[zero+1:])
        if zero % 3 != 2:  # Right
            succ.append(puzzle[:zero] + (puzzle[zero+1], 0) + puzzle[zero+2:])
        return succ

    bound = h(root)
    path = [root]
    while True:
        t = search(path, 0, bound)
        if t == 'FOUND':
            return path
        if t == float('inf'):
            return []
        bound = t


def print_state(state):
    print("-----")
    for i in range(0, 9, 3):
        print(f"{state[i]} {state[i+1]} {state[i+2]}")
    print("-----")


print("1.your input\n2.file\n3.random")
select = int(input("Enter number : "))
root = ()
goal = ()

if select == 2:
    with open("input.txt", "r") as txt_file:
        input_data = [tuple(map(int, line.split())) for line in txt_file]

    tmp_tuple = ()
    tmp_tuple = tmp_tuple + (input_data[0][0], input_data[0][1], input_data[0][2], input_data[0][3],
                             input_data[0][4], input_data[0][5], input_data[0][6], input_data[0][7], input_data[0][8])
    print("file input : ", tmp_tuple)

    root = tmp_tuple

    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    print("Your Goal : ",goal)

    print("starting timer")
    t = datetime.datetime.now()

    solution_path = ida_star(root, goal)

    t = datetime.datetime.now() - t
    tt = f"{t.total_seconds():.5f}"

    if solution_path:
        print("Solution found : ")
        for item in solution_path:
            print_state(item)
        print("Solved in {} moves".format(len(solution_path)))
        print("finished in", tt, "seconds")

    else:
        print("No solution found.")

elif select == 1:
    user_input = input("Enter root : ")
    string_elements = user_input.split()
    root = tuple(map(int, string_elements))

    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    print("Your Goal : ",goal)

    print("starting timer")
    t = datetime.datetime.now()

    solution_path = ida_star(root, goal)
    t = datetime.datetime.now() - t
    tt = f"{t.total_seconds():.5f}"

    if solution_path:
        print("Solution found : ")
        for item in solution_path:
            print_state(item)
        print("Solved in {} moves".format(len(solution_path)))
        print("finished in", tt, "seconds")
    else:
        print("No solution found.")

else:
    random_numbers = random.sample(range(9), 9)
    root = tuple(map(int, random_numbers))
    print(root)

    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    print("Your Goal : ",goal)
    
    print("starting timer")
    t = datetime.datetime.now()

    solution_path = ida_star(root, goal)
    t = datetime.datetime.now() - t
    tt = f"{t.total_seconds():.5f}"

    if solution_path:
        print("Solution found : ")
        for item in solution_path:
            print_state(item)
        print("Solved in {} moves".format(len(solution_path)))
        print("finished in", tt, "seconds")
    else:
        print("No solution found.")
