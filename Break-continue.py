#we use breake keyword to break the loop
for i in range(10):
    if i==2:
        break
    print(i)
    #we use continue keyword for skip the loop 

    for num in range(10):
        if num == 5:
            continue
        print(num)
    else:
        print("Loops excuted successfully")


        #Escape Sequence charater ---->
print("I am learning python\n and i'm doing well!")              
 
#  output---> I'm learning python 
#             and i'm doing well!

print("I'm very \" creative\" girl")
#---> I'm very "creative" girl
print("hello user","hi priti","hi prithvi",sep="~") #by using sep we can separate multiple string's given in one print statement
print("hello user","hi priti","hi prithvi",end="~")
