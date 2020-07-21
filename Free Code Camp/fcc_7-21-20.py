Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Please enter a number: 5
Traceback (most recent call last):
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 258, in <module>
    time_table()
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 255, in time_table
    print(x/2)
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> help(input)
Help on built-in function input in module builtins:

input(prompt=None, /)
    Read a string from standard input.  The trailing newline is stripped.
    
    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.
    
    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.

>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Please enter a number: 6
3.0
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Please enter a number: 6
0
0
0
0
0
0
0
1
2
3
4
5
0
2
4
6
8
10
0
3
6
9
12
15
0
4
8
12
16
20
0
5
10
15
20
25
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Please enter a number: 4
0000012302460369
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Please enter a number: 4
0000
0123
0246
0369
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Please enter a number: 5
0 0 0 0 0 
0 1 2 3 4 
0 2 4 6 8 
0 3 6 9 12 
0 4 8 12 16 
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Please enter a number: 4
 0  0  0  0 
 0  1  2  3 
 0  2  4  6 
 0  3  6  9 
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Please enter a number: 5
 0  0  0  0  0 
 0  1  2  3  4 
 0  2  4  6  8 
 0  3  6  9 12 
 0  4  8 12 16 
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Please enter a number: 5
  0   0   0   0   0 
  0   1   2   3   4 
  0   2   4   6   8 
  0   3   6   9  12 
  0   4   8  12  16 
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Please enter a number: m
Traceback (most recent call last):
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 262, in <module>
    time_table()
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 254, in time_table
    x = int(input("Please enter a number: "))
ValueError: invalid literal for int() with base 10: 'm'
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

help> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Please enter a number: 5
  0   0   0   0   0 
  0   1   2   3   4 
  0   2   4   6   8 
  0   3   6   9  12 
  0   4   8  12  16 
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Please enter a number: 
m
Oops, please enter a number.
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Please enter a number: 5
  0   0   0   0   0 
  0   1   2   3   4 
  0   2   4   6   8 
  0   3   6   9  12 
  0   4   8  12  16 
Please enter a number: 4
  0   0   0   0 
  0   1   2   3 
  0   2   4   6 
  0   3   6   9 
Please enter a number: 3
  0   0   0 
  0   1   2 
  0   2   4 
Please enter a number: n
Oops, please enter a number.
Please enter a number: 5
  0   0   0   0   0 
  0   1   2   3   4 
  0   2   4   6   8 
  0   3   6   9  12 
  0   4   8  12  16 
Please enter a number: 6
  0   0   0   0   0   0 
  0   1   2   3   4   5 
  0   2   4   6   8  10 
  0   3   6   9  12  15 
  0   4   8  12  16  20 
  0   5  10  15  20  25 
Please enter a number: 7
  0   0   0   0   0   0   0 
  0   1   2   3   4   5   6 
  0   2   4   6   8  10  12 
  0   3   6   9  12  15  18 
  0   4   8  12  16  20  24 
  0   5  10  15  20  25  30 
  0   6  12  18  24  30  36 
Please enter a number: 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Please enter a number: 5
  0   0   0   0   0   0 
  0   1   2   3   4   5 
  0   2   4   6   8  10 
  0   3   6   9  12  15 
  0   4   8  12  16  20 
  0   5  10  15  20  25 
Please enter a number: 
=================================== RESTART: Shell ===================================
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

help> break
The "break" statement
*********************

   break_stmt ::= "break"

"break" may only occur syntactically nested in a "for" or "while"
loop, but not nested in a function or class definition within that
loop.

It terminates the nearest enclosing loop, skipping the optional "else"
clause if the loop has one.

If a "for" loop is terminated by "break", the loop control target
keeps its current value.

When "break" passes control out of a "try" statement with a "finally"
clause, that "finally" clause is executed before really leaving the
loop.

Related help topics: while, for

help> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Please enter a number: 5
  0   0   0   0   0   0 
  0   1   2   3   4   5 
  0   2   4   6   8  10 
  0   3   6   9  12  15 
  0   4   8  12  16  20 
  0   5  10  15  20  25 
Do you want another table? y/n y
Please enter a number: 5
  0   0   0   0   0   0 
  0   1   2   3   4   5 
  0   2   4   6   8  10 
  0   3   6   9  12  15 
  0   4   8  12  16  20 
  0   5  10  15  20  25 
Do you want another table? y/n NO
Please enter a number: 5
  0   0   0   0   0   0 
  0   1   2   3   4   5 
  0   2   4   6   8  10 
  0   3   6   9  12  15 
  0   4   8  12  16  20 
  0   5  10  15  20  25 
Do you want another table? y/n 
=================================== RESTART: Shell ===================================
>>> help(str.lower)
Help on method_descriptor:

lower(self, /)
    Return a copy of the string converted to lowercase.

>>> 'SAMUEL'
'SAMUEL'
>>> 'SAMUEL'.lower()
'samuel'
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Please enter a number: 5
  0   0   0   0   0   0 
  0   1   2   3   4   5 
  0   2   4   6   8  10 
  0   3   6   9  12  15 
  0   4   8  12  16  20 
  0   5  10  15  20  25 
Do you want another table? y/n no
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Please enter a number: 
5
Oops, please enter a number.
Do you want another table? y/n Please enter a number: 
Oops, please enter a number.
Do you want another table? y/n okay
Please enter a number: 12
  0   0   0   0   0   0   0   0   0   0   0   0   0 
  0   1   2   3   4   5   6   7   8   9  10  11  12 
  0   2   4   6   8  10  12  14  16  18  20  22  24 
  0   3   6   9  12  15  18  21  24  27  30  33  36 
  0   4   8  12  16  20  24  28  32  36  40  44  48 
  0   5  10  15  20  25  30  35  40  45  50  55  60 
  0   6  12  18  24  30  36  42  48  54  60  66  72 
  0   7  14  21  28  35  42  49  56  63  70  77  84 
  0   8  16  24  32  40  48  56  64  72  80  88  96 
  0   9  18  27  36  45  54  63  72  81  90  99 108 
  0  10  20  30  40  50  60  70  80  90 100 110 120 
  0  11  22  33  44  55  66  77  88  99 110 121 132 
  0  12  24  36  48  60  72  84  96 108 120 132 144 
Do you want another table? y/n y
Please enter a number: 15
  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0 
  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15 
  0   2   4   6   8  10  12  14  16  18  20  22  24  26  28  30 
  0   3   6   9  12  15  18  21  24  27  30  33  36  39  42  45 
  0   4   8  12  16  20  24  28  32  36  40  44  48  52  56  60 
  0   5  10  15  20  25  30  35  40  45  50  55  60  65  70  75 
  0   6  12  18  24  30  36  42  48  54  60  66  72  78  84  90 
  0   7  14  21  28  35  42  49  56  63  70  77  84  91  98 105 
  0   8  16  24  32  40  48  56  64  72  80  88  96 104 112 120 
  0   9  18  27  36  45  54  63  72  81  90  99 108 117 126 135 
  0  10  20  30  40  50  60  70  80  90 100 110 120 130 140 150 
  0  11  22  33  44  55  66  77  88  99 110 121 132 143 154 165 
  0  12  24  36  48  60  72  84  96 108 120 132 144 156 168 180 
  0  13  26  39  52  65  78  91 104 117 130 143 156 169 182 195 
  0  14  28  42  56  70  84  98 112 126 140 154 168 182 196 210 
  0  15  30  45  60  75  90 105 120 135 150 165 180 195 210 225 
Do you want another table? y/n n
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,10))
[2, 3, 4, 5, 6, 7, 8, 9]
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Traceback (most recent call last):
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 282, in <module>
    print(f"{num} is a prime number {is_prime(num)}")
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 273, in is_prime
    for i in range(2,x):
NameError: name 'x' is not defined
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
3 is a prime number True
6 is a prime number False
11 is a prime number True
31 is a prime number True
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> nth_prime(10)
29
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> primes
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>> help(random)
Help on module random:

NAME
    random - Random variable generators.

DESCRIPTION
        integers
        --------
               uniform within range
    
        sequences
        ---------
               pick random element
               pick random sample
               pick weighted random sample
               generate random permutation
    
        distributions on the real line:
        ------------------------------
               uniform
               triangular
               normal (Gaussian)
               lognormal
               negative exponential
               gamma
               beta
               pareto
               Weibull
    
        distributions on the circle (angles 0 to 2pi)
        ---------------------------------------------
               circular uniform
               von Mises
    
    General notes on the underlying Mersenne Twister core generator:
    
    * The period is 2**19937-1.
    * It is one of the most extensively tested generators in existence.
    * The random() method is implemented in C, executes in a single Python step,
      and is, therefore, threadsafe.

CLASSES
    _random.Random(builtins.object)
        Random
            SystemRandom
    
    class Random(_random.Random)
     |  Random(x=None)
     |  
     |  Random number generator base class used by bound module functions.
     |  
     |  Used to instantiate instances of Random to get generators that don't
     |  share state.
     |  
     |  Class Random can also be subclassed if you want to use a different basic
     |  generator of your own devising: in that case, override the following
     |  methods:  random(), seed(), getstate(), and setstate().
     |  Optionally, implement a getrandbits() method so that randrange()
     |  can cover arbitrarily large ranges.
     |  
     |  Method resolution order:
     |      Random
     |      _random.Random
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __getstate__(self)
     |      # Issue 17489: Since __reduce__ was defined to fix #759889 this is no
     |      # longer called; we leave it here because it has been here since random was
     |      # rewritten back in 2001 and why risk breaking something.
     |  
     |  __init__(self, x=None)
     |      Initialize an instance.
     |      
     |      Optional argument x controls seeding, as for Random.seed().
     |  
     |  __reduce__(self)
     |      Helper for pickle.
     |  
     |  __setstate__(self, state)
     |  
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |  
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |  
     |  choices(self, population, weights=None, *, cum_weights=None, k=1)
     |      Return a k sized list of population elements chosen with replacement.
     |      
     |      If the relative weights or cumulative weights are not specified,
     |      the selections are made with equal probability.
     |  
     |  expovariate(self, lambd)
     |      Exponential distribution.
     |      
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |  
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      
     |      The probability distribution function is:
     |      
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |  
     |  gauss(self, mu, sigma)
     |      Gaussian distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |      
     |      Not thread-safe without a lock around calls.
     |  
     |  getstate(self)
     |      Return internal state; can be passed to setstate() later.
     |  
     |  lognormvariate(self, mu, sigma)
     |      Log normal distribution.
     |      
     |      If you take the natural logarithm of this distribution, you'll get a
     |      normal distribution with mean mu and standard deviation sigma.
     |      mu can have any value, and sigma must be greater than zero.
     |  
     |  normalvariate(self, mu, sigma)
     |      Normal distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.
     |  
     |  paretovariate(self, alpha)
     |      Pareto distribution.  alpha is the shape parameter.
     |  
     |  randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
     |  
     |  randrange(self, start, stop=None, step=1, _int=<class 'int'>)
     |      Choose a random item from range(start, stop[, step]).
     |      
     |      This fixes the problem with randint() which includes the
     |      endpoint; in Python this is usually not what you want.
     |  
     |  sample(self, population, k)
     |      Chooses k unique random elements from a population sequence or set.
     |      
     |      Returns a new list containing elements from the population while
     |      leaving the original population unchanged.  The resulting list is
     |      in selection order so that all sub-slices will also be valid random
     |      samples.  This allows raffle winners (the sample) to be partitioned
     |      into grand prize and second place winners (the subslices).
     |      
     |      Members of the population need not be hashable or unique.  If the
     |      population contains repeats, then each occurrence is a possible
     |      selection in the sample.
     |      
     |      To choose a sample in a range of integers, use range as an argument.
     |      This is especially fast and space efficient for sampling from a
     |      large population:   sample(range(10000000), 60)
     |  
     |  seed(self, a=None, version=2)
     |      Initialize internal state from hashable object.
     |      
     |      None or no argument seeds from current time or from an operating
     |      system specific randomness source if available.
     |      
     |      If *a* is an int, all bits are used.
     |      
     |      For version 2 (the default), all of the bits are used if *a* is a str,
     |      bytes, or bytearray.  For version 1 (provided for reproducing random
     |      sequences from older versions of Python), the algorithm for str and
     |      bytes generates a narrower range of seeds.
     |  
     |  setstate(self, state)
     |      Restore internal state from object returned by getstate().
     |  
     |  shuffle(self, x, random=None)
     |      Shuffle list x in place, and return None.
     |      
     |      Optional argument random is a 0-argument function returning a
     |      random float in [0.0, 1.0); if it is the default None, the
     |      standard random.random will be used.
     |  
     |  triangular(self, low=0.0, high=1.0, mode=None)
     |      Triangular distribution.
     |      
     |      Continuous distribution bounded by given lower and upper limits,
     |      and having a given mode value in-between.
     |      
     |      http://en.wikipedia.org/wiki/Triangular_distribution
     |  
     |  uniform(self, a, b)
     |      Get a random number in the range [a, b) or [a, b] depending on rounding.
     |  
     |  vonmisesvariate(self, mu, kappa)
     |      Circular data distribution.
     |      
     |      mu is the mean angle, expressed in radians between 0 and 2*pi, and
     |      kappa is the concentration parameter, which must be greater than or
     |      equal to zero.  If kappa is equal to zero, this distribution reduces
     |      to a uniform random angle over the range 0 to 2*pi.
     |  
     |  weibullvariate(self, alpha, beta)
     |      Weibull distribution.
     |      
     |      alpha is the scale parameter and beta is the shape parameter.
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  __init_subclass__(**kwargs) from builtins.type
     |      Control how subclasses generate random integers.
     |      
     |      The algorithm a subclass can use depends on the random() and/or
     |      getrandbits() implementation available to it and determines
     |      whether it can generate random integers from arbitrarily large
     |      ranges.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  VERSION = 3
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _random.Random:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  getrandbits(self, k, /)
     |      getrandbits(k) -> x.  Generates an int with k random bits.
     |  
     |  random(self, /)
     |      random() -> x in the interval [0, 1).
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from _random.Random:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
    
    class SystemRandom(Random)
     |  SystemRandom(x=None)
     |  
     |  Alternate random number generator using sources provided
     |  by the operating system (such as /dev/urandom on Unix or
     |  CryptGenRandom on Windows).
     |  
     |   Not available on all systems (see os.urandom() for details).
     |  
     |  Method resolution order:
     |      SystemRandom
     |      Random
     |      _random.Random
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  getrandbits(self, k)
     |      getrandbits(k) -> x.  Generates an int with k random bits.
     |  
     |  getstate = _notimplemented(self, *args, **kwds)
     |  
     |  random(self)
     |      Get the next random number in the range [0.0, 1.0).
     |  
     |  seed(self, *args, **kwds)
     |      Stub method.  Not used for a system random number generator.
     |  
     |  setstate = _notimplemented(self, *args, **kwds)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Random:
     |  
     |  __getstate__(self)
     |      # Issue 17489: Since __reduce__ was defined to fix #759889 this is no
     |      # longer called; we leave it here because it has been here since random was
     |      # rewritten back in 2001 and why risk breaking something.
     |  
     |  __init__(self, x=None)
     |      Initialize an instance.
     |      
     |      Optional argument x controls seeding, as for Random.seed().
     |  
     |  __reduce__(self)
     |      Helper for pickle.
     |  
     |  __setstate__(self, state)
     |  
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |  
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |  
     |  choices(self, population, weights=None, *, cum_weights=None, k=1)
     |      Return a k sized list of population elements chosen with replacement.
     |      
     |      If the relative weights or cumulative weights are not specified,
     |      the selections are made with equal probability.
     |  
     |  expovariate(self, lambd)
     |      Exponential distribution.
     |      
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |  
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      
     |      The probability distribution function is:
     |      
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |  
     |  gauss(self, mu, sigma)
     |      Gaussian distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |      
     |      Not thread-safe without a lock around calls.
     |  
     |  lognormvariate(self, mu, sigma)
     |      Log normal distribution.
     |      
     |      If you take the natural logarithm of this distribution, you'll get a
     |      normal distribution with mean mu and standard deviation sigma.
     |      mu can have any value, and sigma must be greater than zero.
     |  
     |  normalvariate(self, mu, sigma)
     |      Normal distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.
     |  
     |  paretovariate(self, alpha)
     |      Pareto distribution.  alpha is the shape parameter.
     |  
     |  randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
     |  
     |  randrange(self, start, stop=None, step=1, _int=<class 'int'>)
     |      Choose a random item from range(start, stop[, step]).
     |      
     |      This fixes the problem with randint() which includes the
     |      endpoint; in Python this is usually not what you want.
     |  
     |  sample(self, population, k)
     |      Chooses k unique random elements from a population sequence or set.
     |      
     |      Returns a new list containing elements from the population while
     |      leaving the original population unchanged.  The resulting list is
     |      in selection order so that all sub-slices will also be valid random
     |      samples.  This allows raffle winners (the sample) to be partitioned
     |      into grand prize and second place winners (the subslices).
     |      
     |      Members of the population need not be hashable or unique.  If the
     |      population contains repeats, then each occurrence is a possible
     |      selection in the sample.
     |      
     |      To choose a sample in a range of integers, use range as an argument.
     |      This is especially fast and space efficient for sampling from a
     |      large population:   sample(range(10000000), 60)
     |  
     |  shuffle(self, x, random=None)
     |      Shuffle list x in place, and return None.
     |      
     |      Optional argument random is a 0-argument function returning a
     |      random float in [0.0, 1.0); if it is the default None, the
     |      standard random.random will be used.
     |  
     |  triangular(self, low=0.0, high=1.0, mode=None)
     |      Triangular distribution.
     |      
     |      Continuous distribution bounded by given lower and upper limits,
     |      and having a given mode value in-between.
     |      
     |      http://en.wikipedia.org/wiki/Triangular_distribution
     |  
     |  uniform(self, a, b)
     |      Get a random number in the range [a, b) or [a, b] depending on rounding.
     |  
     |  vonmisesvariate(self, mu, kappa)
     |      Circular data distribution.
     |      
     |      mu is the mean angle, expressed in radians between 0 and 2*pi, and
     |      kappa is the concentration parameter, which must be greater than or
     |      equal to zero.  If kappa is equal to zero, this distribution reduces
     |      to a uniform random angle over the range 0 to 2*pi.
     |  
     |  weibullvariate(self, alpha, beta)
     |      Weibull distribution.
     |      
     |      alpha is the scale parameter and beta is the shape parameter.
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from Random:
     |  
     |  __init_subclass__(**kwargs) from builtins.type
     |      Control how subclasses generate random integers.
     |      
     |      The algorithm a subclass can use depends on the random() and/or
     |      getrandbits() implementation available to it and determines
     |      whether it can generate random integers from arbitrarily large
     |      ranges.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Random:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from Random:
     |  
     |  VERSION = 3
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _random.Random:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from _random.Random:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.

FUNCTIONS
    betavariate(alpha, beta) method of Random instance
        Beta distribution.
        
        Conditions on the parameters are alpha > 0 and beta > 0.
        Returned values range between 0 and 1.
    
    choice(seq) method of Random instance
        Choose a random element from a non-empty sequence.
    
    choices(population, weights=None, *, cum_weights=None, k=1) method of Random instance
        Return a k sized list of population elements chosen with replacement.
        
        If the relative weights or cumulative weights are not specified,
        the selections are made with equal probability.
    
    expovariate(lambd) method of Random instance
        Exponential distribution.
        
        lambd is 1.0 divided by the desired mean.  It should be
        nonzero.  (The parameter would be called "lambda", but that is
        a reserved word in Python.)  Returned values range from 0 to
        positive infinity if lambd is positive, and from negative
        infinity to 0 if lambd is negative.
    
    gammavariate(alpha, beta) method of Random instance
        Gamma distribution.  Not the gamma function!
        
        Conditions on the parameters are alpha > 0 and beta > 0.
        
        The probability distribution function is:
        
                    x ** (alpha - 1) * math.exp(-x / beta)
          pdf(x) =  --------------------------------------
                      math.gamma(alpha) * beta ** alpha
    
    gauss(mu, sigma) method of Random instance
        Gaussian distribution.
        
        mu is the mean, and sigma is the standard deviation.  This is
        slightly faster than the normalvariate() function.
        
        Not thread-safe without a lock around calls.
    
    getrandbits(k, /) method of Random instance
        getrandbits(k) -> x.  Generates an int with k random bits.
    
    getstate() method of Random instance
        Return internal state; can be passed to setstate() later.
    
    lognormvariate(mu, sigma) method of Random instance
        Log normal distribution.
        
        If you take the natural logarithm of this distribution, you'll get a
        normal distribution with mean mu and standard deviation sigma.
        mu can have any value, and sigma must be greater than zero.
    
    normalvariate(mu, sigma) method of Random instance
        Normal distribution.
        
        mu is the mean, and sigma is the standard deviation.
    
    paretovariate(alpha) method of Random instance
        Pareto distribution.  alpha is the shape parameter.
    
    randint(a, b) method of Random instance
        Return random integer in range [a, b], including both end points.
    
    random() method of Random instance
        random() -> x in the interval [0, 1).
    
    randrange(start, stop=None, step=1, _int=<class 'int'>) method of Random instance
        Choose a random item from range(start, stop[, step]).
        
        This fixes the problem with randint() which includes the
        endpoint; in Python this is usually not what you want.
    
    sample(population, k) method of Random instance
        Chooses k unique random elements from a population sequence or set.
        
        Returns a new list containing elements from the population while
        leaving the original population unchanged.  The resulting list is
        in selection order so that all sub-slices will also be valid random
        samples.  This allows raffle winners (the sample) to be partitioned
        into grand prize and second place winners (the subslices).
        
        Members of the population need not be hashable or unique.  If the
        population contains repeats, then each occurrence is a possible
        selection in the sample.
        
        To choose a sample in a range of integers, use range as an argument.
        This is especially fast and space efficient for sampling from a
        large population:   sample(range(10000000), 60)
    
    seed(a=None, version=2) method of Random instance
        Initialize internal state from hashable object.
        
        None or no argument seeds from current time or from an operating
        system specific randomness source if available.
        
        If *a* is an int, all bits are used.
        
        For version 2 (the default), all of the bits are used if *a* is a str,
        bytes, or bytearray.  For version 1 (provided for reproducing random
        sequences from older versions of Python), the algorithm for str and
        bytes generates a narrower range of seeds.
    
    setstate(state) method of Random instance
        Restore internal state from object returned by getstate().
    
    shuffle(x, random=None) method of Random instance
        Shuffle list x in place, and return None.
        
        Optional argument random is a 0-argument function returning a
        random float in [0.0, 1.0); if it is the default None, the
        standard random.random will be used.
    
    triangular(low=0.0, high=1.0, mode=None) method of Random instance
        Triangular distribution.
        
        Continuous distribution bounded by given lower and upper limits,
        and having a given mode value in-between.
        
        http://en.wikipedia.org/wiki/Triangular_distribution
    
    uniform(a, b) method of Random instance
        Get a random number in the range [a, b) or [a, b] depending on rounding.
    
    vonmisesvariate(mu, kappa) method of Random instance
        Circular data distribution.
        
        mu is the mean angle, expressed in radians between 0 and 2*pi, and
        kappa is the concentration parameter, which must be greater than or
        equal to zero.  If kappa is equal to zero, this distribution reduces
        to a uniform random angle over the range 0 to 2*pi.
    
    weibullvariate(alpha, beta) method of Random instance
        Weibull distribution.
        
        alpha is the scale parameter and beta is the shape parameter.

DATA
    __all__ = ['Random', 'seed', 'random', 'uniform', 'randint', 'choice',...

FILE
    c:\users\samue\appdata\local\programs\python\python38-32\lib\random.py


>>> 
== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py =
17
Please enter a guess: m
Oop please enter a number.
17
Please enter a guess: 17
17
Please enter a guess: 17
17
Please enter a guess: 
== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py =
1
Please enter a guess: 1
1
Please enter a guess: 1
1
Please enter a guess: 3
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.
Please guess a smaller number.

==================================== RESTART: Shell ====================================
>>> 
== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py =
4
Please enter a guess: 5
Please guess a smaller number.
Please enter a guess: 3
Please guess a larger number.
Please enter a guess: 4
4
Please enter a guess: 4
4
Please enter a guess: 
== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py =
10
Please enter a guess: 8
Please guess a larger number.
Please enter a guess: 11
Please guess a smaller number.
Please enter a guess: 10
You guessed the correct number.
10
Please enter a guess: 
== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py =
12
Please enter a guess: 11
Please guess a larger number.
Please enter a guess: 13
Please guess a smaller number.
Please enter a guess: 12
You guessed the correct number.
Do you want to play again? y/n n
>>> 
== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py =
16
Please enter a guess: 15
Please guess a larger number.
Please enter a guess: 17
Please guess a smaller number.
Please enter a guess: 16
You guessed the correct number.
Do you want to play again? y/n n
>>> 
== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py =
8
Please enter a guess: 
Oop please enter a number.
You guessed the correct number.
Do you want to play again? y/n y
8
Please enter a guess: 6
Please guess a larger number.
Please enter a guess: 7
Please guess a larger number.
Please enter a guess: 9
Please guess a smaller number.
Please enter a guess: 8
You guessed the correct number.
Do you want to play again? y/n y
8
Please enter a guess: 8
You guessed the correct number.
Do you want to play again? y/n y
8
Please enter a guess: 8
You guessed the correct number.
Do you want to play again? y/n y
8
Please enter a guess: y
Oop please enter a number.
You guessed the correct number.
Do you want to play again? y/n y
8
Please enter a guess: 8
You guessed the correct number.
Do you want to play again? y/n n
>>> 
== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py =
1
Please enter a guess: 1
You guessed the correct number.
Do you want to play again? y/n y
17
Please enter a guess: 147
Please guess a smaller number.
Please enter a guess: 17
You guessed the correct number.
Do you want to play again? y/n y
3
Please enter a guess: 
== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py =
9
Please enter a guess: 9
You guessed the correct number.
Do you want to play again? y/n n
>>> 
== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py =
19
Please enter a guess: n
Oop please enter a number.
You guessed the correct number.
Do you want to play again? y/n n
>>> 2000%4
0
>>> 1900%4
0
>>> 1600%4
0
>>> 1600%100
0
>>> 1600%400
0
>>> 1900%4
0
>>> 1900%100
0
>>> 1900%400
300
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
True
False
True
False
True
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
1992 True
1600 False
1900 True
2002 False
2020 True
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
1992 False
1600 False
1900 True
2002 False
2020 False
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
1992 False
1600 True
1900 False
2002 False
2020 False
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
1992 True
1600 True
1900 False
2002 False
2020 True
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Sam
Tom
Steve
>>> len(name)
5
>>> len(name)
5
>>> len(names)
3
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'horses', 'name', 'names', 'numbers', 'race', 'random', 'shuffled']
>>> name
'Steve'
>>> len(name)
5
>>> len(name)
5
>>> len(names)
3
>>> help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Traceback (most recent call last):
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 353, in <module>
    for name in range(len(name)):
NameError: name 'name' is not defined
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
0
1
2
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
1
2
3
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
1
2
3
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
1
2
3
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
0
1
2
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
1
2
3
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
1 Sam
2 Tom
3 Steve
>>> help(enumerate)
Help on class enumerate in module builtins:

class enumerate(object)
 |  enumerate(iterable, start=0)
 |  
 |  Return an enumerate object.
 |  
 |    iterable
 |      an object supporting iteration
 |  
 |  The enumerate object yields pairs containing a count (from start, which
 |  defaults to zero) and a value yielded by the iterable argument.
 |  
 |  enumerate is useful for obtaining an indexed list:
 |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> names
['Sam', 'Tom', 'Steve']
>>> new = enumerate(names)
>>> new
<enumerate object at 0x03964EC8>
>>> new = list(new)
>>> new
[(0, 'Sam'), (1, 'Tom'), (2, 'Steve')]
>>> new[0]
(0, 'Sam')
>>> type(new[0])
<class 'tuple'>
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py =
(1, 'Sam')
(2, 'Tom')
(3, 'Steve')
>>> i
(3, 'Steve')
>>> num, name = i
>>> num
3
>>> name
'Steve'
>>> i
(3, 'Steve')
>>> type(i)
<class 'tuple'>
>>> len(i)
2
>>> x,y = [1,2]
>>> x
1
>>> y
2
>>> x
1
>>> y
2
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py =
(1, 'Sam')
(2, 'Tom')
(3, 'Steve')

>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py =
1 Sam
2 Tom
3 Steve
>>> 