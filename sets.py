#sets
a={1,2,3,4,5,6,7,8,9}
#adding and remoeing
a.add(10)
a.remove(1)
print(a)

#coversion 
b=set([1,2,23,4,5,7,3,4,8,2,9,8,3,5])

#union (``)
c=a.union(b)
print(c)

#intersection(&)
d=a.intersection(b)
print(d)

#difference(-)
e=a.difference(b)
print(e)

#symmetric difference(^)
f=a.symmetric_difference(b)
print(f)

#subset(<=)
g=a.issubset(b)
print(g)

#superset(>=)
h=b.issuperset(a)
print(h)

#disjoint sets()
i=a.isdisjoint(b)
print(i)
#frozenset()
j=frozenset([1,2,3,4,4,57,7,8,9])
print(j)
