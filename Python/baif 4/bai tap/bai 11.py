a=float(input('Nhập số kWh điện đã dùng: '))
if a<=50:
    tien = a*1000
    print(f'so tien đã dùng là {tien:.2f}')
else:
    tien= 50*1000+(a-50)*1500
    print(f'so tien đã dùng là {tien:.2f}')

   
