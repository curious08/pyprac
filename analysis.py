from time import time

#defining a function in one way for same problem
def fun1(n):
	return n*(n+1)/2

#for the same problem another way to solve the problem
def fun2(n):
	sum=0
	for i in range(1,n+1):
		sum=sum+i
	return sum

#for the same problem another way to solve the problem
def fun3(n):
	sum=0
	for i in range(1,n+1):
		for j in range(1,i+1):
			sum=sum+1
	return sum

print(fun1(5))
print(fun2(5))
print(fun3(5))
