##Notes
##1-> everything in python treated as the object - functions, variables, class etc
##all
##
###------------------------------------------------------------------------------
##i) #CLass FUnctions
##1) Belong to the class and the object
##2) First argumaent should be class instance 'cls'
##3) No use of self
##4) class var(ex: a1) can be used with cls(cls.a1) shown below and can change
##the var value for the class and that will be updated for all things defined
##in the that class  
##5) use @classmethod to declare
##6) can call any method defined in the class even the static methods with
##cls(ex: cls.method1)
##7) Will be called with the class instance , cant be called directly with the
##class name or via any other ways


####Class Method
class A():
    a1 = 12
    @classmethod
    def a(cls):
        print ('Hello'+str(cls.a1))
        

def main():
    a11 = A()
    a11.a()

main()

###OR
##
##class CLS():
##    @classmethod
##    def A(cls):
##        print ('foo')
##
##    @classmethod
##    def B(cls):
##        cls.A()
##        print('doo')
##
##def main():
##    s = CLS()
##    s.B()
##    
##    
##main()
##
###------------------------------------------------------------------------------
##ii) Static Functions
##
##1)Just a separate function, dont belong to the class or the object
##2)self wont be there due to point 1
##3)@staticmethod use for declaration
##4)Cant use class var declared due to all the above points
##5)Any class funciton can call this function using cls instance of the class
##6)Cant acess any params or anything from outside the class or from other function
##beside the static one
##7)save cost as dont use to instantiate object everytime e access the function
##-no need of self object
##
####Static Method
##class A():
##    a1 = 12
##    @staticmethod
##    def a(name):
##        print ('hello '+'i am', name)
##        
##
##def main():
##    #A.a()
##    a1 = A()
##    a1.a('john')
##
##main()
##
###------------------------------------------------------------------------------
##iii)Decorator
##1)@method_name
##2)used to add additional functionality on the particular function
##
##
##def smart_divide(func):
##    def inner(a,b):
##        print("I am going to divide",a,"and",b)
##        if b == 0:
##            print("Whoops! cannot divide")
##            return
##
##        return func(a,b)
##    return inner
##
##@smart_divide
##def divide(a,b):
##    return a/b
##
##def main():
##    a = divide(2,3)
##    print (a)
##
##main()    
##
##
###OR
##
##def name1(func):
##    def inner(name):
##        print ('Hello')
##        return func(name)
##    return inner
##
##@name1
##def deco(name):
##    #print (name)
##    return name
##
##
##def main():
##   print(deco('john'))
##
##main() 
###------------------------------------------------------------------------------
##iv) *args and **kwargs
##
##1) The special syntax, *args and **kwargs in function definitions is used to
##pass a variable number of arguments to a function.
##2)The single asterisk form (*args) is used to pass a non-keyworded,
##variable-length argument list
##3)The double asterisk form is used to pass a keyworded, variable-length
##argument list. 
##4) kwargs prints the values in tht form of key : value pair(Dictionary)
##5) in kwargs we always use kwargs.keys to get the keys value and for values use
##kwargs[key] and kwargs.items() for the pairs
##
###args and kwargs in python
##def method1(*args,**kwargs):
##    for arg in args:
##        print (arg)
##    for kwarg in kwargs.items():
##        print (kwarg)
###OR
##    for key in kwargs:
##        print ('Pairs are: %s: %s' % (key, kwargs[key]))
##
##def main():
##    method1(1,2,3,4,w = 5,x = 11 , y = 12, z = 13)
##main()
##
###------------------------------------------------------------------------------
##
##v) __init__ in python:
##    :is a constructor
###------------------------------------------------------------------------------
##
##
##vi) Basics:
##
##1) The type Function :
##The type function returns the datatype of any arbitrary object.
##ex: type(1) = <type 'int'>
##
##2) The str Function:
##The str coerces data into a string. Every datatype can be coerced into a string.
##ex: str(1) = '1'
##
##3) Introducing dir:
##
##Ex:a)
##li = []
##dir(li)           1
## = ['append', 'count', 'extend', 'index', 'insert',
##   'pop', 'remove', 'reverse', 'sort']
##
##Ex:b)
##d = {}
##dir(d)            2
##= ['clear', 'copy', 'get', 'has_key', 'items', 'keys',
##   'setdefault', 'update', 'values']
##
##
###------------------------------------------------------------------------------
##
##vii) 
##
##
##
##
##
##
##
##    
