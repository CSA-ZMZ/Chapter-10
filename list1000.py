#Zachary Zawaideh
#Computer Programming
#1/24/18

list_of_names= ["Billy", "Bob", "Joe", "Shaiqua", "Tyrone"]#The first step in the program is to have a list the user can add names to, so I put the list outside of the function.
def the_list(list_of_names):#I only needed one function for the program, in the parenthesis I passed the list to the function.
    name= input("What name would you like to add to the list?: ")#This is the input that asks the user the name they want to put in the list.
    list_of_names.append(name)#.append adds the users input to the end of the list.
    another= input("Would you like to add another name(yes or no)?: ").lower()#This asks the user if they want another name in the list.
    if another=='yes':#If the user says "yes" then they will repeat the steps above untill they say "no".
        the_list(list_of_names)
    elif another=='no':#When they are done adding names, the elif returns the list. 
        return(list_of_names)
    


the_list(list_of_names)
print(list_of_names)#After the list is returned, the final version is printed.
