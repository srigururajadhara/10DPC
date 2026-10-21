#list
task=['eat','code','sleep']
print("The value of task is:", task)

#add repeat task in the list
task.append('repeat')
print("The value of task is:", task)

for i in task:
    print("The value of i is:", i)
    if i == 'code':
        print("I am coding")
    else:
        print("I am not coding")

#all methods of list
#1. append() - adds an element to the end of the list
task.append('exercise')
print("The value of task is:", task)

#2. insert() - adds an element at a specific position in the list
task.insert(1, 'study')
print("The value of task is:", task)

#3. remove() - removes the first occurrence of an element from the list
task.remove('sleep')
print("The value of task is:", task)

#4. pop() - removes and returns the last element from the list
last_task = task.pop()
print("The last task was:", last_task)
print("The value of task is:", task)    

#5. index() - returns the index of the first occurrence of an element in the list
index_of_code = task.index('code')
print("The index of 'code' is:", index_of_code)

#6. count() - returns the number of occurrences of an element in the list
count_of_code = task.count('code')
print("The count of 'code' is:", count_of_code)

#7. sort() - sorts the elements of the list in ascending order
numbers = [5, 2, 9, 1, 5, 6
]
numbers.sort()
print("The sorted numbers are:", numbers)   

#8. reverse() - reverses the order of the elements in the list
numbers.reverse()
print("The reversed numbers are:", numbers)


