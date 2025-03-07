def reverse_graph(N, edge_list):
    reverse_edge_list = []
    for a, b in edge_list:
        reverse_edge_list.append((b, a))
    return reverse_edge_list


def ad_matrix(N, edge_list):
    matrix = [[0] * N for _ in range(N)]
    for a, b in edge_list:
        matrix[a][b] = 1
    return matrix

def print_matrix(matrix):
  for line in matrix:
    print(*line)


N = int(input())
M = int(input())
edge_list = []
for _ in range(M):
    u, v = map(int, input().split())
    edge_list.append((u, v))

reverse_edge_list = reverse_graph(N, edge_list)
reverse_matrix = ad_matrix(N, reverse_edge_list)
print_matrix(reverse_matrix)