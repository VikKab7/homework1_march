def BFS(start_node, adj_list, visited=None):
    if visited is None:
        visited = set()

    queue = [start_node]
    visited.add(start_node)

    while queue:
        curr_node = queue.pop(0)
        for adj_node in adj_list[curr_node]:
            if adj_node not in visited:
                visited.add(adj_node)
                queue.append(adj_node)

    return visited


def count_c(N, adj_list):
    visited = set()
    k = 0

    for node in range(N):
        if node not in visited:
            BFS(node, adj_list, visited)
            k = k + 1

    return k



N = int(input())
M = int(input())
edge_list = []
adj_list = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

comp= count_c(N, adj_list)
print(comp)