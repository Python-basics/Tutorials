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
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\TD Screener.py
     symbol      Margin        PE       PEG    high52
4629   SPWR    39.91179  20.38129  0.000242   24.4000
3824   PCRX   110.75470  21.12716  0.003977   68.0784
4174    RVP    31.83984  20.02876  0.005617   14.3999
2005    HQI    58.27125  16.02324  0.006145    9.4300
3665    PNM    26.55287  20.06514  0.006633   56.1400
3035    NCV   165.08020  14.00399  0.007788    6.1300
942    BMRN   164.60350  18.11560  0.008935  131.9450
870    BIDU    47.57722  13.39127  0.011815  151.1800
3040    NCZ   162.96010  14.53097  0.012852    5.3800
1470   FLGT    48.58429  22.58318  0.013201   52.4700
3966   SBRA    25.45165  25.90921  0.014255   22.5450
2236   HZNP    46.01313  19.07906  0.014692   86.6700
2327   HCFT    31.42799  10.76045  0.016155    3.3400
2941   NLOK    26.51757  15.18783  0.019348   28.7000
5268   UTHR    45.04078  12.29231  0.021206  144.2600
2092   HOLX    36.64712  17.40599  0.026191   77.4880
2254   IDCC    25.03286  32.03625  0.034667   67.0600
2628   IRWD    33.26922  16.83776  0.036400   14.1000
1265   CODX    72.10097  11.91035  0.037786   30.9900
973    CFBI    23.98358  36.35523  0.039058   12.0500
3546   OBCI    24.30322  12.79945  0.053007   22.5500
4101   QDEL    48.78985  22.75106  0.060147  306.7236
5123   VRTX    43.38858  22.22098  0.062560  306.0800
5034    WWE    21.78659  20.27321  0.064023   67.5300
3888   RAND    35.62637  10.26427  0.070575   37.0800
2535   ISSC    21.16099  41.93986  0.071472    8.0900
1364   CLGX    23.24015  30.30481  0.074254   79.2100
2826    LPX    22.26415  21.63497  0.083640   37.2500
2370    HIW    23.38174  13.12032  0.086187   52.7600
347    APPF   163.73240  36.92858  0.099757  180.5595
2199   HMST    28.69043  11.93922  0.111021   35.5200
4490   SSSS  3900.89400  22.51715  0.112065   14.9100
296    ACTG   196.99990  15.75533  0.113612    4.4600
822    BPMC    85.08424  19.39460  0.114178  111.3500
3214    NLS    21.86034  15.70846  0.115816   28.4300
3653     PG    22.30045  26.32273  0.117555  146.9200
3668    OLP    65.14166  14.42480  0.119564   29.0000
1592    EOS   737.79620  10.17752  0.124305   21.3200
4339   PRTH    78.68798  20.49932  0.130188    7.9300
2391   GSMG    46.00275  11.27240  0.131050   11.5295
2868   IRET    47.99493  17.84800  0.141899   85.2400
524      AY    27.84245  59.22666  0.142143   37.9800
1198    DSS   128.71190  14.76359  0.152819   15.6000
2159   HKIB    56.70128  13.49253  0.152874   16.5300
1700   EBAY    23.82962  15.86396  0.152880   61.0600
2621   LOGI    21.23154  22.47971  0.158441   95.7099
2269    HCI    22.95028  14.06449  0.161975   62.9300
4282   RTLR    40.18687  11.85662  0.166546   18.4100
3941   SCPL    23.21429  16.57145  0.166874   18.5000
2307    GCP    40.13688  17.09248  0.168250   27.6200
      symbol      Margin         PE       PEG       high52
4574    TPRE    26.06384   23.17226  0.178691      11.5200
1545     EMF   567.84580   27.30493  0.199894      18.3500
2837     JMM   167.94580   17.70392  0.200260       7.5583
746     CDNS    24.24667   30.93590  0.200542     127.5000
908     CHCT    26.93859   68.63208  0.201856      52.3290
5240     VER    33.18331   31.85381  0.203423      10.1800
759     BDSI    23.78876   30.36232  0.203868       7.2100
2792    IRBT    22.57125   14.17791  0.210602      98.5500
1927     EFX    21.06150   47.47018  0.222824     181.7600
218      AMG    25.82862   41.26571  0.239008      95.7900
4092    PSEC   117.40340   15.41976  0.242599       6.7500
454     ALRS    26.34846   10.69112  0.243729      25.4200
1755    FRBA    29.69913   10.32955  0.245747      11.5600
995      DGX    20.67480   15.22811  0.274211     131.8100
2180    HIFS    56.94918   10.98297  0.274335     230.0200
1909    FFWM    41.10925   11.01597  0.275363      20.2400
2828   LBRDA  1634.51000  131.26390  0.282610     162.2550
4995     WTM    48.46572   10.56168  0.293840    1168.2100
4835    STMP    32.98886   23.69149  0.295662     325.1320
4099    SGEN    59.91791   70.31970  0.297421     213.9400
396     AMNB    28.02575   10.49590  0.300840      40.5700
1738     EXP    20.07465   37.67220  0.303949      97.7900
1313    CTRE    47.17316   24.65633  0.307274      23.6400
4402     TGP    26.90570   11.08228  0.327821      16.0700
2131    HASI    43.78975   37.29697  0.337731      56.8700
2150    HMLP    54.22827   10.50094  0.353481      16.8400
5031    VALU    49.54493   16.39030  0.354556      36.6016
4167    REGN    36.70881   18.10726  0.360099     664.6400
1933    FRPH    86.43818   31.86245  0.369382      52.8800
4318    SAFT    20.56924   10.15740  0.370569      97.2754
3627    PFLT    78.07618   22.93066  0.374084      12.6700
1489    ENPH    22.05117  101.36230  0.377454     148.9373
4688     SWI    20.52270  190.76320  0.381203      23.6600
5252    UBCP    25.47006   10.28432  0.388719      15.5600
849    BRK/B    48.25622   15.22417  0.396493     234.9900
847    BRK/A    48.25622   15.22417  0.396493  352500.0000
4112      PW    51.63725   41.07617  0.405774      33.8899
420     AMRB    25.07753   10.56986  0.407235      16.4290
3102      MS    22.49939   10.83924  0.407947      65.1900
2543    IROQ    20.07541   14.37244  0.419475      24.0500
2783    IIPR    55.97635   49.96005  0.426342     164.9900
2544  IIPRpA    55.97635   49.96005  0.426342      33.0000
309     ATVI    30.91095   28.83116  0.437391      87.7265
5084    UHAL    20.10441   16.53003  0.438073     434.3450
755     CERN    26.05999   28.48161  0.440451      80.9000
38        AX    32.49255   11.15860  0.458755      35.9000
4392    TRIB    22.88061   40.84720  0.467864       4.9400
4288    SBFG    26.68090   11.12566  0.472172      20.4900
2273    GBDC   131.42950  108.85040  0.476392      18.6150
4366     TER    27.17783   29.87998  0.484266     117.3200
     symbol     Margin         PE       PEG    high52
2440   INBK   29.27908   10.42867  0.484561   28.5000
3484    PEG   24.26160   15.26306  0.487011   62.1500
1873   ESSA   25.04144   11.54411  0.491539   17.7000
1816   FRHC   34.89419   46.38577  0.503515   44.2600
2183   GLPI   41.33453   20.72733  0.504130   50.9900
3239    NNI   20.39895   17.35787  0.505282   73.9200
5182     XP   25.76639   58.51842  0.510155   52.9445
877    BPRN   25.22773   12.64403  0.525032   32.2500
1107    CLX   21.76409   22.34410  0.526270  239.8700
4328    SAP   25.27927   24.85618  0.559065  169.3000
1979   GROW   59.90755   65.82633  0.563374    4.3500
3457    PCH   25.87703   39.33079  0.568543   48.3700
15       AB   90.69361   11.91181  0.589991   36.0600
2759   ISBC   31.90902   12.70617  0.594379   12.5700
175    AMAT   24.12543   22.73759  0.595078   89.4600
5162   WLKP   39.59495   11.04479  0.602772   26.4800
1351   CSTR   21.72664   12.27458  0.613680   17.4800
4105   SFBC   26.75298   10.98886  0.624987   37.7900
426    AMSF   28.13445   11.79575  0.633284   80.6500
4605    TSM   38.54322   31.70595  0.644555  107.6100
3704   PRGS   21.85708   32.71750  0.649127   52.5000
1093    CKX   31.11788   45.11354  0.659560   10.3500
625    CCBG   25.41648   13.05851  0.668168   30.9500
5159     WD   21.53302   12.52633  0.674851   84.5150
585     BFC   39.06562   15.19322  0.679985   70.0100
1665    ESS   21.26204   27.72609  0.685775  329.7400
871    CARG   22.08080   41.89009  0.725446   38.5300
3065    MCO   34.43953   29.44168  0.732346  305.9550
4059    RMD   23.72145   44.88984  0.737200  224.2400
909    CHCO   36.61803   12.47819  0.745304   83.0700
2794    LOB   34.32683   48.47667  0.761591   47.5000
2763    LLY   21.05006   24.13856  0.763707  170.7500
2426   GRMN   28.25628   22.79527  0.766294  122.3500
87     APAM   36.38750   16.48519  0.767987   49.0800
62     ABCB   36.11968   11.17595  0.786709   44.9000
2414   GLBZ   29.14619   16.63737  0.800408   11.6400
3327    MRK   23.46427   18.14767  0.816395   92.6400
3138    NHI   50.60557   15.57208  0.833698   91.1200
1569    FPH  434.78570  169.73170  0.886312    9.3100
4509  STZ/B   23.08441   39.64483  0.903119  208.1300
4656    STZ   23.08441   39.64483  0.903119  214.1100
5283   WTBA   33.28539   10.29038  0.903872   25.9283
5135     UI   33.05134   38.55876  0.923229  271.3200
1887   ETSY   20.32458   92.00814  0.939653  164.6400
2232    HAE   22.96144   55.77649  0.940450  126.7400
2477   LRCX   25.91848   28.86070  0.966116  509.4500
1563     FB   36.54401   33.86627  0.973631  304.6700
182    ASML   26.30116   48.80464  0.985334  471.0100
2790    LNT   27.06522   19.90907  0.988983   60.2800
>>> df_peg
     symbol    Margin        PE       PEG    high52
15       AB  90.69361  11.91181  0.589991   36.0600
38       AX  32.49255  11.15860  0.458755   35.9000
62     ABCB  36.11968  11.17595  0.786709   44.9000
87     APAM  36.38750  16.48519  0.767987   49.0800
175    AMAT  24.12543  22.73759  0.595078   89.4600
...     ...       ...       ...       ...       ...
5182     XP  25.76639  58.51842  0.510155   52.9445
5240    VER  33.18331  31.85381  0.203423   10.1800
5252   UBCP  25.47006  10.28432  0.388719   15.5600
5268   UTHR  45.04078  12.29231  0.021206  144.2600
5283   WTBA  33.28539  10.29038  0.903872   25.9283

[149 rows x 5 columns]
>>> file
'Tue_Dec__8_peg.xlsx'
>>> df_peg
     symbol    Margin        PE       PEG    high52
15       AB  90.69361  11.91181  0.589991   36.0600
38       AX  32.49255  11.15860  0.458755   35.9000
62     ABCB  36.11968  11.17595  0.786709   44.9000
87     APAM  36.38750  16.48519  0.767987   49.0800
175    AMAT  24.12543  22.73759  0.595078   89.4600
...     ...       ...       ...       ...       ...
5182     XP  25.76639  58.51842  0.510155   52.9445
5240    VER  33.18331  31.85381  0.203423   10.1800
5252   UBCP  25.47006  10.28432  0.388719   15.5600
5268   UTHR  45.04078  12.29231  0.021206  144.2600
5283   WTBA  33.28539  10.29038  0.903872   25.9283

[149 rows x 5 columns]
>>> df_results
     symbol    Margin         PE       PEG   high52
0      AGLE   0.00000    0.00000  0.000000  11.3800
1      ATEN  11.41888   65.04326  0.439348   9.2100
2      AJRD   6.00720   26.92328  0.000000  57.2749
3     APOpB  66.39657    0.00000  0.000000  27.9300
4     APOpA  66.39657    0.00000  0.000000  27.1500
...     ...       ...        ...       ...      ...
5284   WVFC  28.94555   13.29034  0.000000  17.0600
5285    UGI   0.86284   14.02150  0.192384  45.7100
5286   USFD   0.13680    0.00000  0.000000  42.2800
5287    VIR   0.00000    0.00000  0.000000  75.0000
5288    UGP   1.33561  120.09120  0.000000   6.6800

[5289 rows x 5 columns]
>>> df_results[(df_results['PEG'] < 1) & (df_results['PEG'] > 0) & (df_results['Margin'] > 20) & (df_results['PE'] > 10)]
     symbol    Margin        PE       PEG    high52
15       AB  90.69361  11.91181  0.589991   36.0600
38       AX  32.49255  11.15860  0.458755   35.9000
62     ABCB  36.11968  11.17595  0.786709   44.9000
87     APAM  36.38750  16.48519  0.767987   49.0800
175    AMAT  24.12543  22.73759  0.595078   89.4600
...     ...       ...       ...       ...       ...
5182     XP  25.76639  58.51842  0.510155   52.9445
5240    VER  33.18331  31.85381  0.203423   10.1800
5252   UBCP  25.47006  10.28432  0.388719   15.5600
5268   UTHR  45.04078  12.29231  0.021206  144.2600
5283   WTBA  33.28539  10.29038  0.903872   25.9283

[149 rows x 5 columns]
>>> df_results[(df_results['PEG'] < 1) and (df_results['PEG'] > 0) and (df_results['Margin'] > 20) and (df_results['PE'] > 10)]
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    df_results[(df_results['PEG'] < 1) and (df_results['PEG'] > 0) and (df_results['Margin'] > 20) and (df_results['PE'] > 10)]
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\lib\site-packages\pandas\core\generic.py", line 1552, in __nonzero__
    raise ValueError(
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
>>> True and False
False
>>> True & Flase
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    True & Flase
NameError: name 'Flase' is not defined
>>> True & False
False
>>> True & True
True
>>> 