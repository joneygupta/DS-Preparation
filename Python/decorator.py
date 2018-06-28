def name1(func):
    def inner(name):
        print ('Hello')
        return func(name)
    return inner

@name1
def deco(name):
    #print (name)
    return name


def main():
   print(deco('john'))

main()    


    




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







