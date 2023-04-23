# recursion---> recursion is a way of programming or coding in which a function calls itself one or more times in its body
def fact(n):
    if n == 0:
        return 1
    else:
        return n* fact(n-1)
print(fact(0))
print(fact(8))
print(fact(7))