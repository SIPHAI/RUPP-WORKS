# Python code to demonstrate naive method
# to compute factorial
number = int(input("Enter any integer number:"))
fact = 1
#formula of fact
for i in range(1, number+1):
	fact = fact * i

print("The factorial of 23 is : ", end="")
print(fact)
