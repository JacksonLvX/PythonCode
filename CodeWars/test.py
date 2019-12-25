def accum(s):
	a = list(s)
	s = []
	i = 0
	while i<len(a):
		j = 0
		#a[i] = a[i].upper()
		while j<=i:
			s.append(a[i])
			j+=1
		s.append('-')
		i+=1
	str = "".join(s)
	print(str)
accum('asdf')
