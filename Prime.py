def Prime(k,j):
    n= [m for m in range(k,j) if all(m%i !=0 for i in range(2,int(0.5*m)+1))]
    print(n)
    print(sum(n))
a=int(input("enter starting value :"))
b=int(input("enter ending  value :"))
Prime(a,b)