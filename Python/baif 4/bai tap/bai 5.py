a,b,c=map(float,input('nhap 3 so: ').split())
'''if a>b and b>c:
    print(f'{a} la so lon nhat')
if a<b and b>c:
    print(f'{b} la so lon nhat')
if a<b and b<c:
    print(f'{c} la so lon nhat')'''
if a > b > c:
    print('a la so lon nhat')
elif (a < b) and (b > c):
    print('b la so lon nhat')
else:
    print('c la so lon nhat')        

