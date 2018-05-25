s1=set()
s2=set()
n1=int(input("Enter no. of elements in set 1"))
for i in range(n1):
	m=int(input("Enter " +str(i+1)+ "value"))
	s1.add(m)
num2=int(input("Enter no. of elements in set 2"))
for i in range(num2):
	m=int(input("Enter " +str(i+1)+ "value"))
	s2.add(m)
print("Difference of sets=",s1-s2)
print("Set comparison=", s1^s2)
print("Intersection=",s1&s2)
