p,r,t=map(int,input().split())
z=p*(pow((1+r/100),t))
e="{:.2f}".format(z)
print(e)