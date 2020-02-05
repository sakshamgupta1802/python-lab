a = []
while 1:
	item = input('enter the item')
	a.append(item)
	n = input('do you want continue Y/N')
	if n.lower() == 'n':
		break
print(a)


