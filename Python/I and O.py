import os
import re
print (os.getcwd())

line = 'adsfs, afdgd; agshs ahsshh,      agsgsg'
##l = re.split(r'[\s;,]\s*',line)
##l = re.split(r'(\s|;|,)\s*',line)
l = re.split(r'(?:,|;|\s)\s*',line)
print (l)
p = l[2::2]
print (p)
p1 = l[::-2]
l = re.split(r'(?:,|\s)\s*',line)
print (p1)


##1)
##data = open('Git_Commands1.txt')
##print (data.readline())
##
##for line in data:
##    if not line.find(':') == -1:
##        (first,second) = line.split(':',1)
##        first = line.split(':',1)
##        print (first)
##        print (second)
##data.close()

##2)
##if os.path.exists('Git_Commands1.txt'):
##    data = open('Git_Commands1.txt')
##    for line in data:
##        if not line.find(':') == -1:
##            (first,second) = line.split(':',1)
##            first = line.split(':',1)
##            print (first)
##            print (second)
##    data.close()        
##else:
##    print ('File Missing!!!')


##3)
##try:
##    data = open('Git_Commands.txt')
##    for line in data:
##        try:
##            (first,second) = line.split(':',1)
##            first = line.split(':',1)
##            print (first)
##            print (second)
##        except:
##    ##        raise ValueError
##            pass
##    data.close()  
##except:
##    print ('File Is Missing...')


##NOTES :
##    1) Use the open() BIF to open a disk file, 
##creating an iterator that reads data from 
##the file one line at a time.
##   2) The readline() method reads a 
##single line from an opened file.
##   3) The seek() method can be used to 
##“rewind” a file to the beginning.
##   4) The close() method closes a 
##previously opened file.
##   5) The split() method can break a 
##string into a list of parts.
##   6) An unchangeable, constant list in Python 
##is called a tuple. Once list data is 
##assigned to a tuple, it cannot be changed. 
##Tuples are immutable.
##   7) A ValueError occurs when your data 
##does not conform to an expected format.
##   8) An IOError occurs when your data 
##cannot be accessed properly (e.g., 
##perhaps your data file has been moved or 
##renamed).
##   9) The help() BIF provides access to 
##Python’s documentation within the IDLE 
##shell.
##   10) The find() method locates a specific 
##substring within another string.
##   11) The not keyword negates a condition.
##   12) The try/except statement provides 
##an exception-handling mechanism, 
##allowing you to protect lines of code that 
##might result in a runtime error.
##   13) The pass statement is Python’s empty 
##or null statement; it does nothing.




##Writing to a File , in writ mode if file is not eist it will create one for you and then open the same for writing in it
##try:    
##    w = open('write.txt','w')
##    print ('Hello i am shubham',file = w)
##
##except:
##    print ('File Missing...')
##
##finally:
##    w.close()


##Check out the finally: call ( The locals() returns a collection of names defined in the current scope)
##
##try:    
##    w = open('write2.txt')
##
##except:
##    print ('File Missing...')
##
##finally:
##    if 'w' in locals():
##        w.close()


##( It turns out exception objects and strings are not compatible 
##types, so trying to concatenate one with the other leads to problems. You can convert (or cast) one to the other using the str() )
##try:    
##    w = open('write2.txt')
##
##except Exception as e:
##    print ('Error : ' + str(e))
##    
##
##finally:
##    if 'w' in locals():
##        w.close()



## (When you use with, you no longer have to worry about closing any opened 
##files, as the Python interpreter automatically takes care of this for you.)

##(The with statement takes advantage of a Python technology 
##called the context management protocol.)
## We can also use two 'with' statement by comma(,) separteas between them

##try:    
##    with open('write.txt','w') as w:
##        print ('i am back and hello',file = w)
##
##except Exception as e:
##    print ('Error : ' + str(e))





##prit_lol() function






##Pickle your data
import pickle

##with open('Git_Commands.txt','wb') as datum:
##    pickle.dump([1,2,3],datum)
##    pickle.dump('Hello , I am Shubham',datum)
##    pickle.dump((1,2,3,4,5),datum)
##    datum.close()


##with open('Git_Commands.txt','rb') as datum1:
##    v1 = pickle.load(datum1)
##    print (v1)
##    v = pickle.load(datum1)
##    print (v)



##------------------------------------------------------------------------------------------------------------------------------

##dump vs dumps





















