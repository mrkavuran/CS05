# CS 5 Gold, hw2pr3
# filename: hw2pr3.py
# Name: İsmail Kavuran
# problem description: List comprehensions

# this gives us functions like sin and cos
from math import *

# two more functions (not in the math library above)
def dbl(x):
    """Doubler!  argument: x, a number"""
    return 2*x

def sq(x):
    """Squarer!  argument: x, a number"""
    return x**2



# examples for getting used to list comprehensions...

def lc_mult(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each multiplied by 2**
    """
    return [2*x for x in range(N)]

def lc_idiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       WARNING: this is INTEGER division...!
    """
    return [x//2 for x in range(N)]

def lc_fdiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       NOTE: this is floating-point division...!
    """
    return [x/2 for x in range(N)]

# printing tests
print( "lc_mult(4)   should be [0, 2, 4, 6] :", lc_mult(4) )   
print( "lc_idiv(4)   should be [0, 0, 1, 1] :", lc_idiv(4) ) 
print( "lc_fdiv(4)   should be [0.0, 0.5, 1.0, 1.5] :", lc_fdiv(4) ) 

# assertion tests
assert lc_mult(4) == [0, 2, 4, 6]
assert lc_idiv(4) == [0, 0, 1, 1]
assert lc_fdiv(4) == [0.0, 0.5, 1.0, 1.5]

# Here is where your functions start for the homework:

# Step 1, part 1
def unitfracs( N ):
    """ this example takes in an int N
        and returs a list of N number between 0 and 1
        which have same difference
    """
    
    return [float(x)/N for x in range(N)]


def scaledfracs(low,hi,N):
    """ this example takes in three value low,hi,and N
        and returs a list of N number between low and hi
        which have same difference
    """
    return [float(low+x*(hi-low)) for x in unitfracs(N)]

def sqfracs(low,hi,N):
    """ this example takes in three value low,hi and N
        and returs a list of N number which is the
        square of its scaled fraction
    """
    return [sq(x) for x in scaledfracs(low,hi,N)]


def f_of_fracs(f,low,hi,N):
    """ this example takes in four value f as function,
        low and hi is limit and N is number of division
        and returs a list of N number which is the
        result of f of its scaled fraction
    """
    return [f(x) for x in scaledfracs(low,hi,N)]

def integrate(f,low,hi,N):
    """ integrate returns an estimate of the definite integral
     of the function f (the first input)
     with lower limit low (the second input)
     and upper limit hi (the third input)
     where N steps are taken (the fourth input)

    integrate simply returns the sum of the areas of rectangles
    under f, drawn at the left endpoints of N uniform steps
    from low to hi
  """
    diff = (hi-low)/float(N)
    return sum(f_of_fracs(f,low,hi,N))*diff

def c(x):
    """ c is a semicircular function of radius two """
    return (4-x**2)**0.5
#Q.2
#   integrate(c,0,2,2) is 3.732050807568877
#   integrate(c,0,2,20) is 3.2284648797549815
# if N goes to infinity then integral become zero because 
# if N zero then diff = (hi-low)/float(N) is zero then
# sum(f_of_fracs(f,low,hi,N))*diff become zero so integral become zero.