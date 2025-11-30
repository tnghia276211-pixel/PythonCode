a,b,c= map(float,input('nhap 3 canh a b c: '))
if a < 0 or a > 10:
    print('Điểm không hợp lệ. Vui lòng nhập từ 0 đến 10.')
if a==b==c:
    print('la tam giac deu')
elif a==b:
    print('la tam giac can')
elif a**2+b**2==c**2:
    print('la tam giac vuong')
else:
    print('la tam giac thuong')
