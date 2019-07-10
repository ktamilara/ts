n1,k1=map(int,input().split())
l1=[str(x) for x in input().split()]
d1=l1[k1:]+l1[:k1]
print(' '.join(d1))
