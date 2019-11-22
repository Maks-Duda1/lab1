a=float(input("First number:"))
b=float(input("Second number:"))
operation=(input("Your operatoin:"))
result= None
if operation == "+":
    result=a+b
elif operation == "-":
    result = a-b
elif operation=="*":
    result = a*b
elif operation=="/":
    if b == 0:
        print("you can't do it")
    else:
        result= a/b
else:
    print("Unsupported operation")
if result is not None :
    print("Your result",result)