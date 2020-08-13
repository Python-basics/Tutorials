Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 3*2*1
6
>>> 6*5*4*3*2*1
720
>>> 1
1
>>> 2*0
0
>>> 2*1
2
>>> tot 1
SyntaxError: invalid syntax
>>> tot = 1
>>> tot *= 5
>>> tot
5
>>> x
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x = 5
>>> x -= 1
>>> x
4
>>> tot *= x
>>> tot
20
>>> x -= 1
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
6
None
24
None
1
None
40320
None
479001600
None
6402373705728000
None
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
None
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
6
24
1
40320
479001600
6402373705728000
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
6
24
1
1
Negative
40320
479001600
6402373705728000
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> math.factorial(3)
6
>>> from math import factorial
>>> factorial(3)
6
>>> from math import factorial as fact
>>> fact(3)
6
>>> True
True
>>> False
False
>>> 1 == True
True
>>> 0 == False
True
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Traceback (most recent call last):
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 541, in <module>
    print(odd(69,6))
NameError: name 'odd' is not defined
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
719264832.0
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Enter Number of powerballs: 26
292201338.0
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Enter Number of powerballs: 26
18700885632.0
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
719,264,832.0
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
719,264,832.0
>>> 10*10*10*10
10000
>>> 10*10*10
1000
>>> 
= RESTART: C:/Users/samue/AppData/Local/Programs/Python/Python38-32/temp_1.py
Hello World!
>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> help(math.cos)
Help on built-in function cos in module math:

cos(x, /)
    Return the cosine of x (measured in radians).

>>> help(math)
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
    
    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
    
    asin(x, /)
        Return the arc sine (measured in radians) of x.
    
    asinh(x, /)
        Return the inverse hyperbolic sine of x.
    
    atan(x, /)
        Return the arc tangent (measured in radians) of x.
    
    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.
        
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(x, /)
        Return the inverse hyperbolic tangent of x.
    
    ceil(x, /)
        Return the ceiling of x as an Integral.
        
        This is the smallest integer >= x.
    
    comb(n, k, /)
        Number of ways to choose k items from n items without repetition and without order.
        
        Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
        to zero when k > n.
        
        Also called the binomial coefficient because it is equivalent
        to the coefficient of k-th term in polynomial expansion of the
        expression (1 + x)**n.
        
        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.
    
    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.
        
        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.
    
    cos(x, /)
        Return the cosine of x (measured in radians).
    
    cosh(x, /)
        Return the hyperbolic cosine of x.
    
    degrees(x, /)
        Convert angle x from radians to degrees.
    
    dist(p, q, /)
        Return the Euclidean distance between two points p and q.
        
        The points should be specified as sequences (or iterables) of
        coordinates.  Both inputs must have the same dimension.
        
        Roughly equivalent to:
            sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
    
    erf(x, /)
        Error function at x.
    
    erfc(x, /)
        Complementary error function at x.
    
    exp(x, /)
        Return e raised to the power of x.
    
    expm1(x, /)
        Return exp(x)-1.
        
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(x, /)
        Return the absolute value of the float x.
    
    factorial(x, /)
        Find x!.
        
        Raise a ValueError if x is negative or non-integral.
    
    floor(x, /)
        Return the floor of x as an Integral.
        
        This is the largest integer <= x.
    
    fmod(x, y, /)
        Return fmod(x, y), according to platform C.
        
        x % y may differ.
    
    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).
        
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.
        
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(x, /)
        Gamma function at x.
    
    gcd(x, y, /)
        greatest common divisor of x and y
    
    hypot(...)
        hypot(*coordinates) -> value
        
        Multidimensional Euclidean distance from the origin to a point.
        
        Roughly equivalent to:
            sqrt(sum(x**2 for x in coordinates))
        
        For a two dimensional point (x, y), gives the hypotenuse
        using the Pythagorean theorem:  sqrt(x*x + y*y).
        
        For example, the hypotenuse of a 3/4/5 right triangle is:
        
            >>> hypot(3.0, 4.0)
            5.0
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.
    
    isqrt(n, /)
        Return the integer part of the square root of the input.
    
    ldexp(x, i, /)
        Return x * (2**i).
        
        This is essentially the inverse of frexp().
    
    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(x, /)
        Return the base 10 logarithm of x.
    
    log1p(x, /)
        Return the natural logarithm of 1+x (base e).
        
        The result is computed in a way which is accurate for x near zero.
    
    log2(x, /)
        Return the base 2 logarithm of x.
    
    modf(x, /)
        Return the fractional and integer parts of x.
        
        Both results carry the sign of x and are floats.
    
    perm(n, k=None, /)
        Number of ways to choose k items from n items without repetition and with order.
        
        Evaluates to n! / (n - k)! when k <= n and evaluates
        to zero when k > n.
        
        If k is not specified or is None, then k defaults to n
        and the function returns n!.
        
        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.
    
    pow(x, y, /)
        Return x**y (x to the power of y).
    
    prod(iterable, /, *, start=1)
        Calculate the product of all the elements in the input iterable.
        
        The default start value for the product is 1.
        
        When the iterable is empty, return the start value.  This function is
        intended specifically for use with numeric values and may reject
        non-numeric types.
    
    radians(x, /)
        Convert angle x from degrees to radians.
    
    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.
        
        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.
    
    sin(x, /)
        Return the sine of x (measured in radians).
    
    sinh(x, /)
        Return the hyperbolic sine of x.
    
    sqrt(x, /)
        Return the square root of x.
    
    tan(x, /)
        Return the tangent of x (measured in radians).
    
    tanh(x, /)
        Return the hyperbolic tangent of x.
    
    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.
        
        Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)


>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> d = {}
>>> type(d)
<class 'dict'>
>>> help(d)
Help on dict object:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
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
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
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
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the dict keys.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(self, /)
 |      Remove and return a (key, value) pair as a 2-tuple.
 |      
 |      Pairs are returned in LIFO (last-in, first-out) order.
 |      Raises KeyError if the dict is empty.
 |  
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |      
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> d[1] = 'Sam'
>>> d
{1: 'Sam'}
>>> d = {}
>>> d
{}
>>> t = dict()
>>> t
{}
>>> type(d)
<class 'dict'>
>>> type(t)
<class 'dict'>
>>> 
====== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ======
Traceback (most recent call last):
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 552, in <module>
    d['Sam'] = 43
NameError: name 'd' is not defined
>>> 
====== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ======
>>> dd[1] = 'Sam'd
SyntaxError: invalid syntax
>>> d
{'Sam': 43}
>>> d['Sam']
43
>>> 
====== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ======
>>> frui
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    frui
NameError: name 'frui' is not defined
>>> fruit
{'banana': 3, 'apples': 1, 'grapes': 2}
>>> for i in fruit:
	print(i)

	
banana
apples
grapes
>>> len(fruit)
3
>>> dir(fruit)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> fruit.keys()
dict_keys(['banana', 'apples', 'grapes'])
>>> fruit.values()
dict_values([3, 1, 2])
>>> fruit.items()
dict_items([('banana', 3), ('apples', 1), ('grapes', 2)])
>>> 
====== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ======
banana
apples
grapes
>>> help(dict.items)
Help on method_descriptor:

items(...)
    D.items() -> a set-like object providing a view on D's items

>>> 
====== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ======
banana 3
apples 1
grapes 2
>>> 
====== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ======
I have 3 banana
I have 1 apples
I have 2 grapes
>>> 