def ad_matrix(N, edge_list):
    matrix = [[0] * N for _ in range(N)]
    for x, y in edge_list:
        matrix[x][y] = 1
        matrix[y][x] = 1

    return matrix