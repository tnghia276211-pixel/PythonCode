A=list(map(int,input().split()))
'''tong=0
for i in A:
    if i>0:
        tong+=i
print(tong)'''
print(sum(i for i in A if i>0))
