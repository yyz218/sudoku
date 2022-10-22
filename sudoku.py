import function

def solve_all(row):
    col=function.col(row)
    for num in range(1,46):
        num=str(function.num(num))
        function.change_test(row,col,num)
        cell=function.cell(row)
        col=function.col(row)
        function.col_test(row,col,num)
        function.cell_test(row,cell,num)
        function.all_test(row,cell,col)
        row=function.resotre(row)
    return row

def solve(sudoku):
    if '.' not in solve_all(function.converse(sudoku))[0]:
        print(function.out(solve_all(function.converse(sudoku))))
    else:
        while '.' in solve_all(function.converse(sudoku))[0]:
            a=solve_all(function.converse(sudoku))
            c=solve_all(function.converse(sudoku))
            b=function.col(a)
            function.ddd(solve_all(function.converse(sudoku)),b,c)
            aa=solve_all(function.converse(sudoku))
            for d in range(9):
                for s in range(9):
                    if type(c[d][s])==dict:
                        for q in range(len(c[d][s][(d,s)])):
                           a=solve_all(function.converse(sudoku))
                           a[d][s]=c[d][s][(d,s)][q]
                           m=solve_all(a)
                           gg=function.cell(m)
                           b=function.col(m)
                           for z in range(9):
                               for qq in range(1,10):
                                   if ''.join(m[z]).count(str(qq))>1 or ''.join(gg[(z//3,(qq-1)//3)]).count(str(qq))>1 or ''.join(b[z]).count(str(qq))>1:
                                       c[d][s][(d,s)][q]='a'
                                       continue
                        c[d][s][(d,s)]=list(set(c[d][s][(d,s)]))
                        if 'a' in c[d][s][(d,s)]:
                            c[d][s][(d,s)].remove('a')
                        if len(c[d][s][(d,s)])==1:
                            aa[d][s]=c[d][s][(d,s)][0]
            print(function.out(solve_all(aa)))
            ccc=[''.join(aas) for aas in solve_all(aa)]
            sudoku=(''.join(ccc))   
aa=input('place the input sudoku')
sudoku=aa.replace('-','.')
if len(sudoku)!=81:
    raise TypeError('Wrong Input')
solve(sudoku)