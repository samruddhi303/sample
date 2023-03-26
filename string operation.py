#In python for taking the input for multiple values we use split function
#split() function converts the string into list
rate,quantity = input("enter the rate and quantity: ").split()
Bill = int(rate) * int(quantity)
print(Bill)