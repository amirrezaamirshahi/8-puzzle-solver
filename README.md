# 8-Puzzle Solver

This project provides implementations of three different algorithms to solve the classic **8-puzzle problem**.  
The main goal is to compare the performance of various search strategies in solving a well-known AI problem.

---

## ✨ Implemented Algorithms
1. **A\*** (`Astar.py`)  
   - Uses **Manhattan Distance** heuristic  
   - Guarantees finding the optimal solution  
   - Efficient in most cases  

2. **IDA\*** (`ida.py`)  
   - Combines Iterative Deepening with heuristic search  
   - Uses much less memory compared to A\*  
   - Sometimes slower than A\*  

3. **IDS** (`ids.py`)  
   - Iterative Deepening Search without heuristics  
   - Very low memory usage  
   - Can be slow for complex puzzles  
   - Does not always guarantee the shortest path  

---

## 📂 Project Structure
8-puzzle-solver/
│
├── Astar.py # A* algorithm implementation
├── ida.py # IDA* algorithm implementation
├── ids.py # IDS algorithm implementation
├── input.txt # Example input
├── requirements.txt # Dependencies (numpy)
├── README.md # Project documentation
├── .gitignore # Ignored files for Git
└── LICENSE # MIT License


---

## ⚙️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/USERNAME/8-puzzle-solver.git
   cd 8-puzzle-solver

2. Install dependencies:
    pip install -r requirements.txt

3. Run algorithms:
    python Astar.py
    python ida.py
    python ids.py

📝 Input

The program accepts input in three ways:

Manual input (enter numbers in the terminal)

From file (input.txt)

Randomly generated board

Example input.txt:
    2 1 3 5 4 7 8 6 0


📊 Output

Shows the sequence of puzzle states until the goal is reached

Prints the number of moves

Displays execution time

Example Output (A*):

    file input :  [2, 1, 3, 5, 4, 7, 8, 0]
    Your Goal :  [1, 2, 3, 4, 5, 6, 7, 8, 0]
    starting timer
    -----
    2 1 3
    5 4 7
    8 6 0
    -----
    ...
    Solved in 12 moves
    finished in 0.00452 seconds


🔍 Algorithm Comparison :
    | Algorithm | Heuristic | Memory Usage | Speed  | Guarantees Optimal Solution |
    | --------- | --------- | ------------ | ------ | --------------------------- |
    | A\*       | Manhattan | High         | Fast   | ✅ Yes                       |
    | IDA\*     | Manhattan | Low          | Medium | ✅ Yes                       |
    | IDS       | None      | Very Low     | Slow   | ❌ No                        |


🛠 Requirements:
    Python 3.8+
    numpy




