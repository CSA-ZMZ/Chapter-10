#Zachary Zawaideh
#Computer Programming
#1/22/18

def list_append():#Every task has a different function, this reduces common errors.
    mylist=[]#When we use .append you have to start with blank brackets.
    mylist.append(76)#.append adds one number at a time to the list.
    mylist.append(92.3)
    mylist.append("hello")
    mylist.append(True)
    mylist.append(4)
    mylist.append(76)
    print("By using append, the list is: "+str(mylist))#Prints the final result of the list.
    list_concatenation()

def list_concatenation():#A function for concatenation.
    mylist=[]#When we use concatenation you have to start with blank brackets.
    mylist= mylist+[76]#This is simial to .append but with concatenation the format is different.
    mylist= mylist+[92.3]
    mylist= mylist+["hello"]
    mylist= mylist+[True]
    mylist= mylist+[4]
    mylist= mylist+[76]
    print("By using concatenation, the list is: "+str(mylist))#This prints the final list.
    list_random()

def list_random():#This function executes a list of a hundred random numbers.
    import random#import random is the module that makes the random algarithem in python
    newlist=[]
    for x in range(100): #The for loop tells the program how many times to find a random number.
        RandomNumber = random.randrange(0, 1000)#This sets the random number to be between 0 and 1000
        newlist.append(RandomNumber)
    print(newlist)#This prints the random number list
    num=list_average(newlist)
    
def list_average(newlist):
    average_list= float(sum(newlist))/len(newlist)#This calculates the average of the 100 random numbers.
    print("The average of these 100 numbers is: "+str(average_list))
    
    
list_append()


