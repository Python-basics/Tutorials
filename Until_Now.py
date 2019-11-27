##def ended_with_ed(s):
##    if s[-1] == 'e':    #your code goes here between the if and colon
##        return s + 'd'#your code goes here 
##    elif s[-2:] == 'd':  #your code goes here between the elif and colon
##        return s#your code goes here
##    else:  
##        return s+ 'ed'#your code goes here
##
####After your write your code save and run it.  I have a simple test at the bottom to see
####if you have covered all possibilites.
##
##def test(got, expected):
##    if got == expected:
##        x = "You did it."
##    else:
##        x = "You made a mistake somewhere.  It's ok just find it."
##    print("%s |   What we got: %s  |   What we expected %s" %
##    (x, got,expected))
##def main():
##    print("ended_with_ed")
##    test(ended_with_ed("chock"), "chocked")
##    test(ended_with_ed("bounce"), "bounced")
##    test(ended_with_ed("jumped"), "jumped")
##
#
##x = [435,43,1,-5,43,90,1]

##x = sorted(x)
##print(x[0])
##print(x[-1])
##print(max(x))
##print(min(x))


#zip


##student = ['bob','steve','john','andy']
##
##grades = [98,75,82,91]

##count = 0
##class_grades = []
##for i in student:
##    class_grades.append((i,grades[count]))
##    count += 1 
##class_grades = list(zip(student,grades))
##print(class_grades)
##for i in class_grades:
##    print(i)


##names = ['Sam','Tom','Steve']
##
##count = 1
##for i in names:
##    print(count, i)
##    count += 1
##
##new = list(enumerate(names,1))
##
##for i in new:
##    print(i[0], i[1])



#abs


##x = -4
##
##if x > 0:
##    print(x)
##else:
##    print(0-x)
##    
##print(abs(4-8))



##def cal():
##    x = eval(input("enter: "))
##    print(x)
##
##cal()

##student = ['bob','steve','john','andy']
##
##grades = [98,75,82,91]



##abc = 'abahnvasavgh'
##
##count = 0
##
####for i in abc:
####    if i == 'a':
####        count += 1
####
####
####print(count)
##
##print(abc.count('a'))



#import string.py

##import string
##
##letters = string.ascii_letters
##
##lower = string.ascii_lowercase
##



#zip dict()

##import string
##
##
##letters = string.ascii_lowercase
##
##num = list(range(1,27))
##
##key = dict(zip(letters,num))


##word = 'sam'

#print(ord(word[0]))


##for i in word:
##    print(ord(i))
    

##import string
##
##letters = string.ascii_lowercase
##
##num = list(range(1,27))
##
##key = dict(zip(letters,num))


##word = 'happy'

##count = 0
##
##for i in word:
##    count += key[i]

##count = sum([key[i] for i in word])
##
##print(count)


##word = "happy"
##
##count = sum([ord(i) -96 for i in word])
##
##
##print(count)


#sum

##x = [2,4,1,6,7]

##tot = 0
##
##for i in x:
##    tot += i
##print(tot)

##print(sum(x))



# and or 

##if 3>2 and 4>3:
##    print('yes')
##else:
##    print('no')
##    


##if 3>5 and 4>3:
##    print('yes')
##else:
##    print('no')
    

##if 3>2 or 4>3:
##    print('yes')
##else:
##    print('no')
    


##if 0>2 or 1>3:
##    print('yes')
##else:
##    print('no')
    


# lower denominator

##def lower(x,y):
##    if x > y:
##        print(x/y)
##    else:
##        print(y/x)

##def lower(x,y):
##    print(max(x,y)/min(x,y))
##    
##lower(32,8)
##lower(8,32)


# range

##for i in range(10):
##    print(i)

    
# 6
##x = 6 
##
##for i in range(x):
##    print(i)


# 2-6
##x = 6
##y = 2
##
##for i in range(y,x+1):
##    print(i)


##name = 'Sam'
##
##for i in range(1,len(name)+1):
##    print(i)



# lowest common denominator

##def lcd(x,y):
##    for i in range(2,min(x,y)+1):
##        if max(x,y)%i == 0 and min(x,y)%i == 0:
##            print(i)
##            break
##
##lcd(18,3)


#len

##name = 'sam'
##
##x = [1,2,3]
##
##y = (1,2,3)
##
##d = {'a': 1, 'b': 2}


#multiple assignment and reassign


##a, b = 1, 2
##
##print(a,b)
##
##b, a = a, b
##
##print(a,b)


#len()

##x = '' # length of 3
##
##a = 'abcdefg'

##for i in a:
##    if len(x) < 3:
##        x += i
##    else:
##        break
##    print(x)


##place = 0
##while len(x) < 3:
##    x += a[place]
##    place += 1
##    print(x, place)
##    
##print(x)


#count

##dad = 'dadaddadaadada'
##count = 0
##
##for i in range(len(dad)):
##    if dad[i:i+3] == 'dad':
##        count += 1
##print(count)
    

# boolean short cut


##def odd(x):
##    if x%2 != 0:
##        return True
##    else:
##        return False
##
##
##print(odd(5))
##print(odd(4))
##
##def odd(x):
##    return x%2 != 0
##
##
##print(odd(5))
##print(odd(4))

    
#string find method str.find()


##x = 'abcdefa'
##
##
##print(x.find('a'))
##
##print(x.find('b'))
##print(x.find('d'))
##
##print(x.find('g'))
##
##
##print(x.find('a',1))


# string find method


##dad = 'dadaddadaadada'
##sub = 'dad'
##mom = 'mom'
##count, place = 0,0
##
##
##while dad.find('dad', place) >= 0:
##    place = dad.find('dad',place) + 1
##    count += 1
##print(count)


##def sub_string(s,sub):
##    count, place = 0,0
##    while s.find(sub,place) >= 0:
##        place = s.find(sub,place) + 1
##        count += 1
##    return '{} happens {} times.'.format(sub, count)
##
##print(sub_string(dad, mom))

# why not str.count()

##dad = 'dadaddadaadada'
##count, place = 0,0
##
##while dad.find('dad', place) >= 0:
##    place = dad.find('dad',place) + 1
##    count += 1
##print(count)
##
##print(dad.count('dad'))

# squared

##def square_num(x):
##    return x**2
##
##print(square_num(4))


# square root

##def square_root(x):
####    from math import sqrt
####    print(sqrt(x))
##    print(x**.5)
##
##square_root(25)
##
##square_root(36)
##square_root(30)



# factors/divors

##def factor(x,y):
##    return x%y == 0
##
##print(factor(8,2))
##print(factor(21,7))
##print(factor(10,3))


#factors


##def factors(x):
##    d = []
##    for i in range(2,x+1):
##        if x%i == 0:
##            d.append(i)
##    return d
##
##print(factors(8))


#factors

##def factors(x):
##    d = [i for i in range(x+1,0,-1) if x%i == 0]
##    return d
##
##num = [81,18]
####print(factors(max(num)))
####print(factors(min(num)))
##print("Finding greatest common factor for: {} and {}".format(num[0],num[1]))
##for i in factors(min(num)):
##    if i in factors(max(num)):
##        print('test: {:3} match'.format(i,i))
##        break
##    else:
##        print('test: {:3} fail'.format(i,i))
    
    
#GCD

##def gcd(x,y):
##    common = min(x,y)
##    while x%common != 0 or y%common != 0:
##        common -= 1
##    return common
##
##
##print(gcd(81,18))


#rounding

##def tax(price,tax):
##    print(round(price*tax,2))
##
##tax(25.25,.07)
##tax(31.25,.07)
##tax(89.15,.07)
##tax(13.89,.07)
##tax(7.78,.07)

#  Computer guessing game


##x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


##ans = False
##
##high = 100
##low = 0
##
##
##
##while not ans:
##    guess = (high - low)//2 + low
##    print(guess)
##    resp = input("""Enter 'h' to indicate the guess is too high. 
##Enter 'l' to indicate the guess is too low. 
##Enter 'c' to indicate I guessed correctly.
##Enter Answer: """).lower()
##    if resp == 'h':
##        high = guess
##        print('Is your number {}'.format(guess))
##    elif resp == 'l':
##        low = guess
##        print('Is your number {}'.format(guess))
##    elif resp == 'c':
##        ans = True
##        print('You got it')
##    else:
##        print('Please correct respone')

#37

#Slicing  len function


##x = 'house'
##y = 'football'
##
##def cut_the_word(x):
##    mid = len(x)//2
##    beg = x[:mid]
##    end = x[mid:]
##    print(end+beg)
##
##cut_the_word(x)
##cut_the_word(y)


#  isnumeric


##x = ['1','5','p']
##
##
##for i in x:
##    if i.isnumeric():
##        print(int(i) * 2)

#list of lists

##x = []
##
##for i in range(3):
##    x.append(list(range(3)))
##
##print(x)
##
##y = [list(range(3)) for i in range(3)]
##
##
##print(y)

#string title

##
##names = ['sam','bob','steve','matt']
##
##for name in names:
##    print(name.title())

    
#rounding to next five


##for i in range(100,86,-1):
##    print(i)
    

##def fives(x):
##    if x%5 == 4:
##        x += 1
##    elif x%5 == 3:
##        x += 2
##    print(x)

##def fives(x):
##    if x%5 == 3 or x%5 == 4:
##        x += (5 - x%5)
##    print(x)
##
##
##fives(99)
##fives(98)
##fives(91)
##fives(84)


#type

#variables


##x = []
##
##y1 = ''
##
##d_percent = {}
##
##t_1  = ()
##
##z_t= 1
##
##f = 1.2


#better_than_average

##from random import randint
##
##c_grades = [randint(60,100) for i in range(10)]
##y_grades = [randint(60,100) for i in range(10)]


##print(c_grades)
##print(y_grades)

##def better_than_average(class_grades,your_grades):
##    c_avg = sum(class_grades)/len(class_grades)
##    y_avg = sum(your_grades)/len(your_grades)
##    print(c_avg,y_avg)
##    return y_avg > c_avg
##
##    
####    if y_avg > c_avg:
####        return True
####    else:
####        return False
##
##print(better_than_average(c_grades,y_grades))
##


#variables

##y = 1
##
##
##x_1 = 'x'
##
##
##his_car = 'truck'
##
##
##who = 2


#sorted lists of lists


##x_25 = [list(range(5*i+1,5*i+6)) for i in range(5)]
##
######print(x_25)
##
####def last(x):
####    return x[-1]
##
####x = sorted(x_25,key=last,reverse=True)
##
##x = sorted(x_25,key=lambda x: x[-1] ,reverse=True)
##
##for i in x:
##    print(i)


## 1  3 13 19 25 
## 5 14 18 20 24 
## 6  7 15 17 23 
## 4  8  9 10 22 
## 2 11 12 16 21 

##import random 
##
##x_25 = list(range(1,26))
##
##x = []
##
##tab = [[] for i in range(5)]
##
##random.shuffle(x_25)
##
##for i in range(5):
##    for j in range(5):
##        tab[j].append(x_25.pop())
##
##for i in tab:
##    i.sort()
##    
##def last(x):
##    return x[-1]
##
##tab = sorted(tab,key=last,reverse=True)
##
##for i in tab:
##    for j in i:
##        print('{:2d}'.format(j),end = ' ')
##    print()
##x = tab[0][2:4] + tab[1][3:] + tab[2][4:]
##x.sort()
##print(x)
##
##
###random shuffle
##
##
##import random
##
##x = list(range(10))


#list index


##x = [1,2,5,7,3,2,11]


#keyword del


##x = [1,4,2,6,7]
##y = [3,4,3,8,9]
##tot = 0
##
##name = 'sam'


#syntaxerror



##for i in range(4):
##    print(i)
##   
##for i in range(4):
##    print(i)
##x = 1
##if x == 1:
##    print('y')
##else:
##    print('n')

# longest substring in order

##x = 'abcaafahbaabdfgz'
##
##sub = x[0]
##
##long, length = sub, 1
##
##for i in x[1:]:
##    if ord(sub[-1]) <= ord(i):
##        sub += i
##        if len(sub) > length:
##            length = len(sub)
##            long = sub
##    else:
##        sub = i
##        print(i)
##print(long)


### regex
##
###longest substring
##
##import re
##
##x = 'abcaafahbaabdfgz'      
##    
##abc = 'a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*'
##    
##pat = re.compile(abc)
##
##print(max(pat.findall(x),key=len))


#string 


##from string import ascii_lowercase as lower
##
##abc = ''
##
##for i in lower:
##    abc += i+'*'
##
##print(abc)


# sum positve number


##def sum_pos(numbers):
##    return sum([i for i in numbers if i > 0])
##
##print(sum_pos([1,5,3,-7,-10]))


# doc string


##def greeting():
##    """This will say hi"""
##    print("hello")
    

# tip calculator


##def tip(bill, tip = .12):
##    """enter cost of bill and default of 12%"""
##    return round((bill * tip),2)
##
##print(round(tip(89.57),2))


# join


##abc = 'abc'
##
##new = list(abc)
##
##abc = '*'.join(new)+ '*'
##
##
##
##print(abc)


# packing/unpacking


##x = [3,5,7]
##
##
##a,b,c = x
##
##y = [a,b,c]
##
##print(y)
##print(a)
##print(b)
##print(c)

# try / except


##still = False
##while not still:
##    try:
##        num = int(input('enter number: '))
##        print(num * 2)
##        still = True
##    except ValueError:
##        print('Please enter a number')
    
# local / global

##x = 10 # global
##
##
##def dub():
####    x = 5 # local
##    print(x)
##
##dub()
##print(x)


# time 

##import time


# endswith


##def ends_with(group, string):
##    '''check to see if group is at the end
##of string'''
##    return string.endswith(group)
##
##print(ends_with('ed', 'jumped'))

# Pythagorean theorm


# a^2 + b^2 = c^2 with coordinantes


##def distance():
##    """enter two coordinate points
##to find the distance"""
##    first = input('Please enter x and y with a space ').split()
##    second = input('Please enter x and y with a space ').split()
##    a = int(second[0]) - int(first[0])
##    b = eval(second[1] + '-' + first[1])
##    return ((a**2) + (b**2))**.5
##    
##
##print(distance())


### format phone numbers
##
##def phone_number():
##    x = input("Enter your phone number: ")
##    print('{}-{}-{}'.format(x[:3],x[3:6],x[6:]))

##phone_number()

# Random seed

##from random import randint, seed
##
##seed(123)
##for i in range(10):
##    print(randint(0,10))

#string startswith


##def starts(string,var):
##    return string.startswith(var)
##
##print(starts('Mrs. White','Mrs'))

# math

##from math import factorial as fact
##
####print(factorial(5))
##
##print(fact(5))


# fibonacci


# 0 [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

# 1 [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

##def fib(x):
##    a,b = 0,1
##    tab = []
##    for i in range(x):
##        a,b = b, a+b
##        tab.append(a)
##    print(tab)
##
##fib(19)

# math pi value

##from math import pi

# odds of lottery

#  69/5 * 68/4 * 67/3 * 66/2 * 65/1 * 26  

#           (69! / 5!*(69-5)!)*26  

##def odds(balls,pick, power=False):
##    """enter number a regular balls, number of balls
##picked, and if they use a powerball, you will be asked
##for number of powerballs"""
##    from math import factorial as fact
##    p_ball = 1
##    if p_ball:
##        p_ball = int(input("How many powerballs: "))
##    return (fact(balls))/(fact(5)*fact(balls-pick))*p_ball

### local /  Global / built-in / scope
##
##
####from math import pi
##
####pi = 3.14
##def area(r):
##    global pi
##    pi = 3.14159
##    return pi*r**2
##
##print(area(3))

# new line \n tab \t

##line = "Hi Sam \n\thow are you?"
##
##print(line)
##
##new_line = """how is
##everyone  doing
##    today?"""
##print(new_line)

# random choice

##from random import choice
##
##new = list(range(1,11))
##
##
##for i in range(20):
##    print(choice(new))
    
# list remove

##new = list(range(10))
##
##print(new)
##
##new.remove(3)
##
##print(new)

### time test ep 164
##
##from time import time
##from random import randint,seed
##
##start = time()
##seed(1)
##new = [randint(0,10) for i in range(500000)]
##x = [i*i for i in new]
##end = time()
##print(end-start)
##
##start = time()
##new = []
##seed(1)
##for i in range(500000):
##    new.append(randint(0,10))
##x = []
##for i in new:
##    x.append(i*i)
##
##end = time()
##print(end-start)


# scope nonlocal / nested functions


##def exp(n):
##    n = 1
##    def num(x):
##        nonlocal n
##        n += 1 
##        return x**n
##    return num
##
##square = exp(2)
##
##print(square(2))
##
##cube = exp(3)
##
##print(cube(2))

# monty hall simulation


##from random import shuffle, choice
##
##doors = ['goat','goat','car']
##
##wins, losses = 0,0
##
##shuffle(doors)
##
##def player_choice():
##    return choice(doors)
##
##def game():
##    global wins,losses
##    player_choice()
##    if 'car' == player_choice():
##        wins += 1
##    else:
##        losses += 1
##def switch():
##    doors = ['goat','goat','car']
##    global wins, losses
##    doors.pop(choice(range(3)))
##    doors.remove('goat')
##    second_choice = doors[0]
##    if second_choice == 'car':
##        wins += 1
##    else:
##        losses += 1
##        
##def play(x):
##    for i in range(x):
##        switch()
##    print('wins: {} percent wins: {}'.format(wins,(wins/x)))
##    print('losses: {} percent losses: {}'.format(losses,(losses/x)))
##
##play(10000)

# Monty Hall All wrapped up

##from random import shuffle, choice
##
##def game(x, change=False):
##    doors = ['goat','goat','car']
##    shuffle(doors)
##    wins, losses = 0,0
##
##    def no_switch():
##        nonlocal wins, losses
##        if 'car' == choice(doors):
##            wins += 1
##        else:
##            losses += 1
##
##    def switch():
##        doors = ['goat','goat','car']
##        nonlocal wins,losses
##        doors.pop(choice(range(3)))
##        doors.remove('goat')
##        second_choice = doors[0]
##        if second_choice == 'car':
##            wins += 1
##        else:
##            losses += 1
##    for i in range(x):
##        if change:
##            switch()
##        else:
##            no_switch()
##    print('wins: {} percent wins: {}'.format(wins,(wins/x)))
##    print('losses: {} percent losses: {}'.format(losses,(losses/x)))
##            
##
##game(10000,True)

# dictionary comprehension

##students = ['steve','john','adam','will']
##
##s_dict = {student[0].upper(): student for student in students}
##
##print(s_dict)

# return None

##def even(x):
##    if x%2 == 0:
##        print('is even')
##        return
##    print('is odd')
##
##even(4)
##even(5)

##from urllib.request import urlopen as url
##
##add = url('http://www.google.com')
##
##
##print(add)


#import this


##import this


# decryption/encryption


##sen = "please encrypt me"
##
##def encrp(text,code):
##    enc = [(ord(i) + code) for i in text]
##    new = ''.join([chr(i) for i in enc])
##    print(new)
##    return new
##
##new_sen = encrp(sen,1000)
##
##
##def decrp(text,code):
##    dec = [(ord(i) - code) for i in text]
##    new = ''.join([chr(i) for i in dec])
##    print(new)
##
##
##
##decrp(new_sen,1000)


# string replace method


##text = 'this line has i in it a lot'
##
##new = text.replace('i','*',9)
##
##print(new)
##

# zip unpacking

##student = ['john', 'sam','steve','bob']
##
##
##grade = [6,7,7,8]
##
##classes = list(zip(student,grade))
##
##new_students, grades = zip(*classes)
##
##print(new_students)


### map function
##
##
##grade = [6,7,7,8]
##
##
##def add(x):
##    return x + 1
##
####new_grade = list(map(add,grade))
##
##new_grade = list(map(lambda x: x + 1,grade))
##
##print(new_grade)

# is / id

##x = 13
##
##y = x
##
##x = 12

# list copy method


##x = [1,2,3]
##
####y = x
####
####x[0] = 0
##
##y = x.copy()
##
##x[0] = 0


# set()

##shopping_list = ['apples','cereal','milk','butter','milk']
##
##
##short_list = set(shopping_list)
##
##print(short_list)

# generators / yield

##def series(num):
##    n = 0
##    while n < num:
##        yield n
##        n += 1
##
##five = series(5)


# print 3 with no numbers


##print(len("Sam"))
##
##name = 'name' 
##
##print(name.find('e'))
##
##name = list(name)
##
##print(name.index('e'))
##
##E = "EEE"
##
##print(E.count("E"))

# iter function

##name = "Sam"
##
##print(name)
##
##name = iter(name)


# string format advance


##names = ['Smith','Davis','Thomas']
##
##x = '{},{}& {}'.format('Smith','Davis','Thomas')
##
##x = '{1},{0}& {2}'.format('Smith','Davis','Thomas')
##
##x = '{name[1]},{name[2]}& {name[0]}'.format(name=names)
##
##cast = {'romeo': 'John', 'juliet': 'Sally', 'writer': "Shakespeare"}
##
##x = '{cast[romeo]},{cast[juliet]}& {cast[writer]}'.format(cast=cast)
##
##
##
##print(x)

# next function


##num = list(range(5))
##
##
##num = iter(num)


# as keyword / alias


##from math import factorial as fact
##


# urllib.request as url


##urllib.request.urlopen


##from urllib.request import urlopen as url
##
##
##page = url('http://www.google.com')


# open


##file = open('hello.txt','w')
##
##file.close()


### bytes decode method
##
##
##import urllib.request as url
##
##
##page = url.urlopen('http://www.textfiles.com/etext/AUTHORS/POE/poe-raven-702.txt')
##
##
##text = page.read()
##
##
##text = text.decode()


# write method 


##import urllib.request as url
##
##
##page = url.urlopen('http://www.textfiles.com/etext/AUTHORS/POE/poe-raven-702.txt')
##
##
##text = page.read()
##
##
##text = text.decode()
##
##
##page.close()
##
##
##file = open('raven.txt','w')
##
##
##file.write(text)
##
##
##file.close()
# pass

##def test(v,var):
##    pass


# path 


# ep200  @python_basics


# pip install periodictable


### pprint PrettyPrinter
##
##
##import periodictable as ptable
##
##
##import pprint
##
##
##pprint.pprint(dir(ptable))


### call program from dos prompt
##
##print("Hello")


### sys.argv object/variables list
##
##
##import sys
##
##
##if len(sys.argv) > 1:
##    print("Hello {}".format(sys.argv[1]))
##else:
##    print("Hello World!")

#class objects methods

##class rect():
##
##    def __init__(self, length, width):
##        self.length = length
##        self.width = width
##        print("Your rectangle is {} by {}".format(length,width))
##
##    def perim(self):
##        return 2 * (self.width + self.length)
##
##    def area(self):
##        return self.width * self.length


# requests.get  


##import requests
##
##
##
##url = 'http://www.textfiles.com/etext/AUTHORS/POE/poe-raven-702.txt'
##
##
##page = requests.get(url)
##
##print(page.text)


## readline method
##
##
##file = open('raven.txt')


### keyword with
##
##
##with open('raven.txt') as file:
##    print(file.read())


### write with append 'a'
##
##
##file = open('hello.txt','a')
##
##file.write('hello')
##
##file.close()


### shopping list delete items
##
##
##def my_list():
##    while True:
##        with open('shopping_list.txt','a+') as file:
##            print("type EXIT at anytime")
##            item = input('enter item: ')
##            if item == 'EXIT':
##                break
##            elif item == 'please tell':
##                print(file.tell())
##            elif item == 'LIST':
##                file.seek(0)
####                print(file.read())
##                items = list(enumerate(file.read().split(),1))
##                for count, item in items:
##                    print("{:3d}) {}".format(count,item))
##                remove = int(input('enter number to delete or 0 to continue: '))
##                if remove == 0:
##                    continue
##                else:
##                    del items[remove - 1]
##                    with open('shopping_list.txt', 'w') as file:
##                        for item in items:
##                            file.write(item[1] + '\n')
##            else:
##                file.write(item + '\n')
##            
##
##my_list()              


### download csv files with urllib.request
##
##
##from urllib.request import urlretrieve as retrieve
##
##
##url = 'https://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download'
##
##
##retrieve(url,'company.csv')


#####  csv.DictReader and csv.DictWriter 
##
##
##import csv
##
##
##with open('company.csv','r') as file:
##    reader = csv.DictReader(file)
##
##    with open('symbol.csv','w',newline='') as file:
##        col = ["Symbol", "Name"]
##        writer = csv.DictWriter(file, fieldnames = col)
##        writer.writeheader()
##        for line in reader:
##            del line['']
##            del line['Sector']
##            del line['LastSale']
##            del line['MarketCap']
##            del line['Summary Quote']
##            del line['industry']
##            del line['IPOyear']        
##            writer.writerow(line)
        

### % old formatting
##
##
##name = "Sam"
##
##age = 41
##
##pi = 3.141592653
##
####print("my name is %s and I'm %s." % (name, age))
####
####
####print("%10s" % age)
####
####
####print("%-10s" % age)
####
####
####print("%d" % age)
####
####
####print("%4d" % age)
##
##print('%06.2f' % pi)
##
##
##print('%07.3f' % pi)



### copy and move a file
##
##
##n_file = input("enter file name: ")
##
##path = input("enter directory: ")
##
##with open(n_file,'r') as file:
##    text = file.read()
##    with open(path + n_file,'w') as file:
##        file.write(text)


### list comprehension with condition
##
##def is_prime(x):
##    for i in range(2,x):
##        if x%i == 0:
##            return False
##    else:
##        return True
##
##
##num = [i for i in range(11)]
##
##even_num = [i for i in range(11) if i%2 == 0]
##
##primes = [i for i in range(2,101) if is_prime(i)]
##
##print(primes)


### board game
##
##
##from string import ascii_uppercase as letters
##
##from random import choice
##
##a_f = list(letters[:6])
##
##num = iter(range(1,7))
##
##arr = [['O' for i in range(6)] for i in range(6)]
##
##hidden = [choice(a_f) + str(choice(list(range(1,7)))) for i in range(4)]
##
##play = True
##
##while play:
##    num = iter(range(1,7))
##    print(hidden)
##    print("Find the {} hidden X's".format(len(hidden)))
##    print('  ' + ' '.join(a_f))
##    for i in arr:
##        print(next(num), end = ' ')
##        print(' '.join(i))
##        
##    move = input("enter move (eg. A5): ")
##    if move.lower() == 'q':
##        play = False
##    else:
##        if move in hidden:
##            hidden.pop(hidden.index(move))
##            move = list(move)
##            arr[int(move[1])-1][a_f.index(move[0])] = 'X'
##        else:
##            move = list(move)
##            arr[int(move[1])-1][a_f.index(move[0])] = ' '
##
### number first letter second


# glob  


##import glob


### posted question 
##
##
##a = ['2.3, 4, 1.3', '6.1, 9.0, 7.3']
####
####
####[[2.3, 4.0, 1.3], [6.1, 9.0, 7.3]]
##
##
##b = [[float(j) for j in i.split(',')] for i in a]
##
##
##print(b)


# checking numbers with re 


##import re
##
##from random import randint
##
##def ss():
##    return "{:03d}-{:02d}-{:04d}".format(randint(0,999),randint(0,99),randint(0,999))
##
##def phone():
##    return "{:03d}-{:03d}-{:04d}".format(randint(0,999),randint(0,99),randint(0,999))
##
##
##nums = []
##
##for i in range(20):
##    if randint(0,1):
##        nums.append(ss())
##    else:
##        nums.append(phone())
##
##
##ss = re.compile('[0-9]{3}-[0-9]{2}-[0-9]{4}')
##
##for i in nums:
##    if ss.match(i):
##        print("SS number: {}".format(i))
##    else:
##        print("Phone number: {}".format(i))
##        


# string center 


#***********************help***********************


##x = 'help'
##
##y = 50
##
##print(x.center(50,'*'))


### any/all function
##
##
##x = ['sam', 41,'bob',36,'steve','20']
##
##
##name = [False if str(i).isnumeric() else True for i in x]
##
##
##print(name)


### comma seperation
##
##
##x = 123456789
##
##
##print('{:,}'.format(x))


###itertools 
##
##
##
##import itertools


### os
##
##
##import os


# Generate pseudo-random numbers


##from random import seed, randint


### itertools chain method
##
##
##from itertools import chain
##
##
##x = 'abc'
##y = 'def'
##z = 'ghi'
##
##for i in chain(x,y,z):
##    print(i)


#  pygame


### os.getcwd()
##
##
##import os


### pygame init and quit
##
##
##from pygame import display
##
##
##x = 600
##y = 600
##z = [x,y]
##
##display.set_mode(z)


### itertools chain.from_iterable
##
##
##from itertools import chain
##
##
##x = 'abc'
##y = 'efg'
##z = 'hij'
##
##arr = [x,y,z]
##
##for i in chain.from_iterable(arr):
##    print(i)
    

### matplotlib
##
##
##import matplotlib


### os change directory
##
##
##import os


### pygame event
##
##
##import pygame 
##
##pygame.init()
##
##x = 600
##y = 600
##z = [x,y]
##
##win = pygame.display
##
##win.set_mode(z)
##
##window = True
##
##while window:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            window = False
##
##pygame.quit()


### itertools combinations
##
##
##from itertools import combinations as com
##
##
##letter = 'ABCDEFG'
##
##
##x = com(letter,3)
##
##
##y = [''.join(i) for i in x]


### matplotlib pyplot.histogram
##
##
##from matplotlib import pyplot as plt
##
##from random import randint
##
##
##x = [randint(1,10) for i in range(20)]
##
##
##plt.hist(x)
##
##
##plt.show()


###  os mkdir
##
##
##import os
##
##
##new = os.getcwd() + '\\new'
##
##
##os.mkdir(new)


### pygame set caption
##
##
##import pygame 
##
##pygame.init()
##
##x = 800
##y = 1000
##z = [x,y]
##
##win = pygame.display
##
##win.set_caption('My Window')
##
##win.set_mode(z)
##
##window = True
##
##while window:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            window = False
##
##pygame.quit()


# operator


###itertools accumulate
##
##
##from itertools import accumulate
##
##import operator
##
##
##x = list(range(1,5))
##
##
##y = list(accumulate(x,operator.mul))


### bins and ticks
##
##
##from matplotlib import pyplot as plt
##
##
##x = [10, 6, 9, 2, 5, 10, 10, 8, 2, 2, 6, 6, 3, 2, 10, 8, 6, 4, 10, 9]
##
##bins = list(range(0,11))
##
##plt.hist(x,bins=20)
##
##plt.xticks(bins)
##
##plt.show()


### os listdir
##
##
##import os



#### pygame surface, fill and update
####
####
##import pygame 
##
##pygame.init()
##
##white = (255,255,255)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##
##window = True
##
##while window:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            window = False
##    surface.fill(white)
##    win.update()
##
##pygame.quit()


### itertools count 
##
##
##
##from itertools import count
##
##
##count(1)


### labels
##
##
##from matplotlib import pyplot as plt
##
##
##x = [10, 6, 9, 2, 5, 10, 10, 8, 2, 2, 6, 6, 3, 2, 10, 8, 6, 4, 10, 9]
##
##bins = list(range(0,11))
##
##plt.hist(x,bins=20)
##
##plt.xticks(bins)
##
##plt.xlabel('age of student')
##plt.ylabel('number of student')
##
##plt.show()

##
##'''   1
##    2 3 4
##  5 6 7 8 9
##  
##  '''
##
##from itertools import count
##
##start = count(1,2)
##
##num = count(1)
##
##for i in range(1,4):
##    print(('  ')*(3-i), end = '')
##    for j in range(next(start)):
##        print(next(num), end = ' ')
##    print()
##


### dir and help deep dive
##
##
##from matplotlib import pyplot as plt
##
##
##import pygame
##


###   os  rmdir remove dir
##
##
##import os
##
##
##os.rmdir('new')


#### pygame image.load surface.blit
##
##import pygame 
##
##pygame.init()
##
##white = (255,255,255)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##
##while window:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            window = False
##    surface.fill(white)
##    surface.blit(python,(200,200))
##    win.update()
##
##pygame.quit()


# TRUE == 1 FALSE == 0


### itertools compress
##
##
##import itertools
##
##
##letters = 'abcdefg'
##
##need = [1,0,0,0,1,0,0]
##
##
##new = itertools.compress(letters,need)
##
##print(list(new))
##
##new = itertools.compress(letters,need)
##
##print(''.join(new))


### matplotlib pyplot line graph
##
##
##from matplotlib import pyplot as plt
##from random import randint
##
##
##plt.figure('chart',figsize = (9,3))
##x = list(range(1,6))
####y = [randint(1,10) for i in range(5)]
##y = [2, 3, 6, 1, 7]
##plt.plot(x,y)
##plt.show()


### os.path.getsize method
##
##
##import os
##
##
##files = os.listdir()
##
##for file in files:
##    size = os.path.getsize(file)
##    print('{} -- {} {}'.format(file,size, 'bytes'))


### pygame KEYDOWN


##import pygame 
##
##pygame.init()
##
##white = (255,255,255)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##move_x,move_y = 200,200 #ADD x,y
##change_x, change_y = 0,0 #ADD change
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##
##while window:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            window = False
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                change_x -= 5
##            if event.key == pygame.K_RIGHT:
##                change_x += 5
##    move_x += change_x               
### add
##    surface.fill(white)
##    surface.blit(python,(move_x,move_y)) # change
##    win.update()
##
##pygame.quit()


### itertools islice
##
##
##
##from itertools import islice as slice
##
##
##students = ['tom', 'pete', 'sam', 'john', 'paul','matt']
##
##group_1 = slice(students,0,len(students),2)
##
##group_2 = slice(students,1,len(students),2)


### matplotlib figure and axis
##
##
##from  matplotlib import pyplot as plt
##
##
##plt.figure('my graph',figsize = (10,5))
##
##x = list(range(1,6))
##y = [0,3,4,7,11]
##plt.axis([0,7,0,12])
##plt.plot(x,y)
##
##plt.show()


### os scandir DirEntry object
##
##
##import os
##
##
##x = os.scandir()
##
##for i in x:
##    print(i)
##    


### pygame time clock tick/ fps
##
##
##import pygame 
##
##pygame.init()
##
##white = (255,255,255)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##move_x,move_y = 200,200 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()# Add clock
##while window:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            window = False
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                change_x -= 5
##            if event.key == pygame.K_RIGHT:
##                change_x += 5
##    move_x += change_x               
##
##    surface.fill(white)
##    surface.blit(python,(move_x,move_y)) 
##    win.update()
##    clock.tick(30)# add tick 
##pygame.quit()


#### itertools product
##
##from itertools import product
##
##for i in product('ab', range(3)):
##    print(i)
##    
##
##for i in product((0,1),(0,1),(0,1)):
##    print(i)
##
##
##for i in product("A", repeat=3):
##    print(i)


### matplotlib pyplot line style
### and markers
##
##
##from matplotlib import pyplot as plt
##
##
##plt.figure(1,figsize = (8,6))
##x = list(range(1,6))
##y = [0,3,5,7,11]
##plt.axis([0,6,0,12])
##plt.plot(x,y,'g-.')
##
##plt.show()


### sys getsizeof
##
##
##import sys
##
##
##x = 4
##
##y = [i*i for i in range(100)]
##
##print(sys.getsizeof(x))
##print(sys.getsizeof(y))


### deep dive into generators
##
##
##from time import time
##from random import randint,seed
##from sys import getsizeof as get
##start = time()
##seed(1)
##new = [randint(0,10) for i in range(500000)]
##x = [i*i for i in new]
##end = time()
##print(end-start)
##print(get(x))
##
##start = time()
##new = []
##seed(1)
##for i in range(500000):
##    new.append(randint(0,10))
##x = []
##for i in new:
##    x.append(i*i)
##
##end = time()
##print(end-start)
##print(get(x))
##
##start = time()
##seed(1)
##new = (randint(0,10) for i in range(500000))
##x = (i*i for i in new)
##end = time()
##print(end-start)
##print(get(x))


### slash back and/or forward
##
##f = open('c:/users/samue/shopping_list.txt')
##


### os.path join
##
##
##import os
##
##files = os.listdir()
##
##now = os.getcwd()
##
##for file in files:
##    print(os.path.join(now,file))


### pygame KEYUP, K_UP AND K_DOWN
##
##import pygame 
##
##pygame.init()
##
##white = (255,255,255)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##move_x,move_y = 200,200 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##while window:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            window = False
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                change_x -= 5
##            if event.key == pygame.K_RIGHT:
##                change_x += 5
##            if event.key == pygame.K_UP:
##                change_y += -5
##            if event.key == pygame.K_DOWN:
##                change_y += 5
##        if event.type == pygame.KEYUP:
##            change_x = 0# add
##            change_y = 0
##        
##    move_x += change_x
##    move_y += change_y
##    surface.fill(white)
##    surface.blit(python,(move_x,move_y)) 
##    win.update()
##    clock.tick(30)
##pygame.quit()


### itertools cycle
##
##
##import itertools
##
##
##students = ['matt','steve','bob','sam','john','joe']
##
##num = itertools.cycle(range(1,3))
##
##
##team = [(next(num), student) for student in students]
##
##print(team)


### matplotlib pyplot grid
##
##from matplotlib import pyplot as plt
##
##
##plt.figure(1,figsize = (8,6))
##plt.grid()
##x = list(range(1,6))
##y = [0,3,5,7,11]
##plt.axis([0,6,0,12])
##plt.plot(x,y,'rs')
##
##plt.show()


###os walk method
##
##
##import os 
##
##
##import os
##from os.path import join, getsize
##for root, dirs, files in os.walk('C:\\Users\\samue\\AppData\\Local\\Programs\\Python\\Python36-32'):
##    print(root, "consumes", end=" ")
##    print(sum([getsize(join(root, name)) for name in files]), end=" ")
##    print("bytes in", len(files), "non-directory files")


##
##import pygame 
##
##pygame.init()
##
##white = (255,255,255)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##move_x,move_y = 200,200 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##while window:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            window = False
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                change_x -= 5
##            if event.key == pygame.K_RIGHT:
##                change_x += 5
##            if event.key == pygame.K_UP:
##                change_y += -5
##            if event.key == pygame.K_DOWN:
##                change_y += 5
##        if event.type == pygame.KEYUP:
####            change_x = 0
####            change_y = 0
##            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
##                change_y = 0
##            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
##                change_x = 0# add
##    move_x += change_x
##    move_y += change_y
##    surface.fill(white)
##    surface.blit(python,(move_x,move_y)) 
##    win.update()
##    clock.tick(30)
##pygame.quit()


# sys.argv deep dive


##import sys
##
##
##
####for item in sys.argv:
####    
####    print(item)
####print(sys.argv)
##    
##
##
### 0 1 2 3 4 
##
##
##
##print(sys.argv[1])


# help prompt


# itertools repeat method
##
##import itertools
##
##
##x = itertools.repeat(10)
##

### matplotlib pyplot scatter
##
##
##from matplotlib import pyplot as plt
##from random import randint as rand
##
##
##h = [rand(60,78) for i in range(20)]
##
##w = [rand(150,350) for i in range(20)]
##
##plt.scatter(h,w)
##
##plt.show()
##
##


# Nth prime 1000 views


# attributes what are they


##import math

##class rect():
##    
##    def __init__(self,length,width):
##        self.length = length
##        self.width = width
##        print("Your rectangle is {} by {}".format(length,width))


### os stat
##
##import os
##
##
##f = os.stat('shopping_list.txt')


### pygame multipule keyup events
##
##import pygame 
##
##pygame.init()
##
##white = (255,255,255)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##move_x,move_y = 200,200 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##while window:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            window = False
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                change_x -= 5
##            if event.key == pygame.K_RIGHT:
##                change_x += 5
##            if event.key == pygame.K_UP:
##                change_y += -5
##            if event.key == pygame.K_DOWN:
##                change_y += 5
##        if event.type == pygame.KEYUP:
##            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
##                change_y = 0
##            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
##                change_x = 0
##        
##    move_x += change_x
##    move_y += change_y
##    surface.fill(white)
##    surface.blit(python,(move_x,move_y)) 
##    win.update()
##    clock.tick(30)
##pygame.quit()


# itertools zip_longest


##import itertools
##
##
##students = ['john','sam','matt', 'tom']
##
##grades = [89,90,79]
##
##
##roll = list(itertools.zip_longest(students,grades,fillvalue= 0))


### matplotlib pyplot
##
###multiple scatter
##
##
##from matplotlib import pyplot as plt
##from random import randint as rand
##
##b_h = [rand(50,78) for i in range(20)]
##b_w = [rand(150,350) for i in range(20)]
##
##g_h = [rand(44,72) for i in range(20)]
##g_w = [rand(85,180) for i in range(20)]
##
##plt.scatter(b_h,b_w)
##plt.scatter(g_h,g_w)
##
##plt.show()
##


### os rename method


##import os
##
##
####os.mkdir('new')  # ep 264
##
##
##os.rename('new','old')
##
##
### pygame font
##
##
##import pygame


### builtin pow function
##
##
##
##def square(x):
##    return pow(x,2)
##
##print(square(3))

##
### itertools starmap
##
##
##import itertools
##
##x = [(2,2),(2,3),(10,4)]
##
##
##new = itertools.starmap(pow,x)


###pop quiz extend/append
##
##
##x = [2,3,4]
##
##
##y =[3,5]
##

##
###matplotlib pyplot legend and label 
##
##
##from matplotlib import pyplot as plt
##from random import randint as rand
##
##b_h = [rand(50,78) for i in range(20)]
##b_w = [rand(150,350) for i in range(20)]
##
##g_h = [rand(44,72) for i in range(20)]
##g_w = [rand(85,180) for i in range(20)]
##
##plt.scatter(b_h,b_w, label = 'Boys')
##plt.scatter(g_h,g_w, label = 'Girls')
##
##plt.legend()
##
##plt.show()
##


### os.path splitext 
##
##
##import os
##
##files = os.listdir()
##
##for file in files:
##    print(os.path.splitext(file))
    

# bulit-in functions


### pygame.font get_fonts method
##
##
##import pygame


### itertools permutaions method
##
##
##import itertools
##
##
##x = itertools.permutations(range(4),2)
##
##print(list(x))


### return or **in place**
##
##
##x = [4,3,8,1]


###pop quiz extend/append
##
##
##x = [2,3,4]
##
##y =[3,5]


### __repr__ method 
##
##
### prerequisite class ep 207-209  underscore 190 format 186
##
##
##class rect():
##    
##    def __init__(self,length,width):
##        self.length = length
##        self.width = width
##
##    def __repr__(self):
##        return "rect({self.length},{self.width})".format(self=self)
##    
##    def perim(self):
##        return 2*(self.length+self.width)
##        
##    def area(self):
##        return self.length*self.width


### matplotlib legend location
##
##
##from matplotlib import pyplot as plt
##from random import randint as rand
##
##b_h = [rand(50,78) for i in range(20)]
##b_w = [rand(150,350) for i in range(20)]
##
##g_h = [rand(44,72) for i in range(20)]
##g_w = [rand(85,180) for i in range(20)]
##
##plt.scatter(b_h,b_w,label= 'boys')
##plt.scatter(g_h,g_w,label= 'girls')
##
##plt.legend(loc = 8)
##
##plt.show()
##


### video request triangle
##
##'''
##      1         1 - 0 - 1
##    2 2 2       2 - 1 - 3 
##  3 3 3 3 3     3 - 2 - 5
##4 4 4 4 4 4 4   4 - 3 - 7
##'''
##
##x = 5
##
##for i in range(1,x+1):
##    print('  ' * (x-i), end = '')
##    for j in range(i*2-1):
##        print(i, end = ' ')
##    print()


### os.path abspath
##
##
##import os


### built-in repr function
##
### 190 double underscore
### 207 209 class
### eval
##
##class rect():
##    
##    def __init__(self,length,width):
##        self.length = length
##        self.width = width
##
##    def __repr__(self):
##        return "rect({self.length},{self.width})".format(self=self)
##    
##    def perim(self):
##        print(2*self.length*self.width)
##        return 2*(self.length+self.width)
##        
##    def area(self):
##        print(self.length*self.width)
##        return self.length*self.width
##


##### pygame.font SysFont Function Font Object
##
### ep 275 deep dive dir help
##
##import pygame
##
##
##pygame.init()
##
##text = pygame.font.SysFont('timesnewroman', 20)


### itertools dropwhile method ep 126 lambda
##
##
##from itertools import dropwhile as drop
##from random import shuffle
##
##
##y = [('sam',4.1),('john',4.3),('steve',4.4),('matt',4.45),('tom',4.9)]
##
##shuffle(y)
##print(y)
##check = drop(lambda x: x[1] < 4.5,y)
##
##print(list(check))


#### comment/uncomment and restart
##
##
##for i in range(1000):
##    print(i)


#### __str__ method 
###
#### prerequisite class ep 207,208,209  underscore 190 string format 186
###
##class rect():
##    
##    def __init__(self,length,width):
##        self.length = length
##        self.width = width
##
##    def __repr__(self):
##        return "rect({self.length},{self.width})".format(self=self)
##
##    def __str__(self):
##        return "Your rectangle is {} by {}".format(self.width,self.length)
##    
##    def perim(self):
##        print(2*self.length*self.width)
##        return 2*(self.length+self.width)
##        
##    def area(self):
##        print(self.length*self.width)
##        return self.length*self.width


### matplotlib pyplot title function
##
##import matplotlib.pyplot as plt
##
##
##from matplotlib import pyplot as plt
##from random import randint as rand
##
##b_h = [rand(50,78) for i in range(20)]
##b_w = [rand(150,350) for i in range(20)]
##
##g_h = [rand(44,72) for i in range(20)]
##g_w = [rand(85,180) for i in range(20)]
##
##plt.scatter(b_h,b_w,label= 'boys')
##plt.scatter(g_h,g_w,label= 'girls')
##
##plt.legend()
##plt.title('Boys and Girls height and weight')
##plt.show()
##
##
### os.path split method
##
### ep 325 os.path.abspath
##
##import os
##f = os.path.abspath('ideas.py')

### pop quiz pygame 
##
##
##import pygame
##
##
### ? what is missing ?
##
##
##text = pygame.font.SysFont('timesnewroman', 20)
##
### itertools tee method
##
##import itertools
##
##x = [1,2,3]
##
##z = itertools.tee(x,3)
##
##for i in z:
##    for j in i:
##        print(j)
##        
### matplotlib pyplot text method
##
##from matplotlib import pyplot as plt
##
##
##plt.scatter(5,5)
##plt.text(5.00005,5.0005, 'HERE')
##plt.show()
##

### os.path dirname method
##
##import os
##
##f = os.path.abspath('ideas.py')
##
####base, file = os.path.split(f)
##
##base = os.path.dirname(f)
##
### find current variables dir()
#
##import itertools
##
##x = [1,2,3]
##
##z = itertools.tee(x,3)
##
##for i in z:
##    for j in i:
##        print(j)
##        


### pop quiz #2 pygame 
##
##
##import pygame
##
##
##pygame.init()
##
##
##text = pygame.font.SysFont('timesnewroman', 20)


### font render method
##
##
##import pygame 
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##move_x,move_y = 200,200 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##while window:
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,black)
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            window = False
##
##
##    surface.fill(white)
##    surface.blit(text,(300,400))
##    win.update()
##    clock.tick(30)
##pygame.quit()


### zipfile
##
##
##import zipfile


### zipfile is_zipfile Method
##
##
##
##import zipfile
##from urllib.request import urlretrieve as retrieve
##
##
##address = 'https://www.ssa.gov/oact/babynames/state/namesbystate.zip'
##
##retrieve(address, 'names.zip')


#  16000 views


### itertools groupby method
##
##
##import itertools 
##
##
##x = 'aaaabbbccd'
##
##new = list(itertools.groupby(x))


### matplotlib pyplot figure object
##
##
##from matplotlib import pyplot as plt
##


# pandas and numpy


### os.path basename method
##
##
##import os
##
##
##f = os.path.abspath('ideas.py')
##
##
##print(os.path.basename(f))


### pop quiz #3
##
##
### loop through lists simultaneously
##
##
##cars = ['sudan','van','truck','race car']
##
##engine = ['v4','i6','v8','f12']


### pygame.draw module
##
##
##
##import pygame


# numpy and pandas


### pop quiz #3 answer
##
##
### loop through lists simultaneously
##
##
##cars = ['sudan','van','truck','race car']
##
##engine = ['v4','i6','v8','f12']
##
##for i,car in enumerate(cars):
##    print(car,engine[i])
##
##
####for i in zip(cars,engine):
####    print('{} {}'.format(i[0],i[1]))
##
####for i in range(len(cars)):
####    print('{} {}'.format(cars[i],engine[i]))


### re module part 3 special .
##
##import re
##
##x = ['mop', 'top', 'hop', 'and', 'bob']
##
##expr = '.o.'
##
##for i in x:
##    print(re.findall(expr,i))


### search parameters using [ ]
##
##
####import glob
####
####
####files = glob.glob('[k-o]*.*')
####
##
##for i in files:
##    print(i)


### itertools groupby method pt 2
##
##
##import itertools 
##
##
##x = 'aaaabbbccd'
##
##
##new = itertools.groupby(x)
##
####new = [list(g) for k,g in new]
##
##
##letter_count = {letter[0]: len(list(letter[1])) for letter in new}
##
##


### matplotlib subplots
##
##
##from matplotlib import pyplot as plt
##
##
##fig = plt.figure()
##
##
##figure, axes = plt.subplots(figsize=(5,4))
##
##plt.scatter(5,5)
##
##plt.show()
##


###  path join on new file
##
##
##import os
##
##now = os.getcwd()
##
##new = os.path.join(now,'blank.txt')
##
##f = open(new,'w')
##
##f.close()


##import pygame
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##move_x,move_y = 200,200 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##while window:
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,black)
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            window = False
##
##
##    
##    surface.fill(white)
##    surface.blit(text,(300,400))
##    pygame.draw.circle(surface,black,(200,200),50,10)
##    win.update()
##    clock.tick(30)
##pygame.quit()


### zipfile ZipFile Method
##
##
##
##import zipfile
##
##
##zip_file = 'names.zip'
##
##
##zip_archieve = zipfile.ZipFile(zip_file,'w')
##
##
### re findall Method
##
##
##import re
##
##
##with open('raven.txt') as file:
##    text = file.read()
##
##    
##the = re.findall('the',text)
##
##print(the)


### glob iglob method
##
##
##import glob
##
##files = glob.iglob('*.*')


### itertools groupby method pt. 3
##
##
##import itertools
##
##
##grades = [85,90,100,85,90,80]
##
##grades = itertools.groupby(sorted(grades))
##
##count_grades = {grade[0]:len(list(grade[1])) for grade in grades}
##
##print(count_grades)

# 250 subs

### matplotlib multiple plots
##
##
##from matplotlib import pyplot as plt
##
##
####figure = plt.figure()
##
##fig,axes  = plt.subplots(2,2,figsize=(5,4))
##
##
##plt.show()


### os.path isdir method 
##
##
##import os
##
##
##old_dir = os.getcwd()
##
##print(os.path.isdir(old_dir+'\\names'))


### center text/object
### thickness of line
##
##import pygame
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##move_x,move_y = 200,200 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##while window:
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,black)
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            window = False
##
##    surface.fill(white)
##    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.circle(surface,black,(x//2,y//2),50,1)
##    win.update()
##    clock.tick(30)
##pygame.quit()


### zipfile extractall method
##
##
##import zipfile,os
##
##
##zip_file = 'names.zip'
##
##
##zip_archive = zipfile.ZipFile(zip_file,'r')
##
##names = os.path.join(os.getcwd()+'\\names')
##
##zip_archive.extractall(names)


### re brackets [] more the one letter
##
##
##import re  
##
##with open('raven.txt') as file:
##    text = file.read()
##
##the = re.findall('[Tt]he',text)
##
##print(the)


### glob under the hood
##
##
##import glob


### zipfile extract method
##
##
### prerequisites:
### zipfile.zipfile
### namelist method
##
##import zipfile,os
##
##zip_file = 'names.zip'
##
##zip_archive = zipfile.ZipFile(zip_file,'r')
##
##hi_folder = os.path.join(os.getcwd()+'\\hi')
##
##zip_archive.extract('HI.TXT',hi_folder)


### plt.subplots deep dive 
##
##from matplotlib import pyplot as plt
##
##
##fig,axes = plt.subplots(figsize=(5,4))
##
##
##plt.show()
##


##
### f string 
##
##
##x = 'Sam'
##
##
####print('Hi my name is {}.'.format(x))
##
##print(f'Hi my name is {x}.')
##
##
### numpy intro
##
##
##import numpy as np


### pandas intro
##
##
##import pandas as pd
##

### itertools
### combinations with replacement
##
##
##from itertools import combinations_with_replacement as comb
##
##num = list(range(5))
##
##x = comb(num,3)
##
##y = [i for i in x]
##
##print(y)


# thank you around the world


### matplotlib subplot adjust method
##
##
##from matplotlib import pyplot as plt
##
##fig,axes  = plt.subplots(1,3,figsize=(5,4))
##
##fig.subplots_adjust(wspace=.5)
##
##plt.show()


### Epoch time what is it?
##
### time gmtime method
##
##
##import time


### time ctime method
##
##
##import time
##
##
##print(time.ctime(10))


### os.path get a time method
##
##
##import os,time
##
##last = os.path.getatime('shopping_list.txt')
##
##
##print(time.ctime(last))


### Requested builtins module
##
##
##import builtins


### pygame.mouse get_pos method
##
##
##import pygame
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##move_x,move_y = 200,200 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##while window:
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,black)
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            window = False
##
##    surface.fill(white)
##    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.circle(surface,black,(x//2,y//2),50,1)
##    movement = pygame.mouse.get_pos()
##    print(movement)    
##    win.update()
##    clock.tick(30)
##pygame.quit()


### pandas read_csv method
##
##
##
##import pandas as pd
##
##import os
##
##
##current = os.getcwd()
##
##file = current + '\\hi\\HI.txt'
##
##hi = pd.read_csv(file)


### re findall search for dates
##
##
##import re  
##
##with open('raven.txt') as file:
##    text = file.read()
##
##
##date = re.findall('[1][8-9][0-9][0-9]',text)
##
##print(date)


# have code downloadable


### numpy array method
##
##
##import numpy as np
##
##table = np.array(range(10))
##
##print(table)


### fnmatch fnmatch method  
##
##
##import fnmatch, os
##
##current = os.listdir()
##
##for file in current:
##    if fnmatch.fnmatch(file,'*.txt'):
##        print(file)
##    else:
##        print(file)


### itertools filter false
##
##
##import itertools
##
##
##x = list(range(11))
##
##y = itertools.filterfalse(lambda i:i%2==0,x)
##
##for i in y:
##    print(i)
##

### matplotlib pyplot pie chart
##
##
##from matplotlib import pyplot as plt
##
##
##languages = ['python','everything else']
##
##percent = [99,1]
##
##
##plt.pie(percent,labels=languages)
##
##plt.show()
##


### os.path ntpath
##
##
##
##import os,ntpath
##
##


### pandas DataFrame head method
##
##
##import pandas as pd
##
##import os
##
##
##current = os.getcwd()
##
##file = current + '\\hi\\HI.txt'
##
##hi = pd.read_csv(file)




##import pygame # MOUSEDOWN
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##move_x,move_y = 200,200 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##
##while window:
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,black)
##    for event in pygame.event.get():
##        # moved here
##        if event.type == pygame.QUIT:
##            window = False
##        if event.type == pygame.MOUSEBUTTONDOWN:
##            click += 1
##            print(click)
##          #
###
##    surface.fill(white)
##    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.circle(surface,black,(x//2,y//2),50,1)
##    movement = pygame.mouse.get_pos()
##    win.update()
##    clock.tick(30)
##pygame.quit()


# 400  !!!!!!!!!!!!!!!!!!


#### numpy reshape method  
##
##import numpy as np
##
##table = np.array(range(10))


# Deep Dive re fnmatch glod


##import glob
##
##
##files = glob.glob('[k-o]*.*')
##
##
##for i in files:
##    print(i)


##import fnmatch, os
##
##current = os.listdir()
##
##for file in current:
##    if fnmatch.fnmatch(file,'*.txt'):
##        print(file)
##
##
### re findall dates w/ {}  
##
##
##import re  
##
##with open('raven.txt') as file:
##    text = file.read()
##
##date = re.findall('[1][8-9][0-9]{2}',text)
##
##print(date)


# itertools takewhile


##import itertools
##
##
##x = [1,4,4,1,5,6]
##
##y = itertools.takewhile(lambda i:i<6,x)
##
##for i in y:
##    print(i)


### fnmatch filter 


##import fnmatch,os
##
##current = os.listdir()
##
####for file in current:
####    if fnmatch.fnmatch(file,'*.txt'):
####        print(file)
##
##
##y = fnmatch.filter(current,'*.txt')


### matplotlib pie chart advance
##
##
##from matplotlib import pyplot as plt
##
##languages = ['python','everthing else']
##percent = [99.0,1.0]
##explode = (0,.1)
##
##fig,ax = plt.subplots()
##
##
##ax.pie(percent,labels=languages,autopct='%1.1f%%',
##       explode=explode,startangle=90)
##
##
##plt.show()
##


##import pygame,random # MOUSEDOWN postition
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##move_x,move_y = 200,200 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##colors = [white,black,red,blue,green]
##fill = white
##while window:
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,black)
##    for event in pygame.event.get():
##        c_x,c_y = pygame.mouse.get_pos()
##        if event.type == pygame.QUIT:
##            window = False
##        if event.type == pygame.MOUSEBUTTONDOWN:
##            if ((300-c_x)**2+(400-c_y)**2) < 2500:
##                fill = random.choice(colors)
##        
##          #
###
##    surface.fill(fill)
##    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.circle(surface,black,(x//2,y//2),50,1)
##    movement = pygame.mouse.get_pos()
##    win.update()
##    clock.tick(30)
##pygame.quit()


### ntpath get m time
##
##import ntpath,time
##
##
##last = ntpath.getmtime('shopping_list.txt')
##
##print(time.ctime(last))

##
##import pandas as pd
##
##import os
##
##current = os.getcwd()
##
##file = current + '\\hi\\HI.txt'
##
##col = ['State','Gender','Year','Name','Count']
##
##hi = pd.read_csv(file,header=None)


### numpy increment array
##
##
##import numpy as np
##
##table = np.array(range(10))
##
##table = table.reshape(2,5)
##
##print(table)


### * splat and iterator
##
##
##
##import itertools 
##
##x = [1,4,4,1,5,6]
##
##y = itertools.takewhile(lambda i: i<6,x)
##
##

### re \w character
##
##
##import re  
##
##with open('raven.txt') as file:
##    text = file.read()
##
##word = re.findall('\w+ \w+',text)
##
##print(word)


### reversed built-in function
##
##
##name = "Samuel"
##
##rev = reversed(name)


### tkinter module 
##
##
##
##import tkinter
##
##

### matplotlib fig savefig
##
##
##from matplotlib import pyplot as plt
##import os
##
##languages = ['python','everthing else']
##percent = [99.0,1.0]
##explode = (0,.1)
##
##fig,ax = plt.subplots()
##
##
##ax.pie(percent,labels=languages,autopct='%1.1f%%',
##       explode=explode,startangle=90)
##
##
##plt.show()
##
##current = os.getcwd()
##
##fig.savefig(current+'\pie.png')



# django ?


### ntpath commonpath function
##
##
##
##import ntpath
##
##
##file1 = 'C:\\Users\\samue\\AppData\\Local\\Programs\\Python\\Python36-32'
##file2 = 'C:\\Users\\samue'
##file3 = 'C:\\Users\\samue\\AppData'
##
##
##base = ntpath.commonpath([file1,file2,file3,])
##
##print(base)


##import pygame,random # circle move
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##move_x,move_y = 0,0 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##colors = [white,black,red,blue,green]
##fill = white
##text_color = black
##circle_x,circle_y = x//2,y//2
##while window:
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,text_color)
##    for event in pygame.event.get():
##        c_x,c_y = pygame.mouse.get_pos()
##        if event.type == pygame.QUIT:
##            window = False
##        if event.type == pygame.MOUSEBUTTONDOWN:
##            if ((300-c_x)**2+(400-c_y)**2) < 2500:
##                text_color = white
##                move_x,move_y = random.randint(-20,20),random.randint(-20,20)
####                fill = random.choice(colors)
##    circle_x += move_x
##    circle_y += move_y
##          #
###
##    surface.fill(fill)
##    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.circle(surface,black,(circle_x,circle_y),50,1)
##    movement = pygame.mouse.get_pos()
##    win.update()
##    clock.tick(30)
##pygame.quit()
##


### pandas 
##
##
##import pandas as pd
##
##import os
##
##current = os.getcwd()
##
##file = current + '\\hi\\HI.txt'
##
##col = ['State','Gender','Year','Name','Count']
##
##hi = pd.read_csv(file,names=col)
##


### numpy arange function
##
### and shape attribute
##
##
##import numpy as np
##
####table = np.array(range(10))
####
####table = table.reshape(2,5)
##
####table = np.arange(10).reshape(2,5)
##
##table = np.arange(10)
##
##print(table)
##


### create a window w/ tkinter.Tk()
##
##
##import tkinter
##
##
##tkinter.Tk()


### re findall $XX.XX dollar amounts
##
##
##import re
##
##ad = 'Tvs for $349.99 and microwaves for $39.99'
##
##print(re.findall('\$\d+\.\d*',ad))


### plot a pandas series w/ pyplot
##
##
##import pandas as pd
##
##from matplotlib import pyplot as plt
##
##col = ['State','Gender','Year','Name','Count']
##
##hi = pd.read_csv('C:\\Users\\samue\\.spyder-py3\\hi\\hi.txt',names=col)
##
##plt.hist(hi['Year'])
##
##plt.show()


##
### sys.argv  --->  fileinput module
##
##
##
##import fileinput


### sys exit method
##
##
##import pygame,random,sys # circle move
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##move_x,move_y = 0,0 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##colors = [white,black,red,blue,green]
##fill = white
##text_color = black
##circle_x,circle_y = x//2,y//2
##while window:
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,text_color)
##    for event in pygame.event.get():
##        c_x,c_y = pygame.mouse.get_pos()
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit()            
####            window = False
##        if event.type == pygame.MOUSEBUTTONDOWN:
##            if ((300-c_x)**2+(400-c_y)**2) < 2500:
##                text_color = white
##                move_x,move_y = random.randint(-20,20),random.randint(-20,20)
##                fill = random.choice(colors)
##    circle_x += move_x
##    circle_y += move_y
##  
###
##    surface.fill(fill)
##    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.rect(surface,black,(5,5,590,790),3)
##    pygame.draw.circle(surface,black,(circle_x,circle_y),50,1)
##    movement = pygame.mouse.get_pos()
##    win.update()
##    clock.tick(30)


###pandas DataFrame sort_values method
##
##import pandas as pd
##
##
##col = ['State','Gender','Year','Name','Count']
##
##hi = pd.read_csv('C:\\Users\\samue\\.spyder-py3\\hi\\Hi.txt',names=col)
##
##hi_female_names = hi[hi['Gender'] == 'F']
##
##hi_male_names = hi[hi['Gender'] == 'M']


##
### numpy / random
##
##
##
##import numpy as np
####import random
##
##x = np.arange(12)
###random.shuffle(x)
##np.random.shuffle(x)
##x.shape = 3,4
##print(x)
##


### re findall email  
##
##import re
##
##email = ''' List of email address:
##stev@company.com
##matt@company.com
##john@company.com
##@5pm Tuesday
##
##tom@house.gov
##jon@cia.gov
##
##'''
##
##print(re.findall('\w+@\w+\.gov',email))
##

### tkinter mainloop method
##
##
##import tkinter
##
##win = tkinter.Tk()
##
##
##win.mainloop()


### built-in filter function
##
##
##
##import string
##
##letters = string.ascii_letters
##
##
##cons = filter(lambda i:i.lower() not in 'aeiou',letters)
##
##vowels = filter(lambda i:i.lower() in 'aeiou',letters)
##
##
##
### intro to pickling(pickle)

##
##import pickle


### title multiple plots matplotlib
##
##
##
##from matplotlib import pyplot as plt
##
##fig, axes = plt.subplots(2,2,figsize=(8,6))
##
##axes[0,0].set_title('1')
##axes[0,1].set_title('2')
##axes[1,0].set_title('3')
##axes[1,1].set_title('4')
##plt.show()
##

### relative/ absolute path
##
##
##d = 'C:\\Users\\samue\\AppData\\Local\\Programs\\Python\\Python36-32'
##
##hi = '\\names\\hi.txt'
##

##import pygame,random,sys # circle move
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##move_x,move_y = 0,0 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##colors = [white,black,red,blue,green]
##fill = white
##text_color = black
##circle_x,circle_y = x//2,y//2
##while window:
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,text_color)
##    for event in pygame.event.get():
##        c_x,c_y = pygame.mouse.get_pos()
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit()            
####            window = False
##        if event.type == pygame.MOUSEBUTTONDOWN:
##            if ((300-c_x)**2+(400-c_y)**2) < 2500:
##                text_color = white
##                move_x,move_y = random.randint(-20,20),random.randint(-20,20)
####                fill = random.choice(colors)
##    circle_x += move_x
##    circle_y += move_y
##    if circle_x < 55 or circle_x > 545:
##        move_x = -move_x
##        
##    if circle_y < 55 or circle_y > 745:
##        move_y = -move_y
##        
##
###
##    surface.fill(fill)
##    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.rect(surface,black,(5,5,590,790),3)
##    pygame.draw.circle(surface,black,(circle_x,circle_y),50,1)
##    movement = pygame.mouse.get_pos()
##    win.update()
##    clock.tick(30)


### pandas DataFrame groupby method
##
##
##
##import pandas as pd
##
##
##col = ['State','Gender','Year','Name','Count']
##
##hi = pd.read_csv('C:\\Users\\samue\\.spyder-py3\\hi\\Hi.txt',names=col)
##

### numpy array flatten method
##
##import numpy as np
##
##x = np.arange(12).reshape(4,3)
##
##x = x.flatten()
##
##np.random.shuffle(x)
##x.shape = (4,3)
##print(x)


### pickle dump method
##
##
##import pickle as pkl
##import pandas as pd
##
##
##col = ['State','Gender','Year','Name','Count']
##
##hi = pd.read_csv('C:\\Users\\samue\\.spyder-py3\\hi\\Hi.txt',names=col)
##
##hi_female_names = hi[hi['Gender'] == 'F']
##
##hi_male_names = hi[hi['Gender'] == 'M']
##
##
##file_name = "boy_names.pkl"
##
##file = open(file_name,'wb')
##pkl.dump(hi_male_names,file)
##file.close()


### delimiter / sep
##
##
##sen = """hello everyone nice 
##to see you
##again it has been too long.
##
##"""

### re | (or)
##
##import re
##
##with open('raven.txt') as file:
##    text = file.read()
##
##
##x = re.split('\.|\!|\?',text)
##
##
##print(x)


### tkinter title and size
##
##
##import tkinter
##
##win = tkinter.Tk()
##
##win.title("Window")
##
##win.configure(width=300,height=300)
##
##win.mainloop()


### matplotlib super title method
##
##from matplotlib import pyplot as plt
##
##fig, axes = plt.subplots(2,2,figsize=(8,6))
##
##plt.suptitle("Super Title")
##
##axes[0,0].set_title('1')
##axes[0,1].set_title('2')
##axes[1,1].set_title('3')
##axes[1,0].set_title('4')
##
##plt.show()
##


### built-in float function
##
##
##def total():
##    x = float(input("Enter amount: "))
##    return x + 2

### intro pygame mixer module
##
##
##import pygame
##
##pygame.init()


### pandas dataframe info method
##
##
##
##import pandas as pd
##
##
##col = ['State','Gender','Year','Name','Count']
##
##hi = pd.read_csv('C:\\Users\\samue\\.spyder-py3\\hi\\Hi.txt',names=col)
##
##hi_female_names = hi[hi['Gender'] == 'F']
##
##hi_male_names = hi[hi['Gender'] == 'M']
##
##total_birth_year = hi.groupby("Year").Count.sum()


###  pickle load method
##
##
##
##import pickle as pkl
##
##
##file_name = 'boy_names.pkl'
##
##file = open(file_name,'rb')
##
##boy_names = pkl.load(file)
##
##file.close()


### print sep 
##
##
##f = 'john'
##
##l = 'doe'
##
##m = 'steve'
##
##
##
##print(f,m,l)


### tkinter Label Module
##
##
##import tkinter as tk


### class inheritance
##
##
##class Dog:
##
##    species = "K9"
##    voice = "bark"
##    
##class poodle(Dog):
##    pass


### import *
##
##
##from matplotlib import *
##
##


### DataFrame Tail method
##
##
##import pandas as pd
##
##
##col = ['State','Gender','Year','Name','Count']
##
##hi = pd.read_csv('C:\\Users\\samue\\.spyder-py3\\hi\\Hi.txt',names=col)
##
##hi_female_names = hi[hi['Gender'] == 'F']
##
##hi_male_names = hi[hi['Gender'] == 'M']


### last way to create random array
##
##
##import numpy as np
##
##
##x = np.random.randint(9,size=(3,3))
##
##print(x)


### collections intro module
##
##
##import collections


### pandas slicing w/ iloc
##
##import pandas as pd
##
##
##col = ['State','Gender','Year','Name','Count']
##
##hi = pd.read_csv('C:\\Users\\samue\\.spyder-py3\\hi\\Hi.txt',names=col)



### random image movement
##
##import pygame,random 
##
##pygame.init()
##
##white = (255,255,255)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##python_x,python_y = 200,200
##clock = pygame.time.Clock()
##while window:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            window = False
##    
##    surface.fill(white)
##    surface.blit(python,(python_x,python_y))
##    if event.type == pygame.MOUSEBUTTONDOWN:
##        python_x,python_y = random.randint(100,500),random.randint(100,700)
##    win.update()
##    clock.tick(10)
##
##pygame.quit()



### adding sound
##
##import pygame,random,sys 
##
##pygame.init()
##
##ball = 'ball.ogg'
##bounce = pygame.mixer.Sound(ball)
##
###
##white = (255,255,255)
##black = (0,0,0)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##move_x,move_y = 0,0 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##colors = [white,black,red,blue,green]
##fill = white
##text_color = black
##circle_x,circle_y = x//2,y//2
##
##while window:
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,text_color)
##    for event in pygame.event.get():
##        c_x,c_y = pygame.mouse.get_pos()
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit()            
####            window = False
##        if event.type == pygame.MOUSEBUTTONDOWN:
##            if ((300-c_x)**2+(400-c_y)**2) < 2500:
##                text_color = white
##                move_x,move_y = random.randint(-20,20),random.randint(-20,20)
####                fill = random.choice(colors)
##    circle_x += move_x
##    circle_y += move_y
##    if circle_x < 55 or circle_x > 545:
##        bounce.play()
##        move_x = -move_x
##        
##        
##    if circle_y < 55 or circle_y > 745:
##        bounce.play()
##        move_y = -move_y
##        
###
##    surface.fill(fill)
##    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.rect(surface,black,(5,5,590,790),3)
##    pygame.draw.circle(surface,black,(circle_x,circle_y),50,1)
##    movement = pygame.mouse.get_pos()
##    win.update()
##    clock.tick(30)


### pandas pickling
##
##
##import pandas as pd
##
##
##col = ['State','Gender','Year','Name','Count']
##
##hi = pd.read_csv('C:\\Users\\samue\\.spyder-py3\\hi\\Hi.txt',names=col)
##
##hi_female_names = hi[hi['Gender'] == 'F']
##
##hi_male_names = hi[hi['Gender'] == 'M']
##
##
##hi_names = hi.to_pickle('hi_name.pkl')
##
##del hi
##
##hi = pd.read_pickle('hi_names.pkl')


### os remove 
##
##
##import os




### numpy random uniform
##
##
##import numpy as np


### matplotlib colors
##
##
##from matplotlib import colors





#  nested list comprehension


##x = '01'
##y = 'AB'
##
##for i in x:
##    for j in y:
##        print(i+j)




### numpy full function
##
##
##import numpy as np


### matplotlib add baseline
##
##
##
##from matplotlib import pyplot as plt
##import numpy as np
##
##x = [10, 6, 9, 2, 5, 10, 10, 8, 2, 2, 6, 6, 3, 2, 10, 8, 6, 4, 10, 9]
##
##bins = list(range(11))
##
##plt.hist(x,bins=20)  
##
##plt.plot(bins,np.full(len(bins),2),linewidth=2,color='r')
##
##plt.xticks(bins)
##
##plt.show()


### pandas slicing w/ loc
##
##
##import pandas as pd
##
##
##col = ['State','Gender','Year','Name','Count']
##
##hi = pd.read_csv('C:\\Users\\samue\\.spyder-py3\\hi\\Hi.txt',names=col)


# Subscriber Feedback


# sql


### numpy transpose
##
##
##import numpy as np
##
##
##x = np.arange(12)
##np.random.shuffle(x)
##
##x.shape=(3,4)
##
##
##



# sql


##import sqlite3
##
##
##con = sqlite3.connect('students.db')
##
##
##con.close()


##import tkinter as tk
##
##
##win = tk.Tk()
##
##win.title("Window")
##
##win.configure(background = 'red')
##
##win.geometry('300x300')
##
##win.mainloop()


### matplotlib pyplot bar chart
##
##
##from matplotlib import pyplot as plt
##import numpy as np
##
##d = {'Carbohydrates': 12,
## 'Cholesterol': 0.015,
## 'Fat': 5,
## 'Protein': 9,
## 'Sodium': 0.13}
##
##
##group,amount = zip(*d.items())
##
##fig, ax = plt.subplots()
##
##plt.xticks(np.arange(len(group)),group,rotation=20)
##
##plot = ax.bar(np.arange(len(group)),amount,width=.5)
##
##plt.show()



### pygame Sprite Module
##
##
##import pygame



### matplotlib plots
##
##
##
##import numpy as np
##import matplotlib.pyplot as plt
##
##fig, ax = plt.subplots(figsize=(10,8))
##
##group = ['Fat','Cholesterol','Sodium','Carbohydrates','Protein']
##
##amount = [5,.015,.130,12,9]
##
##wrap = list(zip(amount,group))
##wrap = sorted(wrap,reverse=True)
##amount,group = zip(*wrap)
##
##plt.xticks(np.arange(len(group)),group,rotation=40)
##
##
##
###x = list(range(10))
###
###y = [np.random.randint(1,11) for i in range(10)]
##
##plot = ax.bar(np.arange(len(group)),amount,width=.5)
##
##
###plt.hist(y)
##
##
##plt.show()


### pandas dataframe describe method
##
##
##import pandas as pd
##
##col = ['State','Gender','Year','Name','Count']
##
##hi = pd.read_csv('C:\\Users\\samue\\.spyder-py3\\hi\\Hi.txt',names=col)
##
##hi_female_names = hi[hi['Gender'] == 'F']
##
##hi_male_names = hi[hi['Gender'] == 'M']
##
##total_birth_year = hi.groupby("Year").Count.sum()



### numpy colunm_stack function
##
##
##import numpy as np
##
##x = np.array([0, 22, 28, 17])
##
##y = np.array([14, 5, 9, 20])



### what is __main__ ?
##
##
####def main():
####    pass
##
##print(__name__)
##
##
##if __name__ == '__main__':
##    x = 1

##
### sqlite create a table
##
##
##import sqlite3
##
##
##con = sqlite3.connect('student.db')
##
##cur = con.cursor()
##
####cur.execute("""CREATE TABLE Student(
####first text,
####last text
####)
####
####""")
##
##cur.execute(''' insert into Student values('Sam','Focht')''')
##
##con.commit()
##con.close()
##con = sqlite3.connect('student.db')
##
##cur = con.cursor()
##cur.execute('''select * from Student''')
##
##print(cur.fetchmany())
##
##con.close()



### tkinter ttk
##
##
##import tkinter as tk
##import tkinter.ttk as ttk
##
##win = tk.Tk()
##
##win.title("Window")
##
##
##win.geometry('300x300')
##
##
##win.mainloop()




### matplotlib pyplot bar horizontal
##
##
##import numpy as np
##import matplotlib.pyplot as plt
##
##fig, ax = plt.subplots(figsize=(10,6))
##
##group = ['Fat','Cholesterol','Sodium','Carbohydrates','Protein']
##
##amount = [5,.015,.130,12,9]
##
##
##plt.yticks(np.arange(len(group)),group)
##
##plot = ax.barh(np.arange(len(group)),amount)
##
##plt.show()


### pygame sprite Group
##
##
##import pygame
##
##sprites = pygame.sprite.Group()



### pandas DataFrame transform and add
##
##
##import pandas as pd
##
##col = ['State','Gender','Year','Name','Count']
##
##hi = pd.read_csv('C:\\Users\\samue\\.spyder-py3\\hi\\Hi.txt',names=col)
##
##hi_female_names = hi[hi['Gender'] == 'F']
##
##hi_male_names = hi[hi['Gender'] == 'M']
##
##total_birth_year = hi.groupby("Year").Count.transform('sum')
##
##hi['births_year'] = total_birth_year
##
##hi['percent_of_births'] = (hi.Count / hi.births_year)*100
##
##
##print(hi)


### numpy 3d array
##
##
##import numpy as np
##
##table = np.array(range(30))
##
##table = table.reshape(3,2,5)
##
##print(table)


### insert data into table
##
##
##import sqlite3
##
##
##con = sqlite3.connect('student.db')
##
##cur = con.cursor()
##
####cur.execute("""create table students(
####        first text,
####        last text
####        
####        )"""
####            
####            )
##
####cur.execute('''
####      INSERT INTO Students VALUES ('John', 'Smith')
####      ''')
####
####con.commit()
##cur.execute('SELECT * FROM Students')
##
####con.commit()
##print(cur.fetchone())
##
##
##con.close()


### kivy App Class(object)
##
##
##import kivy
##
##from kivy.app import App






### tkinter ttk Label
##
##
##import tkinter as tk
##import tkinter.ttk as ttk
##
##
##win = tk.Tk()
##
##win.title("Window")
##
##win.geometry('300x300')
##
##label = ttk.Label(win,text='Hello World')
##
##label.pack()
##
##
##win.mainloop()






### matplotlib trick on one line
##
##
##import numpy as np
##import matplotlib.pyplot as plt
##
##
##
##mon = np.arange(1,13)
##
##y_2017 = [5,8,11,15,4,9,9,1,12,10,9,2]
##y_2018 = [7,12,13,17,4,10,11,2,14,12,9,6]
##
##plt.xticks(np.arange(1,13))
##
##
##plt.plot(mon,y_2017,mon,y_2018)
####plt.plot(mon,y_2018)
##
##plt.show()





#### pygame sprite.Sprite Object
##
##
##
##import pygame,random,sys
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##
##sprites = pygame.sprite.Group()
##
##class Block(pygame.sprite.Sprite):
##    def __init__(self,color,width,height):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((width,height))
##        self.image.fill(color)
##        self.rect = self.image.get_rect()
##        self.rect.x = x/2
##        self.rect.y = y/2
##
##block = Block(green,50,50)
##sprites.add(block)
##
##move_x,move_y = 0,0 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##colors = [white,black,red,blue,green]
##fill = white
##text_color = black
##circle_x,circle_y = x//2,y//2
##while window:
##    font = pygame.font.SysFont('timesnewroman', 20)
####    text = font.render('Start',0,text_color)
##    for event in pygame.event.get():
##        c_x,c_y = pygame.mouse.get_pos()
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit()            
##            window = False
##        if event.type == pygame.MOUSEBUTTONDOWN:
##            if ((300-c_x)**2+(400-c_y)**2) < 2500:
##                text_color = white
##                move_x,move_y = random.randint(-20,20),random.randint(-20,20)
##                fill = random.choice(colors)
##    circle_x += move_x
##    circle_y += move_y
##    if circle_x < 55 or circle_x > 545:
##        move_x = -move_x
##        
##    if circle_y < 55 or circle_y > 745:
##        move_y = -move_y
##        
##
###
##    surface.fill(fill)
####    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.rect(surface,black,(5,5,590,790),3)
####    pygame.draw.circle(surface,black,(circle_x,circle_y),50,1)
##    movement = pygame.mouse.get_pos()
##    sprites.update()
##    sprites.draw(surface)
##    win.update()
##    clock.tick(30)



##### pandas.read_excel skiprow
####
####
####from urllib.request import urlretrieve
##import pandas as pd
##
#####url = 'https://www.ers.usda.gov/webdocs/DataFiles/48747/Unemployment.xls?v=9115.7'
######urlretrieve(url, 'unemployment.xls')
####
####
##df = pd.read_excel('unemployment.xls', skiprows=7)
##
##pd.set_option('display.max_columns', 999)
#


### numpy ones and zeros
##
##
##
##import numpy as np
##
##
##x = np.ones((2,3))
##
##y = np.zeros(5)
##
##print(x,y)


### splite SELECT
##
##import sqlite3
##
##
##con = sqlite3.connect('student.db')
##
##cur = con.cursor()
##
####cur.execute(
####        """create table students
####        (first text,
####        last text)"""
####         )
####
####cur.execute('''INSERT INTO students VALUES ('John','Smith')''')
##cur.execute('SELECT * FROM students')
##print(cur.fetchone())
##
####con.commit()
##
##
##con.close()


# kivy file


### tkinter ttk Button  
##
##
##
##import tkinter as tk
##import tkinter.ttk as ttk
##
##
##win = tk.Tk()
##
##win.title("Window")
##
##
##win.geometry('300x300')
##
##
##button = ttk.Button(win,text="Hello")
##
##button.pack()
##
##win.mainloop()



### matplotlib pyplot stacked bar chart
##
##
##import numpy as np
##import matplotlib.pyplot as plt
##
##
##count = np.arange(3)
##teachers = ['Golden','Smith', 'Morgan']
##
##
##boys = [12,8,12]
##girls = [10,12,10]
##
##plt.xticks(count,teachers)
##
##p1 = plt.bar(count,boys,.35)
##p2 = plt.bar(count,girls,.35,bottom=boys)
##
##plt.show()


# pygame rect location


### pandas options/settings
##
##
##
##import pandas as pd
##
##
##df = pd.read_excel('unemployment.xls',skiprows=7)


### numpy attributes nbytes/size/ndim/T
##
##
##import numpy as np
##
##
##x = np.random.randint(12,size=(3,4))
##
##print(x)


### sqlite cursor executemany method
##
##grade_9 = [('John','Adams'),
##           ('Ben','Franklin'),
##           ('John', 'Hancock')]
##
##
##import sqlite3
##
##
##con = sqlite3.connect('student.db')
##
##cur = con.cursor()
##
####cur.execute(
####        """create table students
####        (first text,
####        last text)"""
####         )
####
##
##cur.executemany('INSERT INTO students VALUES(?,?)',grade_9)
##
##
##
##con.commit()
##
##
##con.close()


### tkinter  
##
##
##import tkinter as tk
##import tkinter.ttk as ttk
##
##
##win = tk.Tk()
##
##win.title("Window")
##
##win.geometry('300x300')
##
##check = ttk.Checkbutton(win,text='Please Click Me')
##
##check.pack()
##
##
##win.mainloop()


### functools module 
##
##import functools
##
##
##
##def foo():
##    pass


### calendar module
##
##
##import calendar


### functools reduce
##
##
##from functools import reduce
##
##
##l = list(range(6))
##
##y = reduce(lambda x,y: x+y,l)
##
##print(y)


#### calendar month_name and month_abbr attributes
##
##
##import numpy as np
##import matplotlib.pyplot as plt
##import calendar as c
##
##
##mon = np.arange(1,13)
##
##y_2017 = [5,8,11,15,4,9,9,1,12,10,9,2]
##y_2018 = [7,12,13,17,4,10,11,2,14,12,9,6]
##
##plt.xticks(np.arange(1,13),c.month_abbr[1:13],rotation=40)
##
##plt.plot(mon,y_2017, mon,y_2018)
##
##plt.show()




### Sprite object update method
##
##import pygame,random,sys
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##
##sprites = pygame.sprite.Group()
##
##class Block(pygame.sprite.Sprite):
##    def __init__(self,color,width,height):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((width,height))
##        self.image.fill(color)
##        self.rect = self.image.get_rect()
##        self.rect.x = x/2
##        self.rect.y = y/2
##    def update(self):
##        if event.type== pygame.MOUSEBUTTONDOWN:
##            c_x,c_y = pygame.mouse.get_pos()
##            self.rect.centerx = c_x
##            self.rect.centery = c_y
##            
## 
##block = Block(green,50,50)
##sprites.add(block)
##
##
##move_x,move_y = 0,0 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##colors = [white,black,red,blue,green]
##fill = white
##text_color = black
##circle_x,circle_y = x//2,y//2
##while window:
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,text_color)
##    for event in pygame.event.get():
##        c_x,c_y = pygame.mouse.get_pos()
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit()            
##            window = False
##
##    surface.fill(fill)
####    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.rect(surface,black,(5,5,590,790),3)
####    pygame.draw.circle(surface,black,(circle_x,circle_y),50,1)
##    movement = pygame.mouse.get_pos()
##    sprites.draw(surface)
##    sprites.update()
##    win.update()
##    clock.tick(30)

##


### pandas working more than one sheet
##
##
##
##import pandas as pd
##
####df = pd.read_excel('class_attendance.xlsx')
##df_1 = pd.read_excel('class_attendance.xlsx',0)
##df_2 = pd.read_excel('class_attendance.xlsx',1)
####print(df)
##print(df_1)
##print(df_2)



### numpy slicing
##
##
##import numpy as np
##
##
##x = np.random.randint(12,size=(3,4))


### tkinter IntVar()
##
##
##import tkinter as tk
##import tkinter.ttk as ttk
##
##
##win = tk.Tk()
##
##win.title("Window")
##
##win.geometry('300x300')
##
##var = tk.IntVar()
##
##check = ttk.Checkbutton(win,text="Please click me",variable=var)
##check.pack()
##
##
##win.mainloop()


#### Matplotlib set_xlabel _ylabel
##
##
##import numpy as np
##import matplotlib.pyplot as plt
##import calendar as c
##
##
##mon = np.arange(1,13)
##
##fig,ax1 = plt.subplots(figsize=(8,6))
##
####y_2017 = [5,8,11,15,4,9,9,1,12,10,9,2]
##y_2018 = [7,12,13,17,4,10,11,2,14,12,9,6]
##
##plt.xticks(np.arange(1,13),c.month_abbr[1:13],rotation=40)
##
##ax1.plot(mon,y_2018)
##ax1.set_title('Sales 2018')
##ax1.set_xlabel('Month',labelpad=.05)
##ax1.set_ylabel('Sales')
##
##
##plt.show()


### Multiple Sprite objects 
##
##import pygame,random,sys
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##
##sprites = pygame.sprite.Group()
##
##class Block(pygame.sprite.Sprite):
##    def __init__(self,color,width,height):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((width,height))
##        self.image.fill(color)
##        self.rect = self.image.get_rect()
##        self.rect.x = x/2
##        self.rect.y = y/2
##    def update(self):
##        if event.type== pygame.MOUSEBUTTONDOWN:
##            c_x,c_y = pygame.mouse.get_pos()
##            self.rect.centerx = c_x
##            self.rect.centery = c_y
## 
####block = Block(green,50,50)
####sprites.add(block)
##
##class Bad_Block(pygame.sprite.Sprite):
##    def __init__(self,color,width,height):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((width,height))
##        self.image.fill(color)
##        self.rect = self.image.get_rect()
##        self.rect.x = random.randint(50,550)
##        self.rect.y = 0
##    def update(self):
##       self.rect.centery += 5
##
##
##            
##
##move_x,move_y = 0,0 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##colors = [white,black,red,blue,green]
##fill = white
##text_color = black
##circle_x,circle_y = x//2,y//2
##while window:
##    block = Bad_Block(red,50,50)
##    sprites.add(block)
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,text_color)
##    for event in pygame.event.get():
##        c_x,c_y = pygame.mouse.get_pos()
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit()            
##            window = False
##
##    surface.fill(fill)
####    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.rect(surface,black,(5,5,590,790),3)
####    pygame.draw.circle(surface,black,(circle_x,circle_y),50,1)
##    movement = pygame.mouse.get_pos()
##    sprites.update()
##    sprites.draw(surface)
##    win.update()
##    clock.tick(30)


### pandas ExcelFile Objcet
##
##
##
##
##import pandas as pd
##
##
##file = pd.ExcelFile('class_attendance.xlsx')
##
####df = pd.read_excel('class_attendance.xlsx')
##df_1 = pd.read_excel(file.io,sheet_name='2017')
##df_2 = pd.read_excel(file.io,sheet_name='2018')
####print(df)
##print(df_1)
##print(df_2)


### numpy save and load function
##
##
##import numpy as np
##
##x = np.random.randint(12,size=(3,4))
##
##
##np.save('Random_arr',x)


#### sqlite SELECT fetchmany
##
##
##import sqlite3
##
##
##con = sqlite3.connect('student.db')
##
##cur = con.cursor()
##
##cur.execute('SELECT * FROM students')



##import tkinter as tk
####import tkinter.ttk as ttk
##
##
##
##win = tk.Tk()
##
##win.title("Window")
##
##win.geometry('300x300')
##
##Main_menu = tk.Menu(win)
##win.config(menu=Main_menu)
##
##File_menu = tk.Menu(Main_menu)
##Main_menu.add_cascade(label='File',menu=File_menu)
##
##
##
##win.mainloop()


#### Matplotlib twin axes
##
##import numpy as np
##import matplotlib.pyplot as plt
##
##import calendar as c
##
##
##mon = np.arange(1,13)
##
##fig, ax1 = plt.subplots(figsize=(8,6))
##
###y_2017 = [5,8,11,15,4,9,9,1,12,10,9,2]
##y_2018 = [5,10,20,15,6,15,11,9,16,10,12,5]
##showings = [63, 108, 117, 153, 36, 90, 99, 18, 126, 108, 81, 54]
##
##
##plt.xticks(np.arange(1,13),c.month_abbr[1:13], rotation = 60)
##
##ax1.plot(mon,y_2018)
##ax1.set_xlabel("Month")
##ax1.set_ylabel("Sales")
##ax1.set_title("2018 Sales")
##
##ax2 = ax1.twinx()
##
##ax2.plot(mon,showings)
##ax2.set_ylabel("Showings")
##
##plt.show()


### Multiple Sprite objects control
##
##import pygame,random,sys
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##bad_block_reload = 20# delay of frames per bad block
##
##sprites = pygame.sprite.Group()
##
##class Block(pygame.sprite.Sprite):
##    def __init__(self,color,width,height):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((width,height))
##        self.image.fill(color)
##        self.rect = self.image.get_rect()
##        self.rect.x = x/2
##        self.rect.y = y/2
##    def update(self):
##        if event.type== pygame.MOUSEBUTTONDOWN:
##            c_x,c_y = pygame.mouse.get_pos()
##            self.rect.centerx = c_x
##            self.rect.centery = c_y
## 
####block = Block(green,50,50)
####sprites.add(block)
##
##class Bad_Block(pygame.sprite.Sprite):
##    def __init__(self,color,width,height):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((width,height))
##        self.image.fill(color)
##        self.rect = self.image.get_rect()
##        self.rect.x = random.randint(50,550)
##        self.rect.y = 0
##    def update(self):
##       self.rect.centery += 5
##       
##
##
##move_x,move_y = 0,0 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##colors = [white,black,red,blue,green]
##fill = white
##text_color = black
##circle_x,circle_y = x//2,y//2
##bad_block = bad_block_reload
##while window:
##    if bad_block:
##        bad_block -= 1
##    else:
##        block = Bad_Block(red,50,50)
##        sprites.add(block)
##        bad_block = bad_block_reload
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,text_color)
##    for event in pygame.event.get():
##        c_x,c_y = pygame.mouse.get_pos()
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit()            
##            window = False
##
##    surface.fill(fill)
####    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.rect(surface,black,(5,5,590,790),3)
####    pygame.draw.circle(surface,black,(circle_x,circle_y),50,1)
##    movement = pygame.mouse.get_pos()
##    sprites.update()
##    sprites.draw(surface)
##    win.update()
##    clock.tick(30)


# 50,000 views


### pandas concatenate
##
##
##import pandas as pd
##
##
##file = pd.ExcelFile('class_attendance.xlsx')
##sheets = file.sheet_names
##
##df_1 = pd.read_excel('class_attendance.xlsx',sheet_name = '2017')
##df_2 = pd.read_excel('class_attendance.xlsx',sheet_name = '2018')
##file.close()
##
##
##print(df_1)
##print(df_2)


###  numpy homogeneous
##
##import numpy as np
##
##y = ['Sam', 6, 'feet', 0, 'inches']
##
##y = ['Sam', 6, 'feet', 0, 'inches']
##
####z = [12,.1,12,1.01]
##
##z = [12,.01,12,1.012]
##
##
### sqlite SELECT fetchall
##
##
##import sqlite3
##
##
##con = sqlite3.connect('student.db')
##
##cur = con.cursor()
##
##cur.execute('SELECT * FROM students')

### tkinter add command and seperator
##
##
##import tkinter as tk
##
##
##def do():
##    print('OMG, this works!!!!')
##
##win = tk.Tk()
##
##win.title("Window")
##
##win.geometry('300x300')
##
##
##Main_menu = tk.Menu(win)
##win.config(menu=Main_menu)
##
##
##
##File_Menu = tk.Menu(Main_menu)
##Main_menu.add_cascade(label='File',menu=File_Menu)
##File_Menu.add_command(label='New', command=do)
##File_Menu.add_command(label='Save', command=do)
##File_Menu.add_separator()
##File_Menu.add_command(label='Exit', command=do)
##
##Edit_Menu = tk.Menu(Main_menu)
##Main_menu.add_cascade(label='Edit',menu=Edit_Menu)
##Edit_Menu.add_command(label='Undo',command=do)
##Edit_Menu.add_command(label='Redo',command=do)
##
##
##
##win.mainloop()
##

#### Matplotlib twin axes add color
##
##import numpy as np
##import matplotlib.pyplot as plt
##from matplotlib import colors
##import calendar as c
##
##
##mon = np.arange(1,13)
##
##fig, ax1 = plt.subplots(figsize=(8,6))
##
###y_2017 = [5,8,11,15,4,9,9,1,12,10,9,2]
##y_2018 = [5,10,20,15,6,15,11,9,16,10,12,5]
##showings = [63, 108, 117, 153, 36, 90, 99, 18, 126, 108, 81, 54]
##
##
##plt.xticks(np.arange(1,13),c.month_abbr[1:13], rotation = 60)
##
##color = colors.cnames['green']
##ax1.plot(mon,y_2018,color=color)
##ax1.set_xlabel("Month")
##ax1.set_ylabel("Sales",color=color)
##ax1.set_title("2018 Sales")
##
##ax2 = ax1.twinx()
##color = colors.cnames['red']
##ax2.plot(mon,showings,color=color)
##ax2.set_ylabel("Showings",color=color)
##
##plt.show()


#### Multiple Sprite objects kill method
##
##import pygame,random,sys
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##bad_block_reload = 20# delay of frames per bad block
##
##sprites = pygame.sprite.Group()
##
##class Block(pygame.sprite.Sprite):
##    def __init__(self,color,width,height):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((width,height))
##        self.image.fill(color)
##        self.rect = self.image.get_rect()
##        self.rect.x = x/2
##        self.rect.y = y/2
##    def update(self):
##        if event.type== pygame.MOUSEBUTTONDOWN:
##            c_x,c_y = pygame.mouse.get_pos()
##            self.rect.centerx = c_x
##            self.rect.centery = c_y
## 
####block = Block(green,50,50)
####sprites.add(block)
##
##class Bad_Block(pygame.sprite.Sprite):
##    def __init__(self,color,width,height):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((width,height))
##        self.image.fill(color)
##        self.rect = self.image.get_rect()
##        self.rect.x = random.randint(50,550)
##        self.rect.y = 0
##    def update(self):
##       self.rect.centery += 5
##       if self.rect.y == 750:
##           self.kill()
##       
##
##
##move_x,move_y = 0,0 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##colors = [white,black,red,blue,green]
##fill = white
##text_color = black
##circle_x,circle_y = x//2,y//2
##bad_block = bad_block_reload
##while window:
##    if bad_block:
##        bad_block -= 1
##    else:
##        block = Bad_Block(red,50,50)
##        sprites.add(block)
##        bad_block = bad_block_reload
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,text_color)
##    for event in pygame.event.get():
##        c_x,c_y = pygame.mouse.get_pos()
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit()            
##            window = False
##
##    surface.fill(fill)
####    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.rect(surface,black,(5,5,590,790),3)
####    pygame.draw.circle(surface,black,(circle_x,circle_y),50,1)
##    movement = pygame.mouse.get_pos()
##    sprites.update()
##    sprites.draw(surface)
##    win.update()
##    clock.tick(30)


### deep dive slicing and loop
### start stop
##
##'''
##p y t h o n 
##0 1 2 3 4 5 
##'''
##
##
##name = 'python basics'
##
##

### Rylan collaboration
### numpy median
##
##import numpy as np
##
##data = [5,2,3,4,1,2,3,6,7,8,7,5,3,2,4,3,2,3,
##        4,5,6,7,6,5,4,4,5,2,1,9,9,8,1,1,4,6]
##
##
##'''
##
##        0 
##        ^
##        | 
##   1-> [5, 2, 3, 4, 1, 2],
##       [3, 6, 7, 8, 7, 5],
##       [3, 2, 4, 3, 2, 3],
##       [4, 5, 6, 7, 6, 5],
##       [4, 4, 5, 2, 1, 9],
##       [9, 8, 1, 1, 4, 6]    
##
##
##'''



### for loop control
##
##
##
##s='aslifog'
##vowels = 'aeiou'
##new_s =''
##
##for i in s:
##    
##    if i not in vowels:
##        new_s += i
##    
##print(new_s)


# break / continue loop control


##for i in range(9):
##    print(i)
##    if i == 4:
##        break

##guesses = 0 
##
##while True:
##    num = int(input('enter guess: '))
##    if num != 0:
##        guesses += 1
##        continue
##    break
##print(guesses)

##for i in range(3):
##    print('i')
##    for j in range(3):
##        if j == 2:
##            break
##        print(j)
##    break

### requested video string increment
### with while loop 
##
##
##count = 0
##s='aslifog'
##vowels = 'aeiou'
##new_s = ''
##
####while count < len(s):
####    if s[count] not in vowels:
####        new_s += s[count]
####    count += 1
####
####print(new_s)
##
##while True:
##    if count == len(s):
##        break
##    elif s[count] not in vowels:
##        new_s += s[count]
##    count += 1
##    print(count)
##print(new_s)


### Collections Counter
##
##
##import collections
##
##
##c = collections.Counter('abcdeabcdabcaba')


### copy list
##
##
##x = [1,2,3]
##


# sum of square roots


##def sum_of_2(a,b):
##    return a**(1/2)+b**(1/2)
##
##print(sum_of_2(4,9))


##def sum_of_squ(*nums):
##    ttl = 0
##    for num in nums:
##        ttl += num**(1/2)
##    return ttl
##
##print(sum_of_squ(1,4,9,16,25))


### pandas DataFrame to_excel function
### openpyxl install
##
##
##import pandas as pd
##
##
##file = pd.ExcelFile('class_attendance.xlsx')
##sheets = file.sheet_names
##
##df = pd.read_excel(file.io,sheet_name=None)
##
##
##new_df = pd.concat(df,ignore_index=True)
##print(new_df)
##
##
##no_friday = new_df[new_df['day'] != 'Friday']


### collections orderedDict
##
##
##import collections
##
##
##fruit = 'banana'
##
##
##count = collections.Counter(fruit)



### Deep Dive
### Sprite object update method
##
##import pygame,random,sys
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##
##sprites = pygame.sprite.Group()
##
##class Block(pygame.sprite.Sprite):
##    def __init__(self,color,width,height):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((width,height))
##        self.image.fill(color)
##        self.rect = self.image.get_rect()
##        self.rect.x = x/2
##        self.rect.y = y/2
##    def update(self):
##        if event.type== pygame.MOUSEBUTTONDOWN:
##            c_x,c_y = pygame.mouse.get_pos()
##            self.rect.centerx = c_x
##            self.rect.centery = c_y
##            self.image.fill(random.choice([black,red,blue]))
##            
## 
##block = Block(green,50,50)
##sprites.add(block)
##
##
##move_x,move_y = 0,0 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##colors = [white,black,red,blue,green]
##fill = white
##text_color = black
##circle_x,circle_y = x//2,y//2
##while window:
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,text_color)
##    for event in pygame.event.get():
##        c_x,c_y = pygame.mouse.get_pos()
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit()            
##            window = False
##
##    surface.fill(fill)
####    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.rect(surface,black,(5,5,590,790),3)
####    pygame.draw.circle(surface,black,(circle_x,circle_y),50,1)
##    movement = pygame.mouse.get_pos()
##    sprites.update()
##    sprites.draw(surface)
##    win.update()
##    clock.tick(30)

##
### numpy median function
##
##
##import numpy as np
##
##
##data = [1,8,4,8,5,1,4,6,7,3,6,9,4,8,6,1,2,2,
##        8,7,3,3,8,2,5,3,1,4,2,7,2,7,2,7,5,1]
##
##arr = np.array(data)
##
##arr.shape = 6,6
##
##
##'''
##
##        0 
##        ^
##        | 
##   1-> [1, 8, 4, 8, 5, 1],
##       [4, 6, 7, 3, 6, 9],
##       [4, 8, 6, 1, 2, 2],
##       [8, 7, 3, 3, 8, 2],
##       [5, 3, 1, 4, 2, 7],
##       [2, 7, 2, 7, 5, 1]   
##
##
##'''

### sqlite cursor description attr.
##
##
##import sqlite3
##
##
##con = sqlite3.connect('student.db')
##
##cur = con.cursor()
##
##cur.execute('SELECT * FROM students')


#### pygame sprite.Sprite Object call
### Sprite.Group add method
##
##import pygame,random,sys
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##
##sprites = pygame.sprite.Group()
##
##class Block(pygame.sprite.Sprite):
##    def __init__(self,color,width,height):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((width,height))
##        self.image.fill(color)
##        self.rect = self.image.get_rect()
##        self.rect.x = x/2
##        self.rect.y = y/2
##
##block = Block(green,50,50)
##sprites.add(block)
##
##
##move_x,move_y = 0,0 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##colors = [white,black,red,blue,green]
##fill = white
##text_color = black
##circle_x,circle_y = x//2,y//2
##while window:
##    font = pygame.font.SysFont('timesnewroman', 20)
####    text = font.render('Start',0,text_color)
##    for event in pygame.event.get():
##        c_x,c_y = pygame.mouse.get_pos()
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit()            
##            window = False
##        if event.type == pygame.MOUSEBUTTONDOWN:
##            if ((300-c_x)**2+(400-c_y)**2) < 2500:
##                text_color = white
##                move_x,move_y = random.randint(-20,20),random.randint(-20,20)
##                fill = random.choice(colors)
##    circle_x += move_x
##    circle_y += move_y
##    if circle_x < 55 or circle_x > 545:
##        move_x = -move_x
##        
##    if circle_y < 55 or circle_y > 745:
##        move_y = -move_y
##        
##
###
##    surface.fill(fill)
####    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.rect(surface,black,(5,5,590,790),3)
####    pygame.draw.circle(surface,black,(circle_x,circle_y),50,1)
##    movement = pygame.mouse.get_pos()
##    sprites.draw(surface)
##    sprites.update()
##    win.update()
##    clock.tick(30)


### requested os rename outside
### of current directory
##
##
##
##
##import os
##
##
##d = os.getcwd()
##
##
##d_1 = d +'\\new\\newer'
##
##d_2 = d + '\\new\\newest'

### tkinter Tk() destroy method
##
##import tkinter as tk
##
##
##def do():
##    print("OMG,this works!!!")
##
##win = tk.Tk()
##
##win.title("Window")
##
##win.geometry('300x300')
##
##
##Main_menu = tk.Menu(win)
##win.config(menu=Main_menu)
##
##
##File_Menu = tk.Menu(Main_menu)
##Main_menu.add_cascade(label='File',menu=File_Menu)
##
##
##File_Menu.add_command(label='New',command=do)
#### new
##File_Menu.add_command(label='Save',command=do)
##File_Menu.add_separator()
##File_Menu.add_command(label='Exit',command=win.destroy)
##
##Edit_Menu = tk.Menu(Main_menu)
##Main_menu.add_cascade(label='Edit',menu=Edit_Menu)
##Edit_Menu.add_command(label='Undo',command=do)
##Edit_Menu.add_command(label='Redo',command=do)
##
##
##win.mainloop()

### matplotlib grouped bar chart
##
##
##
##import numpy as np
##import matplotlib.pyplot as plt
##
##
##
##teachers = ['Golden','Smith', 'Morgan']
##count = np.arange(len(teachers))
##width = .35
##
##fig, ax = plt.subplots()
##
##boys = [12,8,12]
##girls = [10,12,10]
##
##plt.xticks(count,teachers)
##
##bar_1 = ax.bar(count-width/2,boys,width)
##bar_2 = ax.bar(count+width/2,girls,width)
##
##plt.show()


### pandas DataFrame Index Change
##
##
##
##import pandas as pd 
##
##
##file = pd.ExcelFile('class_attendance.xlsx')
##sheets = file.sheet_names
##
##df = pd.read_excel(file.io,sheet_name=None)
##
##
##new_df = pd.concat(df,ignore_index=True)
##
##
##no_friday = new_df[new_df['day'] != 'Friday']
##
##
##no_friday.set_index('date',inplace=True)
##
##no_friday.index.name = None


# what is __main__ ?


##def main():
##    pass
##
##print(__name__)
##
##
##if __name__ == '__main__':
##    x = 1


### what is __file__ ? 
##
##'''
##what this line means:
##cwd = os.path.dirname(__file__)
##'''
##


### numpy array indexing / Slicing
##
##
##import numpy as np
##
##
##
##x = np.arange(1,101)
##
##y = x>50
##
##x[y]
##
##print(x)


### sqlite sql one column query
##
##
##
##import sqlite3
##
##
##con = sqlite3.connect('student.db')
##
##cur = con.cursor()
##
##cur.execute("SELECT first FROM students")
##
##for i in cur:
##    print(i[0])
    

### calendar is leap year function
##
##
##import calendar
##
##'''
##RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python36-32\ideas.py =
##>>> help(calendar.isleap)
##Help on function isleap in module calendar:
##
##isleap(year)
##    Return True for leap years, False for non-leap years.
##
##>>> calendar.isleap(2000)
##True
##>>> calendar.isleap(2019)
##False
##>>> calendar.isleap(2020)
##True
##>>> 1900/4
##475.0
##>>> calendar.isleap(1900)
##False
##>>> calendar.isleap(1600)
##True
##>>> 
##'''


### tkinter Menu tearoff argument
##
##
##import tkinter as tk
##
##
##def do():
##    print("OMG,this works!!!")
##
##win = tk.Tk()
##
##win.title("Window")
##
##win.geometry('300x300')
##
##
##Main_menu = tk.Menu(win)
##win.config(menu=Main_menu)
##
##
##File_Menu = tk.Menu(Main_menu,tearoff=False) # added
##Main_menu.add_cascade(label='File',menu=File_Menu)
##
##
##File_Menu.add_command(label='New',command=do)
#### new
##File_Menu.add_command(label='Save',command=do)
##File_Menu.add_separator()
##File_Menu.add_command(label='Exit',command=win.destroy)
##
##Edit_Menu = tk.Menu(Main_menu,tearoff=False) # added
##Main_menu.add_cascade(label='Edit',menu=Edit_Menu)
##Edit_Menu.add_command(label='Undo',command=do)
##Edit_Menu.add_command(label='Redo',command=do)
##
##
##win.mainloop()


#### matplotlib set_ylim method
##
##
##import numpy as np
##import matplotlib.pyplot as plt
##
##
##teachers = ['Golden','Smith', 'Morgan']
##count = np.arange(len(teachers))
##width = .35
##
##fig,ax = plt.subplots()
##
##boys = [12,8,12]
##girls = [10,12,10]
##
##plt.xticks(count,teachers)
##plt.yticks(np.arange(0,15,2))
##
##bar_1 = ax.bar(count-width/2,boys,width,label='Boys')
##bar_2 = ax.bar(count+width/2,girls,width,label='Girls')
##
##
##ax.legend()
##ax.set_ylim([0,16])
##plt.show()


###

### pandas dataframe dtypes attribute
##
##
##
##
##import pandas as pd 
##
##df = pd.read_excel('unemployment.xls',skiprows=7)
##
##



### Requested Video comma seperation
##
##
##
##x = 123456789
##
##
##print('{:,}'.format(x))


#### Pygame Sprite Update Method
#### with keyboard input
## 
##
##import pygame,random,sys
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##bad_block_reload = 20 # delay of frames per bad block
##
##sprites = pygame.sprite.Group()
##
##class Block(pygame.sprite.Sprite):
##    def __init__(self,color,width,height):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((width,height))
##        self.image.fill(color)
##        self.rect = self.image.get_rect()
##        self.rect.x = x//2
##        self.rect.y = 743 #changed
##    def update(self):  # changed all
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                self.rect.x -= 5
##            if event.key == pygame.K_RIGHT:
##                self.rect.x += 5
## 
##block = Block(green,50,50)
##sprites.add(block)
##
##class Bad_Block(pygame.sprite.Sprite):
##    def __init__(self,color,width,height):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((width,height))
##        self.image.fill(color)
##        self.rect = self.image.get_rect()
##        self.rect.x = random.randint(50,550)
##        self.rect.y = 0
##    def update(self):
##       self.rect.centery += 5
##       if self.rect.y == 750:
##           self.kill()
##       
##
##
##move_x,move_y = 0,0 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##colors = [white,black,red,blue,green]
##fill = white
##text_color = black
##circle_x,circle_y = x//2,y//2
##bad_block = bad_block_reload
##while window:
##    if bad_block:
##        bad_block -= 1
##    else:
##        block = Bad_Block(red,50,50)
##        sprites.add(block)
##        bad_block = bad_block_reload
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,text_color)
##    for event in pygame.event.get():
##        c_x,c_y = pygame.mouse.get_pos()
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit()            
##            window = False
##
##    surface.fill(fill)
####    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.rect(surface,black,(5,5,590,790),3)
####    pygame.draw.circle(surface,black,(circle_x,circle_y),50,1)
##    movement = pygame.mouse.get_pos()
##    sprites.update()
##    sprites.draw(surface)
##    win.update()
##    clock.tick(30)




### numpy vstack function
##
##import numpy as np
##
##
##x = np.array([0,22,28,17])
##
##y = np.array([14,5,9,20])



### sql name of the tables in database
##
##
##
##import sqlite3
##
##
##con = sqlite3.connect('student.db')
##
##cur = con.cursor()
##
##
##cur.execute('SELECT name from sqlite_master where type="table"')




### Calendar monthcalendar method
##
##
##import calendar
##
##
##mon = calendar.monthcalendar(2019,10)
##
##
##for week in mon:
##    print(week)
    


#### tkinter text input widget
##
##
##import tkinter as tk
##from tkinter import ttk
##
##
##def do():
##    print("OMG,this works!!!")
##
##win = tk.Tk()
##
##win.title("Window")
##
##win.geometry('300x300')
##
##
##Main_menu = tk.Menu(win)
##win.config(menu=Main_menu)
##
##
##File_Menu = tk.Menu(Main_menu,tearoff=False) # added
##Main_menu.add_cascade(label='File',menu=File_Menu)
##
##
##File_Menu.add_command(label='New',command=do)
## new
##File_Menu.add_command(label='Save',command=do)
##File_Menu.add_separator()
##File_Menu.add_command(label='Exit',command=win.destroy)
##
##Edit_Menu = tk.Menu(Main_menu,tearoff=False) # added
##Main_menu.add_cascade(label='Edit',menu=Edit_Menu)
##Edit_Menu.add_command(label='Undo',command=do)
##Edit_Menu.add_command(label='Redo',command=do)
##
##username_label = tk.Label(win,text='User Name')
##username_label.pack()
##username = tk.Entry(win)
##username.pack()
##password_label = tk.Label(win,text='Password')
##password_label.pack()
##password = tk.Entry(win)
##password.pack()
##
##
##win.mainloop()



### Requested Deep Dive
### Numpy Random Uniform
##
##
##
##import numpy as np


### matplotlib text annotation 
##
##
##import numpy as np
##import matplotlib.pyplot as plt
##
##
##teachers = ['Golden','Smith', 'Morgan']
##count = np.arange(len(teachers))
##width = .35
##
##fig,ax = plt.subplots() 
##
##boys = [12,8,12]
##girls = [10,12,10]
##
##plt.xticks(count,teachers)
##plt.yticks(np.arange(0,15,2)) 
##bar_1 = ax.bar(count-width/2,boys,width,label='Boys')
##bar_2 = ax.bar(count+width/2,girls,width,label='Girls')
##
##ax.legend() 
##ax.set_ylim([0,17]) 
##
##def autolabel(rects):
##    for rect in rects:
##        height = rect.get_height()
##        ax.annotate('{}'.format(height),
##                    xy=(rect.get_x() + rect.get_width() / 2, height),
##                    xytext=(0, 3), 
##                    textcoords="offset points", # show 
##                    ha='center', va='bottom',size=16,rotation=45) # alignment size and rotation
##
##autolabel(bar_1)
##autolabel(bar_2)
##
##
##plt.show()




### pandas dataframe more with describe method
##
##
##
##import pandas as pd
##
##col = ['State','Gender','Year','Name','Count']
##
##hi = pd.read_csv('hi\\Hi.txt',names=col)



### pygame add a Sprite Explosion
## 
##
##import pygame,random,sys
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##bad_block_reload = 20 # delay of frames per bad block
##
##sprites = pygame.sprite.Group()
##
##class Block(pygame.sprite.Sprite):
##    def __init__(self,color,width,height):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((width,height))
##        self.image.fill(color)
##        self.rect = self.image.get_rect()
##        self.rect.x = x//2
##        self.rect.y = 743 
##    def update(self):  
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                self.rect.x -= 5
##            if event.key == pygame.K_RIGHT:
##                self.rect.x += 5
## 
##block = Block(green,50,50)
##sprites.add(block)
##
##class Explosion(pygame.sprite.Sprite):
##    defaultlife = 12
##    def __init__(self,center):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.image.load('explosion.jpg')
##        self.rect = self.image.get_rect()
##        self.rect.center = center
##        self.life = self.defaultlife
##    def update(self):
##        self.life -= 1
##        if self.life <= 0:
##            self.kill()
##
##
##class Bad_Block(pygame.sprite.Sprite):
##    def __init__(self): #change
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((50,50)) #change
##        self.image.fill(red)#change
##        self.rect = self.image.get_rect()
##        self.rect.x = random.randint(50,550)
##        self.rect.y = 0
##    def update(self):
##       self.rect.centery += 5
##       if self.rect.y == 750:
##           sprites.add(Explosion(self.rect.center))# add
##           self.kill()
##
##
##
##move_x,move_y = 0,0 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##colors = [white,black,red,blue,green]
##fill = white
##text_color = black
##circle_x,circle_y = x//2,y//2
##bad_block = bad_block_reload
##while window:
##    if bad_block:
##        bad_block -= 1
##    else:
##        block = Bad_Block()#change
##        sprites.add(block)
##        bad_block = bad_block_reload
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,text_color)
##    for event in pygame.event.get():
##        c_x,c_y = pygame.mouse.get_pos()
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit()            
##            window = False
##
##    surface.fill(fill)
####    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.rect(surface,black,(5,5,590,790),3)
####    pygame.draw.circle(surface,black,(circle_x,circle_y),50,1)
##    movement = pygame.mouse.get_pos()
##    sprites.update()
##    sprites.draw(surface)
##    win.update()
##    clock.tick(30)
##
### more with numpy arange function
##
##
##
##import numpy as np
##
##
##x = list(np.arange(1,6,.5))
##print(x)


### sqlite where keyword
##
##
##
##import sqlite3
##
##
##con = sqlite3.connect('student.db')
##
##cur = con.cursor()
##
##cur.execute("SELECT * FROM students where first != 'John'")
##
##for i in cur:
##    print(i)
    


### calendar Print Calendar
##
##
##import calendar




### difference between ttk and tk
##
##import tkinter as tk
##from tkinter import ttk
##
##
##def do():
##    print("OMG,this works!!!")
##
##win = tk.Tk()
##
##win.title("Window")
##
##win.geometry('300x300')
##
##
##Main_menu = tk.Menu(win)
##win.config(menu=Main_menu)
##
##
##File_Menu = tk.Menu(Main_menu,tearoff=False) # added
##Main_menu.add_cascade(label='File',menu=File_Menu)
##
##
##File_Menu.add_command(label='New',command=do)
#### new
##File_Menu.add_command(label='Save',command=do)
##File_Menu.add_separator()
##File_Menu.add_command(label='Exit',command=win.destroy)
##
##Edit_Menu = tk.Menu(Main_menu,tearoff=False) # added
##Main_menu.add_cascade(label='Edit',menu=Edit_Menu)
##Edit_Menu.add_command(label='Undo',command=do)
##Edit_Menu.add_command(label='Redo',command=do)
##
##
##user_label = ttk.Label(win,text='Username:')
##user_label.pack()
##username = ttk.Entry(win)
##username.pack()
##password_label = ttk.Label(win,text='password')
##password_label.pack()
##password = ttk.Entry(win).pack()
##win.mainloop()







### maptplotlib twin plots different types
### with legend box_to_anchor and data control 
##
##
##import numpy as np
##from matplotlib import pyplot as plt
##import calendar as c
##
##ot = [300,700,600,200,500,1000,500,800,100,400,200,500]
##
##
###ot = [300,700,600,200,500,1000,500,800,100,400,200,500]
##
##mon_per = np.array([  8.33333333,  16.66666667,  25.        ,  33.33333333,
##        41.66666667,  50.        ,  58.33333333,  66.66666667,
##        75.        ,  83.33333333,  91.66666667, 100.        ])
##    
##mon_per = mon_per[:len(ot)]
##
##
##fig,ax1 = plt.subplots(figsize=(8,6))
##
##mon = np.arange(1,len(mon_per)+1)
##
##tot = 0
##ot_p = []
##for i in ot:
##    tot += i
##    ot_p.append(tot)
##
##bins = np.arange(1,len(ot)+1)
##plt.xticks(np.arange(1,len(ot)+1),c.month_abbr[1:len(ot)+1], rotation = 60)
##ot_per = np.array(ot_p)*100/6000
##    
###plt.xticks(bins)
##ax1.plot(bins, np.full(len(ot),500), linewidth=2, color='c',label='Baseline')
##ax1.bar(bins,ot)
##
##ax2 = ax1.twinx()
##ax2.plot(mon,ot_per,linewidth=2,color='r',label='OT %/Buget')
##ax2.plot(mon,mon_per,linewidth=4, color='g',label='Baseline %')
##
##plt.title('Overtime Cost and Percent')
##ax1.set_xlabel('Month')
##ax1.set_ylabel('Monthly Budget')
##ax2.set_ylabel('% of Yearly Budget')
##
##
##fig.legend(bbox_to_anchor=(.32,.88))
##plt.show()




### pygame Sprite Boundary
## 
##
##import pygame,random,sys
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##bad_block_reload = 20 # delay of frames per bad block
##
##sprites = pygame.sprite.Group()
##
##class Block(pygame.sprite.Sprite):
##    def __init__(self):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((50,50))
##        self.image.fill(green)
##        self.rect = self.image.get_rect()
##        self.rect.x = x//2
##        self.rect.y = 743 
##    def update(self):  
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                if self.rect.x > 5:
##                    self.rect.x -= 5
##            if event.key == pygame.K_RIGHT:
##                if self.rect.x < 545:
##                    self.rect.x += 5
## 
##block = Block() #change
##sprites.add(block) # change
##
##class Explosion(pygame.sprite.Sprite):
##    defaultlife = 12
##    def __init__(self,center):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.image.load('explosion.jpg')
##        self.rect = self.image.get_rect()
##        self.rect.center = center
##        self.life = self.defaultlife
##    def update(self):
##        self.life -= 1
##        if self.life <= 0:
##            self.kill()
##
##
##class Bad_Block(pygame.sprite.Sprite):
##    def __init__(self): #change
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((50,50)) #change
##        self.image.fill(red)#change
##        self.rect = self.image.get_rect()
##        self.rect.x = random.randint(50,550)
##        self.rect.y = 0
##    def update(self):
##       self.rect.centery += 5
##       if self.rect.y == 750:
##           sprites.add(Explosion(self.rect.center))# add
##           self.kill()
##
##
##
##move_x,move_y = 0,0 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##colors = [white,black,red,blue,green]
##fill = white
##text_color = black
##circle_x,circle_y = x//2,y//2
##bad_block = bad_block_reload
##while window:
##    if bad_block:
##        bad_block -= 1
##    else:
##        block = Bad_Block()#change
##        bad_block = bad_block_reload
##        sprites.add(block)
##   
##
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,text_color)
##    for event in pygame.event.get():
##        c_x,c_y = pygame.mouse.get_pos()
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit()            
##            window = False
##
##    surface.fill(fill)
####    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.rect(surface,black,(5,5,590,790),3)
####    pygame.draw.circle(surface,black,(circle_x,circle_y),50,1)
##    movement = pygame.mouse.get_pos()
##    sprites.update()
##    sprites.draw(surface)
##    win.update()
##    clock.tick(30)







### pandas reset_index method
##
##
##
##
##
##import pandas as pd 
##
##
##file = pd.ExcelFile('class_attendance.xlsx')
##sheets = file.sheet_names
##
##df = pd.read_excel(file.io,sheet_name=None)
##
##
##new_df = pd.concat(df,ignore_index=True)
###print(new_df)
##
##
##no_friday = new_df[new_df['day'] != 'Friday']
###
##no_friday.set_index('date',inplace=True) # new set
##
##no_friday.index.name = None # remove date
##
##no_friday.to_excel('no_friday.xlsx')
##












#### numpy linspace Sunday
##
##import numpy as np
##
##
##
##'''
##
##mon_per = np.array([  8.33333333,  16.66666667,  25.        ,  33.33333333,
##        41.66666667,  50.        ,  58.33333333,  66.66666667,
##        75.        ,  83.33333333,  91.66666667, 100.        ])
##    
##'''


#### ame Sprite Boundary
## 
##
##import pygame,random,sys
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##bad_block_reload = 20 # delay of frames per bad block
##
##sprites = pygame.sprite.Group()
##
##class Block(pygame.sprite.Sprite):
##    def __init__(self):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((50,50))
##        self.image.fill(green)
##        self.rect = self.image.get_rect()
##        self.rect.x = x//2
##        self.rect.y = 743 
##    def update(self):  
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                if self.rect.x > 5:
##                    self.rect.x -= 5
##            if event.key == pygame.K_RIGHT:
##                if self.rect.x < 545:
##                    self.rect.x += 5
## 
##block = Block() #change
##sprites.add(block) # change
##
##class Explosion(pygame.sprite.Sprite):
##    defaultlife = 12
##    def __init__(self,center):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.image.load('explosion.jpg')
##        self.rect = self.image.get_rect()
##        self.rect.center = center
##        self.life = self.defaultlife
##    def update(self):
##        self.life -= 1
##        if self.life <= 0:
##            self.kill()
##
##
##class Bad_Block(pygame.sprite.Sprite):
##    def __init__(self): #change
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((50,50)) #change
##        self.image.fill(red)#change
##        self.rect = self.image.get_rect()
##        self.rect.x = random.randint(50,550)
##        self.rect.y = 0
##    def update(self):
##       self.rect.centery += 5
##       if self.rect.y == 750:
##           sprites.add(Explosion(self.rect.center))# add
##           self.kill()
##
##
##
##move_x,move_y = 0,0 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##colors = [white,black,red,blue,green]
##fill = white
##text_color = black
##circle_x,circle_y = x//2,y//2
##bad_block = bad_block_reload
##while window:
##    if bad_block:
##        bad_block -= 1
##    else:
##        block = Bad_Block()#change
##        bad_block = bad_block_reload
##        sprites.add(block)
##   
##
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,text_color)
##    for event in pygame.event.get():
##        c_x,c_y = pygame.mouse.get_pos()
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit()            
##            window = False
##
##    surface.fill(fill)
####    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.rect(surface,black,(5,5,590,790),3)
####    pygame.draw.circle(surface,black,(circle_x,circle_y),50,1)
##    movement = pygame.mouse.get_pos()
##    sprites.update()
##    sprites.draw(surface)
##    win.update()
##    clock.tick(30)





### sqlite sql keyword order 
##
##
##
##
##import sqlite3
##
##con = sqlite3.connect('student.db')
##
##cur = con.cursor()
##
##cur.execute('SELECT * from students ORDER BY FIRST DESC,LAST DESC')
##
##print(cur.fetchall())



### Calendar set first weekday
##
##
##
##import calendar





### tkinter button press
##
##
##
##import tkinter as tk
##import tkinter.ttk as ttk
##
##
##win = tk.Tk()
##
##win.title("Window")
##
###win.configure()
##
##win.geometry('300x300')
##
##def press(event):
##    print('You pressed the button')
##
##button = ttk.Button(win,text="Press")
##button.bind('<Button-1>',press)
##button_exit = ttk.Button(win,text="Exit",command=win.destroy)
##
##button.pack()
##button_exit.pack()
###
##label = ttk.Label(win,text="Hello World")
##
##label.pack()
##
##win.mainloop()










##import numpy as np
##from matplotlib import pyplot as plt
##from matplotlib.ticker import MultipleLocator
##import calendar as c
##
##ot = [300,700,600,200,500,1000,500,800,100,400,200,500]
##
##
###ot = [300,700,600,200,500,1000,500,800,100,400,200,500]
##
##mon_per = np.array([  8.33333333,  16.66666667,  25.        ,  33.33333333,
##        41.66666667,  50.        ,  58.33333333,  66.66666667,
##        75.        ,  83.33333333,  91.66666667, 100.        ])
##    
##mon_per = mon_per[:len(ot)]
##
##
##fig,ax1 = plt.subplots(figsize=(10,8))
##
##mon = np.arange(1,len(mon_per)+1)
##
##tot = 0
##ot_p = []
##for i in ot:
##    tot += i
##    ot_p.append(tot)
##
##
##
##bins = np.arange(1,len(ot)+1)
##plt.xticks(np.arange(1,len(ot)+1),c.month_abbr[1:len(ot)+1], rotation = 60)
##ot_per = np.array(ot_p)*100/6000
##    
###plt.xticks(bins)
##ax1.plot(bins, np.full(len(ot),500), linewidth=2, color='c',label='Baseline')
##ax1.bar(bins,ot)
##
##ax2 = ax1.twinx()
##ax2.plot(mon,ot_per,linewidth=2,color='r',label='OT %/Buget')
##ax2.plot(mon,mon_per,linewidth=4, color='g',label='Baseline %')
##
##ax3 = ax1.twinx()
##ax3.spines['left'].set_position(('axes',2.15))
##ax3.plot(mon,ot_p,linewidth=3,color = 'k',label='Acumulative Overtime')
##
####majorLocator = MultipleLocator(2)
####ax1.yaxis.set_major_locator(majorLocator)
##
##
##plt.title('Overtime Cost and Percent')
##ax1.set_xlabel('Month')
##ax1.set_ylabel('Monthly Budget')
##ax2.set_ylabel('% of Yearly Budget')
##ax3.set_ylabel("Overtime Total", labelpad=15)
##
##fig.legend(bbox_to_anchor=(.4,.85))
##plt.show()


# interactive matplotlib


##import matplotlib as mpl
##import matplotlib.pyplot as plt
##
##plt.ion()
##
##mpl.is_interactive()
##
##plt.plot([1.5,3.0])
##
##
##
##plt.title('Interactive')
##
##
##plt.xlabel("X-axis")
##
##
##plt.ylabel('Y-axis')
##
##
##plt.plot([3.5,2.5])
##
##plt.ioff()
##
##mpl.is_interactive()


# 600





### pygame Sprite Group Collide
##
## 
##
##import pygame,random,sys
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##bad_block_reload = 20 # delay of frames per bad block
##
##sprites = pygame.sprite.Group()
##bad_sprites = pygame.sprite.Group()# add
##
##class Block(pygame.sprite.Sprite):
##    def __init__(self):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((50,50))
##        self.image.fill(green)
##        self.rect = self.image.get_rect()
##        self.rect.x = x//2
##        self.rect.y = 743 
##    def update(self):  
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                if self.rect.x > 5:
##                    self.rect.x -= 5
##            if event.key == pygame.K_RIGHT:
##                if self.rect.x < 545:
##                    self.rect.x += 5
## 
##good_block = Block() # change
##sprites.add(good_block) #change
##
##class Explosion(pygame.sprite.Sprite):
##    defaultlife = 12
##    def __init__(self,center):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.image.load('explosion.jpg')
##        self.rect = self.image.get_rect()
##        self.rect.center = center
##        self.life = self.defaultlife
##    def update(self):
##        self.life -= 1
##        if self.life <= 0:
##            self.kill()
##
##
##class Bad_Block(pygame.sprite.Sprite):
##    def __init__(self): #change
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((50,50)) #change
##        self.image.fill(red)#change
##        self.rect = self.image.get_rect()
##        self.rect.x = random.randint(50,550)
##        self.rect.y = 0
##    def update(self):
##       self.rect.centery += 5
##       if self.rect.y == 750:
##           sprites.add(Explosion(self.rect.center))# add
##           self.kill()
##
##
##
##move_x,move_y = 0,0 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##colors = [white,black,red,blue,green]
##fill = white
##text_color = black
##circle_x,circle_y = x//2,y//2
##bad_block = bad_block_reload
##while window:
##    if bad_block:
##        bad_block -= 1
##    else:
##        block = Bad_Block()
##        bad_block = bad_block_reload
##        bad_sprites.add(block) #change
##    sprite_hits = pygame.sprite.spritecollide(good_block,bad_sprites,True)# add
##    for block in sprite_hits:
##        sprites.add(Explosion(good_block.rect.center))
##        sprites.add(Explosion(block.rect.center))
##        block.kill()
##        good_block.kill()
##        pygame.quit()
##        sys.exit()
##   
##
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,text_color)
##    for event in pygame.event.get():
##        c_x,c_y = pygame.mouse.get_pos()
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit()            
##            window = False
##
##    surface.fill(fill)
####    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.rect(surface,black,(5,5,590,790),3)
####    pygame.draw.circle(surface,black,(circle_x,circle_y),50,1)
##    movement = pygame.mouse.get_pos()
##    sprites.update()
##    sprites.draw(surface)
##    bad_sprites.draw(surface)
##    bad_sprites.update()
##    win.update()
##    clock.tick(30)




### pandas fillna method
##
##
##import pandas as pd
##import numpy as np






### numpy array tolist method
##
##
##import numpy as np
##
##
##x = np.arange(10).reshape(2,5)



### sql sqlite3 Row Object
##
##
##
##import sqlite3
##
##
##
##con = sqlite3.connect('student.db')
##con.row_factory = sqlite3.Row
##
##
##cur = con.cursor()
##
##
##cur.execute('SELECT * from students')
##
##rows = cur.fetchall()
##
##for row in rows:
##    print(row.keys())
##    

### calendar weekheader
##
##
##import calendar


### repeat pattern w/ one for loop
##
##for i in range(12):
##    print((i%3+1)*4)
    












# channel playlists









### install django  
##
##
##import django






### tkinter pop up window 
##
##
##import tkinter as tk
##import tkinter.ttk as ttk
##import tkinter.messagebox as mbox
##
##win = tk.Tk()
##
##win.title("Window")
##
##win.geometry('300x300')
##
##def press(event):
##    print('you pressed the button')
##
##def exit_win():
##    ans = mbox.askyesno('Exit','Are you sure?')
##    if ans:
##        win.destroy()
##    
## 
##button = ttk.Button(win,text='Press')       
##button.bind('<Button-1>',press)
##
##button_exit = ttk.Button(win,text='Exit',command=exit_win)
##
##button.pack()
##button_exit.pack()
##
##label = ttk.Label(win,text="Hello World")
##
##label.pack()
##
##win.mainloop()



### pygame Add Explosion Sound
##
## 
##
##import pygame,random,sys
##
##pygame.init()
##
##white = (255,255,255)
##black = (0,0,0)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##
##x = 600
##y = 800
##z = [x,y]
##
##win = pygame.display
##
##bad_block_reload = 20 # delay of frames per bad block
##
##sprites = pygame.sprite.Group()
##bad_sprites = pygame.sprite.Group()# add
##
##def load_sound(file):
##    sound = pygame.mixer.Sound(file)
##    return sound
##
##explosion_sound = load_sound('boom.wav')
##
##
##
##class Block(pygame.sprite.Sprite):
##    def __init__(self):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((50,50))
##        self.image.fill(green)
##        self.rect = self.image.get_rect()
##        self.rect.x = x//2
##        self.rect.y = 743 
##    def update(self):  
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                if self.rect.x > 5:
##                    self.rect.x -= 5
##            if event.key == pygame.K_RIGHT:
##                if self.rect.x < 545:
##                    self.rect.x += 5
## 
##good_block = Block() # change
##sprites.add(good_block) #change
##
##class Explosion(pygame.sprite.Sprite):
##    defaultlife = 12
##    def __init__(self,center):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.image.load('explosion.jpg')
##        self.rect = self.image.get_rect()
##        self.rect.center = center
##        self.life = self.defaultlife
##    def update(self):
##        self.life -= 1
##        if self.life <= 0:
##            self.kill()
##
##
##class Bad_Block(pygame.sprite.Sprite):
##    def __init__(self): #change
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((50,50)) #change
##        self.image.fill(red)#change
##        self.rect = self.image.get_rect()
##        self.rect.x = random.randint(50,550)
##        self.rect.y = 0
##    def update(self):
##       self.rect.centery += 5
##       if self.rect.y == 750:
##           sprites.add(Explosion(self.rect.center))# add
##           explosion_sound.play()
##           self.kill()
##
##
##
##move_x,move_y = 0,0 
##change_x, change_y = 0,0 
##win.set_caption('My Window')
##
##surface = win.set_mode(z)
##python = pygame.image.load('python basics.jpeg')
##window = True
##clock = pygame.time.Clock()
##click = 0
##colors = [white,black,red,blue,green]
##fill = white
##text_color = black
##circle_x,circle_y = x//2,y//2
##bad_block = bad_block_reload
##while window:
##    if bad_block:
##        bad_block -= 1
##    else:
##        block = Bad_Block()
##        bad_block = bad_block_reload
##        bad_sprites.add(block) #change
##    sprite_hits = pygame.sprite.spritecollide(good_block,bad_sprites,True)# add
##    for block in sprite_hits:
##        sprites.add(Explosion(good_block.rect.center))
##        sprites.add(Explosion(block.rect.center))
##        block.kill()
##        good_block.kill()
##        pygame.quit()
##        sys.exit()
##   
##
##    font = pygame.font.SysFont('timesnewroman', 20)
##    text = font.render('Start',0,text_color)
##    for event in pygame.event.get():
##        c_x,c_y = pygame.mouse.get_pos()
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit()            
##            window = False
##
##    surface.fill(fill)
####    surface.blit(text,(x//2-19,y//2-12))
##    pygame.draw.rect(surface,black,(5,5,590,790),3)
####    pygame.draw.circle(surface,black,(circle_x,circle_y),50,1)
##    movement = pygame.mouse.get_pos()
##    sprites.update()
##    sprites.draw(surface)
##    bad_sprites.draw(surface)
##    bad_sprites.update()
##    win.update()
##    clock.tick(30)



# pandas Connect to Sqlite DataBase


































##import numpy as np
##from matplotlib import pyplot as plt
##from matplotlib.ticker import MultipleLocator
##import calendar as c
##
##ot = [300,700,600,200,500,1000,500,800,100,400,200,500]
##
##
###ot = [300,700,600,200,500,1000,500,800,100,400,200,500]
##
##mon_per = np.array([  8.33333333,  16.66666667,  25.        ,  33.33333333,
##        41.66666667,  50.        ,  58.33333333,  66.66666667,
##        75.        ,  83.33333333,  91.66666667, 100.        ])
##    
##mon_per = mon_per[:len(ot)]
##
##
##fig,ax1 = plt.subplots(figsize=(14,6))
##
##mon = np.arange(1,len(mon_per)+1)
##
##tot = 0
##ot_p = []
##for i in ot:
##    tot += i
##    ot_p.append(tot)
##
##
##
##bins = np.arange(1,len(ot)+1)
##plt.xticks(np.arange(1,len(ot)+1),c.month_abbr[1:len(ot)+1], rotation = 60)
##ot_per = np.array(ot_p)*100/6000
##    
###plt.xticks(bins)
##ax1.plot(bins, np.full(len(ot),500), linewidth=2, color='c',label='Baseline')
##ax1.bar(bins,ot)
##
##ax2 = ax1.twinx()
##ax2.plot(mon,ot_per,linewidth=2,color='r',label='OT %/Buget')
##ax2.plot(mon,mon_per,linewidth=4, color='g',label='Baseline %')
##
##ax3 = ax1.twinx()
##ax3.spines['right'].set_position(('axes',1.15))
##ax3.plot(mon,ot_p,linewidth=3,color='k',label='Acumulative Overtime')
##
####majorLocator = MultipleLocator(2)
####ax1.yaxis.set_major_locator(majorLocator)
##
##
##plt.title('Overtime Cost and Percent')
##ax1.set_xlabel('Month')
##ax1.set_ylabel('Monthly Budget')
##ax2.set_ylabel('% of Yearly Budget')
##ax3.set_ylabel("Overtime Total", labelpad=20)
##
##fig.legend(bbox_to_anchor=(.4,.9))
##plt.show()







#######################################################################
##

##import numpy as np
##from matplotlib import pyplot as plt
##from matplotlib.ticker import MultipleLocator
##import calendar as c
##
##ot = [300,700,600,200,500,1000,500,800,100,400,200,500]
##
##
##ot = [300,700,600,200,500,1000,500,800,100,400,200,500]
##
##mon_per = np.array([  8.33333333,  16.66666667,  25.        ,  33.33333333,
##        41.66666667,  50.        ,  58.33333333,  66.66666667,
##        75.        ,  83.33333333,  91.66666667, 100.        ])
##    
##mon_per = mon_per[:len(ot)]
##
##
##fig,ax1 = plt.subplots(figsize=(6,4))
##
##mon = np.arange(1,len(mon_per)+1)
##
##tot = 0
##ot_p = []
##for i in ot:
##    tot += i
##    ot_p.append(tot)
##
##
##
##bins = np.arange(1,len(ot)+1)
##plt.xticks(np.arange(1,len(ot)+1),c.month_abbr[1:len(ot)+1], rotation = 60)
##ot_per = np.array(ot_p)*100/6000
##    
##plt.xticks(bins)
##ax1.plot(bins, np.full(len(ot),500), linewidth=2, color='c',label='Baseline')
##ax1.bar(bins,ot)
##
##ax2 = ax1.twinx()
##ax2.plot(mon,ot_per,linewidth=2,color='r',label='OT %/Buget')
##ax2.plot(mon,mon_per,linewidth=4, color='g',label='Baseline %')
##
##ax3 = ax1.twinx()
##ax3.spines['right'].set_position(('axes',1.15))
##ax3.plot(mon,ot_p,linewidth=3,color='k',label='Acumulative Overtime')
##
##majorLocator = MultipleLocator(2)
##ax1.yaxis.set_major_locator(majorLocator)
##
##
##plt.title('Overtime Cost and Percent')
##ax1.set_xlabel('Month')
##ax1.set_ylabel('Monthly Budget')
##ax2.set_ylabel('% of Yearly Budget')
##ax3.set_ylabel("Overtime Total", labelpad=10)
##
##fig.legend(bbox_to_anchor=(.5,.85))
##plt.show()






### more numpy slicing 
##
##
##
##import numpy as np
##
##
##x = np.arange(27).reshape(3,3,3)






### calendar month range function
##
##
##import calendar



















