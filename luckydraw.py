from random import*
print('please carefully read all the terms and conditions associated with this program.')
def spinwheel(drawnumber):
    if drawnumber == 1:
        return 'Your are about to win,Its just the start.'
    elif drawnumber == 2:
        return 'you lose'
    elif drawnumber == 3:
        return  'Better luck next time.'
    elif drawnumber == 4:
        return 'You are so close.'
    elif drawnumber == 5:
        return  'Try harder!!'
    elif drawnumber == 6:
        return  'you have won my heart, Try little more.'
    elif drawnumber == 7:
        return  'you have won INR.1'
    elif drawnumber == 8:
        return  'You are wise but try again.'
    elif drawnumber == 9:
        return  'You got a bicycle,good fortune.'
    elif drawnumber == 10:
        return  'you have won a car !!,Lucky One!'
    elif drawnumber > 10 and drawnumber < 16:
        return 'suck my nuts!!'
    elif drawnumber > 15 and drawnumber < 21:
        return 'You are trying to fart while squeezing ass,push harder baby!!'
    elif drawnumber > 20 and drawnumber < 26:
        return ' You are such a good gambler but destination is far away'
    elif drawnumber > 25 and drawnumber < 31:
        return 'you have won INR.5'
    elif drawnumber > 30 and drawnumber < 36:
        return 'you have won INR.3'
    elif drawnumber > 35 and drawnumber < 41:
        return 'You have won nothing but my gratitude, Sir/Madam'
    elif drawnumber > 40 and drawnumber < 46:
        return 'Not enough,try again'
    elif drawnumber > 45 and drawnumber < 51:
        return 'Yes! Yes!! Yes!!!,you have won INR.1,25,00,00,00,000....HELLO,I WAS KIDDING,LOL!!'
    elif drawnumber > 50 and drawnumber < 56:
        return 'Just dont chase pussy, Keep it goinn, good luck next time'
    elif drawnumber > 55 and drawnumber < 61:
        return 'you have won a beer can but it will be served hot.'
    elif drawnumber > 60 and drawnumber < 66:
        return 'you have won membership of my golf club at 50% discount'
    elif drawnumber > 65 and drawnumber < 71:
        return 'Focus you idoit/s,You are losing'
    elif drawnumber > 70 and drawnumber < 76:
        return 'you have won movie tickets..( Read T&C for more info.)'
    elif drawnumber > 75 and drawnumber < 81:
        return 'flee away, come another day'
    elif drawnumber > 80 and drawnumber < 86:
        return 'you have won electric dildo, take good care of your holes.'
    elif drawnumber > 85 and drawnumber < 91:
        return 'you have won a mobilephone...(Read T&C.)'
    elif drawnumber > 90 and drawnumber < 96:
        return'you are hereby declared as Brazzers premium member for one year...(Read T&C.)'
    elif drawnumber > 95 and drawnumber < 101:
        return 'Yor far away,but you have won INR.900'
r = randint(1, 100)
print('drawn no.'+ str(r))
fortune = spinwheel(r)
print(fortune)
print('Type "1" for reading terms and condition oherwise enter any number')
x =int(input())
if x == 1:
    print('By using this program, you are considered to be agreed with these Terms and Conditions:- '
          ' 1. This program is made for only fun purpose.  '
          ' 2.Nothing will be awarded for any kind of winning.  '
          ' 3.Nothing will be charged for the use of  this program.  '
          ' 4.Be discreet, valgur language is used in this program.  '
          ' 5.This program can be modified and distributed at your own risk.  '
          ' 6.No copyrights,do whatever you want, I dont give a shit about it.')
else:
    print('Thank You')
