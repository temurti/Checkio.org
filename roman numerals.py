def checkio(number):
	ROMANS = (('M',  1000),
          ('CM', 900),
          ('D',  500),
          ('CD', 400),
          ('C',  100),
          ('XC', 90),
          ('L',  50),
          ('XL', 40),
          ('X',  10),
          ('IX', 9),
          ('V',  5),
          ('IV', 4),
          ('I',  1))
	result = ''
	for roman, value in ROMANS:
		while number >= value:
			#print number
			number -= value
			result = result + (roman)
	return result

print checkio(6) == 'VI'
print checkio(76) == 'LXXVI'
print checkio(13) == 'XIII'
print checkio(44) == 'XLIV'
print checkio(3999) == 'MMMCMXCIX'
