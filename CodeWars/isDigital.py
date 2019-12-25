def filter_list(str):
	# new_str = []
	# i = 0
	# while i<len(str):
	# 	if isinstance(str[i],int):
	# 		new_str.append(str[i])
	# 	i+=1
	# return new_str
	return [x for x in str if isinstance(x,int)]
ret = filter_list([1,2,'s','d',15,43])
print(ret)