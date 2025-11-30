a= int(input('nhap nam: ')
if a%400==0 or a%4==0 and a%100!=100:
    print(f'{a} la nam nhuan')
 else:
     print(f'{a} la nam khong nhuan')