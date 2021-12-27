#Problem-34: Given a string inputStr and a string pattern, find minimum window in inputStr which will contain all chars in pattern.

def minWindowSubStr(inputStr, pattern):
	if inputStr == '' or pattern == '':
		return ''
	lastSeen = {}
	start = 0
	end = len(inputStr)-1
	pattern = set(pattern)		#eliminate duplicates

	for i, ch in enumerate(inputStr):
		if ch not in pattern:
			continue
		lastSeen[ch] = i 	#update to the latest value

		if len(lastSeen) == len(pattern):
			first = min(lastSeen.values())

			if i-first+1 < end-start+1:		#len(newWindow) < len(oldWindow)
				start = first
				end = i

	window = inputStr[start:end+1] if len(lastSeen) == len(pattern) else ''
	print(window, len(window))
	return window

minWindowSubStr('XFDOYEZODEYXNZD','XYZF')
minWindowSubStr('ADOBECODEBANC','ABC')
minWindowSubStr('a','aa')
minWindowSubStr('XXXYYYY','XY')



