country = input('哪国人')
age = input('年龄：')
#casting不能少
age = int(age)
if country == 'China':
	if age >= 18:
		print('Yes')
	else:
		print('No')