from collections import deque
from collections import defaultdict
from collections import Counter
from collections import namedtuple
from collections import OrderedDict


a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(2)[0][0])
print(list(my_counter.elements()))
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)

print(pt.x, pt.y)

od = OrderedDict()

od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

print(od)

d = defaultdict(int)

d['a'] = 1
d['b'] = 2

print(d['b'])


d = deque()

d.append(1)
d.append(2)
d.appendleft(3)
print(d)

d.extend([4, 5, 6])
print(d)
d.extendleft([9, 10, 11])
print(d)

d.rotate(1)
print(d)
d.rotate(2)

print(d)
