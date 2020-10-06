UP = "up"
RIGHT = "right"
DOWN = "down"
LEFT = "left"

# O(N^2) T O(N^2) S
def rectangleMania(coords):
    coordsTable = getCoordsTable(coords, {})
	return countRectangles(coordsTable, coords)
	
# O(N^2) T O(N^2) S
def getCoordsTable(coords, coordsTable):
	for coord1 in coords:
		coord1Table = {UP: [], RIGHT: [], DOWN: [], LEFT: []}
		for coord2 in coords:
			direction = getCoordsDirection(coord1, coord2)
			if direction in coord1Table:
				coord1Table[direction].append(coord2)
		coord1String = coordToString(coord1)
		coordsTable[coord1String] = coord1Table
	return coordsTable
	
def getCoordsDirection(coord1, coord2):
	x1, y1 = coord1
	x2, y2 = coord2
	if y1 == y2:
		if x2 > x1:
			return RIGHT
		elif x2 < x1:
			return LEFT
	elif x1 == x2:
		if y2 > y1:
			return UP
		elif y2 < y1:
			return DOWN
	return ""
	
def coordToString(coord):
	x, y = coord
	return str(x) + "-" + str(y)
	
# O(N^2) T O(4) S, O(4) because that's the max possible on the recursive stack
def countRectangles(coordsTable, coords):
	rectangles = 0
	for coord in coords:
		rectangles += getRectangles(coordsTable, coord, UP, coord)
	return rectangles
	
def getRectangles(coordsTable, coord, direction, bottomLeft):
	coordString = coordToString(coord)
	if direction == LEFT:
		foundRectangle = bottomLeft in coordsTable[coordString][direction]
		return 1 if foundRectangle else 0
	else:
		rectangles = 0
		nextDirection = getNextDirection(direction)
		for coord in coordsTable[coordString][direction]:
			rectangles += getRectangles(coordsTable, coord, nextDirection, bottomLeft)
	return rectangles
		
def getNextDirection(direction):
	if direction == UP:
		return RIGHT
	elif direction == RIGHT:	
		return DOWN
	elif direction == DOWN:
		return LEFT
	else:
		return ""
		
#======================================Solution 2==============================================
# O(N^2) T O(N) S
def rectangleMania(coords):
    coordsTable = getCoordsTable(coords, {})
	return countRectangles(coordsTable, coords)
	
# O(N) T O(N) S
def getCoordsTable(coords, coordsTable):
	for coord in coords:
		coordString = coordToString(coord)
		coordsTable[coordString] = True
	return coordsTable
	
def coordToString(coord):
	x, y = coord
	return str(x) + "-" + str(y)
	
# O(N^2) T O(1) S
def countRectangles(coordsTable, coords):
	rectangles = 0
	for x1, y1 in coords:
		for x2, y2 in coords:
			if inUpperRight([x1, y1], [x2, y2]):
				upperCoord = coordToString([x1, y2])
				rightCoord = coordToString([x2, y1])
				if upperCoord in coordsTable and rightCoord in coordsTable:
					rectangles += 1
	return rectangles
	
def inUpperRight(coord1, coord2):
	x1, y1 = coord1
	x2, y2 = coord2
	return x2 > x1 and y2 > y1

		
		