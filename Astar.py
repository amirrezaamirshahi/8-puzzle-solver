import datetime
import heapq
import random


class PuzzleState:
    def __init__(self, board, goal, moves=0, prev=None):
        self.board = board
        self.goal = goal
        self.moves = moves
        self.prev = prev
        self.priority = self.moves + self.manhattan()

    def __lt__(self, other):
        return self.priority < other.priority

    def manhattan(self):
        distance = 0
        for i in range(len(self.board)):
            if self.board[i] != 0:
                x, y = divmod(self.board[i] - 1, 3)  # goal
                current_x, current_y = divmod(i, 3)
                distance += abs(x - current_x) + abs(y - current_y)
        print("distance is : ", distance)
        return distance

    def is_goal(self):
        return self.board == self.goal

    def moves_available(self):
        zero_index = self.board.index(0)
        x, y = divmod(zero_index, 3)
        moves = []
        if x > 0:
            moves.append(-3)     # Up
        if x < 2:
            moves.append(3)      # Down
        if y > 0:
            moves.append(-1)     # Left
        if y < 2:
            moves.append(1)      # Right
        return moves

    def swap(self, zero, move):
        new_board = self.board[:]
        new_zero_index = zero + move
        new_board[zero], new_board[new_zero_index] = new_board[new_zero_index], new_board[zero]
        return new_board


def a_star(start, goal):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, PuzzleState(start, goal))

    while open_list:
        current = heapq.heappop(open_list)
        if current.is_goal():
            return current
        closed_set.add(tuple(current.board))
        zero = current.board.index(0)

        for move in current.moves_available():
            new_board = current.swap(zero, move)
            if tuple(new_board) not in closed_set:
                heapq.heappush(open_list, PuzzleState(
                    new_board, goal, current.moves + 1, current))

    return None  # No solution found


def print_state(state):
    print("-----")
    for i in range(0, 9, 3):
        print(f"{state[i]} {state[i+1]} {state[i+2]}")
    print("-----")


start_board = []
goal_board = []

print("1.your input\n2.file\n3.random")
select = int(input("Enter number : "))

if select == 2:
    with open("input.txt", "r") as txt_file:
        input_data = [list(map(int, line.split())) for line in txt_file]

    tmp_list = []
    for i in range(0, 9):
        tmp_list.append(input_data[0][i])
    print("file input : ", tmp_list)
    start_board = tmp_list

    goal_board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    print("Your Goal : ", goal_board)

    print("starting timer")
    t = datetime.datetime.now()

    solution = a_star(goal_board, start_board)

    t = datetime.datetime.now() - t
    tt = f"{t.total_seconds():.5f}"

    if solution:
        moves = []
        while solution.prev:
            moves.append(solution.board)
            solution = solution.prev
        moves.reverse()
        for move in moves:
            print_state(move)
        print("Solved in {} moves".format(len(moves)))
        print("finished in", tt, "seconds")
    else:
        print("No solution exists.")

elif select == 1:
    user_input = input("Enter start : ")
    string_list = user_input.split()
    start_board = list(map(int, string_list))

    goal_board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    print("Your Goal : ", goal_board)

    print("starting timer")
    t = datetime.datetime.now()

    solution = a_star(goal_board, start_board)

    t = datetime.datetime.now() - t
    tt = f"{t.total_seconds():.5f}"

    if solution:
        moves = []
        while solution.prev:
            moves.append(solution.board)
            solution = solution.prev
        moves.reverse()
        for move in moves:
            print_state(move)
        print("Solved in {} moves".format(len(moves)))
        print("finished in", tt, "seconds")
    else:
        print("No solution exists.")

else:
    random_numbers = random.sample(range(9), 9)
    print(random_numbers)
    start_board = random_numbers
    goal_board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    print("Your Goal : ", goal_board)

    print("starting timer")
    t = datetime.datetime.now()

    solution = a_star(goal_board, start_board)

    t = datetime.datetime.now() - t
    tt = f"{t.total_seconds():.5f}"

    if solution:
        moves = []
        while solution.prev:
            moves.append(solution.board)
            solution = solution.prev
        moves.reverse()
        for move in moves:
            print_state(move)
        print("Solved in {} moves".format(len(moves)))
        print("finished in", tt, "seconds")
    else:
        print("No solution exists.")
