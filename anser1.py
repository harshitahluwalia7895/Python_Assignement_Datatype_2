print("Enter 20 numbers")
i=0
l1=[]

while(i<20):
	element=input("Enter Integer No. %d->" % (i+1))
	l1.append(int(element))
	i=i+1

t1=tuple(l1)
pos,neg,odd,even,zeroes=0,0,0,0,0

for num in t1:
	if num>0:
		pos=pos+1
	if num<0:
		neg=neg+1
	if num==0:
		zeroes=zeroes+1
	if num%2==0:
		even=even+1
	if num%2!=0:
		odd=odd+1

print("number of positive numbers= %d" %(pos))
print("number of negative numbers= %d" %(neg))
print("number of odd numbers= %d" %(odd))
print("number of even numbers= %d" %(even))
print("number of zeros numbers= %d" %(zeroes))
