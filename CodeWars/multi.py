from functools import reduce
def multi(x,y):
	return x*y

ret = reduce(multi,[1,2,3,4])
print(ret)