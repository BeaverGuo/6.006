
'''
# this is for python beginners,actually novices
#1
def HelloWorld():
    print('Hello World!')
    
HelloWorld()
#print in one line
print('carpe',end=' zzz')
print('diem')

#2
wish = input('Enter your wish:')
print('Your wish is: ',wish)

#3 Input a number with int()
x = int(input("Enter a number: "))
print("One half of", x, "=", x/2)

#4
# list all the functions in the math module
# (ignore items in __double_underscores__)
import math
print(dir(math))

# even better, read the online docs!
import webbrowser
input("Hit enter to see the online docs for the math module.")
webbrowser.open("https://docs.python.org/3/library/math.html")

#5
x = 5
def f(y, z):
    result = x + y + z
    return result
print(f(1, 2)) # 8
print(f(3, 4)) # 12

# Vocabulary:
#   global variable
#   local variable
#   statement
#   expression
#   function definition (or declaration)
#   function call
#   parameter (or "formal parameter")
#   argument
#   return value
#   return type

#6
def isPositive(x):
    print("Hello!")   # runs
    return (x > 0)
    print("Goodbye!") # does not run ("dead code")

print(isPositive(5))  # prints Hello, then True

def f(x):
    x + 42

print(f(5)) # None NoneType

#7
g = 100

def f(x):
    # If we modify a global variable, we must declare it as global.
    # Otherwise, Python will assume it is a local variable.
    global g
    g += 1
    return x + g

print(f(5)) # 106
print(f(6)) # 108
print(g)    # 102

#8
import math
def f():
    print("This is a user-defined function")
    return 42

print("Some basic types in Python:")
print(type(2))           # int
print(type(2.2))         # float
print(type("2.2"))       # str  (string)
print(type(2 < 2.2))     # bool (boolean)
print(type(math))        # module
print(type(math.tan))    # builtin_function_or_method ("function" in Brython)
print(type(f))           # function (user-defined function)
print(type(type(42)))    # type

print("#####################################################")

print("And some other types we will see later in the course...")
print(type(Exception())) # Exception
print(type(range(5)))    # range
print(type([1,2,3]))     # list
print(type((1,2,3)))     # tuple
print(type({1,2}))       # set
print(type({1:42}))      # dict (dictionary or map)
print(type(2+3j))        # complex  (complex number) (we may not see this type)

#9
print(3 * 2)
print(3 * "abc")
print(3 + 2)
print("abc" + "def")
print(3 + "def")

#10
print("The / operator does 'normal' float division:")
print(" 5/3  =", ( 5/3))
print()
print("The // operator does integer division:")
print(" 5//3 =", ( 5//3))
print(" 2//3 =", ( 2//3))
print("-1//3 =", (-1//3))
print("-4//3 =", (-4//3))

#11
def mod(a, b):
  return a - (a//b)*b

print(41%14, mod(41,14))
print(14%41, mod(14,41))
print(-32%9, mod(-32,9))
print(32%-9, mod(32,-9))

#12
print(0.1 + 0.1 == 0.2)        # True, but...
print(0.1 + 0.1 + 0.1 == 0.3)  # False!
print(0.1 + 0.1 + 0.1)         # prints 0.30000000000000004 (uh oh)
print((0.1 + 0.1 + 0.1) - 0.3) # prints 5.55111512313e-17 (tiny, but non-zero!)

#13
def isPositive(n):
    result = (n > 0)
    print("isPositive(",n,") =", result)
    return result

def isEven(n):
    result = (n % 2 == 0)
    print("isEven(",n,") =", result)
    return result

print("Test 1: isEven(-4) and isPositive(-4))")
print(isEven(-4) and isPositive(-4)) # Calls both functions
print("----------")
print("Test 2: isEven(-3) and isPositive(-3)")
print(isEven(-3) and isPositive(-3)) # Calls only one function!

#14
def isLegalTriangle(s1, s2, s3):
    if(s1>0 and s2>0 and s3>0 and (s1+s2) > s3 and (s3+s1) > s2 and (s2+s1) > s3):
        return True # replace with your solution
    else:
        return False

def testIsLegalTriangle():
    print("Testing isLegalTriangle()...", end="")
    assert(isLegalTriangle(3, 4, 5))
    assert(isLegalTriangle(5, 4, 3))
    assert(isLegalTriangle(3, 5, 4))
    assert(isLegalTriangle(0.3, 0.4, 0.5))
    assert(not isLegalTriangle(3, 4, 7))
    assert(not isLegalTriangle(7, 4, 3))#why this fail?
    assert(not isLegalTriangle(3, 7, 4))
    assert(not isLegalTriangle(5, -3, 1))
    assert(not isLegalTriangle(-3, -4, -5))
    print("Passed.")
    print("(Add more tests to be more sure!)")

testIsLegalTriangle()

#15
def nthFibonacci(n):
    if(n==0 or n==1):
        return 1
    elif(n==2):
        return 2
    else:
        return nthFibonacci(n-1) + nthFibonacci(n-2)

def testNthFibonacci():
    print("Testing nthFibonacci()...", end="")
    assert(nthFibonacci(0) == 1)
    assert(nthFibonacci(1) == 1)
    assert(nthFibonacci(2) == 2)
    assert(nthFibonacci(3) == 3)
    assert(nthFibonacci(4) == 5)
    assert(nthFibonacci(5) == 8)
    assert(nthFibonacci(6) == 13)
    print("Passed.")
    print("(Add more tests to be more sure!)")

testNthFibonacci()

#16
def circlesIntersect(x1, y1, r1, x2, y2, r2):
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if(r1+r2>=distance):
        return True # replace with your solution
    else:
        return False# do not forget else

def testCirclesIntersect():
    print("Testing circlesIntersect()...", end="")
    assert(circlesIntersect(0, 0, 2, 3, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    print("Passed.")
    print("(Add more tests to be more sure!)")

testCirclesIntersect()

#17 Write the function nearestOdd(n) that takes an int or float n, and returns 
# as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value.
import math
def nearestOdd(n):
    #method 1
    # floorVal = math.floor(n)
    # if(n%2 == 0):
    #     return n-1;
    # elif(floorVal%2 == 0):
    #     return floorVal+1
    # else:
    #     return floorVal
    #method 2
    if(n%2==0):
        return n-1
    elif(n%2>=1):
        return math.floor(n)
    else:
        return math.floor(n)+1

def testNearestOdd():
    print("Testing nearestOdd()...", end="")
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    print("Passed.")
    print("(Add more tests to be more sure!)")

testNearestOdd()

#18 Write the function eggCartons(eggs) that takes a non-negative integer number
# of eggs, and returns the smallest integer number of cartons required to hold 
#that many eggs, where a carton may hold up to 12 eggs.
def eggCartons(eggs):
    if(eggs%12 == 0):
        return eggs/12
    else:
        return eggs//12+1

def testEggCartons():
    print("Testing eggCartons()...", end="")
    assert(eggCartons(0) == 0)
    assert(eggCartons(1) == 1)
    assert(eggCartons(12) == 1)
    assert(eggCartons(13) == 2)
    assert(eggCartons(24) == 2)
    assert(eggCartons(25) == 3)
    print("Passed.")
    print("(Add more tests to be more sure!)")

testEggCartons()

#19 Write the function pittsburghHour(londonHour) that takes a non-negative integer, 
# the current hour in London, and returns as an integer the current hour in Pittsburgh 
# (which is 5 hours behind London). However, London time is given in 24-hour time 
# (so londonHour is between 0 and 23, inclusive), but Pittsburgh time must be 
# returned in 12-hour time (so the result must be between 1 and 12, inclusive, 
#     where "am" and "pm" are ignored). 
# See the test cases in the code below for some examples.
def pittsburghHour(londonHour):
    if(londonHour-5<=0):
        return londonHour + 7
    elif(londonHour-5>12):
        return londonHour - 17
    else:
        return londonHour - 5

def testPittsburghHour():
    print("Testing pittsburghHour()...", end="")
                                     # London   Pittsburgh
    assert(pittsburghHour( 0) ==  7) # midnight    7pm
    assert(pittsburghHour( 5) == 12) #   5am      12am (midnight)
    assert(pittsburghHour(10) ==  5) #  10am       5am
    assert(pittsburghHour(12) ==  7) #  noon       7am
    assert(pittsburghHour(17) == 12) #   5pm       12pm (noon)
    assert(pittsburghHour(18) ==  1) #   6pm       1pm
    print("Passed.")
    print("(Add more tests to be more sure!)")

testPittsburghHour()

#20
def areCollinear(x1, y1, x2, y2, x3, y3):
    if(y1-y2 == 0 or y1-y3 == 0):
        if(y1==y2 and y1==y3):
            return True
        else:
            return False
    else:
        if((x1-x2)/(y1-y2) == (x1-x3)/(y1-y3)):
            return True
        else:
            return False

def testAreCollinear():
    print("Testing testAreCollinear()...", end="")
    assert(areCollinear(0, 0, 1, 1, 2, 2) == True)
    assert(areCollinear(0, 0, 1, 1, 2, 3) == False)
    assert(areCollinear(1, 1, 0, 0, 2, 2) == True)
    assert(areCollinear(1, 1, 0, -1, 2, 2) == False)
    assert(areCollinear(2, 0, 2, 1, 2, 2) == True)
    assert(areCollinear(2, 0, 2, 1, 3, 2) == False)
    assert(areCollinear(3, 0, 2, 1, 3, 2) == False)
    print("Passed.")
    print("(Add more tests to be more sure!)")

testAreCollinear()

#21 ???
def numberOfPoolBallRows(balls):
    return 42 # replace with your solution

def testNumberOfPoolBallRows():
    print("Testing numberOfPoolBallRows()...", end="")
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print("Passed.")
    print("(Add more tests to be more sure!)")

testNumberOfPoolBallRows()

#22 N = d + 2m + [3(m+1)/5] + y + [y/4] - [y/100] + [y/400] + 2   ??
import math
def dayOfWeek(month, day, year):
    N = day + 2*month + math.ceil(3*(month+1)/5) + year + math.ceil(year/4) - math.ceil(year/100) + math.ceil(year/400) + 2
    return math.floor(N%7) + 1

def testDayOfWeek():
    print("Testing dayOfWeek()...", end="")
    # On 2/5/2006, the Steelers won Super Bowl XL on a Sunday!
    assert(dayOfWeek(2, 5, 2006) == 1)
    # On 6/15/1215, the Magna Carta was signed on a Monday!
    assert(dayOfWeek(6, 15, 1215) == 2)
    # On 3/11/1952, the author Douglas Adams was born on a Tuesday!
    assert(dayOfWeek(3, 11, 1952) == 3)
    # on 4/12/1961, Yuri Gagarin became the first man in space, on a Wednesday!
    assert(dayOfWeek(4, 12, 1961) == 4)
    # On 7/4/1776, the Declaration of Independence was signed on a Thursday!
    assert(dayOfWeek(7, 4, 1776) == 5)
    # on 1/2/1920, Isaac Asimov was born on a Friday!
    assert(dayOfWeek(1, 2, 1920) == 6)
    # on 10/11/1975, Saturday Night Live debuted on a Saturday (of course)!
    assert(dayOfWeek(10, 11, 1975) == 7)
    print("Passed.")
    print("(Add more tests to be more sure!)")

testDayOfWeek()

#23
# nearestBusStop(street)
# Write the function nearestBusStop(street) that takes a non-negative int street number, 
# and returns the nearest bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, so the nearest bus stop to 12th street 
# is 8th street, and the nearest bus stop to 13 street is 16th street.

street = 50;
def nearestBusStop(street):
    left = street % 8
    right = (street//8 + 1)*8 - street
    if(street<0):
        return False
    elif(street<8):
        return street
    elif(left > right):
        return right + street
    else:
        return street//8 * 8
        
print (nearestBusStop(50))

#24
# setKthDigit(n, k, d) 
# Write the function setKthDigit(n, k, d) that takes three non-negative integers -- n, k, and d -- 
# where d is a single digit (between 0 and 9 inclusive), and returns the number n but with the kth digit 
# replaced with d. Counting starts at 0 and goes right-to-left, so the 0th digit is the rightmost digit. 
# For example: 
# setKthDigit(468, 0, 1) returns 461
# setKthDigit(468, 1, 1) returns 418
# setKthDigit(468, 2, 1) returns 168
# setKthDigit(468, 3, 1) returns 1468
num = 468
def setKthDigit(n,k,d):
    m = n
    for i in range(k+1):#0....k means range(k+1)
        m = m % 10;
    return n - m*(10**k) + d*(10**k)

print(setKthDigit(num,0,1))

#25
def isPrime(n):
    if(n < 2):
        return False
    else:
        for i in range(2,n):
            if(n % i == 0):
                return False
        return True

def fasterIsPrime(n):
    if(n < 2):
        return False
    if(n == 2):
        return True
    if(n % 2 == 0):
        return False
    maxFactor = int(n**0.5);
    for i in range(3,maxFactor+1,2):
        if( n % i == 0):
            return False
    return True
# And try out this version:
for n in range(100):
    if fasterIsPrime(n):
        print(n, end=" ")
print()  # output a linefeed

# Now let's see if we really sped things up
import time
bigPrime = 1010809 #499 # Try 1010809, or 10101023, or 102030407
print("Timing isPrime(",bigPrime,")", end=" ")
time0 = time.time()
print(", returns ", isPrime(bigPrime), end=" ")
time1 = time.time()
print(", time = ",(time1-time0)*1000,"ms")

print("Timing fasterIsPrime(",bigPrime,")", end=" ")
time0 = time.time()
print(", returns ", fasterIsPrime(bigPrime), end=" ")
time1 = time.time()
print(", time = ",(time1-time0)*1000,"ms")

#26 ?
# mostFrequentDigit(n) 
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and 
# returns the digit from 0 to 9 that occurs most frequently in it, with ties going 
# to the smaller digit.
def mostFrequentDigit(n):
    if(n<0):
        return False

    while(n>=10):
        curNum = n%10
        n//=10
        curNumCnt

        for i in curVal:
            if(i==n%10):
                counter[j++]++
            else:
                curVal.extend(n%10)

        curVal.extend(n%10)

    maxcnt = 0
    for i in curVal:
        if i>maxcnt:
            maxcnt=i


#27 ?

# isRotation(x, y) 
# Write the function isRotation(x, y) that takes two non-negative integers x and y and returns True 
# if x is a rotation of the digits of y and False otherwise. For example, 3412 is a rotation of 1234,
#  and 321 (with an implicit leading 0) is a rotation of 3210. Any number is a rotation of itself.
def isRotation(x, y):
    if(x==y):
        return True
    i=-1
    while(x>=10):
        i++
        x%10
        x//=10

#28
# hasOnlyOddDigits(n) 
# Write the function hasOnlyOddDigits(n) that takes a possibly-negative integer n and 
# returns True if n only has odd digits, and False otherwise (that is, if it has any even digits).
def isEven(n):
    if(n%2 == 0):
        return True
    return False

def hasOnlyOddDigits(n):
    if(n<0):
        n = -n
    while(n>0):
        if(isEven(n%10)):
            return False
        n//=10
    return True

print(hasOnlyOddDigits(111))

#29
# longestDigitRun(n) 
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and 
# returns the digit that has the longest consecutive run, or the smallest such digit if 
# there is a tie. So, longestDigitRun(117773732) returns 7 (because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestDigitRun(n):
    if(n<0):
        n = -n
    maxNum=0
    last=-1
    curCnt = 0
    result = -1
    while(n>0):
        if(last==n%10):
            curCnt+=1
            last=n%10
            n//=10
            #处理最高位为最大连续数字的情况
            if(n==0 and curCnt>maxNum or (curCnt==maxNum and last < result)):
                return last
        elif(curCnt>maxNum or (curCnt==maxNum and n%10 < result)):
            result = last
            maxNum = curCnt
            curCnt = 1
            last = n%10
            n//=10
        else:
            last = n%10
            curCnt = 1
            n//=10

    return result

print(longestDigitRun(11555959))

#30
#backslash in string
print('hello world! "Wow~" \'use backslash\' ')
print("ring" in "strings")
print("wow" in "amazing!")
print("Yes" in "yes!")
print("" in "No way!")

#31
s = "abcdefgh"
print(s)
print(s[-1])
print(s[-2])
s = "abcdefgh"
print(s)
print(s[0:3])
print(s[1:3])
print("-----------")
print(s[2:3])
print(s[3:3])
s = "abcdefgh"
print(s)
print(s[3:])
print(s[:3])
print(s[:])

#32
s = "abcdefgh"

print("This works, but is confusing:")
print(s[::-1])

print("This also works, but is still confusing:")
print("".join(reversed(s)))

print("Best way: write your own reverseString() function:")

def reverseString(s):
    return s[::-1]

print(reverseString(s)) # crystal clear!

#33
s = "abcd"
for i in range(len(s)):
    print(i, s[i])

s = "abcd"
for c in s:
    print(c)

name = input("Enter your name: ")
print("Hi, " + name + ". Your name has " + str(len(name)) + " letters!")

#34
# Note: As this requires read-write access to your hard drive,
#       this will not run in the browser in Brython.

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

contentsToWrite = "This is a test!\nIt is only a test!"
writeFile("foo.txt", contentsToWrite)

contentsRead = readFile("foo.txt")
assert(contentsRead == contentsToWrite)

print("Open the file foo.txt and verify its contents.")

a = [ 2, 3, 5, 7 ]
print("a =", a)

a[0],a[1] = a[1],a[0]
print("After swapping a[0] and a[1]:")
print("   a=",a)

#35

a = [ 2, 3, 5, 3, 7 ]
print("a =", a)

# Failed attempt to remove all the 3's
for index in range(len(a)):
    if (a[index] == 3):  # this eventually crashes!
        a.pop(index)

print("This line will not run!")

#36
import copy
a = [2, 3]
b = copy.copy(a)
c = a[:]
d = a + [ ]
e = list(a)
f = copy.deepcopy(a)
g = sorted(a)
a[0] = 42
print(a, b, c, d, e, f, g)

a = [i for i in range(10)]
print(a)
a = [(i*100) for i in range(20) if i%5 == 0]
print(a)

from tkinter import *
def draw(canvas, width, height):
    pass # replace with your drawing code!
def runDrawing(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("bye!")
runDrawing(400, 200)

import math
def drawClock(canvas, x0, y0, x1, y1, hour, minute):
    # draw a clock in the area bounded by (x0,y0) in
    # the top-left and (x1,y1) in the bottom-right
    # with the given time
    # draw an outline rectangle
    canvas.create_rectangle(x0, y0, x1, y1, outline="black", width=1)
    # find relevant values for positioning clock
    width = (x1 - x0)
    height = (y1 - y0)
    r = min(width, height)/2
    cx = (x0 + x1)/2
    cy = (y0 + y1)/2
    # draw the clock face
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline="black", width=2)
    # adjust the hour to take the minutes into account
    hour += minute/60.0
    # find the hourAngle and draw the hour hand
    # but we must adjust because 0 is vertical and
    # it proceeds clockwise, not counter-clockwise!
    hourAngle = math.pi/2 - 2*math.pi*hour/12
    hourRadius = r*1/2
    hourX = cx + hourRadius * math.cos(hourAngle)
    hourY = cy - hourRadius * math.sin(hourAngle)
    canvas.create_line(cx, cy, hourX, hourY, fill="black", width=1)
    # repeat with the minuteAngle for the minuteHand
    minuteAngle = math.pi/2 - 2*math.pi*minute/60
    minuteRadius = r*9/10
    minuteX = cx + minuteRadius * math.cos(minuteAngle)
    minuteY = cy - minuteRadius * math.sin(minuteAngle) 
    canvas.create_line(cx, cy, minuteX, minuteY, fill="black", width=1)
def draw(canvas, width, height):
    # Draw a large clock showing 2:30
    drawClock(canvas, 25, 25, 175, 150, 2, 30)
    # And draw a smaller one below it showing 7:45
    drawClock(canvas, 75, 160, 125, 200, 7, 45)
    # Now let's have some fun and draw a whole grid of clocks!
    width = 40
    height = 40
    margin = 5
    hour = 0
    for row in range(3):
        for col in range(4):
            left = 200 + col * width + margin
            top = 50 + row * height + margin
            right = left + width - margin
            bottom = top + height - margin
            hour += 1
            drawClock(canvas, left, top, right, bottom, hour, 0)

#37
# Write the function areaOfPolygon(L) that takes a list of (x,y) points that are 
# guaranteed to be in either clockwise or counter-clockwise order around a polygon,
#  and returns the area of that polygon, as described here. For example (taken from 
#     that text), areaOfPolygon([(4,10), (9,7), (11,2), (2,2)]) returns 45.5 
#  (at least the result is almostEqual to 45.5).
def scalarProduct(l1,l2):
    return l1[0]*l2[1] - l1[1]*l2[0]
def areaOfPolygon(L):
    area = 0
    for i in range(len(L)-1):
        area += scalarProduct(L[i],L[i+1])
    area += scalarProduct(L[len(L)-1],L[0])
    return 0.5*area
def almostEqual(d1, d2):
    epsilon = 10**-8
    return abs(d1 - d2) < epsilon
def testAreaOfPolygon():
    print("Testing areaOfPolygon()...", end="")
    assert(almostEqual(areaOfPolygon([(4,10), (9,7), (11,2), (2,2)]), 45.5))
    assert(almostEqual(areaOfPolygon([(9,7), (11,2), (2,2), (4, 10)]), 45.5))
    assert(almostEqual(areaOfPolygon([(0, 0), (0.5,1), (1,0)]), 0.5))
    assert(almostEqual(areaOfPolygon([(0, 10), (0.5,11), (1,10)]), 0.5))
    assert(almostEqual(areaOfPolygon([(-0.5, 10), (0,-11), (0.5,10)]), 10.5))
    print("Passed!")

testAreaOfPolygon()

#38
# Background: we can represent a polynomial as a list of its coefficients. For example, 
# [2, 3, 0, 4] could represent the polynomial 2x3 + 3x2 + 4. With this in mind, write 
# the function evalPolynomial(coeffs, x) that takes a list of coefficients and a value x 
# and returns the value of that polynomial evaluated at that x value. For example, 
# evalPolynomial([2,3,0,4], 4) returns 180 (2*43 + 3*42 + 4 = 2*64 + 3*16 + 4 = 128 + 48 + 4 = 180).
def evalPolynomial(coeffs, x):
    val = 0
    reversedCoeff = coeffs[::-1]
    for index in range(len(reversedCoeff)):
        val += reversedCoeff[index]*x**index
    return val # place your answer here!
def testEvalPolynomial():
    print("Testing evalPolynomial()...", end="")
    # f(x) = 2x^3 + 3x^2 + 4, f(4) = 180
    assert(evalPolynomial([2,3,0,4], 4) == 180)
    # f(x) = 6, f(42) = 6
    assert(evalPolynomial([6], 42) == 6)
    # f(x) = 6x^2 -2x - 20, f(-1) = -12
    assert(evalPolynomial([6,-2,-20], -1) == -12)
    # f(x) = 6x^5-8x^3-8x, f(2) = 112, f(1) = -10, f(0) = 0
    assert(evalPolynomial([6,0,-8,0,-8,0], 2) == 112)
    assert(evalPolynomial([6,0,-8,0,-8,0], 1) == -10)
    assert(evalPolynomial([6,0,-8,0,-8,0], 0) == 0)
    print("Passed!")
testEvalPolynomial()

#39
# Write the function multiplyPolynomials(p1, p2) which takes two polynomials as 
# defined in the previous problem and returns a third polynomial which is the product
#  of the two. For example, multiplyPolynomials([2,0,3], [4,5]) represents the problem 
#  (2x2 + 3)(4x + 5), and:
#     (2x2 + 3)(4x + 5) = 8x3 + 10x2 + 12x + 15
# And so this returns [8, 10, 12, 15].
def multiplyPolynomials(p1, p2):
    tp1 = p1[::-1]
    tp2 = p2[::-1]
    p = [0]*(len(tp1)+len(tp2) - 1)
    for i in range(len(tp1)):
        for j in range(len(tp2)):
            p[i+j] += tp1[i]*tp2[j]
    return p[::-1]
def testMultiplyPolynomials():
    print("Testing multiplyPolynomials()...", end="")
    # (2)*(3) == 6
    assert(multiplyPolynomials([2], [3]) == [6])
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    assert(multiplyPolynomials([2,-4],[3,5]) == [6,-2,-20])
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    assert(multiplyPolynomials([2,0,-4],[3,0,2,0]) == [6,0,-8,0,-8,0])
    print("Passed!")
testMultiplyPolynomials()

#40 ?
# Write the function repeatingPattern(L) that takes a list L and returns a tuple 
# of (pattern, repeat), where pattern is a list and repeat is an integer >= 2, where 
# the list L is composed of "repeat" consecutive instances of pattern. Return None 
# if no such pattern exists. For example, repeatingPattern([1,2,3,1,2,3]) returns ([1,2,3], 2).
def repeatingPattern(L):
    j=0
    for i in range(len(L)):
        if(i and L[j] == L[i]):

            j += 1
        else:
            return False
    return True

def testRepeatingPattern():
    print("Testing repeatingPattern()...", end="")
    assert(repeatingPattern([]) == None)
    assert(repeatingPattern([42]) == None)
    assert(repeatingPattern([1,2]) == None)
    assert(repeatingPattern([1,1]) == ([1], 2))
    assert(repeatingPattern([1,2,1]) == None)
    assert(repeatingPattern([1,2,3,1,2,3]) == ([1,2,3], 2))
    assert(repeatingPattern([1,2,3,1,2]) == None)
    assert(repeatingPattern([1,2,3,1,2,3,1]) == None)
    L = list(range(10))
    assert(repeatingPattern(L*20) == (L, 20))
    print("Passed!")

testRepeatingPattern()

#41 ?
# Write the function isNearlySorted(L) that takes a possibly-empty list L and 
# returns True if the list is "nearly sorted", and False otherwise, where a 
# "nearly sorted" list is one which is not sorted and requires exactly one swap 
# of two elements to become sorted.
def isNearlySorted(L):
    counter = 0
    tmp = sorted(L)
    if(L == tmp):
        return False
    for i in range(len(L)):
        if(i-1>=0 and i<= len(L)):
            if(L[i]<L[i-1] or L[i]>L[i+1]):
                counter += 1
    if(counter == 2):
        return True
    return False # place your answer here!
def testIsNearlySorted():
    print("Testing isNearlySorted()...", end="")
    assert(isNearlySorted([0,1,2,3]) == False)
    assert(isNearlySorted([]) == False)
    assert(isNearlySorted([42]) == False)
    assert(isNearlySorted([3,2]) == True)
    assert(isNearlySorted([2,2]) == False)
    assert(isNearlySorted([5,2,3,4,1,6]) == True)
    assert(isNearlySorted([1,2,3,5,4]) == True)
    print("Passed!")
testIsNearlySorted()

#42
import webbrowser
input("Hit enter to see the online docs for the math module.")
webbrowser.open("http://mathforum.org/alejandre/frisbie/student.locker.html")
def lockerProblem(lockers):
    isOpen = [ False ] * (lockers+1)
    students = lockers
    for student in range(1,students+1):
        for locker in range(student, lockers+1, student):
            isOpen[locker] = not isOpen[locker]
    openLockers = [ ]
    for locker in range(1, lockers+1):
        if isOpen[locker]:
            openLockers.append(locker)
    return openLockers
print(lockerProblem(2000))

#43
def letterCounts(s):
    counts = [0] * 26
    for ch in s.upper():
        if ((ch >= "A") and (ch <= "Z")):
            counts[ord(ch) - ord("A")] += 1
    return counts

def isAnagram(s1, s2):
    # First approach: same #'s of each letter
    return (letterCounts(s1) == letterCounts(s2))

def isAnagram(s1, s2):
    # Second approach: sorted strings must match!
    return sorted(list(s1.upper())) == sorted(list(s2.upper()))

def testIsAnagram():
    print("Testing isAnagram()...", end="")
    assert(isAnagram("", "") == True)
    assert(isAnagram("abCdabCd", "abcdabcd") == True)
    assert(isAnagram("abcdaBcD", "AAbbcddc") == True)
    assert(isAnagram("abcdaabcd", "aabbcddcb") == False)
    print("Passed!")

testIsAnagram()

#44
# sorting.py
import time, random
####################################################
# swap
####################################################

def swap(a, i, j):
    (a[i], a[j]) = (a[j], a[i])

####################################################
# selectionSort这是有一个值是固定的最小在最前面，然后遍历后面的
####################################################

def selectionSort(a):
    n = len(a)
    for startIndex in range(n):
        minIndex = startIndex
        for i in range(startIndex+1, n):
            if (a[i] < a[minIndex]):
                minIndex = i
        swap(a, startIndex, minIndex)

####################################################
# bubbleSort遍历一轮两两比较，找到大哥换到最后面 end-1再遍历
####################################################

def bubbleSort(a):
    n = len(a)
    end = n
    swapped = True
    while (swapped):
        swapped = False
        for i in range(1, end):
            if (a[i-1] > a[i]):
                swap(a, i-1, i)
                swapped = True
        end -= 1

####################################################
# mergeSort这个有点难?
####################################################

def merge(a, start1, start2, end):
    index1 = start1
    index2 = start2
    length = end - start1
    aux = [None] * length
    for i in range(length):#遍历将更小的项放入aux
        if ((index1 == start2) or
            ((index2 != end) and (a[index1] > a[index2]))):
            aux[i] = a[index2]#放入更小项
            index2 += 1#继续下一个融合
        else:
            aux[i] = a[index1]
            index1 += 1
    for i in range(start1, end):
        a[i] = aux[i - start1]#minus start1 for extend array a

def mergeSort(a):
    n = len(a)
    step = 1
    while (step < n):
        for start1 in range(0, n, 2*step):#教如何按指数2来分类分成2组,利用loop,([0],[2]),([1],[3]) 0,2  2*step, start1+step
            start2 = min(start1 + step, n)#start2从start1+step开始，没问题
            end = min(start1 + 2*step, n)#end =start1+2*step,如果就2组，如([0],[2]),([1],[3]),那么结束是2，即是(start1+step+step或者是start2+step),[2]就结束了
            merge(a, start1, start2, end)#start1和start2都是原来数组的序号
        step *= 2

####################################################
# builtinSort (wrapped as a function)
####################################################

def builtinSort(a):
    a.sort()

####################################################
# testSort
####################################################

def testSort(sortFn, n):
    a = [random.randint(0,2**31) for i in range(n)]
    sortedA = sorted(a)
    startTime = time.time()
    sortFn(a)
    endTime = time.time()
    elapsedTime = endTime - startTime
    assert(a == sortedA)
    print("%20s n=%d  time=%6.3fs" % (sortFn.__name__, n, elapsedTime))

def testSorts():
    n = 2**8 # use 2**8 for Brython, use 2**12 or larger for Python
    for sortFn in [selectionSort, bubbleSort, mergeSort, builtinSort]:
        testSort(sortFn, n)

testSorts()

#45
import math

price = 24
item = 'banana'
itemdict = {"item":"banana","cost":24}
print('the %s costs %d cents'%(item,price))
print('the %+10s costs %5.2f cents'%(item,price))#10s 5 white spaces?
print("The %+10s costs %10.2f cents"%(item,price))
print("The %(item)s costs %(cost)7.1f cents"%itemdict)

sqlist=[x*x for x in range(1,11)]
sqlist=[x*x for x in range(1,11) if x%2 != 0]
print(sqlist)

anumber = int(input('pls enter a interger:'))
try:
  print(math.sqrt(anumber))
except:
  print("Bad Value for square root")
  print("Using absolute value instead")
  print(math.sqrt(abs(anumber)))

if anumber < 0:
    raise RuntimeError("You can't use a negative number")
else:
    print(math.sqrt(anumber))

def squareroot(n):
    root = n/2    #initial guess will be 1/2 of n
    for k in range(20):
        root = (1/2)*(root + (n / root))
    return root
print(squareroot(9))

import random
def generateOne(strlen):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    res = ''
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]
    return res
def score(goal,teststring):
    numSame = 0
    for i in range(len(goal)):
        if(goal[i] == teststring[i]):
            numSame = numSame + 1;
    return numSame / len(goal)
def main():
    goalstring = 'methinks it is like a weasel'
    newstring =  generateOne(28)
    best = 0
    newscore = score(goalstring,newstring)
    while newscore < 1:
        if newscore > best:
            print(newscore,newstring)
            best =  newscore
        newstring = generateOne(28)
        newscore = score(goalstring,newstring)

main()

a = range(2,10,7)
a = [2,9]
(b,c) = (a,a[:2])#b is reference to a ,c is not
b[0] += 3 #change a[]
a += [3]
a = a + [4]
print (c + [b[0]])
print (c.append(b[1]))
print (a,b,c)

import copy
def f(a,b):
    a=copy.copy(a)
    a[0] = b[1]
    b[0] = a[1]
    return a+b
a1 = a2 = [5,6]#range(5,7)
b1 = b2 = [0,1]#range(2)
a1 = f(a1,b1)
print (a1,a2,b1,b2)
'''
