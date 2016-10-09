##Jalaali Python

Python implementation of [jalaali.js](https://github.com/jalaali/jalaali-js) which contains functions for converting Jalaali and Gregorian calnedar systems to each other.

##About

Jalaali calendar is a solar calendar that was used in Persia, variants of which today are still in use in Iran as well as Afghanistan. [Read more on Wikipedia](http://en.wikipedia.org/wiki/Jalali_calendar) or see [Calendar Converter](http://www.fourmilab.ch/documents/calendar/).
Calendar conversion is based on the [algorithm provided by Kazimierz M. Borkowski](http://www.astro.uni.torun.pl/~kb/Papers/EMP/PersianC-EMP.htm) and has a very good performance.

##Install
    
    pip install jalaali

or download and run

    python setup.py install

##Usage

    from jalaali import Jalaali
    # Call static methods on Jalaali class


###to_jalaali(gy,gm,gd)

Converts a Gregorian date to Jalaali.

```python
Jalaali.to_jalaali(2016, 10, 6) # {jy:1395, jm:7, jd:15}
```

###to_gregorian(jy,jm,jd)

Converts a Jalaali date to Gregorian.

```python
    Jalaali.to_gregorian(1395, 7, 15) # {gy:2016, gm:10, gd:6}
```

###is_valid_jalaali_date(jy,jm,jd)

Checks whether a Jalaali date is valid or not.

```python
    Jalaali.is_valid_jalaali_date(1394,12,30) # False
    Jalaali.is_valid_jalaali_date(1395,12,30) # True
```

###is_leap_jalaali_year(jy)

Is this a leap year or not?

```python
    Jalaali.is_leap_jalaali_year(1394) # False
    Jalaali.is_leap_jalaali_year(1395) # True
```

###jalaali_month_length(jy,jm)

Number of days in a given month in a Jalaali year.

```python
    Jalaali.jalaali_month_length(1394, 12) # 29
    Jalaali.jalaali_month_length(1395, 12) # 30
```

##Licence

MIT

