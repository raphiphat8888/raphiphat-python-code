
"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("raphiphat ", 20, "pathumthani", "thailand")  # name, age, city, country
    hobbies = ["playgame"]
    while True:
        print("1.check date person")
        print("2.change hobby")
        print("3.remove hobby")
        print("4.change age")
        print("5.exit")
        choice=input("what choice")
        if(choice=='1'):
            print ("name:",person[0])
            print ("age:",person[1])
            print ("City:",person[2])
            print ("country:",person[3])   
        elif(choice=='2'):
            hobby=input("what is your hobbies?")
            hobbies.append(hobby)
        elif(choice=='3'):
            hobbies.pop()
            person_list=list(person)
        elif(choice=='4'):
            age= input("how old are you ,broo ?")
            person_list[1]= age
            person=tuple(person_list)
        else:
            break
    

if __name__ == "__main__":
    personal_info_manager()

