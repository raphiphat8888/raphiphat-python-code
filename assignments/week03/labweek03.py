# Complete this program to classify people by age

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
age = int(input("Enter age: "))
if age<=12:
    print("child")
elif age<=19:
    print("Teenager ")
elif age<=50:
    print("Adult")
else:
    print("Senior")