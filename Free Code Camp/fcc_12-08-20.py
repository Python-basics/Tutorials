Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> import random
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>> help(random.randint)
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

>>> door = random.randint(1,5)
>>> doort
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    doort
NameError: name 'doort' is not defined
>>> door
2
>>> type(door)
<class 'int'>
>>> x = 4
>>> y = 1.2
>>> name = "Sam"
>>> type(x)
<class 'int'>
>>> type(y)
<class 'float'>
>>> type(name)
<class 'str'>
>>> x = '4'
>>> x
'4'
>>> type(x)
<class 'str'>
>>> x = int(x)
>>> x
4
>>> 4 == 4
True
>>> 4 != 4
False
>>> 4 != 5
True
>>> name
'Sam'
>>> "My name is " + name
'My name is Sam'
>>> age
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    age
NameError: name 'age' is not defined
>>> age = 43
>>> "I am " + age
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    "I am " + age
TypeError: can only concatenate str (not "int") to str
>>> "I am " + str(age)
'I am 43'
>>> life = 5
>>> life
5
>>> life = life - 1
>>> life
4
>>> life -= 1
>>> life
3
>>> name
'Sam'
>>> name[0]
'S'
>>> name[1]
'a'
>>> name[2]
'm'
>>> dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> name
'Sam'
>>> help(name.lower)
Help on built-in function lower:

lower() method of builtins.str instance
    Return a copy of the string converted to lowercase.

>>> name
'Sam'
>>> name.lower()
'sam'
>>> name
'Sam'
>>> name.upper()
'SAM'
>>> name
'Sam'
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
ESCAPE ROOM FIND THE RIGHT DOOR TO EXIT
EACH TIME YOU FAIL THE DOOR WILL CHANGE POSITION
Door:  2
Life:  5
Enter a guess of door: 2
Well, done, you managed to escape!
Do you want to play agian?
Yes or Noy
Door:  2
Life:  5
Enter a guess of door: 3
Guess Again!
Door:  4
Life:  4
Enter a guess of door: 1
Guess Again!
Door:  4
Life:  3
Enter a guess of door: 1
Guess Again!
Door:  2
Life:  2
Enter a guess of door: 1
Guess Again!
Door:  3
Life:  1
Enter a guess of door: 1
You Lose all of your life. The correct door was 3
Do you want to play agian?
Yes or Noy
Door:  1
Life:  5
Enter a guess of door: 5
Guess Again!
Door:  3
Life:  4
Enter a guess of door: 2
Guess Again!
Door:  4
Life:  3
Enter a guess of door: 3
Guess Again!
Door:  1
Life:  2
Enter a guess of door: 2
Guess Again!
Door:  3
Life:  1
Enter a guess of door: 1
You Lose all of your life. The correct door was 3
Do you want to play agian?
Yes or Non
Game Over
Thank You for Playing!!!!
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> file
'thur Nov 28 2020 18:16:16'
>>> dir(file)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(file.replace)
Help on built-in function replace:

replace(old, new, count=-1, /) method of builtins.str instance
    Return a copy with all occurrences of substring old replaced by new.
    
      count
        Maximum number of occurrences to replace.
        -1 (the default value) means replace all occurrences.
    
    If the optional argument count is given, only the first count occurrences are
    replaced.

>>> file.replace(' ','_')
'thur_Nov_28_2020_18:16:16'
>>> file
'thur Nov 28 2020 18:16:16'
>>> file = file.replace(' ','_').replace(':','_')
>>> file
'thur_Nov_28_2020_18_16_16'
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
thur_Nov_28_2020_18_16_16
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
thur_Nov_28_2020_18_16_16
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> file
'thur_Nov_28_2020_18_16_16'
>>> dir(file)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'file', 're']
>>> __name__
'__main__'
>>> main()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    main()
NameError: name 'main' is not defined
>>> main
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    main
NameError: name 'main' is not defined
>>> __name__
'__main__'
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> __name__
'__main__'
>>> x
1
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python36-32\ideas.py
__main__
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python36-32\ideas.py
__main__
>>> x
1
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python36-32\ideas.py
__main__
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python36-32\ideas.py
__main__
>>> x
1
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python36-32\test.py
ideas
__main__
>>> x
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    x
NameError: name 'x' is not defined

    
    
    
   
