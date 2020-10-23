# O(c1 + c2) T O(c1 + c2) S
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    updatedCalendar1 = updateCalendar(calendar1, dailyBounds1)
	updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)
	mergedCalendar = mergeCalendar(updatedCalendar1, updatedCalendar2)
	flattenedCalendar = flattenCalendar(mergedCalendar)
	return meetingAvailability(flattenedCalendar, meetingDuration)
	
def updateCalendar(calendar, dailyBounds):
	calendar.insert(0, ["0:00", dailyBounds[0]])
	calendar.append([dailyBounds[1], "23:59"])
	return list(map(lambda m: [timeToMins(m[0]), timeToMins(m[1])], calendar))
	
def timeToMins(time):
	hours, mins = time.split(":")
	return int(hours)*60 + int(mins)
	
def mergeCalendar(updatedCalendar1, updatedCalendar2):
	i = 0
	j = 0
	mergedCalendar = []
	while i < len(updatedCalendar1) and j < len(updatedCalendar2):
		if updatedCalendar1[i][0] < updatedCalendar2[j][0]:	
			mergedCalendar.append(updatedCalendar1[i])
			i += 1
		else:
			mergedCalendar.append(updatedCalendar2[j])
			j += 1
	while i < len(updatedCalendar1):
		mergedCalendar.append(updatedCalendar1[i])
		i += 1
	while j < len(updatedCalendar2):
		mergedCalendar.append(updatedCalendar2[j])
		j += 1
	return mergedCalendar
		
def flattenCalendar(mergedCalendar):
	flattenedCalendar = [mergedCalendar[0]]
	for i in range(1, len(mergedCalendar)):
		previousTime = flattenedCalendar[-1]
		currentTime = mergedCalendar[i]
		previousStartTime, previousEndTime = previousTime
		currentStartTime, currentEndTime = currentTime
		if currentStartTime <= previousEndTime:
			flattenedCalendar[-1][1] = max(previousEndTime, currentEndTime)
		else:	
			flattenedCalendar.append(currentTime)
	return flattenedCalendar
	
def meetingAvailability(flattenedCalendar, meetingDuration):
	meetingAvailability = []
	for i in range(1, len(flattenedCalendar)):
		previousEndTime = flattenedCalendar[i-1][1]
		currentStartTime = flattenedCalendar[i][0]
		if currentStartTime-previousEndTime >= meetingDuration:
			meetingAvailability.append([previousEndTime, currentStartTime])
	return list(map(lambda m: [minsToTime(m[0]), minsToTime(m[1])], meetingAvailability))
		
def minsToTime(mins):	
	hours = mins // 60
	min = mins % 60
	hoursString = str(hours)
	minString = "0" + str(min) if min < 10 else str(min)
	return hoursString + ":" + minString