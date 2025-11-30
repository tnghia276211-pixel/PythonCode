a=float(input('Nhap so gio lam viec'))
if a<=40:
    tien= a*200000
    print(f'tien luong la {tien}')
if a>40:
    tien= 40*200000+(a-40)*300000
    print(f'tien luong la {tien}')
