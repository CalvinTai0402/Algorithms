# O(AlogA+A+R+A(A+R)) T O(A+R) S
def airportConnections(airports, routes, startingAirport):
    airportGraph = createAirportGraph(airports, routes)
	unreachableAirportNodes = getUnreachableAirportNodes(airportGraph, airports, startingAirport)
	getUnreachableConnections(airportGraph, unreachableAirportNodes)
	return getMinConnectionsToAdd(airportGraph, unreachableAirportNodes)

# O(A+R) T O(A+R) S
def createAirportGraph(airports, routes):
	airportGraph = {}
	for airport in airports:
		airportGraph[airport] = AirportNode(airport)
	for route in routes:
		airport, connection = route
		airportGraph[airport].connections.append(connection)
	return airportGraph
	
# Next two functions mark the nodes to isReachable = False if we can't get to them from the startingAirport
# O(A+R) T O(A) S
def getUnreachableAirportNodes(airportGraph, airports, startingAirport):
	visited = {}
	dFSUnreachableNodes(airportGraph, startingAirport, visited)
	unreachableAirportNodes = []
	for airport in airports:
		if airport in visited:
			continue
		airportGraph[airport].isReachable = False
		unreachableAirportNodes.append(airportGraph[airport])
	return unreachableAirportNodes
	
def dFSUnreachableNodes(airportGraph, airport, visited):
	if airport in visited:
		return
	visited[airport] = True
	for connection in airportGraph[airport].connections:
		dFSUnreachableNodes(airportGraph, connection, visited)

# Next two functions append the airport to the current airportNode's
# unreachableConnections if we can't get to them from the startingAirport (hence unreachable)
# but the airport can be reached from the current airportNode (hence connections)

# O(A*(A+R)) T O(A) S
def getUnreachableConnections(airportGraph, unreachableAirportNodes):
	for airportNode in unreachableAirportNodes:
		airport = airportNode.airport
		unreachableConnections = []
		dFSUnreachableConnections(airportGraph, airport, unreachableConnections, {})
		airportNode.unreachableConnections = unreachableConnections

def dFSUnreachableConnections(airportGraph, airport, unreachableConnections, visited):
	if airportGraph[airport].isReachable:
		return
	if airport in visited:
		return
	visited[airport] = True
	unreachableConnections.append(airport)
	for connection in airportGraph[airport].connections:
		dFSUnreachableConnections(airportGraph, connection, unreachableConnections, visited)

# Find the airport with the largest unreachableConnections length. Connect the startingAirport to it.
# Make all the unreachableConnections' isReachable = True.
# O(AlogA+A+R) T O(1) S
def getMinConnectionsToAdd(airportGraph, unreachableAirportNodes):
	unreachableAirportNodes.sort(key = lambda airportNode: len(airportNode.unreachableConnections), reverse = True)
	minConnectionsToAdd = 0
	for airportNode in unreachableAirportNodes:
		if airportNode.isReachable:
			continue
		minConnectionsToAdd += 1
		for connection in airportNode.unreachableConnections:
			airportGraph[connection].isReachable = True
	return minConnectionsToAdd

# reachable, unreachable is with respect to the starting airport
class AirportNode:	
	def __init__(self, airport):
		self.airport = airport
		self.connections = []
		self.isReachable = True
		self.unreachableConnections = []
