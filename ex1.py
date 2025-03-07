def adj_matrix(N, edge_list):
    res = [[0 for j in range(N)] for i in range(N)]

    for x, y in edge_list:
        res[x][y] = 1
        res[y][x] = 1

    return res

def print_matrix(matrix):
  for line in matrix:
    print(*line)


N = int(input())
M = int(input())
edge_list = []
for _ in range(M):
    u, v = map(int, input().split())
    edge_list.append((u, v))


ad_matrix = adj_matrix(N, edge_list)
print_matrix(ad_matrix)
