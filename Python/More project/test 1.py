'''print('nhập các số nguyên: ')
a=list(map(int,input().split()))
b= input('Nhập kí tự để thay thế(có thể nhập nhiều kí tự):' )
s=' '.join(map(str,a))
total_width= len(s)
padding= total_width-len(s)//2
left= (total_width*b)[:padding]
right= (total_width*b)[:padding]
print(left + s + right)'''


print('nhập các số nguyên: ')
a=list(map(int,input().split()))
-l_padding= input('Nhập kí tự để thay thế(có thể nhập nhiều kí tự):' )
-r_padding= input('Nhập kí tự để thay thế(có thể nhập nhiều kí tự):' )
s=' '.join(map(str,a))
total_width= len(s)
padding= total_width-len(s)//2
left= (total_width*-l_padding)[:padding]
right= (total_width*-r_padding)[:padding]
print(left + s + right)

