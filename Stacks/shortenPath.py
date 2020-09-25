# O(N) T O(N) S
def shortenPath(path):
	finalStack = []
	if path[0] == "/":
		finalStack.append("")
	tokenList = path.split("/")
	tokenList = list(filter(lambda token: token != "", tokenList))
	tokenList = list(filter(lambda token: token != ".", tokenList))
	for token in tokenList:
		if token != "..":
			finalStack.append(token)
		else:
			if len(finalStack) == 0 or finalStack[-1] == "..":
				finalStack.append(token)
			elif finalStack[-1] == "":
				continue
			else:
				finalStack.pop()
	return "/" if len(finalStack) == 1 and finalStack[0] == "" else "/".join(finalStack)