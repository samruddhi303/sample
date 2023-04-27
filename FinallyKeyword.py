# Finally keyword -->The finally keyword is available in Python, and it is always used after the try-except block.
# The finally code block is always executed after the try block has terminated normally or after the try block has terminated for some other reason
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