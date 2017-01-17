
def checkio(string):
	string = sorted(list(string.lower()))
	string = ''.join(e for e in string if e.isalnum()) # remove special symbols
	string = ''.join([i for i in string if not i.isdigit()]) # remove digits
	A,done, number = [], [],1
	for i in range(0,len(string)):
		if string[i] not in done:
			for j in range(i+1, len(string)-1):
				if string[i] == string[j]:
					number += 1
			A.append([string[i],number])
			done.append(string[i])
			number = 1
	
		
	for i in xrange(0,len(A)):
		for j in xrange(i,len(A)):
			if A[i][1] < A[j][1]:
				tmp = A[i]
				A[i] = A[j]
				A[j]= tmp
	return A[0][0]

	
print checkio("AAaooo!!!!")
