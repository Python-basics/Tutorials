
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



#  8/11/20 

# recursion, command line, and dictionaries


# ! factorial

# 3! 

##def fact(x):
##    tot = 1
##    while x > 0:
##        tot *= x
##        x -= 1
##    print(tot)

##tests = [3,4,1,0,-2,8,12,18,100]
##
##
##def fact(n):
##    if n > -1:
##        if n == 0:
##            return 1
##        else:
##            return n * fact(n-1)
##        
##    else:
##        return "Negative"
##
##
##
##for test in tests:
##    print(fact(test))



### lottery powerball
##
##
###  69/5 * 68/4 * 67/3 * 66/2 * 65/1 * 26  
##
###           (69! / 5!*(69-5)!)*26  
##
##
##def odds(balls,pick,power=False):
##    """Enter number a regular balls, number of balls
##picked, and if they are using a powerball, you will be asked
##for the number of powerballs"""
##    from math import factorial as fact
##    p_ball = 1
##    if power:
##        p_ball = int(input("Enter Number of powerballs: "))
##    return (fact(balls))/(fact(5)*fact(balls-pick))*p_ball
##    
##    
####print("{:,}".format(odds(69,6)))
##
##print(f"{odds(69,6):,}")


##import sys
##
##print(sys.argv)

# dictionary

d = {}

d['Sam'] = 43


fruit = {'banana': 3,'apples': 1, 'grapes': 2}


for k,v in fruit.items():
    print(f'I have {v} {k}')

    
   
# 8/18/20 finish dict Scope and decorators


from string import ascii_lowercase as lower



##key = {}
##
##
##for i in range(len(lower)):
##    key[lower[i]] = 1+i

    

##letters = lower
##
##num = list(range(1,27))
##
##key = dict(zip(letters,num))


file = ''' 1845
                                   THE RAVEN
                               by Edgar Allan Poe

    Once upon a midnight dreary, while I pondered, weak and weary,
  Over many a quaint and curious volume of forgotten lore,
    While I nodded, nearly napping, suddenly there came a tapping,
   As of some one gently rapping, rapping at my chamber door.
  "'Tis some visitor," I muttered, "tapping at my chamber door-
                Only this, and nothing more."

    Ah, distinctly I remember it was in the bleak December,
  And each separate dying ember wrought its ghost upon the floor.
    Eagerly I wished the morrow;- vainly I had sought to borrow
    From my books surcease of sorrow- sorrow for the lost Lenore-
  For the rare and radiant maiden whom the angels name Lenore-
                Nameless here for evermore.

    And the silken sad uncertain rustling of each purple curtain
  Thrilled me- filled me with fantastic terrors never felt before;
    So that now, to still the beating of my heart, I stood repeating,
    "'Tis some visitor entreating entrance at my chamber door-
  Some late visitor entreating entrance at my chamber door;-
                This it is, and nothing more."

    Presently my soul grew stronger; hesitating then no longer,
  "Sir," said I, "or Madam, truly your forgiveness I implore;
    But the fact is I was napping, and so gently you came rapping,
    And so faintly you came tapping, tapping at my chamber door,
  That I scarce was sure I heard you"- here I opened wide the door;-
                Darkness there, and nothing more.

    Deep into that darkness peering, long I stood there wondering,
        fearing,
  Doubting, dreaming dreams no mortals ever dared to dream before;
    But the silence was unbroken, and the stillness gave no token,
    And the only word there spoken was the whispered word, "Lenore!"
  This I whispered, and an echo murmured back the word, "Lenore!"-
                Merely this, and nothing more.

    Back into the chamber turning, all my soul within me burning,
   Soon again I heard a tapping somewhat louder than before.
    "Surely," said I, "surely that is something at my window lattice:
    Let me see, then, what thereat is, and this mystery explore-
  Let my heart be still a moment and this mystery explore;-
                'Tis the wind and nothing more."

    Open here I flung the shutter, when, with many a flirt and
        flutter,
  In there stepped a stately raven of the saintly days of yore;
    Not the least obeisance made he; not a minute stopped or stayed
        he;
    But, with mien of lord or lady, perched above my chamber door-
  Perched upon a bust of Pallas just above my chamber door-
                Perched, and sat, and nothing more.

   Then this ebony bird beguiling my sad fancy into smiling,
  By the grave and stern decorum of the countenance it wore.
   "Though thy crest be shorn and shaven, thou," I said, "art sure no
        craven,
   Ghastly grim and ancient raven wandering from the Nightly shore-
  Tell me what thy lordly name is on the Night's Plutonian shore!"
                Quoth the Raven, "Nevermore."

    Much I marvelled this ungainly fowl to hear discourse so plainly,
  Though its answer little meaning- little relevancy bore;
    For we cannot help agreeing that no living human being
    Ever yet was blest with seeing bird above his chamber door-
  Bird or beast upon the sculptured bust above his chamber door,
                With such name as "Nevermore."

    But the raven, sitting lonely on the placid bust, spoke only
  That one word, as if his soul in that one word he did outpour.
    Nothing further then he uttered- not a feather then he fluttered-
    Till I scarcely more than muttered, "other friends have flown
        before-
  On the morrow he will leave me, as my hopes have flown before."
                Then the bird said, "Nevermore."

     Startled at the stillness broken by reply so aptly spoken,
  "Doubtless," said I, "what it utters is its only stock and store,
     Caught from some unhappy master whom unmerciful Disaster
     Followed fast and followed faster till his songs one burden bore-
  Till the dirges of his Hope that melancholy burden bore
                Of 'Never- nevermore'."

    But the Raven still beguiling all my fancy into smiling,
  Straight I wheeled a cushioned seat in front of bird, and bust and
        door;
    Then upon the velvet sinking, I betook myself to linking
    Fancy unto fancy, thinking what this ominous bird of yore-
  What this grim, ungainly, ghastly, gaunt and ominous bird of yore
                Meant in croaking "Nevermore."

    This I sat engaged in guessing, but no syllable expressing
  To the fowl whose fiery eyes now burned into my bosom's core;
    This and more I sat divining, with my head at ease reclining
    On the cushion's velvet lining that the lamplight gloated o'er,
  But whose velvet violet lining with the lamplight gloating o'er,
                She shall press, ah, nevermore!

    Then methought the air grew denser, perfumed from an unseen censer
  Swung by Seraphim whose footfalls tinkled on the tufted floor.
    "Wretch," I cried, "thy God hath lent thee- by these angels he
        hath sent thee
    Respite- respite and nepenthe, from thy memories of Lenore!
  Quaff, oh quaff this kind nepenthe and forget this lost Lenore!"
                Quoth the Raven, "Nevermore."

    "Prophet!" said I, "thing of evil!- prophet still, if bird or
        devil!-
  Whether Tempter sent, or whether tempest tossed thee here ashore,
    Desolate yet all undaunted, on this desert land enchanted-
    On this home by horror haunted- tell me truly, I implore-
  Is there- is there balm in Gilead?- tell me- tell me, I implore!"
                Quoth the Raven, "Nevermore."

    "Prophet!" said I, "thing of evil- prophet still, if bird or
        devil!
  By that Heaven that bends above us- by that God we both adore-
    Tell this soul with sorrow laden if, within the distant Aidenn,
    It shall clasp a sainted maiden whom the angels name Lenore-
  Clasp a rare and radiant maiden whom the angels name Lenore."
                Quoth the Raven, "Nevermore."

    "Be that word our sign in parting, bird or fiend," I shrieked,
        upstarting-
  "Get thee back into the tempest and the Night's Plutonian shore!
    Leave no black plume as a token of that lie thy soul hath spoken!
    Leave my loneliness unbroken!- quit the bust above my door!
  Take thy beak from out my heart, and take thy form from off my
        door!"
               Quoth the Raven, "Nevermore."

    And the Raven, never flitting, still is sitting, still is sitting
  On the pallid bust of Pallas just above my chamber door;
    And his eyes have all the seeming of a demon's that is dreaming,
    And the lamplight o'er him streaming throws his shadow on the
        floor;
  And my soul from out that shadow that lies floating on the floor
                Shall be lifted- nevermore!

                             -THE END-'''

##file = file.split()
##
##book = {}
##
##for word in file:
##    if word not in book:
##        book[word] = 1
##    else:
##        book[word] += 1
        


##def phone_number():
##    x = input("Enter your phone number: ")
##    print(f'({x[:3]}){x[3:6]}-{x[6:]}')
##
##def ssn():
##    x = input("Enter your ssn: ")
##    print(f'{x[:3]}-{x[3:5]}-{x[5:]}')
##    
##
##students = ['steve','john','adam','will']
##
##s_dict = {student[0].upper(): student for student in students}
##
##print(s_dict)


### local (nonlocal) global built-in
##
##from math import pi
##
####pi = 3.14
##def area(r):
##    global pi
####    pi = 3.14159
##    return pi*r**2
##
##print(area(3))

# enclosing  enclosed (nonlocal)


##def exp(n):
##    n = 1
##    def num(x):
##        nonlocal n
##        return x**n
##    return num
##
##
##square = exp(2)
##
##cube = exp(3)


# decoratros


##def cube(func):
##    def wrapper(arg):
##        return func(arg)**3
##    return wrapper
##
##@cube
##def num(x):
##    return x


##def upper(func):
##    def wrapper():
##        return func().upper()
##    return wrapper
##
##@upper
##def hi():
##    return "Hi how are you?"





##from random import shuffle, choice
##
##
##def game(x,change=False):
##    doors = ['goat','goat','car']
##    shuffle(doors)
####    print(doors)
##    wins, losses = 0,0
##
##    def no_switch():
##        nonlocal wins,losses
##        if 'car' == choice(doors):
##            wins += 1
##        else:
##            losses += 1
##
##    def switch():
##        door = ['goat','goat','car']
##        nonlocal wins, losses
##        door.pop(choice(range(3)))
##        door.remove('goat')
##        second_choice = door[0]
##        if second_choice == 'car':
##            wins += 1
##        else:
##            losses += 1
##
##    
##    for i in range(x):
##        if change:
##            switch()
##        else:
##            no_switch()
##    print(f'wins: {wins} percent wins: {(wins/x)}')
##    print(f'losses: {losses} percent losses: {(losses/x)}')
##        
##
##game(10000)
##print()
##game(10000,True)



# urllib


##import urllib.request as url
##
##
##
##page = url.urlopen('http://www.textfiles.com/etext/AUTHORS/POE/poe-raven-702.txt')
##
##text = page.read()
##
##text = text.decode()
##
##page.close()
##
##
##file = open('raven.txt','w')
##
##file.write(text)
##
##file.close()


    

file = file.split()

book = {}

for word in file:
    if word not in book:
        book[word] = 1
    else:
        book[word] += 1
    

def last(x):
    return x[-1]

book = book.items()

sort_book = sorted(book,key=last,reverse=True)

for i in sort_book[:10]:
    print(i[0], ':', i[1])

def my_list():
    while True:
        with open('shopping_list.txt','a+') as file:
            print("""type anytime
EXIT: to quit
LIST: To Read and Delete
""")
            item = input('enter item: ')
            if item == 'EXIT':
                break
            elif item == 'please tell':
                print(file.tell())
            elif item == 'LIST':
                file.seek(0)
##                print(file.read())
                items = list(enumerate(file.read().split(),1))
                for count, item in items:
                    print(f"{count:3d}) {item}")
##                remove = int(input('enter number to delete or 0 to continue: '))
                while True:
                    try:
                        remove = int(input('enter number to delete or 0 to continue: '))
                        if remove == 0:
                            break
##                            continue
                        else:
                            del items[remove - 1]
                            with open('shopping_list.txt', 'w') as file:
                                for item in items:
                                    file.write(item[1] + '\n')
                    except ValueError:
                        print("If you don't want to delete please enter 0")
                          
            else:
                file.write(item + '\n')
            

my_list()       



##def my_list():
##    while True:
##        with open('shopping_list.txt','a+') as file:
##            print("""type anytime
##EXIT: to quit
##LIST: To Read and Delete
##""")
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
##                    print(f"{count:3d}) {item}")
####                remove = int(input('enter number to delete or 0 to continue: '))
##                while True:
##                    try:
##                        remove = int(input('enter number to delete or 0 to continue: '))
##                        if remove == 0:
##                            break
####                            continue
##                        else:
##                            del items[remove - 1]
##                            with open('shopping_list.txt', 'w+') as file:
##                                for item in items:
##                                    file.write(item[1] + '\n')
##                                file.seek(0)
##                                items = list(enumerate(file.read().split(),1))
##                                for count, item in items:
##                                    print(f"{count:3d}) {item}")
##                    except ValueError:
##                        print("If you don't want to delete please enter 0")
##                          
##            else:
##                file.write(item + '\n')
##            
##
##my_list()              




##class rect():
##
##    def __init__(self,length,width):
##        self.length = length
##        self.width = width
####        print(f"Your rectangle is {length} by {width}")
##
##    def __repr__(self):
##        return "rect({self.length},{self.width})".format(self=self)
##
##    def __str__(self):
##        return f"Your rectangle is {self.width} by {self.length}"
##
##    def perim(self):
##        print(2*self.width*self.length)
##
##    def area(self):
##        print(self.width*self.length)

    
##class Dog():
##
##    species = "Canine"
##    voice = "Bark"
##
##    
##class poodle(Dog):
##    pass

    
##name = "Sam"
##
##name = iter(name)
##
####for i in name:
####    print(i)
    
        
# generatros



##def series(num):
##    n = 0
##    while n < num:
##        yield n
##        n += 1
##
##
##five = series(5)



'''
78 --> 80
77 --> 77
93 --> 95
72 --> 72
74 --> 75


'''

##def fives(x):
##    if x%5 == 4:
##        x += 1
##    elif x%5 == 3:
##        x += 2
##    print(x)

def fives(x):
    if x%5 == 3 or x%5 == 4:
        x += (5 - x%5)
    print(x)
        


grades = [72,98,94,83,71,73,100]

for grade in grades:
    print(grade, end=" "), fives(grade)
    
    
'''
Find the 4 hidden X's
  A B C D E F
1 O O O O O O
2 O O O O O O
3 O O O O O O
4 O O O O O O
5 O O O O O O
6 O O O O O O

Q to quit
enter move (eg. A5):
'''

##x = ['sam', 41,'bob',36,'steve','20']
##
##
##name = [True for i in x if str(i).isnumeric()]
##
##
####name = [False if str(i).isnumeric() else True for i in x]

from string import ascii_uppercase as letters

from random import choice

a_f = list(letters[:6])

num = iter(range(1,7))

hidden = [choice(a_f) + str(choice(list(range(1,7)))) for i in range(4)]

arr = [[ "O" for i in range(6)] for i in range(6)]

play = True

while play:
    num = iter(range(1,7))
    print(hidden)
    print(f"Find the {len(hidden)} hidden X's")
    print('  '+' '.join(a_f))
    for i in arr:
        print(next(num),end = ' ')
        print(' '.join(i))
    move = input("""Q to Quit
Enter move (eg. A5):""")
    if move.lower() == 'q':
        play = False
    else:
        if move in hidden:
            hidden.pop(hidden.index(move))
            move = list(move)
            arr[int(move[1]) - 1][a_f.index(move[0])] = "X"
        else:
            move = list(move)
            arr[int(move[1]) - 1][a_f.index(move[0])] = " "



# Chicken Nuggets and itertools 10/6/20


t,n,s = 20,9,6

def nuggets(ttl):
    global x
    x = {}
    for i in range(10):
        for j in range(10):
            for k in range(10):
                tot = i*t+j*n+k*s
                x[tot] = [i,j,k]
                if ttl == tot:
                    break
            if ttl == tot:
                break
        if ttl == tot:
            break
    print(f"""{ttl}
{x[ttl][2]}: 6 piece
{x[ttl][1]}: 9 piece
{x[ttl][0]}: 20 piece""")
                

comb = []

for i in range(101):
    try:
        nuggets(i)
        comb.append(i)
    except:
        print(i, 'no results')





from itertools import chain



x = 'abc'
y = 'def'
z = 'ghi'

for i in chain(x,y,z):
    print(i)

arr = [x,y,z]


for i in chain.from_iterable(arr):
    print(i)
    

from itertools import combinations as comb


letter = "ABCDEFG"


x = comb(letter,3)

y = [''.join(i) for i in x]



from itertools import count

x = count(1)

'''

    1 
  2 3 4 
5 6 7 8 9 

'''

from itertools import count

start = count(1,2) # it's the starting point

num = count(1)

for i in range(1,4):
    print(('  ')*(3-i), end = '')
    for j in range(next(start)):
        print(next(num), end = ' ')
    print()
    
    

    
# tkinter calculator gui



import tkinter as tk
import tkinter.ttk as ttk


win = tk.Tk()

win.title("Calculator")

##win.configure(width=300,height=300,background='red')

##win.geometry('300x300+500+200')


##label = tk.Label(win,text="Hello World")
##button = ttk.Button(win,text="Hello")
##
##label.pack()
##button.pack()

expr = ''

text = tk.StringVar()


def press(num):
    global expr
    expr += str(num)
    text.set(expr)

def clr():
    global expr
    expr = ''
    text.set(expr)

def equal():
    global expr
    ttl = str(eval(expr))
    text.set(ttl)

entry = ttk.Entry(win,justify='right',textvariable=text)
entry.grid(row=0,columnspan=4,sticky='nsew')

button_7 = ttk.Button(win,text='7',command=lambda:press(7))
button_7.grid(row=1,column=0)

button_8 = ttk.Button(win,text='8',command=lambda:press(8))
button_8.grid(row=1,column=1)

button_9 = ttk.Button(win,text='9',command=lambda:press(9))
button_9.grid(row=1, column=2)

button_d = ttk.Button(win,text='/',command=lambda:press('/'))
button_d.grid(row=1,column=3)


button_4 = ttk.Button(win,text='4',command=lambda:press(4))
button_4.grid(row=2,column=0)

button_5 = ttk.Button(win,text='5',command=lambda:press(5))
button_5.grid(row=2,column=1)

button_6 = ttk.Button(win,text='6',command=lambda:press(6))
button_6.grid(row=2, column=2)

button_m = ttk.Button(win,text='*',command=lambda:press('*'))
button_m.grid(row=2,column=3)


button_1 = ttk.Button(win,text='1',command=lambda:press(1))
button_1.grid(row=3,column=0)

button_2 = ttk.Button(win,text='2',command=lambda:press(2))
button_2.grid(row=3,column=1)

button_3 = ttk.Button(win,text='3',command=lambda:press(3))
button_3.grid(row=3, column=2)

button_s = ttk.Button(win,text='-',command=lambda:press('-'))
button_s.grid(row=3,column=3)


button_0 = ttk.Button(win,text='0',command=lambda:press(0))
button_0.grid(row=4,column=0)

button_dot = ttk.Button(win,text='.',command=lambda:press('.'))
button_dot.grid(row=4,column=1)

button_c = ttk.Button(win,text='c',command=clr)
button_c.grid(row=4, column=2)

button_a = ttk.Button(win,text='+',command=lambda:press('+'))
button_a.grid(row=4,column=3)

button_e = ttk.Button(win,text='=',command=equal)
button_e.grid(row=5,columnspan=4,sticky='nsew')


win.mainloop()

    






























