from time import time


def fun1(n):
	return n*(n+1)/2

def fun2(n):
	sum=0
	for i in range(1,n+1):
		sum=sum+i
	return sum

def fun3(n):
	sum=0
	for i in range(1,n+1):
		for j in range(1,i+1):
			sum=sum+1
	return sum

print(fun1(5))
print(fun2(5))
print(fun3(5))
