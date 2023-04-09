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