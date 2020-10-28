try:
    a=[]
    n=int(input("Enter number of elements:"))
    for i in range(1,n+1):
        b=int(input("Number:"))
        a.append(b)
    a.sort()
    print("Largest element is:",a[n-1]) 
except ValueError:
     print("Wrong input")