import functools
def toJadenCase(str):
	list = str.split(" ")
	for i in list:
		i=i.capitalize()
	return list

ret = toJadenCase('How can mirrors be real if our eyes aren\'t real')
print(ret)