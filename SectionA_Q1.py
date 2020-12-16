from random import randint
def foo(length):
	list = []
	while( len(list) <= 10 ):
		r = randint(1,length)
		if (r not in list):
			list.append(r)
		if (len(list) == 10):
 			break;
	return list
x = foo(10)
print(x)