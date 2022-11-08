# CS5, Lab1 part 2
# Filename: hw1pr2.py
# Name: İsmail Kavuran
# Problem description: First few functions!

def dbl(x):
    """Result: dbl returns twice its argument
       Argument x: a number (int or float)
       Spam is great, and dbl("spam") is better!
    """
    return 2*x

def sq(x):
   """Result: sq returns square of its argument
       Argument x: a number (int or float)
   """
   return x*x

def interp(low, hi, fraction):
   """Result: interp returns floating-point of its argument
       Argument x: a number (int or float)
   """
   return ((hi-low)*fraction) + low

def checkends(s):
   """Result: returns True if the first character in s is the same as the last character in s. It returns False otherwise.
       Argument s: strings
   """
   if s[0] == s[-1] :
      return True
   else:
      return False

def has42(d):
   """Result:  takes in a dictionary d and returns True if the key 42 is in the dictionary. It returns False otherwise.
       Argument d: dictionary
   """
   if 42 in d:
      return True
   else:
      return False

def hasKey(k,d):
   """Result:  takes in a dictionary d and returns True if the key k is in the dictionary. It returns False otherwise.
       Argument d: dictionary
       argument k: string, number, key
   """
   if k in d:
      return True
   else:
      return False

def flipside(s):
    """
    Result:a string whose first half is s's second half and whose second half is s's first half
    Argument s: strings
    """
    x = len(s)//2
    return  s[x:]+s[0:x]

def convertFromSeconds(s):
    """
    Result:returns a list (we'll call it L) of four nonnegative integers that represents that number of seconds in more conventional units of time
    Argument s: nonnegative integer
    """
    days = s // (24*60*60)  # Number of days
    s = s % (24*60*60)      # The leftover
    hours = s // (60*60)
    s = s % (60*60)
    minutes = s // 60
    s = s % 60
    seconds = s
    return [days, hours, minutes, seconds]