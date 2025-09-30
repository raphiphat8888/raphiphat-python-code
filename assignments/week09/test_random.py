import random
#refactor != debug
def test_random():
    random_number = random.randint(1, 100)
    while True:
        number=int(input("what is number do you think ?"))
        if(number==random_number):
            print("good gay bro")
            break
        elif (number>random_number):
            print("your number is more")
        elif (number<random_number):
            print("your number is less")

    print(random_number)
    
test_random()
