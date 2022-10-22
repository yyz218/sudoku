import copy

def resotre(x):
    for a in range(9):
        for aa in range(9):
            if x[a][aa]=='0':
                x[a][aa]='.'
    return x

def col(x):
    col=[[],[],[],[],[],[],[],[],[]]
    for v in range(9):
        for n in range(9):
            col[n].append(x[v][n])
    return col

def out(bd):
    a=open('out.py','w')
    bc=copy.deepcopy(bd)
    b=[]
    for i in range(len(bc)):
        for l in range(len(bc[i])):
            bc[i][l]=str(bc[i][l])
            if l==0 :
                bc[i].insert(0,'|')
                bc[i].insert(4,'|')
                bc[i].insert(8,'|')
        if i/3==int(i/3):
            b.append(' '+'-'*25)
        bc[i].append('|')
        b.append(' '+' '.join(bc[i]))
    b.append(' '+'-'*25)
    a.write('\n'.join(b))
    a.close()
    a=open('out.py','r').read()
    return a
    
def cell(bc):
    ba=dict()
    for z in range(0,9,3):
        for m in range(0,9,3):
            ba[(z//3,m//3)]=[bc[x][y] for x in range(z,z+3) for y in range(m,m+3)]
    return ba

def cell_test(bc,ba,num):
    for q in ba.keys():
        if ''.join(ba[q]).count('.')==1 and ''.join(ba[q]).count(num)==0:
            abc=q[0]*3+ba[q].index('.')//3
            bbc=q[1]*3+ba[q].index('.')%3
            bc[abc][bbc]=num
            
def col_test(bc,bd,num):
    for cc in range(9):
        if ''.join(bc[cc]).count('.')==1 and ''.join(bc[cc]).count(num)==0:
            bc[cc]=list(''.join(bc[cc]).replace('.',num))
        if ''.join(bd[cc]).count('.')==1 and ''.join(bd[cc]).count(num)==0:
            bc[bd[cc].index('.')][cc]=num
            
def change_test(bc,bd,num):
    for k in range(9):
        if num in bc[k]:
            mm=bc[k].index(num)
            for x in range(9):
                for y in range(9):
                    if x//3==k//3 and y//3==mm//3 and bc[x][y]=='.':
                        bc[x][y]='0'
                                
        for z in range(9):
            if ''.join(bc[k]).count(num)>0 and bc[k][z]=='.':
                bc[k][z]='0'
            if ''.join(bd[k]).count(num)>0 and bc[z][k]=='.':
                bc[z][k]='0'
                
def all_test(bc,ba,bd):
    for n in range(9):
        for q in range(9):
            sbs=[set(bc[n]),set(bd[q]),set(ba[(n//3,q//3)]),set(str(x) for x in range(1,10))]
            if len(sbs[3]-(sbs[0]|sbs[1]|sbs[2]))==1 and bc[n][q]=='0':
                bc[n][q]=list(sbs[3]-(sbs[0]|sbs[1]|sbs[2]))[0]
                
def converse(b):
    dd=[b[0+z*9]+b[1+z*9]+b[2+z*9]+b[3+z*9]+b[4+z*9]+b[5+z*9]+b[6+z*9]+b[7+z*9]+b[8+z*9] for z in range(9)]
    bc=[list(dd[m]) for m in range(9)]
    return bc
                
def num(z):
    if z<10:
        return z
    elif z%9==0:
        return z-(z//9-1)*9
    else:
        return z-9*(z//9)
    
def ddd(a,b,c):
    for k in range(1,10):
        num=str(k)
        change_test(a,b,num)
        for m in range(9):
            for z in range(9):
                if c[m][z]=='.':
                    c[m][z]=dict()
                    c[m][z][(m,z)]=[]
                if a[m][z]=='.':
                    c[m][z][(m,z)].append(num)
        a=resotre(a)
        b=col(a)
    return c
