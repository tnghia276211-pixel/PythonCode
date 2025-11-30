a,b= map(int,input('Nhap hai so a,b:').split())
if a!=0:
         pt= -b/a
         print(f'{a}x+{b}=0 co nghiem la x={pt}')
else:
    if b == 0:
        print('Phương trình có vô số nghiệm')
    else:
        print('Phương trình vô nghiệm')
