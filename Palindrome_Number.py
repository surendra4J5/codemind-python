t=int(input())
for i in range(t):
    n=int(input())
    temp=n
    rev=0
    while(n>0):
        dig=n%10 #121%10=1       2     1
        rev=rev*10+dig #0+1=1    12    121
        n=n//10 #121//10=12      1
    if(temp==rev): 
        print("True")
    else:
        print("False")