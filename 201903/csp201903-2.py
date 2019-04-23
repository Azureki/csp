import operator as op

def is24(string):
    oprds = []
    optrs = []
    for i in range(7):
        if i%2 == 0:
            oprds.append(int(string[i]))
        else:
            if optrs and d[optrs[-1]] >= d[string[i]]:
                    optr = opd[optrs.pop()]
                    a = oprds.pop()
                    oprds[-1] = optr(oprds[-1], a)

            optrs.append(string[i])


    while optrs:
        optr = opd[optrs.pop()]
        a = oprds.pop()
        oprds[-1] = optr(oprds[-1], a)
    # print(oprds, optrs)
    return 'Yes' if oprds[0] == 24 else 'No'
        


d = {'+':1,'-':1,'x':2,'/':2}
opd = {
    '+':op.add,
    '-':op.sub,
    'x':op.mul,
    '/':op.floordiv
    }

n = int(input())
for i in range(n):
    print(is24(input()))
    
