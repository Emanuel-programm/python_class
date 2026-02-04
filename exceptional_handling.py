

try:
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
    print("Resource open")
    print("The division is",a/b);
   
# except Exception as e:
except ZeroDivisionError as e:
    print("You cannot divide a number by zero",e);
except ValueError as e:
    print("Invalid input",e);
except Exception as e:
    print("Something went wrong",e);


finally:
    print("Resource closed")