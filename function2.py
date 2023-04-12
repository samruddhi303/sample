def cal_geomean(a, b): #Declaring a function
    mean = (a*b)/(a+b)  #Defining a function
    print(mean)  
def Is_greater(a, b):
    if(a>b):
        print("a is greater!")
    else:
        print("b is greater!")


a = 9
b = 2
cal_geomean(a, b) #calling the function
Is_greater(a, b)

b = 128
a = 90
cal_geomean(a, b) #calling the function
Is_greater(a, b)

#here we calculating bill by defining parameter discount and billamount 
def bill(billamount, discount):
    T_bill = (discount/100)*billamount
    print(T_bill)
    print("You have {}% discount on your bill".format(discount))

billamount = 25000
discount = 5
bill(billamount, discount)