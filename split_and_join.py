#Zachary Zawaideh
#Computer Programming
#1/25/18

def list_str():#We only need one function for this program because of its size.
    jose= ("My name is Jose")#The first thing to do is to make a string to split.
    wrd= jose.split()#Using .split, jose, turns into a list. 
    print(wrd)#This prints jose the list version.
    user= ("user1;user2;user3")#This is like jose but the .split takes out the semicolon.
    user2= user.split(";")
    print(user2)#This prints user2 as a list without the semicolon
    sentence= ["this","is","a","sentence"]
    print(" ".join(sentence))# A blank .join turns the list into a sentence, the oposite of .split. 



list_str()
