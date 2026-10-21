#dict
student = {
    "name": "Guru",
    "age": 20,
    "grade": "A"
}
print("The value of student is:", student)

#only age value is printed
print("The value of age is:", student["age"])

#modified the age value
student["age"] = 21
print("The value of student is:", student)

#ADD new key-value pair
student["city"] = "New York"
print("The value of student is:", student)

#add one age value with 1
student["age"] += 1
print("The value of student is:", student)

#create multiple dictionaries
student1 = {
    "name": "Guru",
    "age": 20,
    "grade": "A"
}
student2 = {
    "name": "Dhara",
    "age": 22,
    "grade": "B"
}
#combine multiple dictionaries into a list
students = [student1, student2]
print("The value of students is:", students)


#using update() method to merge two dictionaries with no replace the values we need both the student data in the same dictionary
student1.update(student2)
print("The value of student1 is:", student1)

#update the value of a key in a dictionary
student1["age"] = 23
print("The value of student1 is:", student1)