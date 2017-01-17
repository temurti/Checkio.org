import re

def find_path(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return path
	if not graph.has_key(start):
		return None
	for node in graph[start]:
		if node not in path:
			newpath = find_path(graph, node, end, path)
			if newpath: return newpath
	return None


def check_connection(network, name1,name2):
	network = list(network)
	A,tmp = [],[]
	for i in xrange(0,len(network)):
		p = re.match('([a-z0-9]*)-([a-z0-9]*)',network[i])
		A.append([p.group(1),p.group(2)])
		if p.group(1) not in tmp:
			tmp.append(p.group(1))
		if p.group(2) not in tmp:
			tmp.append(p.group(2))
	#print network
	#print A
	#print tmp
	
	B = []
	for i in xrange(0,len(tmp)):
		for j in xrange(0,len(A)):
			if tmp[i] in A[j]:
				if tmp[i] != A[j][0]:
					B.append([tmp[i],A[j][0]])
				else: 
					B.append([tmp[i],A[j][1]])
	for i in xrange(0,len(B)-1):
		for j in xrange(i,len(B)-1):
			if B[i] == B[j][::-1]:
				B.pop(j)
	B = sorted(B)
	
	Graph = {}
	#print B
	for i in xrange(0,len(tmp)):
		test = []
		for j in xrange(0,len(B)):
			if tmp[i] in B[j]  :
				if tmp[i] != B[j][1]:
					test.append(B[j][1])
				else: 
					test.append(B[j][0])
			Graph.update({tmp[i] : test })
			#B.pop(j)
		
	
	#print Graph

	if (find_path(Graph,name1,name2)):
		return True
	else:
		return False


print check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "scout2", "scout3") 


