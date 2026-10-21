#for loop 
for i in range(1,10):
    print("The value of i is:", i)

#list use in for loop
my_list = [1, 2, 'guru', 4.4, 'learning', 6, 7, 8, 9, 10]
for item in my_list:
    print("The value of item is:", item)

#using dictionary in for loop
my_dict = {'name': 'Dhara', 'age': 25, 'city': 'New York'}
for key, value in my_dict.items():
    print("The key is:", key, "and the value is:", value)

#2 lists is there change to dictionary and then use in for loop
list1 = ['name', 'age', 'city']
list2 = ['Sri', 30, 'Tamil Nadu']
my_dict = dict(zip(list1, list2))
for key, value in my_dict.items():
    print("The key is:", key, "and the value is:", value)