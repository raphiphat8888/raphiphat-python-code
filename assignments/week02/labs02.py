
direction=input("choose conversion direction (  1.USD or 2.THB  )")
amount=float(input("Amount to convert:"))
if direction=='1':
    result=amount/35.5
    print("Result:",result,"USD")
else:
    result=amount*35.5
    print("Result:",result,"THB")

             
