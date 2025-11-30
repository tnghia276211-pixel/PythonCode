
ds= list(range(5))
print(ds)

ds= []
for i in range(100):
    ds.append(i)
print(ds)

ds= [i for i in range(100)]
print(ds)

ds= [i*i for i in range(6)]
print(ds)

n= int(input())
ds= [i*i for i in range(n)]
print(*ds)
print(*ds,sep=' ')

ds= [i for i in range(100)if i%2==0]
print(ds)

i=int(input())
a=[10, 20, 30, 40]
print(a[i])

a=[10, 20, 30, 40, 50, 60]
print(a[2]) or  del[1]
                print(a[])

ds= input().split()
ds= list(map(int, input().split()))

import sys
ds= sys.stdin.readline().split()
print(ds)

ds= list(map(int,sys.stdin.readline().split()))
print(ds)

'''n= int(input())
ds=[]
for _ in range(n):
    x = input()
    ds.append(x)
print(ds)

n= int(input())
ds=[input()for _ in range(n)]
print(ds)

'''n= int(input())
ds=[]
for _ in range(n):
    a= int(input())
    ds.append(a)
print(ds)
# moi phan tu nam tren mot dong voi so lan chua biet truoc
#c1
ds=[]
while True:
    dong = input('nhap phan tu (enter de dung): ').strip()
    if dong =='':
        break
    ds.append(dong)
print(ds)































