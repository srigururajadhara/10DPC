#numbers
a=5
#String
x="GURU"
#list
y=['a', 'b', 5, 6, 7.7]
#tuples
z=(1, 2, 3, 4, 5)
#dict
b={'number': 5, 'name': 'GURU', 'age': 25}
#set
k={1, 2, 3, 4, 5}

print(type(a))
print(type(x))
print(type(y))
print(type(z))
print(type(b))
print(type(k))

print("The value of a is:", a)
print("The value of x is:", x)
print("The value of y is:", y)
print("The value of z is:", z)
print("The value of b is:", b)
print("The value of k is:", k)

#replace k value
k={6, 7, 8, 9, 10}
print("The value of k is:", k)
#in the same k variable we can replace the value of k with new values. In this case, we have replaced the old set {1, 2, 3, 4, 5} with a new set {6, 7, 8, 9, 10}.
k={11, 12, 13, 14, 15}
print("The value of k is:", k)
#add `new value to k`
k.add(16)
print("The value of k is:", k)

#remove value from k
k.remove(11)
print("The value of k is:", k)

#duplicate value in k
k.add(12)               #this is mutable and it will not allow duplicate values in the set.
print("The value of k is:", k)

