n=int(input())
count=0
m=0
for i in range(1,n+1):
    count=0
    if n%i==0:
        for j in range(2,i):
            if i%j==0:
                count=count+1
    if count>0:
        m=m+1
print(m+1)