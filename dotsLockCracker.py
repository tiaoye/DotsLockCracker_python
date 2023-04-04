import argparse


def main(original, goal):
    step = 999
    N = 8
    L2 = "L2"
    R2 = "R2"
    X = "X"
    # memo maps a pattern to the minimum number of steps to reach it 
    memo = {}
    # parent maps a pattern to the pattern and operation that leads to it
    parent = {}
    def dfs(current_pattern, previous_pattern, operation, current_step):
        nonlocal step
        # prune 1
        if (current_step > step):
            return
        # prune 2
        if current_pattern in memo and current_step > memo[current_pattern]:
            return
        else:
            memo[current_pattern] = current_step
            parent[current_pattern] = (previous_pattern, operation)
        # prune 3
        if current_pattern == goal:
            step = current_step
            return
        # left 2
        new_pattern = current_pattern[2:] + current_pattern[:2]
        dfs(new_pattern, current_pattern, L2, current_step + 1)
        # right 2
        new_pattern = current_pattern[-2:] + current_pattern[:-2]
        dfs(new_pattern, current_pattern, R2, current_step + 1)
        # click: Rotate the middle three elements if not all elements are the same
        if current_pattern[3] != current_pattern[4] or current_pattern[4] != current_pattern[5]:
            new_pattern = current_pattern[:3] + current_pattern[4] + current_pattern[5] + current_pattern[3] + current_pattern[6:]
            dfs(new_pattern, current_pattern, X, current_step + 1)
        return

    def get_path():
        path = []
        current_pattern = (goal, "")
        while True:
            path.append(current_pattern)
            if current_pattern[0] == original:
                break
            current_pattern = parent[current_pattern[0]]
        return path[::-1]

    dfs(original, "", "", 0)
    if step == 999:
        print("No solution found. check your input.")
        return
    print("Minimum number of steps: ", step)
    path = get_path()
    for i in range(len(path) - 1):
        print(path[i][0], " -> ", path[i + 1][0], " : ", path[i][1])
    return

def valid_arguments(args):
    for line in args.o,args.p:
        if len(line) != 8:
            return False
    return True

if __name__ == "__main__":
    #Adding necessary input arguments
    parser = argparse.ArgumentParser(description='test')
    parser.add_argument('--o', type=str, default="", help ='original pattern')
    parser.add_argument('--p', type=str, default="", help = 'pattern to crack')
    args = parser.parse_args()
    if not valid_arguments(args):
        print( "Invalid arguments.")
        print("Usage: python dotsLockCracker.py --o <original pattern> --p <pattern to crack>")
        print("Example: python dotsLockCracker.py --o 30000013 --p 03100030")
        exit()
    main(args.o,args.p)