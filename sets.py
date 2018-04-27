#UPDOG
#Jasper Cheung and Shannon Lau
#SoftDev2 pd7
#K16 -- Ready, Set, Math!
#2018-04-27

def union(a,b):
    return set_difference(a,b) + b

def intersection(a,b):
    return [i for i in a if i in b]

def set_difference(a,b):
    return [i for i in a if i not in b]

def symmetric_difference(a,b):
    return union(set_difference(a,b),set_difference(b,a))

def cartesian_product(a,b):
    return [(i,j) for i in a for j in b]

a = [1,2,3]
b = [2,3,4]

print union(a,b)
print intersection(a,b)
print set_difference(a,b)
print symmetric_difference(a,b)
print cartesian_product(a,b)
