# O(V) T O(V+V+V+V+E) S == O(V) T O(V+E) S
def topologicalSort(jobs, deps):
    visitedSet = set([])
	sortedStack = []
	graph = {job: [] for job in jobs}
	for prereq, job in deps:
		graph[prereq].append(job)
	for vertex in graph:
		if vertex in visitedSet:
			continue
    	if topologicalSortR(graph, vertex, visitedSet, set([]), sortedStack):
			return []
	return sortedStack[::-1]
	
def topologicalSortR(graph, vertex, visitedSet, visitedSetTemp, sortedStack):
	visitedSet.add(vertex)
	visitedSetTemp.add(vertex)
	for childVertex in graph[vertex]:
		if len(list(visitedSetTemp & set(graph[childVertex]))) != 0:
        	return True
		if childVertex in visitedSet:
			continue
		if topologicalSortR(graph, childVertex, visitedSet, visitedSetTemp, sortedStack):
			return True
	sortedStack.append(vertex)
	visitedSetTemp.remove(vertex)
	return False