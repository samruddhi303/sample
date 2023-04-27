# Exception handling---> An object in Python that describes an error is called an exception.

# When a Python code throws an exception, it has two options: handle the exception immediately or stop and quit.

a = ["python", "Exception", "Try and except"]
try:
 for i in range(4):
    print("The Index and element from an array is", i,a[i])
except:
    print("Index Out Of Range")


    # How to raise an exception in python--->
Num = [3,4,5,6,9]
print(Num)
if len(Num)>3:
    raise Exception(f"The length of number is less than 3 or equal to 3 but it is {len(Num)}")