with open('TINH.INP', 'r') as f:
    a,b= map(int, f.readline().split())
with open('TINH.OUT', 'w') as f:
    f.write(str(a+b)+'\n'+str(a-b)+'\n'+str(a*b)+'\n'+(f'{a/b:.2f}'))
    '''f.write(str(a-b)+'\n')
    f.write(str(a*b)+'\n')
    f.write(str(a/b)+'\n')'''
    

