while True:
    print('Enter the amount of Home Loan')
    p=int(input())
    print('Enter the rate of interest e.g 12.5,9.35,9.35  per annum etc')
    r = float(input())
    print('Enter the time period in years...e.g. 5,10,15,20,30')
    m = int(input())
    m = (m * 12)
    r = ( r/1200 )
    emi = (p*r*((1+r)**m))/(((1+r)**m)-1)
    print('Equated Monthly Installment is Rs.',emi)
    print()
    print('Enter 1 to Continue and 2 for Discontinue')
    x=input()
    if x == '1':
        continue
        print()
    elif x == '2':
        break
    else:
        print('@@###~~INVALID INPUT~~###@@')
        print()
    
    
