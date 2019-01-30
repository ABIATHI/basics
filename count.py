n=int(input("enter a integer"))
i=0
count=1
while i<=n:
    r=n%10
    count=count+1
    n=n//10
    i=i+1
print(count)    
    
