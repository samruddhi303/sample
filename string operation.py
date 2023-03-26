#In python for taking the input for multiple values we use split function
#split() function converts the string into list
rate,quantity = input("enter the rate and quantity: ").split()
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
str1 = "mango is sweet"
print(str1[2:7])

#Length function
#len() is a built-in function in python. You can use the len() to get the length of the given string, array, list
name = "RadhaKrishna"
print(len(name))

# in operator
#The 'in' operator is used to check if a value exists in a sequence or not.
print("Radha" in name)