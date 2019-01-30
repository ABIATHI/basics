n1,n2,n3=map(int,input().split())
if n1>n2 and n1>n3:
    print(n1,"is greatest")
elif n2>n3:
    print(n2,"is greatest")
else:
    print(n3,"is greatest")
