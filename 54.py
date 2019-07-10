n1=int(input())
l1=[int(x1) for x1 in input().split()]
b1=[str(l1[0])]
for i in range(1,len(l1)):
    s1=l1[:i+1]
    b1.append(str(min(s1)))
print(' '.join(b1))
