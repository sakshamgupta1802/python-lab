l = list(map(int,input().split(' ')))
b = []
k =0
for k in l:
   if k not in b:
    b.append(k)
print(*b,sep='*')

