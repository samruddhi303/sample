num = int(input("How many times do you want to print: "))
f = 0
s = 1
for i in range(num):
 num = f + s
 f = s
 s = num
print(num)