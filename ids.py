# Iterative deepening search

import datetime
import random
import sys


def move_tile(state, direction):
    # Moves the blank tile in the given direction if possible
    new_state = state[:]
    index = new_state.index(0)
    if direction == 'up' and index not in [0, 1, 2]:
        new_state[index], new_state[index -
                                    3] = new_state[index - 3], new_state[index]
    elif direction == 'down' and index not in [6, 7, 8]:
        new_state[index], new_state[index +
                                    3] = new_state[index + 3], new_state[index]
    elif direction == 'left' and index not in [0, 3, 6]:
        new_state[index], new_state[index -
                                    1] = new_state[index - 1], new_state[index]
    elif direction == 'right' and index not in [2, 5, 8]:
        new_state[index], new_state[index +
                                    1] = new_state[index + 1], new_state[index]
    return new_state


def is_goal(state, goal):
    # Checks if the current state is the goal state
    return state == goal


def ids(start, goal):
    # Iterative deepening search
    def dls(current, depth):  # Depth-limited search
        if depth == 0 and is_goal(current, goal):
            return [current]
        if depth > 0:
            for direction in ['up', 'down', 'left', 'right']:
                new_state = move_tile(current, direction)
                if new_state != current:
                    next_path = dls(new_state, depth - 1)
                    if next_path:
                        return [current] + next_path
        return []

    for depth in range(1, 25):  # Adjust the range as needed
        path = dls(start, depth)
        if path:
            return path
    return None


def print_state(state):
    print("-----")
    for i in range(0, 9, 3):
        print(f"{state[i]} {state[i+1]} {state[i+2]}")
    print("-----")


start_state = []
goal_state = []

print("1.your input\n2.file\n3.random")
select = int(input("Enter number : "))

if select == 2:
    with open("input.txt", "r") as txt_file:
        input_data = [list(map(int, line.split())) for line in txt_file]
    tmp_list = []

    for i in range(0, 9):
        tmp_list.append(input_data[0][i])
    print("file input : ", tmp_list)
    start_state = tmp_list

    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    print("Your Goal : ", goal_state)
    
    print("starting timer")
    t = datetime.datetime.now()

    solution_path = ids(start_state, goal_state)

    t = datetime.datetime.now() - t
    tt = f"{t.total_seconds():.5f}"

    if start_state == goal_state:
        print("Alredy Ok")
        sys.exit(0)
    if solution_path:
        print("Solution found in {} steps:".format(len(solution_path)))
        for step in solution_path:
            print_state(step)
        print("finished in", tt, "seconds")
    else:
        print("No solution found within the depth limit.")

elif select == 1:
    user_input = input("Enter start : ")
    string_list = user_input.split()
    start_state = list(map(int, string_list))

    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    print("Your Goal : ", goal_state)

    print("starting timer")
    t = datetime.datetime.now()

    solution_path = ids(start_state, goal_state)

    t = datetime.datetime.now() - t
    tt = f"{t.total_seconds():.5f}"

    if start_state == goal_state:
        print("Alredy Ok")
        sys.exit(0)
    if solution_path:
        print("Solution found in {} steps:".format(len(solution_path)))
        for step in solution_path:
            print_state(step)
        print("finished in", tt, "seconds")
    else:
        print("No solution found within the depth limit.")

else:
    random_numbers = random.sample(range(9), 9)
    print(random_numbers)
    start_state = random_numbers
    
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    print("Your Goal : ", goal_state)
    
    print("starting timer")
    t = datetime.datetime.now()

    solution_path = ids(start_state, goal_state)

    t = datetime.datetime.now() - t
    tt = f"{t.total_seconds():.5f}"

    if start_state == goal_state:
        print("Alredy Ok")
        sys.exit(0)
    if solution_path:
        print("Solution found in {} steps:".format(len(solution_path)))
        for step in solution_path:
            print_state(step)
        print("finished in", tt, "seconds")
    else:
        print("No solution found within the depth limit.")
