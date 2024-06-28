
#create 2d grid
grid = [
['.','2','1','.','.','.','.','.','.','.'],
['.','#','#','.','.','#','.','.','.','.'],
['3','.','.','.','.','#','.','.','.','.'],
['.','.','#','#','.','.','.','.','.','.'],
['.','.','.','#','.','.','#','.','.','.'],
['.','#','.','.','5','4','#','.','.','.'],
['.','.','.','#','.','.','.','.','.','.'],
['.','.','#','.','7','#','.','.','.','.'],
['.','.','.','8','6','#','.','.','.','.']
]
for row in grid:
    print(row)

start_row = 0
start_col = 0
goal_row = 8
goal_col = 9

start_point = (start_row, start_col)
goal_point = (goal_row, goal_col)

print(start_point)
print(goal_point)

grid[start_point[0]][start_point[1]] = 'S'
grid[goal_point[0]][goal_point[1]] = 'G'

for row in grid:
    print(row)


def bfs_search(grid, start_point, goal_point):
    space_size_rows = len(grid)
    space_size_cols = len(grid[0])
    grid_parent = [[None]*space_size_cols for _ in range(space_size_rows)]
    V = []
    F = [start_point]
    Actions = [(-1,0), (0,1), (1, 0), (0, -1)]
    while(len(F) > 0):
        n = F.pop(0)
        if(n == goal_point):
            print('Success :)')
            print('Total nodes visited: ', len(V))
            path = []
            cur_path = n
            while cur_path is not None:
                path.append(cur_path)
                cur_path = grid_parent[cur_path[0]][cur_path[1]]
            path.reverse()
            return path
        V.append(n)

        for cur_act in Actions:
            next_F_point = (n[0]+cur_act[0], n[1]+cur_act[1])
            #check rows bound
            if(next_F_point[0] < 0 or next_F_point[0]>= space_size_rows):
                continue
            #check columns bound
            if (next_F_point[1] < 0 or next_F_point[1] >= space_size_cols):
                continue
            if(next_F_point in V):
                continue
            if(next_F_point in F):
                continue
            if (grid[next_F_point[0]][next_F_point[1]] == '#'):
                continue
            F.append(next_F_point)
            grid_parent[next_F_point[0]][next_F_point[1]] = n


    print('Failed to find a path!!')
    return None


def dfs_search(grid, start_point, goal_point):
    space_size_rows = len(grid)
    space_size_cols = len(grid[0])
    grid_parent = [[None] * space_size_cols for _ in range(space_size_rows)]
    V = []
    F = [start_point]
    Actions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while (len(F) > 0):
        n = F.pop()
        if (n == goal_point):
            print('Success :)')
            print('Total nodes visited: ', len(V))
            path = []
            cur_path = n
            while cur_path is not None:
                path.append(cur_path)
                cur_path = grid_parent[cur_path[0]][cur_path[1]]
            path.reverse()
            return path
        V.append(n)

        for cur_act in Actions:
            next_F_point = (n[0] + cur_act[0], n[1] + cur_act[1])
            # check rows bound
            if (next_F_point[0] < 0 or next_F_point[0] >= space_size_rows):
                continue
            # check columns bound
            if (next_F_point[1] < 0 or next_F_point[1] >= space_size_cols):
                continue
            if (next_F_point in V):
                continue
            if (next_F_point in F):
                continue
            if (grid[next_F_point[0]][next_F_point[1]] == '#'):
                continue
            F.append(next_F_point)
            grid_parent[next_F_point[0]][next_F_point[1]] = n


    print('Failed to find a path!!')
    return None


def ucs_search(grid, start_point, goal_point):
    space_size_rows = len(grid)
    space_size_cols = len(grid[0])
    grid_parent = [[None] * space_size_cols for _ in range(space_size_rows)]
    V = []
    F = [start_point]
    Actions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while (len(F) > 0):
        n = F.pop(0)
        if (n == goal_point):
            print('Success :)')
            print('Total nodes visited: ', len(V))
            path = []
            cur_path = n
            while cur_path is not None:
                path.append(cur_path)
                cur_path = grid_parent[cur_path[0]][cur_path[1]]
            path.reverse()
            return path
        V.append(n)

        for cur_act in Actions:
            next_F_point = (n[0] + cur_act[0], n[1] + cur_act[1])
            # check rows bound
            if (next_F_point[0] < 0 or next_F_point[0] >= space_size_rows):
                continue
            # check columns bound
            if (next_F_point[1] < 0 or next_F_point[1] >= space_size_cols):
                continue
            if (next_F_point in V):
                continue
            if (next_F_point in F):
                continue
            if (grid[next_F_point[0]][next_F_point[1]] == '#'):
                continue
            if (not F):
                F.append(next_F_point)
                grid_parent[next_F_point[0]][next_F_point[1]] = n
            elif F:
                F.append(next_F_point)
                grid_parent[next_F_point[0]][next_F_point[1]] = n
                for i in range(0, len(F)):
                    for j in range(i + 1, len(F)):
                        if grid[F[i][0]][F[i][1]] == '.':
                            grid[F[i][0]][F[i][1]] = 0
                        if grid[F[j][0]][F[j][1]] == '.':
                            grid[F[j][0]][F[j][1]] = 0
                        if grid[F[i][0]][F[i][1]] == '#':
                            grid[F[i][0]][F[i][1]] = 100
                        if grid[F[j][0]][F[j][1]] == "#":
                            grid[F[j][0]][F[j][1]] = 100
                        if grid[F[i][0]][F[i][1]] == 'S':
                            grid[F[i][0]][F[i][1]] = 0
                        if grid[F[j][0]][F[j][1]] == 'S':
                            grid[F[j][0]][F[j][1]] = 0
                        if grid[F[i][0]][F[i][1]] == 'G':
                            grid[F[i][0]][F[i][1]] = 0
                        if grid[F[j][0]][F[j][1]] == 'G':
                            grid[F[j][0]][F[j][1]] = 0
                        grid[F[i][0]][F[i][1]] = int(grid[F[i][0]][F[i][1]])
                        grid[F[j][0]][F[j][1]] = int(grid[F[j][0]][F[j][1]])
                        oof = grid[F[i][0]][F[i][1]]
                        if grid[F[i][0]][F[i][1]] >= grid[F[j][0]][F[j][1]]:
                            # temporary variable
                            temp = F[i]
                            F[i] = F[j]
                            F[j] = temp


    print('Failed to find a path!!')
    return None


def gfs_search(grid, start_point, goal_point):
    space_size_rows = len(grid)
    space_size_cols = len(grid[0])
    grid_parent = [[None] * space_size_cols for _ in range(space_size_rows)]
    V = []
    F = [start_point]
    Actions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while (len(F) > 0):
        n = F.pop(0)
        if (n == goal_point):
            print('Success :)')
            print('Total nodes visited: ', len(V))
            path = []
            cur_path = n
            while cur_path is not None:
                path.append(cur_path)
                cur_path = grid_parent[cur_path[0]][cur_path[1]]
            path.reverse()
            return path
        V.append(n)

        for cur_act in Actions:
            next_F_point = (n[0] + cur_act[0], n[1] + cur_act[1])
            # check rows bound
            if (next_F_point[0] < 0 or next_F_point[0] >= space_size_rows):
                continue
            # check columns bound
            if (next_F_point[1] < 0 or next_F_point[1] >= space_size_cols):
                continue
            if (next_F_point in V):
                continue
            if (next_F_point in F):
                continue
            if (grid[next_F_point[0]][next_F_point[1]] == '#'):
                continue
            if (not F):
                F.append(next_F_point)
                grid_parent[next_F_point[0]][next_F_point[1]] = n
            elif F:
                F.append(next_F_point)
                grid_parent[next_F_point[0]][next_F_point[1]] = n
                for i in range(0, len(F)):
                    for j in range(i + 1, len(F)):
                        distance1 = abs(F[i][0]-goal_point[0]) + abs(F[i][1]-goal_point[1])
                        distance2 = abs(F[j][0]-goal_point[0]) + abs(F[j][1]-goal_point[1])
                        if (distance1 > distance2):
                            temp = F[i]
                            F[i] = F[j]
                            F[j] = temp


    print('Failed to find a path!!')
    return None


def ast_search(grid, start_point, goal_point):
    space_size_rows = len(grid)
    space_size_cols = len(grid[0])
    grid_parent = [[None] * space_size_cols for _ in range(space_size_rows)]
    V = []
    F = [start_point]
    Actions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while (len(F) > 0):
        n = F.pop(0)
        if (n == goal_point):
            print('Success :)')
            print('Total nodes visited: ', len(V))
            path = []
            cur_path = n
            while cur_path is not None:
                path.append(cur_path)
                cur_path = grid_parent[cur_path[0]][cur_path[1]]
            path.reverse()
            return path
        V.append(n)

        for cur_act in Actions:
            next_F_point = (n[0] + cur_act[0], n[1] + cur_act[1])
            # check rows bound
            if (next_F_point[0] < 0 or next_F_point[0] >= space_size_rows):
                continue
            # check columns bound
            if (next_F_point[1] < 0 or next_F_point[1] >= space_size_cols):
                continue
            if (next_F_point in V):
                continue
            if (next_F_point in F):
                continue
            if (grid[next_F_point[0]][next_F_point[1]] == '#'):
                continue
            if (not F):
                F.append(next_F_point)
                grid_parent[next_F_point[0]][next_F_point[1]] = n
            elif F:
                F.append(next_F_point)
                grid_parent[next_F_point[0]][next_F_point[1]] = n
                for i in range(0, len(F)):
                    for j in range(i + 1, len(F)):
                        dis_from_start1 = abs(start_point[0]-F[i][0]) + abs(start_point[1]-F[i][1])
                        dis_from_start2 = abs(start_point[0]-F[j][0]) + abs(start_point[1]-F[j][1])
                        dis_to_goal1 = abs(F[i][0] - goal_point[0]) + abs(F[i][1] - goal_point[1])
                        dis_to_goal2 = abs(F[j][0] - goal_point[0]) + abs(F[j][1] - goal_point[1])
                        total_distance1 = dis_from_start1 + dis_to_goal1
                        total_distance2 = dis_from_start2 + dis_to_goal2
                        if (total_distance1 > total_distance2):
                            temp = F[i]
                            F[i] = F[j]
                            F[j] = temp

    print('Failed to find a path!!')
    return None


searchChoice = input('Which algorithm you would like to use for searching? Enter one of the following bfs, dfs, ucs, gfs or ast ' )
if searchChoice == 'bfs':
    path = bfs_search(grid, start_point, goal_point)
    if(path is not None):
        print('Path length is: ', len(path))
        print(path)
    i = 1
    while i < len(path) - 1:
        grid[path[i][0]][path[i][1]] = "P"
        i += 1
if searchChoice == 'dfs':
    path = dfs_search(grid, start_point, goal_point)
    if (path is not None):
        print('Path length is: ', len(path))
        print(path)
    i = 1
    while i < len(path) - 1:
        grid[path[i][0]][path[i][1]] = "P"
        i += 1
if searchChoice == 'ucs':
    path = ucs_search(grid, start_point, goal_point)
    if (path is not None):
        print('Path length is: ', len(path))
        print(path)
    grid = [
        ['.', '2', '1', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '#', '#', '.', '.', '#', '.', '.', '.', '.'],
        ['3', '.', '.', '.', '.', '#', '.', '.', '.', '.'],
        ['.', '.', '#', '#', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '#', '.', '.', '#', '.', '.', '.'],
        ['.', '#', '.', '.', '5', '4', '#', '.', '.', '.'],
        ['.', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '#', '.', '7', '#', '.', '.', '.', '.'],
        ['.', '.', '.', '8', '6', '#', '.', '.', '.', '.']
    ]
    grid[start_point[0]][start_point[1]] = 'S'
    grid[goal_point[0]][goal_point[1]] = 'G'
    i = 1
    while i < len(path) - 1:
        grid[path[i][0]][path[i][1]] = "P"
        i += 1
if searchChoice == 'gfs':
    path = gfs_search(grid, start_point, goal_point)
    if (path is not None):
        print('Path length is: ', len(path))
        print(path)
    i = 1
    while i < len(path) - 1:
        grid[path[i][0]][path[i][1]] = "P"
        i += 1
if searchChoice == 'ast':
    path = ast_search(grid, start_point, goal_point)
    if (path is not None):
        print('Path length is: ', len(path))
        print(path)
    i = 1
    while i < len(path) - 1:
        grid[path[i][0]][path[i][1]] = "P"
        i += 1

for row in grid:
    print(row)


#PART SEVEN
#The example grid is not good for testing as bfs, gfs and A* search all resonalbly do the same things here path wise.
#that said dfs, ucs and gfs all do much better on the example grid given in terms of nodes visited with gfs being the best
#both bfs and A* search visit the same amount of nodes on the example grid and have the same path length
#if you were to change the grid start and goal points A* search performs much better in certian scenarioes
#for strengths bfs will always find the goal but will take a while, same with dfs, ucs will find the least costly path
#but that does not mean that it will visit the least amount of nodes possible
#gfs seems to be the best over all for path length and nodes visited but does not care about cost
#A* search is close behind gfs and performs relatively the same as far as I can tell.