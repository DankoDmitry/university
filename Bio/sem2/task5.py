names = ["name","Dave", "Dennis", "Peter", "Jess"]
languages = ["language",'Python', 'C', "Java", 'Python']

data = dict(zip(names, languages))


with open ('file.txt', 'w') as f:
	s=''
	for i in data:
		l = len(i)
		s += i + ' '*(10-l) + data[i] + '\n'
	f.write(s)
