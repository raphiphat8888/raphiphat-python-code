"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha()#ตรวจสอบตัวอักษรภาษาอังกฦษ, isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""
print("=== PERSONAL INFORMATION VALIDATOR ===")
name = input("enter your name")
Age = input("enter your age")
Phone=input("enter your phone number")
int(Age)

#name validation
nameFlag = True
for char in name:
    print(char,char.isalpha())
    if not(char.isalpha()==False or char==" "):
        nameFlag =False
   
print(nameFlag)
ageFlag=True
if int(Age)>=18 or int(Age)<=65:
    ageFlag = False
phoneFlag=True
if len(Phone)!=10:
    phoneFlag=False
else:
    for char in Phone:
        if char.isdigit()==False:
            phoneFlag=False
            break
print("Varidetion Results:")
if nameFlag:
    print("Name:Valid (contains only letters and spaces)")
else:
    print("Name: Invalid(not contains only letters and spaces)")

if(ageFlag):
    print(f"Age: Valid ({Age} years old)")
else:
    print(f"Age: Invalid ({Age} years old)")
if (phoneFlag):
    print("Phone:Valid (10-digit number)")
else:
    print("Phone:Ivalid (not 10-digit number)")

print("formatted information:")
print("Name:",name.upper(),name.lower(),name.capitalize())
if int(Age)>=18 and int(Age)<=30:

    print("Age Group: Young adult (18-30)")
else:
    print("Age Group: not YOung Adult")

print(f"Phone:+{Phone}")