n=int(input("enter a year"))
if n%4==0:
    if n%100==0:
        if n%400==0:
            print("leap year")
        else:
            print("not")
    else:
        print("leap")
else:
    print("not")
