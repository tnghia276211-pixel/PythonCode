"""A=list(map(int,input().split()))
x=int(input("Nhap phan tu can tim"))
if x in A:
    dem = A.count(x)
    VT_min=A.index(x)
    print(f"Phần tử {x} có trong danh sách")
    print('số lần xuất hiện của phần tử : {dem}')
    print("Vị trí nhỏ nhất:{VT_min} ")
else:
    print('phần tử {x} không xuất hiện trong danh sách ')"""

A=list(map(int,input().split()))
x=int(input("Nhap phan tu can tim"))
if x in A:
    print(f"Phần tử {x} có trong danh sách")
    print('số lần xuất hiện của phần tử :', A.count(x))
    print("Vị trí nhỏ nhất:", A.index(x))
else:
    print(f'phần tử {x} không xuất hiện trong danh sách ')