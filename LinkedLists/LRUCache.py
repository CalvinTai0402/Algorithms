# Do not edit the class below except for the insertKey"val"uePair,
# get"val"ueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
# O(1) T O(1) S for all methods
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
		self.mostRecent = None
		self.leastRecent = None
		self.cache = {}

    def insertKeyValuePair(self, key, value):
		if key in self.cache:
			self.cache[key]["val"] = value
		elif len(self.cache) == 0:
			self.cache[key] = {"val": value, "next": None, "prev": None}
			self.mostRecent = key
			self.leastRecent = key
        elif len(self.cache) < self.maxSize:
			self.cache[self.mostRecent]["prev"] = key
			self.cache[key] = {"val": value, "next": self.mostRecent, "prev": None}
			self.mostRecent = key
		elif len(self.cache) >= self.maxSize:
			if self.maxSize == 1:
				self.cache.pop(self.leastRecent)
				self.cache[key] = {"val": value, "next": None, "prev": None}
				self.mostRecent = key
				self.leastRecent = key
			else:
				# get rid of leastRecent
				self.leastRecent = self.cache[self.leastRecent]["prev"]
				self.cache.pop(self.cache[self.leastRecent]["next"])
				self.cache[self.leastRecent]["next"] = None
				# take care of mostRecent
				self.cache[self.mostRecent]["prev"] = key
				self.cache[key] = {"val": value, "next": self.mostRecent, "prev": None}
				self.mostRecent = key

    def getValueFromKey(self, key):
		if key in self.cache:
			if self.maxSize == 1:
				return self.cache[key]["val"]
			else:
				if self.leastRecent == key:
					self.leastRecent = self.cache[self.leastRecent]["prev"]
					self.cache[self.leastRecent]["next"] = None
				if self.cache[self.mostRecent]["next"] == key:
					self.cache[self.mostRecent]["next"] = self.cache[key]["next"]
					self.cache[self.cache[key]["next"]]["prev"] = self.mostRecent
				self.cache[self.mostRecent]["prev"] = key
				self.cache[key]["next"] = self.mostRecent
				self.cache[key]["prev"] = None
				self.mostRecent = key
				return self.cache[key]["val"]
		else:
			return None

    def getMostRecentKey(self):
        return self.mostRecent
