# O(N) T O(N) S
def riverSizes(matrix):
    sizes = []
    visited = [[False for col in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if visited[i][j] == False:
                traverse(i, j, matrix, visited, sizes)
    return sizes
    
def traverse(i, j, matrix, visited, sizes):
    currentSize = 0
    nodes = [[i,j]]
    while len(nodes):
        i,j = nodes.pop()
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentSize += 1
        neighbours = getUnvisitedNeighbours(i, j, matrix, visited)
        for neighbour in neighbours:
            nodes.append(neighbour)
    if currentSize > 0:
        sizes.append(currentSize)

def getUnvisitedNeighbours(i, j, matrix, visited):
    neighbours = []
    # up, down, left, right
    if i > 0 and not visited[i-1][j]:
        neighbours.append([i-1,j])
    if i < len(matrix)-1 and not visited[i+1][j]:
        neighbours.append([i+1,j])
    if j > 0 and not visited[i][j-1]:    
        neighbours.append([i,j-1])
    if j < len(matrix[0])-1 and not visited[i][j+1]:
        neighbours.append([i,j+1])
    return neighbours
        