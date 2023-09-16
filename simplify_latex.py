from config import *

def tokenize(inputted:str):
    other = inputted
    #tokenizedtype = []
    tokenized = []
    rb = False# is ] a r]? 方括号
    db = False#是否是函数调用
    last_one_ended = True
    left_in_special = False
    def find_pair_brackets():
        for i in range(len(tokenized)):
            if tokenized[i]==']':
                j = i-1
                while tokenized[j]!= '[':
                    j -= 1
                return j, i
        raise
    def find_pair_brackets2(ii):
        #print(ii)
        while other[ii]!='"':
            ii +=1
        return ii
        
    def next(i):
        if i+1 == len(other):
            return None
        else:
            return other[i+1]
    def appenditem(cp=None,typee='kw', ended=True):
        if cp == None:
            cp = c
        nonlocal last_one_ended
        tokenized.append([cp,typee])
        #tokenizedtype.append(bracket)
        last_one_ended = ended
    def appendletter(cp=None):
        if cp == None:
            cp = c
        tokenized[-1][0] += cp

    i = -1
    while i+1 < len(other):
        left_in_special -= 1
        i += 1
        c = other[i]

        if c=='"':
            #appenditem('"')
            aa = find_pair_brackets2(i+1)
            a = other[i+1:aa]
            if a == " "*len(a):
                appenditem(a,typee='space')
            else:
                appenditem(a, typee='text')
            #appenditem('"')
            i = aa+1
        #elif c == ' 'or c=='\n':#空格
        #    #last_one_ended = True
        #    continue
        elif c == '/':
            appenditem()
        elif c == '[':
            #print(tokenized[-1][0])
            if left_in_special > 0:
                appenditem('d[')
                db = True
                left_in_special = 0
            else:
                appenditem()
        elif c == ']':
            if rb:
                appenditem("r]")
                rb = False
            elif db:
                appenditem("d]")
                db = False
            else:
                appenditem()
        elif c == ';':
            appenditem()
        #gt_divs
        #elif c == '^':
        #    appenditem(typee="gt_div")
        elif c == '\\' and other[i+1]=='[':
            appenditem("r[")
            i += 1
            rb = True
        elif c in '0123456789':
            if other[i-1]in '0123456789':
                appendletter()
            else:
                appenditem(typee='number',ended=False)
        elif c=='.'and other[i-1]in '0123456789':#6. but not 6 .
            appendletter()
        elif c=='('or c==')':
            appenditem(typee='replace')
        else:
            if last_one_ended:
                appenditem(typee='others',ended=False)
            elif other[i-1]in '0123456789':#6tt
                appenditem(typee='others',ended=False)
            else:
                appendletter()
            #print(tokenized[-1][0])

            for j in range(7,0,-1):#max+1 and min length of function names
                t_end = tokenized[-1][0][-j:]
                t_end_s = tokenized[-1][0][-j-1:]
                #print(tokenized[-1][0],f'"{t_end}"')
                #print(tokenized[-1][0],j,tokenized[-1][0][-j-1:])
                #if not(t_end==t_end_s or t_end_s=='\n'+t_end):
                #    continue
                if tokenized[-1][0][-j-1:-j]=='':
                    pass
                elif tokenized[-1][0][-j-1:-j] in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
                    continue
                #print('6',t_end)
                def change(name):
                    #print(tokenized[-1][0][:-j])
                    if tokenized[-1][0][:-j]=='':
                        del tokenized[-1]
                    else:
                        tokenized[-1][0] = tokenized[-1][0][:-j]
                    appenditem(t_end,name)
                    
                if t_end in backslash:
                    change('backslash')
                    break
                if t_end in replaces.keys():
                    change('replace')
                    break
                if t_end in other_func_name:
                    change('other_func_name')
                    break
                if t_end in special:
                    #print(t_end)
                    change('special')
                    left_in_special = 2
                    break

                #last_one_ended = False
    #for i in tokenized
    return tokenized




def analyse(tokenized,align=False,middle = False):
    analysed = tokenized[:]
    
    def split_div(inp):
        '''
        in: [a+[b+c/d]/e]
        out: \frac{a+\frac{b+c}{d}}{e}, nntba
        '''
        def find_pair_brackets(inp):
            for i in range(len(inp)):
                if inp[i][0]==']'and inp[i][1]=='kw':
                    j = i-1
                    while not (inp[j][0]== '['and inp[i][1]=='kw'):
                        j -= 1
                    return j, i
            return None
        res = inp[:]
        while find_pair_brackets(res)!=None:
            #print(find_pair_brackets(res))
            _ = find_pair_brackets(res)
            left = _[0]
            right = _[1]
            temp = r'\frac{ '
            for i in res[left+1:right]:
                if i[0]=='/'and i[1]=='kw':
                    temp += ' }{ '
                else:
                    temp += i[0]
            temp += ' }'
            #print(res[left:right+1],[[temp,'nntba']])
            res[left:right+1] = [[temp,'nntba']]
        return res

    def replace():
        for j in range(len(analysed)) :
            i = analysed[j]
            #print(analysed,i[1])
            if i[1]=='backslash':
                analysed[j] = [f'\{i[0]}', 'nntba']
            elif i[1]=='replace':
                #print(i[0])
                analysed[j] = [replaces[i[0]], 'nntba']
            elif i[1]=='other_func_name':
                analysed[j] = [r'\operatorname{'+i[0]+r'}', 'nntba']
    def handle_special(inpa):
        def find_pair_brackets(inp):
            for i in range(len(inp)):
                if inp[i][0]=='d]'and inp[i][1]=='kw':
                    j = i-1
                    while not (inp[j][0]== 'd['and inp[i][1]=='kw'):
                        j -= 1
                    return j, i
            return None
        res = inpa[:]
        while find_pair_brackets(res)!=None:
            #print(find_pair_brackets(res))
            _ = find_pair_brackets(res)
            #print(_)
            left = _[0]
            right = _[1]
            name = left-1
            j = res[name]
            #print(j,analysed[left],analysed[right])
            if j[0]=='_'or j[0]=='^':
                res[left] = ['{','nntba']
                res[right] = ['}','nntba']
            if j[0]=='ceil':
                res[left] = [r'\left \lceil','nntba']
                res[right] = [r'\right \rceil','nntba']
                del res[name]
            if j[0] in ["cal","bb","rm","tt","sf","scr"]:
                #print(j)
                res[left] = [r'\math'+j[0]+'{','nntba']
                res[right] = ['}','nntba']
                del res[name]
                #print(res)
        return res

    replace()
    #print('h')
    #print(analysed)
    analysed = handle_special(analysed)
    analysed = split_div(analysed)
    analysed = ' '.join([i[0]for i in analysed])
    if align:
        analysed = r'$$\displaystyle{ \begin{align*}'+analysed+r'\end{align*} }$$'
    elif middle:
        analysed = r'$$\displaystyle{ '+analysed+r' }$$'
    else:
        analysed = '$\\displaystyle{ '+analysed+' }$'
    return analysed


#print(tokenize('sum[;p "  " [rm; pri]"me" ] loga\[1/p]ceil[2] [a+c/b]'))
if __name__ =='__main__':
    print(analyse(tokenize(r'''&[sum vec{p_i}/m]\\=&[1/m]sum_{i=1}^{m}int int sum_b vec{a_{i,b}}\,dt dt\\=&[1/m]int int sum_{i=1}^{m}sum_b vec{a_{i,b}}\,dt dt\\=&[1/m]int int vec{0}\,dt dt\\=&[1/m](vec{C_1}t+vec{C_2})'''),True))
