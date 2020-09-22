Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Traceback (most recent call last):
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 1094, in <module>
    hidden = [choice(a_f) + str(choice(list(range(1,7)))) for i in range(4)]
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 1094, in <listcomp>
    hidden = [choice(a_f) + str(choice(list(range(1,7)))) for i in range(4)]
NameError: name 'choice' is not defined
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> hidden
['F3', 'C6', 'A1', 'B6']
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
  A B C D E F
1 O O O O O O
2 O O O O O O
3 O O O O O O
4 O O O O O O
5 O O O O O O
6 O O O O O O
  A B C D E F
Traceback (most recent call last):
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 1106, in <module>
    print(next(num),end = ' ')
StopIteration
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
  A B C D E F
1 O O O O O O
2 O O O O O O
3 O O O O O O
4 O O O O O O
5 O O O O O O
6 O O O O O O
Q to Quit
Enter move (eg. A5):q
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
['E6', 'F4', 'B1', 'B5']
  A B C D E F
1 O O O O O O
2 O O O O O O
3 O O O O O O
4 O O O O O O
5 O O O O O O
6 O O O O O O
Q to Quit
Enter move (eg. A5):q
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(str.lower)
Help on method_descriptor:

lower(self, /)
    Return a copy of the string converted to lowercase.

>>> 'SAM'.lower()
'sam'
>>> name = "SAM"
>>> name
'SAM'
>>> name.lower()
'sam'
>>> name
'SAM'
>>> lower = name.lower()
>>> name
'SAM'
>>> lower
'sam'
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
['E4', 'F1', 'B3', 'D1']
  A B C D E F
1 O O O O O O
2 O O O O O O
3 O O O O O O
4 O O O O O O
5 O O O O O O
6 O O O O O O
Q to Quit
Enter move (eg. A5):q
>>> 
B= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
['F4', 'C6', 'C6', 'A4']
  A B C D E F
1 O O O O O O
2 O O O O O O
3 O O O O O O
4 O O O O O O
5 O O O O O O
6 O O O O O O
Q to Quit
Enter move (eg. A5):h
['F4', 'C6', 'C6', 'A4']
  A B C D E F
1 O O O O O O
2 O O O O O O
3 O O O O O O
4 O O O O O O
5 O O O O O O
6 O O O O O O
Q to Quit
Enter move (eg. A5):q
>>> hidden
['F4', 'C6', 'C6', 'A4']
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
['B1', 'C4', 'F3', 'E4']
  A B C D E F
1 O O O O O O
2 O O O O O O
3 O O O O O O
4 O O O O O O
5 O O O O O O
6 O O O O O O
Q to Quit
Enter move (eg. A5):q
>>> hidden
['B1', 'C4', 'F3', 'E4']
>>> help()

Welcome to Python 3.8's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.8/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> in
Membership test operations
**************************

The operators "in" and "not in" test for membership.  "x in s"
evaluates to "True" if *x* is a member of *s*, and "False" otherwise.
"x not in s" returns the negation of "x in s".  All built-in sequences
and set types support this as well as dictionary, for which "in" tests
whether the dictionary has a given key. For container types such as
list, tuple, set, frozenset, dict, or collections.deque, the
expression "x in y" is equivalent to "any(x is e or x == e for e in
y)".

For the string and bytes types, "x in y" is "True" if and only if *x*
is a substring of *y*.  An equivalent test is "y.find(x) != -1".
Empty strings are always considered to be a substring of any other
string, so """ in "abc"" will return "True".

For user-defined classes which define the "__contains__()" method, "x
in y" returns "True" if "y.__contains__(x)" returns a true value, and
"False" otherwise.

For user-defined classes which do not define "__contains__()" but do
define "__iter__()", "x in y" is "True" if some value "z", for which
the expression "x is z or x == z" is true, is produced while iterating
over "y". If an exception is raised during the iteration, it is as if
"in" raised that exception.

Lastly, the old-style iteration protocol is tried: if a class defines
"__getitem__()", "x in y" is "True" if and only if there is a non-
negative integer index *i* such that "x is y[i] or x == y[i]", and no
lower integer index raises the "IndexError" exception.  (If any other
exception is raised, it is as if "in" raised that exception).

The operator "not in" is defined to have the inverse truth value of
"in".

Related help topics: SEQUENCEMETHODS

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
===== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
['F2', 'F5', 'F6', 'F4']
  A B C D E F
1 O O O O O O
2 O O O O O O
3 O O O O O O
4 O O O O O O
5 O O O O O O
6 O O O O O O
Q to Quit
Enter move (eg. A5):q
>>> hidden
['F2', 'F5', 'F6', 'F4']
>>> name = "Sam"
>>> "S" in name
True
>>> 'F2' in hidden
True
>>> 'f2' in hidden
False
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.8's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.8/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> in
Membership test operations
**************************

The operators "in" and "not in" test for membership.  "x in s"
evaluates to "True" if *x* is a member of *s*, and "False" otherwise.
"x not in s" returns the negation of "x in s".  All built-in sequences
and set types support this as well as dictionary, for which "in" tests
whether the dictionary has a given key. For container types such as
list, tuple, set, frozenset, dict, or collections.deque, the
expression "x in y" is equivalent to "any(x is e or x == e for e in
y)".

For the string and bytes types, "x in y" is "True" if and only if *x*
is a substring of *y*.  An equivalent test is "y.find(x) != -1".
Empty strings are always considered to be a substring of any other
string, so """ in "abc"" will return "True".

For user-defined classes which define the "__contains__()" method, "x
in y" returns "True" if "y.__contains__(x)" returns a true value, and
"False" otherwise.

For user-defined classes which do not define "__contains__()" but do
define "__iter__()", "x in y" is "True" if some value "z", for which
the expression "x is z or x == z" is true, is produced while iterating
over "y". If an exception is raised during the iteration, it is as if
"in" raised that exception.

Lastly, the old-style iteration protocol is tried: if a class defines
"__getitem__()", "x in y" is "True" if and only if there is a non-
negative integer index *i* such that "x is y[i] or x == y[i]", and no
lower integer index raises the "IndexError" exception.  (If any other
exception is raised, it is as if "in" raised that exception).

The operator "not in" is defined to have the inverse truth value of
"in".

Related help topics: SEQUENCEMETHODS

help> keyword
Help on module keyword:

NAME
    keyword - Keywords (from "Grammar/Grammar")

DESCRIPTION
    This file is automatically generated; please don't muck it up!
    
    To update the symbols in this file, 'cd' to the top directory of
    the python source tree and run:
    
        python3 -m Parser.pgen.keywordgen Grammar/Grammar                                       Grammar/Tokens                                       Lib/keyword.py
    
    Alternatively, you can run 'make regen-keyword'.

FUNCTIONS
    iskeyword = __contains__(...) method of builtins.frozenset instance
        x.__contains__(y) <==> y in x.

DATA
    __all__ = ['iskeyword', 'kwlist']
    kwlist = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'aw...

FILE
    c:\users\samue\appdata\local\programs\python\python38-32\lib\keyword.py


help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> help(list.pop)
Help on method_descriptor:

pop(self, index=-1, /)
    Remove and return item at index (default last).
    
    Raises IndexError if list is empty or index is out of range.

>>> arr
[['O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O']]
>>> for i in arr:
	print(i)

	
['O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O']
>>> arr[0][2] = " "
>>> for i in arr:
	print(i)

	
['O', 'O', ' ', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O']
>>> arr[0]
['O', 'O', ' ', 'O', 'O', 'O']
>>> arr[0][5] = 'X'
>>> arr[0]
['O', 'O', ' ', 'O', 'O', 'X']
>>> type(arr)
<class 'list'>
>>> type(arr[0])
<class 'list'>
>>> type(arr[0][0])
<class 'str'>
>>> hidden
['F2', 'F5', 'F6', 'F4']
>>> 
===== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
['C3', 'E6', 'A4', 'D4']
Find the 4 hidden X's
  A B C D E F
1 O O O O O O
2 O O O O O O
3 O O O O O O
4 O O O O O O
5 O O O O O O
6 O O O O O O
Q to Quit
Enter move (eg. A5):q
>>> hidden
['C3', 'E6', 'A4', 'D4']
>>> help(list.index)
Help on method_descriptor:

index(self, value, start=0, stop=2147483647, /)
    Return first index of value.
    
    Raises ValueError if the value is not present.

>>> list("A5")
['A', '5']
>>> 
===== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
['A4', 'B5', 'C2', 'D5']
Find the 4 hidden X's
  A B C D E F
1 O O O O O O
2 O O O O O O
3 O O O O O O
4 O O O O O O
5 O O O O O O
6 O O O O O O
Q to Quit
Enter move (eg. A5):A5
['A4', 'B5', 'C2', 'D5']
Find the 4 hidden X's
  A B C D E F
1 O O O O O O
2 O O O O O O
3 O O O O O O
4 O O O O O O
5 O O O O O O
6 O O O O O O
Q to Quit
Enter move (eg. A5):A4
['B5', 'C2', 'D5']
Find the 3 hidden X's
  A B C D E F
1 O O O O O O
2 O O O O O O
3 O O O O O O
4 X O O O O O
5 O O O O O O
6 O O O O O O
Q to Quit
Enter move (eg. A5):C2
['B5', 'D5']
Find the 2 hidden X's
  A B C D E F
1 O O O O O O
2 O O X O O O
3 O O O O O O
4 X O O O O O
5 O O O O O O
6 O O O O O O
Q to Quit
Enter move (eg. A5):B6
['B5', 'D5']
Find the 2 hidden X's
  A B C D E F
1 O O O O O O
2 O O X O O O
3 O O O O O O
4 X O O O O O
5 O O O O O O
6 O O O O O O
Q to Quit
Enter move (eg. A5):Q
>>> 
===== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
['B2', 'C4', 'B5', 'D3']
Find the 4 hidden X's
  A B C D E F
1 O O O O O O
2 O O O O O O
3 O O O O O O
4 O O O O O O
5 O O O O O O
6 O O O O O O
Q to Quit
Enter move (eg. A5):B2
['C4', 'B5', 'D3']
Find the 3 hidden X's
  A B C D E F
1 O O O O O O
2 O X O O O O
3 O O O O O O
4 O O O O O O
5 O O O O O O
6 O O O O O O
Q to Quit
Enter move (eg. A5):B1
['C4', 'B5', 'D3']
Find the 3 hidden X's
  A B C D E F
1 O   O O O O
2 O X O O O O
3 O O O O O O
4 O O O O O O
5 O O O O O O
6 O O O O O O
Q to Quit
Enter move (eg. A5):F6
['C4', 'B5', 'D3']
Find the 3 hidden X's
  A B C D E F
1 O   O O O O
2 O X O O O O
3 O O O O O O
4 O O O O O O
5 O O O O O O
6 O O O O O  
Q to Quit
Enter move (eg. A5):C3
['C4', 'B5', 'D3']
Find the 3 hidden X's
  A B C D E F
1 O   O O O O
2 O X O O O O
3 O O   O O O
4 O O O O O O
5 O O O O O O
6 O O O O O  
Q to Quit
Enter move (eg. A5):C4
['B5', 'D3']
Find the 2 hidden X's
  A B C D E F
1 O   O O O O
2 O X O O O O
3 O O   O O O
4 O O X O O O
5 O O O O O O
6 O O O O O  
Q to Quit
Enter move (eg. A5):Q
>>> move
'Q'
>>> a_f
['A', 'B', 'C', 'D', 'E', 'F']
>>> move = 'C4'
>>> move = list(move)
>>> move
['C', '4']
>>> a_f.index("C")
2
>>> 