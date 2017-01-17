def count_neighbours(grid,x,y):
	t = list(grid)
	if (x==0) and (y==0):
		c2    =    t[x][y+1]
		b3,c3 = t[x+1][y], t[x+1][y+1]
		res      = c2+b3+c3
		
	elif x == 0 :
		a2,c2    = t[x][y-1]  ,           t[x][y+1]
		a3,b3,c3 = t[x+1][y-1],t[x+1][y], t[x+1][y+1]
		res      = a2+a3+b3+c2+c3
		
	elif y == 0 :
		b1,c1 = t[x-1][y], t[x-1][y+1]
		c2    = t[x][y+1]
		b3,c3 = t[x+1][y], t[x][y+1]
		res      = b1+b3+c1+c2+c3
		

	else:
		a1,b1,c1 = t[x-1][y-1],t[x-1][y], t[x-1][y+1]
		a2,c2    = t[x][y-1]  ,           t[x][y+1]
		a3,b3,c3 = t[x+1][y-1],t[x+1][y], t[x+1][y+1]
		res      = a1+a2+a3+b1+b3+c1+c2+c3

	return res
	
print count_neighbours(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 1, 2)
                  
print count_neighbours(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 0, 0)
print count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2)
