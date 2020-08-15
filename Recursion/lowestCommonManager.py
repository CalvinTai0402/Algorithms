# O(N) T O(d) S
def getLowestCommonManager(topManager, reportOne, reportTwo):
	if reportOne is topManager or reportTwo is topManager:
		return topManager
	return getLowestCommonManagerR(topManager, reportOne, reportTwo)
	
def	getLowestCommonManagerR(topManager, reportOne, reportTwo):
	count = 0
	for report in topManager.directReports:
		if report is reportOne or report is reportTwo:
			count += 1
		if len(report.directReports) != 0:
			returnedValue = getLowestCommonManagerR(report, reportOne, reportTwo)
			if isinstance(returnedValue, int):
				count += returnedValue
				if count == 2 and returnedValue != 0:
					if report is reportOne or report is reportTwo:
						return report
			else:
				return returnedValue
	if count == 2:
		return topManager
	else:
		return count

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
