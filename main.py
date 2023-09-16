import sys

from simplify_latex import *

#print(sys.argv)
with open(sys.argv[1],encoding='utf-8') as fileobj:
    text = fileobj.read()
    #print(text)
#out = list(text[:])
out = list(text[:])

lr = 0
i = -1
while i < len(out)-1:
    i += 1
    j=out[i]
    if i==len(out)-1:
        k = ''
    else:
        k = out[i+1]
    m=out[i:i+3]
    n=out[i:i+2]
    #print(m)
    if m==['`','`','`']:
        #print('m')
        i += 2
    elif n==['`','`']:
        #print('n')
        del out[i+1]
        #del out[i+1]
    elif j=='`':
        #print(lr)
        if lr==0:
            if i==0:
                out.insert(0,' ')
                i += 1
            elif out[i-1]!=' 'and (out[i-1]not in'am'):
                out.insert(i,' ')
                i += 1
            #while out[i+1]==' ':
            #    del out[i+1]
            i -= 1
            lr = 1
            #print(out[i-2:i+3])
        else:
            if k!=' ':
                out.insert(i+1,' ')
                #i += 1
            #print(out[i-1]==' ',out[i-2:i+1])
            #print(out[i-1],out,i)
            #while out[i-1]==' ':
            #    #print('s',i-1)
            #    del out[i-1]
            #    i -= 1
            lr = 0

#print(' '.join(out))


i = -1
while i < len(out)-1:
    i+=1
    #print(findl)
    if i==0:
        j=''
    else:
        j=out[i-1]
    if i>=len(out)-1:
        k=''
    else:
        #print(i,len(out))
        k=out[i+1]
    #print(out[i])
    if out[i]=='`'and j!='`'and k!='`':
        #print(out[i-2:i+2])
        #left = i
        for index in range(i+1,len(out)):
            if out[index]=='`':##########################
                right = index
                break
        #print(out[left+1:right])
        if j=='a':
            out[i-1:right+1] = [analyse(tokenize(out[i+1:right]),align=True)]
            #i = i -1
        elif j=='m':
            out[i-1:right+1] = [analyse(tokenize(out[i+1:right]),middle=True)]
            #i = i -1
        else:
            #print(out[i-1:right+1])
            out[i:right+1] = [analyse(tokenize(out[i+1:right]))]
        #print(out[i])


#print(out)


out = ''.join(out)
#print(out)

outputfile_name = sys.argv[1][:-3]+'_o.md'

with open(outputfile_name,'w',encoding='utf-8') as outfile_obj:
    outfile_obj.write(out)