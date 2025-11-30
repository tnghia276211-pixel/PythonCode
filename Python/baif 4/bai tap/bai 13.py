a,b=map(int,input('Nhan hai so nguyen a, b').split())
if a%b==0:
    print(f'{a} chia het cho {b}')
if b%a==0:
    print(f'{b} chia het cho {a}')
else:
    print('Không số nào chia hết cho số kia')
