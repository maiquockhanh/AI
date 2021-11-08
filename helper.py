def input(path_file):
    with open(path_file, 'r') as file:
        input_lines = [line.strip() for line in file]

    N = int(input_lines[0])
    goal = int(input_lines[N*N+1])
    adj = []

    for i in range(1,N*N+1):
        int_arr = list(map(int,input_lines[i].split(" ")))
        adj.append(int_arr)

    return [N, adj, goal]