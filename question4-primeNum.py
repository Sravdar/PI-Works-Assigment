for number in range(500, 601):
	isPrime = True
	for divider in range(2, number-1):
		if (number % divider == 0):
			isPrime = False
			break
	if(isPrime):
		print(number)
	
		
	 