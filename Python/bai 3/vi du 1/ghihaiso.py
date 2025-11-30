'''fi= open ('HAISO.INP', 'r')
data= fi.read()
numbers= data.splitlines()
fi.close()
fo=open ('HAISO.OUT', 'w')
fo.write(' '.join(numbers))
fo.close()'''
'''fi= open('HAISO.INP',  'r')
a= fi.readline().strip()
b= fi.readline().strip()
fi.close()
fo=open('HAISO.OUT', 'w')
fo.write(a+" "+b)
fo.close()"'''
'''f= open('HAISO.INP',  'r')
a= int(f.readline())
b= int(f.readline())
f.close
f= open('HAISO.OUT', 'w')
f.write(str(a)+' '+str(b))
f.close()'''
'''f=open('HAISO.INP', 'r')
lines=f.readlines()
f.close()
number[x.strip()for x in lines]
fo=open('HAISO.OUT', 'w')
fo.write(' '.join(number))
fo.close()'''
'''with open('HAISO.INP', 'r') as fi:
    data=fi.read().splitlines()
with open('HAISO.OUT', 'w') as fo:
    fo.write(' '.join(data))'''
with open('HAISO.INP', 'r') as fi:
    a= fi.readline().strip()
    b=fi.readline().strip()
with open('HAISO.OUT', 'w')as fo:
    fo.write(str(a)+' '+str(b))

    
