
weight =float(input("your weight:"))
height=float(input("your height:"))

BMI=weight/height**2
if BMI<18.5:
    print(" Underweight")
elif BMI<=24.9:
    print(" Normal weight")
elif BMI<=29.9:
    print("Overweight")
elif BMI>=30.0:
    print("Obese")
