from itertools import count, \
 cycle

limit = 10
cnt = 0
for el in count(int(input('Введите число'))):
	cnt += 1
	print(el)
	if cnt >= limit:
		cnt = 0
		break

my_list = [True, 'ABC', 123, False]

print('')
for el in cycle(my_list):
	cnt +=1
	print(el)
	if cnt >= limit:
		cnt = 0
		break