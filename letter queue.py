
def checkio(cmnds):
	cmnds_new, output = [] , []
	for i in xrange(0,len(cmnds)):
		cmd = cmnds[i].split()
		cmnds_new.append(cmd)
		
	for j in xrange(0,len(cmnds_new)):
		if cmnds_new[j][0] == 'PUSH':
			output.append(cmnds_new[j][1])
		if cmnds_new[j][0] == 'POP' and (output != []) :
			output.pop(0)
			
	return ''.join(output)
	
print checkio(["PUSH A", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"])
	
