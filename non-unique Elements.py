def checkio(data):
	output = []
	for i in xrange(0,len(data)):
		tmp = data[i]
		if data.count(tmp) != 1:
			output.append(tmp)
	return output
	
	
data = [[1, 2, 3, 1, 3],[1, 2, 3, 4, 5],[5, 5, 5, 5, 5],[10, 9, 10, 10, 9, 8]]

for v in data:
	print checkio(v)
