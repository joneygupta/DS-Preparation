##def main():
####    line = 'asdf fjdk; afed, fjek,asdf,      foo'
##    import re
##    line1 = re.split(r'\s*\,\;', line)
##    print(line1)
##main()



##l = [1,2,3,4]
##ext = [1,2,3,4]
##
##l.extend(ext)
##l.append(ext)
##
##print (tuple(l))#Converted to Tuple
####print (set(l)) #Duplicate Removal

##----------------------------------------------------------------------------------------------------------------------------------------------------------

##add = lambda x ,y : x + y
##a = add(1,1)
##print (a)

##r = [1,2,3,4,5,6]
##plus_one = list(map(lambda x : x+1 , r))
##print (plus_one)

##filt = list(filter(lambda x : x >3 , r))
##print(filt)

##Something wrong here
##from functools import reduce
##red = list(reduce(lambda x : x+1 , r))
##print (red)


##c = [1,2,3,4,5,6,7]
##d = list()
##[d.append(i+2) for i in c]
##print (d)

##----------------------------------------------------------------------------------------------------------------------------------------------------------

##Dictionary

##s = dict()
##s['name'] = 'Shubham' , 'Gupta'
##print (s)
##s1 = dict()
##s1 = {'a' : 'Apple' , 'b' : 'Ball'}
##print (s1)

##----------------------------------------------------------------------------------------------------------------------------------------------------------

##
####Decorator
##
##def comment(func):
##    def inner(a,b):
##        print ('Adding Number' ,a, 'and', b )
##        return func(a,b)
##    return inner
##
##@comment
##def add(x,y):
##    print (x+y)
##def main():
##    add(1,2)
##main()


## I/O##-----------------------------------------------------------------------------------------------------------------------------------------------------------------

##Read and Write Entire file

##with open('Git_Commands1.txt','wt',errors = 'ignore') as data1:
##    data1.write('hhssd ahs qvbav kabva vaavb qjvnjf')
##
##with open('Git_Commands1.txt','rt',errors = 'ignore') as data:
##    print (data.read())
##
####print ('asdfghjkk,dgvf,sdf',sep = ';',end = '!!n')
##print (';'.join('i am shubham'))


##
##If you ever need to read or write text from a binary-mode file, make sure you remember
##to decode or encode it. For example:
##with open('somefile.bin', 'rb') as f:
##    data = f.read(16)
##    text = data.decode('utf-8')


##
##import array
##nums = array.array('i', [1, 2, 3, 4])
##print (nums)
##


##You want to write data to a file, but only if it doesn’t already exist on the filesystem

##
##This problem is easily solved by using the little-known x mode to open() instead of the
##usual w mode. For example:
##>>> with open('somefile', 'wt') as f:
##...     f.write('Hello\n')
##...
##>>> with open('somefile', 'xt') as f:
##...     f.write('Hello\n')


##If the file is binary mode, use mode xb instead of xt.

##--------------------------------------------------------------------------------------------------------------------------------------

##---------------------------------------------------------------------------------------------------------------------------------------


##
##list1 = ["1","2","3","4","5"]
##list2 = ";".join(list1)
##print(list2)


##words = 'The quick brown fox jumps over the lazy dog'.split()
##print(words)
##stuff = (map(lambda w: [w.upper(), w.lower(), len(w)], words))
##print (list(stuff))


##str = "Dictionary"
##
##it = iter(str)
##print (next(it))
##print (next(it))
##print (list(it))
##

##----------------------------------------------------------------------------------------------------------------------------------------------------------

##Normal Class in Python
##class A():
##    def __init__(self,a,b):
##        self.a = a
##        self.b = b
##    
##    def m1(self):
##        c = self.a + self.b
##        return c
##        
##def main():
##    a = A(21,2)
##    add = a.m1()
##    print(add)
##main()
##

##----------------------------------------------------------------------------------------------------------------------------------------------------------

##Sorting
##k = [7,6,5,4,3,2,1]

##k.remove(2)
##print (k)

####In Order Sorting(k will be updated)
##k.sort()
##print (k)


##Copied Sorting(k will remain same the sortd contents will be copied to a new variable)
##k1 = sorted(k)
##print (k1)
##print(k)
##k = k1.sort(reverse = True)
##print (k1)


##---------------------------------------------------------------------------------------------------------------------------------------

##Why we need class and static functions in python?

## 1) @StaticMethod : Dont access class insatnce or self - use in case of where u dont need to instantiate instance. or self or anything like (Math function)
## eg : istead of : math = Math() and then math.floor(1.22) , use this  : Math.floor(1.22)


##2) @ClassMehod  : Used class instance as first argument and we use it when we want to use variable defined in class without any self.

##ClassMehod

##class A():
##    x = 1
##    y = 6
##    def __init__(self,a,b):
##        self.a = a
##        self.b = b
##        
##    @classmethod
##    def m1(cls):
##        c = cls.x + cls.y
##        return c
##        
##def main():
##    a1 = A(21,2)
##    add = a1.m1()
##    print(add)
##main()



##StaticMehod
##import math
##class A():
##    x = 1
##    y = 6
##    def __init__(self,a,b):
##        self.a = a
##        self.b = b
##
##    #Normal Function
##    def m3(self):
##        add = self.a + self.b
##        return add
##
##    @classmethod
##    def m2(cls):
##        c1 = cls.x + cls.y
##        return c1
##    
##    @staticmethod
##    def m1():
##        c = math.floor(1.222)
##        c3 = math.ceil(1.222)
##        return c,c3
##        
##def main():
##    a1 = A(21,2)
##    d ,d1= a1.m1()
##    print(d,d1)
##main()
##

##----------------------------------------------------------------------------------------------------------------------------------------------------------

##Inheritance , Overriding and overloading in python

##Overloading methods in Python is not supported ? Yes, Python supports overloading but in a Pythonic way

##class Baseclass(object):
##    def __init__(self,name):
##        self.name = name
##        
##    def printname(self):
##        print (self.name)
##        
##    def OverRide(self):
##        print ('Parent OverRiding')
##        
##class InheritClass(Baseclass):
##    def __init__(self,n):
##        super(InheritClass,self).__init__(n)
##
##    def OverRide(self):
##        super(InheritClass,self).OverRide()
##        print ('child OverRiding')
##        
##def main():
##    i = InheritClass('I Am Shubham')
##    i.printname()
##    i.OverRide()
##main()



##Method Overloading
##
##def add(instanceOf, *args):
##    if instanceOf == 'int':
##        result = 0
##    if instanceOf == 'str':
##        result = ''
##    for i in args:
##        result = result + i
##    return result
## 
##print (add('int', 3,4,5))
##print (add('str', 'I',' am',' in', ' Python'))

##----------------------------------------------------------------------------------------------------------------------------------------------------------

##yield , generators and iterators


##iterators
##mylist = [x*x for x in range(3)]
##print (mylist)
##for i in mylist:
##    print(i)


##generators
##Generators are iterators, but you can only iterate over them once. It’s because they do not store all the values in memory, they generate the values on the fly:

##It is just the same except you used () instead of []. BUT, you can not perform for i in mygenerator a second time since generators can only be used once:
##they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one

##mygenerator = (x*x for x in range(3))
##print (mygenerator)
##for i in mygenerator:
##    print(i)


##yield
##Yield is a keyword that is used like return, except the function will return a generator.

##def createGenerator():
##    mylist = range(3)
##    for i in mylist:
##        yield i*i
##        break
##
##mygenerator = createGenerator() # create a generator
##
##print(mygenerator) # mygenerator is an object!
##
##for i in mygenerator:
##     print(i)

##OR


# A generator function that yields 1 for first time,
# 2 second time and 3 third time
##def simpleGeneratorFun():
##    yield 1
##    yield 2
##    yield 3
## 
### Driver code to check above generator function
##for value in simpleGeneratorFun(): 
##    print(value)

##----------------------------------------------------------------------------------------------------------------------------------------------------------

##Random Var
##import random
##x = random.randrange(1,1000)
##print(x)

##----------------------------------------------------------------------------------------------------------------------------------------------------------

#3#zip function
##
##first = ['Bucky','Tom','Taylor']
##last = ['Roberts','Hanks','Swift']
##middle = ['kumar','bresnan','smelly']
##
###zip lists together and store them in name 
##names = zip(first,middle,last)
##
##for a, b, c in names:
##    print(a,b,c)

##----------------------------------------------------------------------------------------------------------------------------------------------------------

##----------------------------------------------------------------------------------------------------------------------------------------------------------
##Min , Max Function

##stocks = {
##     'GOOG':520.54,
##     'FB':76.45,
##     'YHOO':39.28,
##     'AMN':306.21,
##     'APPL':99.76
##}
##
##print('Min value According to the values (as we mentioned values first and keys later) :')
##print(min(zip(stocks.keys() ,stocks.values())))
##print('Max value in the dictionary : ')
##print(max(zip(stocks.values(),stocks.keys())))
##----------------------------------------------------------------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------------------------------------------------------------
##5.6. Performing I/O Operations on a String





##----------------------------------------------------------------------------------------------------------------------------------------------------------
##Thread in python


##----------------------------------------------------------------------------------------------------------------------------------------------------------
##Input From COnsole(USer)
##a = int(input('Enter a number : '))
##print (a+1)
##----------------------------------------------------------------------------------------------------------------------------------------------------------







