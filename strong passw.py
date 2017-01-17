import re	

def checkio(passw):
	res = 0
	t1,t2,t3 = 0,0,0
	if 10 <= len(passw) <=64:
		M = list(passw)
		for i in range(0,len(passw) ):
			if t1!=1:
				if re.match('[A-Z]',M[i]):
					res =res+1
					t1 = 1
			if t2!=1:
				if re.match('[a-z]', M[i]):
					res =res+1
					t2 = 1
			if t3!=1:
				if re.match('[0-9]', M[i]):
					res =res+1
					t3 = 1
		print res
		if res == 3 :
			return True
		else:
			return False
	else: 
		return False
		
print checkio('ULFFunH8ni')
