n=int(input())
n1=str(n)
product=1
sum=0
for i in n1:
    product=product*int(i)
    sum=sum+int(i)
    result=product-sum
print(result)

    