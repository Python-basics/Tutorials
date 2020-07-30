
##name = "Sam"


##print(name)


##for _ in range(3):
##    print(name)
    
##for i in range(1,5):
##    print(i)

##l_5 = list(range(5))

##for i in range(2,11,2):
##    print(i)
    
##for num in l_5:
##    print(num)
##    print(num*2)
##    print()
    
'''
S a m u e l
0 1 2 3 4 5



'''

##letters = "PTJB"
##
##for letter in letters:
##    print(letter + name[1:])
    


##def hello():
##    name = input("Enter name: ")
##    print("Hello " + name)
##
##
##hello()





##def blank():
##    print()
##
##def blank_3():
##    blank()
##    blank()
##    blank()
##
##def blank_9():
##    blank_3()
##    blank_3()
##    blank_3()
##
##
##    
##blank_9()






##for number in numbers:
##    if number % 2 == 0:
##        print(number, "is even")
##    else:
##        print(number, "is odd")
        
    

##for number in numbers:
##    if number == 0:
##        print("Zero")
##    elif number > 0:
##        print("positive")
##    else:
##        print("negative")
        
    
##def even(x):
##    """enter number to be checked if even"""
##    if x % 2 == 0:
##        return True

##def even(x):
##    return x % 2 == 0
##
##def odd(y):
##    return y % 2 != 0
##
##print(even(4))
##
##print(odd(5))

##
##for row in range(5):
####    print(row)
##    for col in range(5):
##        print(col,end='')
##    print()


##numbers = [1,-5,2,-4,0,6,-10,3]
##
##
##def Pos_Neg(x):
##    if number == 0:
##        print("Zero")
##    else:
##        if number > 0:
##            print("Positive")
##        else:
##            print("Negative")
##            
##
##for number in numbers:
####    print(number)
##    Pos_Neg(number)
    
    



##for row in range(5):
####    print(row)
##    for col in range(5):
##        print(col,end='')
##    print()


##for row in range(1,14):
##    for col in range(1,row+1):
##        print('{:3}'.format(col),end="")
##    print()
    



##def hello():
##    name = input("Enter name: ")
##    print("Hello " + name + " nice to meet you.")
##
##
##hello()



##def hello():
##    name = input("Enter name: ")
##    print("Hello {} nice to meet you.".format(name))
##
##
##hello()

##count = int(input("Enter Number: "))
####number = int(number)
##
####print(type(number))
##print("ready")
##while count >= 0:
##    
##    print(count)
##    count -= 1
##print("Blastoff!!!!!!!")

    

numbers = [1,-5,2,-4,0,6,-10,3]

##pos = []
##neg = []
##
##
##for number in numbers:
##    if number > 0:
##        pos.append(number)
##    else:
##        neg.append(number)
        
##pos = [i for i in numbers if i > 0]

##list_numbers = []
##
##for i in range(3):
##    list_numbers.append(list(range(1,6)))

import random

##number = [random.randint(1,5) for i in range(10)]

##numbers = [i for i in range(1,26)]
##
##random.shuffle(numbers)

shuffled = [8, 5, 2, 25, 7,
            1, 11, 17, 15, 13,
            23, 9, 19, 21, 22,
            3, 16, 24, 12, 14,
            4, 10, 20, 6, 18]
horses = [[],
          [],
          [],
          [],
          []
    ]
##for i in range(5):
##    for j in range(5):
##        horses[j].append(shuffled.pop())
        
    
horses = [[18, 14, 22, 13, 7],
          [6, 12, 21, 15, 25],
          [20, 24, 19, 17, 2],
          [10, 16, 9, 11, 5],
          [4, 3, 23, 1, 8]]

for race in horses:
##    race.sort()
    race.sort()
##
##
##for race in horses:
##    print(race)
##    
##def last(x):
##    return x[-1]
##
##
##new_horses = sorted(horses,key=last,reverse=True)
##
##print()
##for race in new_horses:
##    print(race)
    
## 1  3 13 19 25 
## 5 14 18 20 24 
## 6  7 15 17 23 
## 4  8  9 10 22 
## 2 11 12 16 21




##def time_table():
##    while True:
##        try:
##            x = int(input("Please enter a number: "))
##            for row in range(x+1):
##                for col in range(x+1):
##                    print(f"{row*col:3}", end = " ")
##                print()
##        except ValueError:
##            print("Oops, please enter a number.")
##        q = input("Do you want another table? y/n ").lower()
##        if q[0] == 'n':
##            break
##        
##
##
##time_table()


##def is_prime(num):
##    for i in range(2,num):
##        if num%i == 0:
##            return False        
##    return True
####
####test = [3,6,11,31]
####
####
####for num in test:
####    print(f"{num} is a prime number {is_prime(num)}")
##
##
##def nth_prime(x):
##    num = 3
##    prime = 2
##    if x == 1:
##        return 2
##    while prime < x:
##        num += 2
##        if is_prime(num):
##            prime += 1
##    return num
##        
##primes = [i for i in range(2,101) if is_prime(i)]



##import random
##
##while True:
##    number = random.randint(1,20)
##    print(number)
##    try:
##        guess = int(input("Please enter a guess: "))
##        while guess != number:
##            if guess > number:
##                print("Please guess a smaller number.")
##                guess = int(input("Please enter a guess: "))
##            else:
##                print("Please guess a larger number.")
##                guess = int(input("Please enter a guess: "))
##        else:
##            print("You guessed the correct number.")
##    except ValueError:
##        print("Oop please enter a number.")
####    print("You guessed the correct number.")
##    q = input("Do you want to play again? y/n ").lower()
##    if q[0] == 'n':
##        break



# leap year

# 1992 1600 1900 2002 2020


##def leap_year(x):
##    if x % 4 == 0:
##        if x % 100 == 0:
##            if x % 400 == 0:
##                return True
##            else:
##                return False
##        else:
##            return True
##    else:
##        return False
##            
##
##years = [1992,1600,1900,2002,2020]
##
##for year in years:
##    print(year,leap_year(year))
##


names = ['Sam','Tom','Steve']


##for i in range(len(names)):
##    print(i+1,names[i])

    


##for i in enumerate(names,start=1):
##    print(i)
    


for num, name in enumerate(names,start=1):
    print(num,name)
    
# 7/28/20 longest sub-string compuer guessing game 


##sen = 'hi Sam nice to meet you'
##
##comma = 'Sam,Tom,Pete,Matt'


##name = input("Please enter names use commas: ").split(',')
##
##names = [i.strip() for i in name]
##
##print(names)



##x = 'abcaafahbaabdfgz'
##
##sub = x[0]
##
##long, length = sub, 1
##
##for letter in x[1:]:
##    if ord(sub[-1]) <= ord(letter):
##        sub += letter
##        if len(sub) > length:
##            length = len(sub)
##            long = sub
##            print(long)
##    else:
##        sub = letter
####        print(letter)
##print(long)






##dad = 'dadaddadaadada'
##
##count, place = 0,0
##
##while dad.find('dad', place) >= 0:
##    place = dad.find('dad',place) + 1
##    count += 1
##print(count)
##    

##from string import ascii_lowercase as lower
##import re
##
##x = 'abcaafahbaabdfgz'
##
##abc = ''
##
####for letter in lower:
####    abc += letter+'*'
####    print(abc)
##
####abc = '*'.join(lower)
####abc += '*'
##
##
##abc = 'a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*'
##  
##pat = re.compile(abc)
##
##print(max(pat.findall(x),key=len))


##ans = False
##
##high = 100
##low = 0
##
##input = ('Think of a number between 1 and 100. Please press enter to continue')
##
##
##while not ans:
##    guess = 0
##    print(f'Is you number {guess}')
##    resp = input("""Enter 'h' to indicate the guess is too high. 
##Enter 'l' to indicate the guess is too low. 
##Enter 'c' to indicate I guessed correctly.
##Enter Answer: """).lower()
##    if resp == 'h':
##        print('My guess was too high')
##    elif resp == 'l':
##        print('MY guess was too low')
##    elif resp == 'c':
##        print('Thanks for playing with me!')
##        ans = True


##import re
##
##dad = 'dadaddadaadada'
##
##found = re.findall(r'(?=(\w\w\w))',dad)
##
##dads = [dad for dad in found if dad == 'dad']
##
##print(len(dads))



x = 4
def add(x):
    print(x + 2)

add(2)













