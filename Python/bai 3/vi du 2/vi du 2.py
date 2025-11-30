'''fi=open('HAISO.INP', 'r')
a,b=fi.readline().strip().split()
fi.close()
fo=open('HAISO.OUT', 'w')
fo.write(a+ '\n'+b)
fo.close()'''
'''with open('HAISO.INP', 'r') as f:
    a,b= f.readline().strip().split()
with open('HAISO.OUT', 'w') as f:
    f.write(f'{a}\n{b}')'''
with open ('HAISO.INP', 'r') as f:
    a,b= map(int, f.readline().strip().split())
with open('HAISO.OUT', 'w') as f:
    f.write(f'{a}\n{b}')
    
