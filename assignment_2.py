#task_1
a = int(input("Enter a number: "))

if a%2 == 0:
    print(a,"is an even number")
else:
    print(a,"is an odd number")

#task_2
sum= 0
for i in range(1,51):
 sum += i

print("The sum of numbers from 1 to 50 is:", sum)