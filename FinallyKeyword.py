def func1():
    try:
        l = [5,3,9,8,7]
        x = int(input("Enter the index"))
        print(l[x])
        return 1
    except:
        print("Some error is occured")
        return 0
    
    finally:
        print("I am always excuted")
x = func1()
print(x)