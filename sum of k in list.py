n,k=map(int,input().split())
n1=int(input("enter no. of elements in array"))
i=0
j=0
arr=[]
sum=0
while i<=n:
    a=int(input("enter the number"))
    arr.append(a)
    i=i+1
while j<k:
    sum=sum+arr[j]
    j=j+1
print(sum)    

