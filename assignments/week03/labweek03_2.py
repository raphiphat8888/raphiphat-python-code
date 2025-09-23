# Complete this ATM simulation
balance=float(1000)
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice=='1':
            print(f"The money in your account is{balance}THB")

        elif choice =='2':
            Withdraw = float(input("How much do you want to withdraw?"))
            if Withdraw <=balance:
                print(f"withdraw complete{Withdraw}THB")
                balance-=Withdraw
            else:
                print("Sorry,There is insufficient money in your account.")

        elif choice =='3':
             Deposit=int(input("How much do you want to Deposit?"))
             if Deposit>0:
                 print("withdraw complete",Deposit)
                 balance+=Deposit
             else:
                 print("Sorry,your don't have money")
        elif choice == '4':
            print("Thank you for using the service. ")
            break
        else:
            print("sorry Invalid number ")
        
else:
    print("Invalid PIN")