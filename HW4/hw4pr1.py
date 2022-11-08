#CS5, hw4pr1
#Filename: hw4pr1.py
# Name: İsmail Kavuran
#Problem Description: Binary <-> decimal conversions
# I got help from Wilson A. Zambrano for the last 4 functions

def isOdd(n):
    if n % 2 == 0:
        return False
    else:
        return True
    
print("isOdd(42)    should be  False:", isOdd(42))
print("isOdd(43)    should be  True:", isOdd(43))


def numToBinary(N):
    """
    """
    if N == 0:
        return ''
    elif N >= 1:
      numToBinary(N//2)
      print(N % 2, end = '')


print("numToBinary(0)      should be  '':",  numToBinary(0))
print("numToBinary(42)     should be  '101010':",  numToBinary(42))

def binaryToNum(S):
    if len(S) == 0:
        return 0 
    else:
        return binaryToNum(S[:-1])*2+int(S[-1])


def increment(S):
    N1 = binaryToNum(S)
    N2 = N1 + 1
    BN2 = numToBinary(N2)
    W = 8-len(BN2)
    BN2_Value = W*('0') + BN2
    if len(BN2_Value) < 8:
        return BN2_Value
    else:
        return BN2_Value[-8:] 
print("increment('00101001')    should be  00101010:", increment('00101001'))
print("increment('00000011')    should be  00000100:", increment('00000011'))
print("increment('11111111')    should be  00000000:", increment('11111111'))

def count (S,n):
    NewNumSet = increment(S)
    print(S)
    if n == 1:
        return NewNumSet
    else:
        return count(NewNumSet, n-1)

def numToTernary(N):
    """The ternary representation of 59 equates to '2012'. 2(3^4)+0(0^3)+1(3^2)+2(3^1)=59"""
    if N == 0:
        return ''
    else: 
        return numToTernary(N//3) + str(N%3)

def ternaryToNum(S):
    if len(S) == 0:
        return 0 
    else:
        return ternaryToNum(S[:-1])*3+int(S[-1])