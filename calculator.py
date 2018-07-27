while True:
    import math

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y

    
    print()
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Root")
    print("6.Discontinue")


    choice = input("Enter choice(1/2/3/4/5/6):")

    if choice == '1':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1,"+",num2,"=", add(num1,num2))

    elif choice == '2':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1,"-",num2,"=", subtract(num1,num2))

    elif choice == '3':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1,"*",num2,"=", multiply(num1,num2))

    elif choice == '4':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1,"/",num2,"=", divide(num1,num2))

    elif choice == '5':
        n = float(input('Enter number whose root you want to find: '))
        print('Root of',n,'is: ', math.sqrt(n))

    elif choice == '6':
        print('     $$$~Thank~You~$$$')
        break

    else:
        print('              ++@@@###~Invalid~Choice~###@@@++')
        print('              Please choose among given option :- 1,2,3,4,5,6')
