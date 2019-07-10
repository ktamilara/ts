n1,k1=map(str,input().split())
k1=int(k1)
list=[]
for i in range(len(n1)-k1+1):
	list.append(n1[i:i+k1])
print(*list)
