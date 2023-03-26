#In python for taking the input for multiple values we use split function
#split() function converts the string into list
rate,quantity = input("enter the rate and quantity: ").split()                                            #output---> enter the rate and quantity: 6 8 Bill =48
Bill = int(rate) * int(quantity)                                                                                         
print(Bill)


#Multiline string-->
#You can print multiples lines then we enclosing that lines it in a triple quotes """ """.
poem="""
Twinkle, twinkle, little star,
How I wonder what you are.
Up above the world so high,
Like a diamond in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!"""
print(poem)

#Slicing-->
#A slice object is used to specify how to slice a sequence. You can specify where to start the slicing, and where to end.
str1 = "mango is sweet"                           #output---> ngo i
print(str1[2:7])

#Length function
#len() is a built-in function in python. You can use the len() to get the length of the given string, array, list
name = "RadhaKrishna"       #output ---> 12
print(len(name))

# in operator
#The 'in' operator is used to check if a value exists in a sequence or not.
print("Radha" in name)            #output ---> True


#Comments in python --->

#comments are the lines of code ignored by the compiler during the process of execution
#1-->singleline comment(# This is a sample program)
#2-->Multiline comments("""This is a sample program""")


#Upper() method ---> this converts a string into uppercase
myString = "radhakrishna"                                  #output ---> RADHAKRISHNA
print("Original String :",myString)
newString = myString.upper()
print("New String :",newString)

#lower() ---> converts a string into lowercase
myString = "RADHAKRISHNA"                                 #OUTPUT ---> radhakrishna
print("Original String :",myString)
newString = myString.lower()
print("New String :",newString)

#strip() ---> it removes a white space from the end of string
str1 = "RTC                 "
print(str1)

#Replace---> it use to replace
newstr = str1.Replace("R", "N")      
print(newstr)                     #output ---> NTC