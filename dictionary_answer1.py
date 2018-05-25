dict={}
num=int(input("Enter no. of elements for adding in  dictionary"))
for i in range(num):
    m=input("Enter name and marks as name:marks of student" +str(i+1)+": ")
    new=m.split(':')
    dict[new[0]]=new[1]
print(dict)
