while True:
    def len_cm():                            # 1.convert b/w centimetre and millimetre
        return (10*cm)
    def len_mm():
        return (mm/10)                       # 1.convert b/w centimetre and millimetre

    def len_cm1():                           # 2.convert b/w centimetre and inches
        return (.394*inch)
    def len_inch():
        return (cm1/.394)                    # 2.convert b/w centimetre and inches

    def len_cm2():                           # 3.convert b/w centimetre and yards
        return (cm2*.01094444)
    def len_yard():
        return (yard/.01094444)                 # 3.convert b/w centimetre and yards

    def len_inch1():                         # 4.convert b/w inches and yards
        return (inch1*0.027777777777777776)
    def len_yard1():
        return (yard1/0.027777777777777776)         # 4.convert b/w inches and yards

    def len_inch2():
        return (inch2*0.0254000)
    def len_metre():
        return (metre / 0.0254000)                  #5.convert b/w inches and metre

    def len_metre1():                               # 6.convert b/w metre and yards
        return (metre1/0.9144)
    def len_yard2():                               # 6.convert b/w metre and yards
        return (yard2*.9144)

    def len_metre2():                                        # 7.convert b/w metre and killometre
        return(metre2*.001)
    def len_killometre():
        return(killometre/.001)

    def len_metre3():                                                # 8.convert b/w metre and centimetre
        return(metre3/.01)
    def len_cm3():
        return(cm3*
        .01)                                               # 8.convert b/w metre and centimetre

    def len_killometre1():                                  #9.convert b/w killometre and miles
        return(km*.6213712)
    def len_miles():
        return(miles/.6213712)

    def len_metre4():                                       #10.convert b/w miles and metre
        return(metre4*.0006213712)
    def len_miles1():
        return(miles1/.0006213712)

    def len_km2():
        return(km2/0.0009143999)                             # 11.convert b/w killometre and yards
    def len_yard3():
        return(yard3*0.0009144)

    def len_miles2():                                            #12.convert b/w miles and yards
        return(miles2/0.0005681818181818182)
    def len_yard4():
        return(yard4*0.0005681818181818182)

    def len_feet():                                             # 13.convert b/w feet and yard
        return(feet*0.3333333333333333)
    def len_yard5():
        return(yard5/0.3333333333333333)
    
    def len_feet1():                                             #14.convert b/w feet and killometer
        return(feet1*.0003048)
    def len_km4():
        return(km4/.0003048)

    def len_feet2():                                        #15.convert b/w feet and miles
        return (feet2*0.0001893939393939394)
    def len_miles3():
        return (miles3/0.0001893939393939394)

    def len_feet3():                                                #16.convert b/w feet and meter
        return(feet3*0.30480000000214824)
    def len_meter():
        return(meter/0.30480000000214824)

    
    print()
    print()
    print('please select option')
    print('  1.convert b/w centimetre and millimetre')
    print('  2.convert b/w centimetre and inches')
    print('  3.convert b/w centimetre and yards')
    print('  4.convert b/w inches and yards')
    print('  5.convert b/w inches and metre')
    print('  6.convert b/w metre and yards')
    print('  7.convert b/w metre and killometre')
    print('  8.convert b/w metre and centimetre')
    print('  9.convert b/w killometre and miles')
    print('  10.convert b/w miles and metre')
    print('  11.convert b/w killometre and yards')
    print('  12.convert b/w miles and yard')
    print('  13.convert b/w feet and yard')
    print('  14.convert b/w feet and killometer')
    print('  15.convert b/w feet and miles')
    print('  16.convert b/w feet and meter')
    print('  17. To DISCONTINUE')
    print(' Enter your choice...e.g 1/2/3/4/...../15/16/17')
    choice = input()
    if choice == '1':
        print('Enter value centimetre or millimetre')             # 1.convert b/w centimetre and millimetre
        cm = float(input())
        mm = cm
        print(cm,'cm','=',len_cm(),'mm')
        print(mm,'mm','=',len_mm(),'cm')

    elif choice =='2':
        print('Enter value of centimetre or inches')               # 2.convert b/w centimetre and inches
        cm1 = float(input())
        inch = cm1
        print(cm1,'cm','=',len_cm1(),'inch')
        print(inch,'inch','=',len_inch(),'cm')

    elif choice == '3':
        print('Enter value of centimetre or yards')                # 3.convert b/w centimetre and yards
        cm2 = float(input())
        yard = cm2
        print(cm2,'cm','=',len_cm2(),'yard')
        print(yard,'yard','=',len_yard(),'cm')

    elif choice=='4':
        print('Enter value of inches or yards')                     # 4.convert b/w inches and yards
        inch1 = float(input())
        yard1 = inch1
        print(inch1,'inches','=',len_inch1(),'yards')
        print (yard1,'yards','=',len_yard1(),'inches')

    elif choice == '5':
        print('Enter value of inches or metre')                              #5.convert b/w inches and metre
        inch2 = float(input())
        metre = inch2
        print(inch2,'inches','=',len_inch2(),'metre')
        print(metre,'metre','=',len_metre(),'inches')

    elif choice == '6':                                              # 6.convert b/w metre and yards
        print('Enter value of metres or yards')
        metre1 = float(input())
        yard2 = metre1
        print(metre1,'metre','=',len_metre1(),'yards')
        print(yard2,'yards','=',len_yard2(),'metre')

    elif choice == '7':                                               # 7.convert b/w metre and killometre
        print('Enter value of metre or killometre')
        metre2 = float(input())
        killometre = metre2
        print(metre2,'metres','=',len_metre2(),'killometre')
        print(killometre,'km','=',len_killometre(),'metres')

    elif choice =='8':                                                  # 8.convert b/w metre and centimetre
        print('Enter value of metre or centimetre')
        metre3 = float(input())
        cm3 = metre3
        print(metre3,'metres','=',len_metre3(),'centimetre')
        print(cm3,'centimetre','=',len_cm3(),'metres')

    elif choice == '9':                                                   #9.convert b/w killometre and miles
        print('Enter value of killometre or miles')
        km = float(input())
        miles  = km
        print(km,'km','=',len_killometre1(),'miles')
        print(miles,'miles','=',len_miles(),'km')

    elif choice == '10':                                            #10.convert b/w miles and metre
        print('Enter value of miles or metre')
        metre4 = float(input())
        miles1 = metre4
        print (metre4,'metre','=',len_metre4(),'miles')
        print(miles1,'miles','=',len_miles1(),'metre')

    elif choice == '11':                                        # 11.convert b/w killometre and yards
        print('Enter value of killometre and yard')
        km2 = float(input())
        yard3 = km2
        print(km2,'km','=',len_km2(),'yards')
        print(yard3,'yards','=',len_yard3(),'km')

    elif choice == '12':                                         #12.convert b/w miles and yards
        print('Enter value of yard or miles')
        miles2 = float(input())
        yard4 = miles2
        print(miles2,'miles','=',len_miles2(),'yard')
        print(yard4,'yard','=',len_yard4(),'miles')

    elif choice == '13':                                        # 13.convert b/w feet and yard
        print('Enter value of feet or yard')
        feet = float(input())
        yard5 = feet
        print(feet,'feet','=',len_feet(),'yards')
        print(yard5,'yard','=',len_yard5(),'feet')

    elif choice == '14':                                        #14.convert b/w feet and killometer
        print('Enter value of feet or killometer')
        feet1 = float(input())
        km4 = feet1
        print(feet1,'feet','=',len_feet1(),'km')
        print(km4,'km','=',len_km4(),'feet')

    elif choice == '15':                                         #15.convert b/w feet and miles
        print('Enter value of feet or miles')
        feet2 = float(input())
        miles3 = feet2
        print(feet2,'feet','=',len_feet2(),'miles')
        print(miles3,'miles','=',len_miles3(),'feet')


    elif choice == '16':
        print('Enter value of feet or meter')
        feet3 = float(input())
        meter = feet3;
        print(feet3,'feet','=',len_feet3(),'meter')
        print(meter,'meter','=',len_meter(),'feet')

    elif choice == '17':                                                         # break loop
        print('Thank You..!')
        break
    else:
        print('##@@@____INVALID~CHOICE____##@@@')
