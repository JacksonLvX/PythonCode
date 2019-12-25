'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
'''

def getMinLen(s):
	return min(len(l) for l in s.split())
	#return min(map(len,s.split(" "))
	#return len(min(s.split(' '),key=len))

ret = getMinLen("how old are you n")
print(ret)



