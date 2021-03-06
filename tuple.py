mytuple = ("Max", 28, Boston)
print(mytuple)

mytuple = "Max", 28, "Boston"
print(mytuple)


item = mytuple[1]
print(item)


for i in mytuple:
    print(i)


if "Max" in mytuple:
    print("Yes")

else:
    print("No")

my_tuple = ['a', 'p', 'p', 'l', 'e']
print(len(my_tuple))


print(my_tuple.count('e'))

print(my_tuple.index('p'))


list1 = list(my_tuple)
print(list1)

tuple2 = tuple(list1)
print(tuple2)
tuple = "Rafath", 18, "ctg"

name, age, city = tuple

print(name)
print(age)
print(city)


import sys

lis1 = [0, 1, 2, 3, "hello", True]S
tup1e = (0, 1, 2, 3, "hello", True)

print(sys.getsizeof(lis1), "bytes")

print(sys.getsizeof(tup1e), "bytes")


import timeit

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))


print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))
