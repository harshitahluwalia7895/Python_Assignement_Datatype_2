dict={}
num=int(input("Enter no. of elements for adding in  dictionary"))
for i in range(num):
    n=input("Enter name and marks as name:marks of student" +str(i+1)+": ")
    l=n.split(':')
    dict[l[0]]=l[1]
print(dict)
print(sorted(dict.values()))
