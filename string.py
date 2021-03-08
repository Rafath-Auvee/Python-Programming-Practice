# str = '    Auvee   '
# str2 = str.strip()
# str2 = str2[::-2]
# print(str2)


# str = 'How are you doing'

# last = str.split(" ")
# print(last)

from timeit import default_timer as timer

one = ['a'] * 1000000

start = timer()

str = ''.join(one)

stop = timer()

print(stop-start)
