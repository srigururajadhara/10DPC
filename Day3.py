#Conditional statements are used to perform different actions based on different conditions. In this code, we are taking a score as input from the user and then using conditional statements to determine the grade based on the score.
score = int(input("Enter your score: "))
#if the score given 100 above then its wrong right? then how to handle that? we can use else statement to handle that.

if score > 100:
    print("Invalid score. Please enter a score between 0 and 100.") 
elif score >= 90: 
    print("Grade: A+")
elif score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: FAIL")


#nested if else statement
#In this code, we are taking a score as input from the user and then using nested
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
    if age <= 18:
        print("You are not eligible to vote.")
    elif age >= 60:
        print("You are eligible for senior citizen benefits.")
    else:
        print("You are not eligible for any other benefits.")
else:
    print("You are not eligible to vote.")

#ternary operator
#In this code, we are taking a score as input from the user and then using a
status = "Pass" if score >= 60 else "Fail"
print("Your status is:", status)