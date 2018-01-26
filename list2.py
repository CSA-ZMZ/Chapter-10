#Zachary Zawaideh
#Computer Programming
#1/17/18

def list_function():#In this asignment I only need one function because there are not many tasks.
    my_list = ["Zachary", "July", "10th", "2002", "Austin,TX"]#The next step, sonce this is a list asignment, is to create a list.
    for x in my_list:#The for loop has x go through the list and print every word in the list vertically.
        print(x)
    print("I was born in " +(my_list[4])+".")#This takes "Austin,TX" and adds it into a string by its self.
    print("The month was " +(my_list[1])+".")#This takes "July" and adds it into a string by its self.
    my_list[2:2]=["Rana"]#This adds the name of my mother, "Rana", into the list without changing anything else.
    print(my_list)#This prints the new version of the list.




list_function()#This starts the program.
