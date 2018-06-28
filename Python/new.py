
#args and kwargs in python
def method1(*args,**kwargs):
    for arg in args:
        print (arg)
    for kwarg in kwargs.items():
        print (kwarg)
    for key in kwargs:
        print ('Pairs are: %s: %s' % (key, kwargs[key]))

def main():
    method1(1,2,3,4,w = 5,x = 11 , y = 12, z = 13)
    #print (dir(method1))

main()    

    
###__init__ function
##class home():
##    def __init__(self):
##        self.a = 12
##    def method11(self):
##        print (self.a + 2)
##    
##
##def method12():
##    print ('i am john!!')
##    
##def main():
##    h = home()
##    h.method11()
##    method12()
##
##
##main()
##    
