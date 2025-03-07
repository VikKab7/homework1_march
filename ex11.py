def read_graph():

  arr = input().split()
  N = int(arr[0])
  M = int(arr[1])

  edge_list = []
  for _ in range(M):
    arr = input().split()
    a = int(arr[0])
    b = int(arr[1])
    edge_list.append((a, b))

  return edge_list