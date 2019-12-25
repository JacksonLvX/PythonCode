
'''
The main idea is to count all the occuring characters(UTF-8) in string. If you have string like this aba then the result should be { 'a': 2, 'b': 1 }

What if the string is empty ? Then the result should be empty object literal { }

For C#: Use a Dictionary<char, int> for this kata!
'''
from collections import Counter

def count(str):
	return {i:str.count(i) for i in str}
	#return Counter(str)

ret = count('aba')
print(ret)