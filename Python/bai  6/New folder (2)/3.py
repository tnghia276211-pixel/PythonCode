'''while True:
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n > 0:
            break   
        else:
            print(" Bạn phải nhập số nguyên dương, vui lòng nhập lại.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

print("Bạn đã nhập số nguyên dương:", n)'''
n = 0
while n <= 0:
    n = int(input("Nhập số nguyên dương n: "))
print("Bạn đã nhập số nguyên dương:", n)

