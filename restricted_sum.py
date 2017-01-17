def checkio(numbers):
	ans , t,q = 0,0, len(numbers)
	if q!=0:
		q,ans,t = test(q,ans,t,numbers)
	print q,ans,t
	return ans
	
def test(q,ans,t,numbers):
	ans +=numbers[0+t]
	t +=1
	q -=1

	return q,ans,t	
	
print checkio([1,2])
