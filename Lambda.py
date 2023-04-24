# Lambda Functions in Python are anonymous functions, implying they don't have a name. 
# The def keyword is needed to create a typical function in Python, as we already know. 
# We can also use the lambda keyword in Python to define an unnamed function.

# insted of this --->

# def add( num ):  
#    return num + 4  
# print( add(6) ) 

# BY USING LAMBDA FUNCTION --->

#SYNTAX--> lambda arguments: expression     
 
add = lambda num: num + 4
print(add(6))

# Code to filter odd numbers from a given list  
list_ = [34, 12, 64, 55, 75, 13, 63]  
  
odd_list = list(filter( lambda num: (num % 2 != 0) , list_ ))  
  
print(odd_list)  