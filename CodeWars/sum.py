def sum(s):
	i = 1
	sum = 0
	while i<=s:
		sum += 1/(3*i-2) 
		i+=1
	return "%.2f"%sum
ret = sum(1)
print(ret)

sum(x for x in range(0,10))