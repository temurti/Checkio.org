def checkio(lst):
	# x-win
	tmp = []
	for i in xrange(len(lst)):
		tmp.append(list(lst[i]))
	# stolbec dlya X	
	if ('X' == tmp[0][0] == tmp[1][0] == tmp[2][0]) or ('X' == tmp[0][1] == tmp[1][1] == tmp[2][1]) or ('X' == tmp[0][2] == tmp[1][2] == tmp[2][2]):
		return 'X'
	#stoka dlya X
	if ('X' == tmp[0][0] == tmp[0][1] == tmp[0][2]) or ('X' == tmp[1][0] == tmp[1][1] == tmp[1][2]) or ('X' == tmp[2][0] == tmp[2][1] == tmp[2][2]):
		return 'X'
	#vertical dlya X
	if ('X' == tmp[0][0] == tmp[1][1] == tmp[2][2]) or ('X' == tmp[0][2] == tmp[1][1] == tmp[2][0]):
		return'X'
		
	# stolbec dlya O
	if ('O' == tmp[0][0] == tmp[1][0] == tmp[2][0]) or ('O' == tmp[0][1] == tmp[1][1] == tmp[2][1]) or ('O' == tmp[0][2] == tmp[1][2] == tmp[2][2]):
		return 'O'
	#stoka dlya O
	if ('O' == tmp[0][0] == tmp[0][1] == tmp[0][2]) or ('O' == tmp[1][0] == tmp[1][1] == tmp[1][2]) or ('O' == tmp[2][0] == tmp[2][1] == tmp[2][2]):
		return 'O'
	#vertical dlya O
	if ('O' == tmp[0][0] == tmp[1][1] == tmp[2][2]) or ('O' == tmp[0][2] == tmp[1][1] == tmp[2][0]):
		return'O'
				 
	return 'D'
print checkio([
    "X.O",
    "XX.",
    "XOO"])
	
