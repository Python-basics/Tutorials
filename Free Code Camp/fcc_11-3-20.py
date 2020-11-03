Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
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


>>> >>>
SyntaxError: invalid syntax
>>> help(random.choice)
Help on method choice in module random:

choice(seq) method of random.Random instance
    Choose a random element from a non-empty sequence.

>>> help(random.shuffle)
Help on method shuffle in module random:

shuffle(x, random=None) method of random.Random instance
    Shuffle list x in place, and return None.
    
    Optional argument random is a 0-argument function returning a
    random float in [0.0, 1.0); if it is the default None, the
    standard random.random will be used.

>>> 
====== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ======
>>> dir(string)
['Formatter', 'Template', '_ChainMap', '_TemplateMetaclass', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_re', '_sentinel_dict', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> len(string.ascii_letters)
52
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> sting.digits
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sting.digits
NameError: name 'sting' is not defined
>>> string.digits
'0123456789'
>>> sum()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    sum()
TypeError: sum() takes at least 1 positional argument (0 given)
>>> 
====== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ======
>>> 
====== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ======
>>> 
====== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ======
>>> password(5)
>>> 
====== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ======
>>> password(5)
'dtkyv'
>>> 
====== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ======
vpvco
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
29cbv
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
87soi
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
69tgy
57lKDtLvzC
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
None
None
>>> help(random.shuffle)
Help on method shuffle in module random:

shuffle(x, random=None) method of random.Random instance
    Shuffle list x in place, and return None.
    
    Optional argument random is a 0-argument function returning a
    random float in [0.0, 1.0); if it is the default None, the
    standard random.random will be used.

>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
['5', 'c', 't', '5', 'w']
['y', 's', 'p', 'a', 'v', 'Y', 'Y', '4', '1', 'j']
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
0n5mu
Lnr8D7UJOa
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
5hco6
rVHDNgl69M
&LQJ1#4ZDu\Gjj1
>>> help(string.join)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    help(string.join)
AttributeError: module 'string' has no attribute 'join'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(str.join)
Help on method_descriptor:

join(self, iterable, /)
    Concatenate any number of strings.
    
    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.
    
    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

>>> name = 'Sam'
>>> name = list(name)
>>> name
['S', 'a', 'm']
>>> ''.join(name)
'Sam'
>>> ' '.join(name)
'S a m'
>>> '*'.join(name)
'S*a*m'
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> student
['john', 'sam', 'steve', 'bob']
>>> grade
[6, 7, 7, 8]
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> classes
[('john', 6), ('sam', 7), ('steve', 7), ('bob', 8)]
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> new_students
('john', 'sam', 'steve', 'bob')
>>> grades
(6, 7, 7, 8)
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> x
'help'
>>> dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(x.center)
Help on built-in function center:

center(width, fillchar=' ', /) method of builtins.str instance
    Return a centered string of length width.
    
    Padding is done using the specified fill character (default is a space).

>>> x.center(50,'#')
'#######################help#######################'
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> x
['sam', 41, 'bob', 36, 'steve', '20']
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> name
[True, False, True, False, True, False]
>>> for i in x:
	print(i)

	
sam
41
bob
36
steve
20
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


help> buitins
No Python documentation found for 'buitins'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> functions
No Python documentation found for 'functions'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

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

help> for
The "for" statement
*******************

The "for" statement is used to iterate over the elements of a sequence
(such as a string, tuple or list) or other iterable object:

   for_stmt ::= "for" target_list "in" expression_list ":" suite
                ["else" ":" suite]

The expression list is evaluated once; it should yield an iterable
object.  An iterator is created for the result of the
"expression_list".  The suite is then executed once for each item
provided by the iterator, in the order returned by the iterator.  Each
item in turn is assigned to the target list using the standard rules
for assignments (see Assignment statements), and then the suite is
executed.  When the items are exhausted (which is immediately when the
sequence is empty or an iterator raises a "StopIteration" exception),
the suite in the "else" clause, if present, is executed, and the loop
terminates.

A "break" statement executed in the first suite terminates the loop
without executing the "else" clause’s suite.  A "continue" statement
executed in the first suite skips the rest of the suite and continues
with the next item, or with the "else" clause if there is no next
item.

The for-loop makes assignments to the variables in the target list.
This overwrites all previous assignments to those variables including
those made in the suite of the for-loop:

   for i in range(10):
       print(i)
       i = 5             # this will not affect the for-loop
                         # because i will be overwritten with the next
                         # index in the range

Names in the target list are not deleted when the loop is finished,
but if the sequence is empty, they will not have been assigned to at
all by the loop.  Hint: the built-in function "range()" returns an
iterator of integers suitable to emulate the effect of Pascal’s "for i
:= a to b do"; e.g., "list(range(3))" returns the list "[0, 1, 2]".

Note: There is a subtlety when the sequence is being modified by the
  loop (this can only occur for mutable sequences, e.g. lists).  An
  internal counter is used to keep track of which item is used next,
  and this is incremented on each iteration.  When this counter has
  reached the length of the sequence the loop terminates.  This means
  that if the suite deletes the current (or a previous) item from the
  sequence, the next item will be skipped (since it gets the index of
  the current item which has already been treated).  Likewise, if the
  suite inserts an item in the sequence before the current item, the
  current item will be treated again the next time through the loop.
  This can lead to nasty bugs that can be avoided by making a
  temporary copy using a slice of the whole sequence, e.g.,

     for x in a[:]:
         if x < 0: a.remove(x)

Related help topics: break, continue, while

help> range
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |  
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __reduce__(...)
 |      Helper for pickle.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
 |  
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  start
 |  
 |  step
 |  
 |  stop

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

help> while
The "while" statement
*********************

The "while" statement is used for repeated execution as long as an
expression is true:

   while_stmt ::= "while" expression ":" suite
                  ["else" ":" suite]

This repeatedly tests the expression and, if it is true, executes the
first suite; if the expression is false (which may be the first time
it is tested) the suite of the "else" clause, if present, is executed
and the loop terminates.

A "break" statement executed in the first suite terminates the loop
without executing the "else" clause’s suite.  A "continue" statement
executed in the first suite skips the rest of the suite and goes back
to testing the expression.

Related help topics: break, continue, if, TRUTHVALUE

help> None
Help on NoneType object:

class NoneType(object)
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
>>> 