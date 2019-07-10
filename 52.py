n1=int(input())
c1=0
for i in range(n1):
    j=n1-i
    if((i%2 == 0 or j%2 == 0) and i+j == n1):
        c1+=1
if n1==2:
    c1=2
print(c1)
