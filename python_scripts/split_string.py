#this script is used to split data strings containing alphabets and "()"

import re
rex=re.compile(r'[a,b,c,‡,\(,n/]')


def not_empty(s):
    return s and s.strip()  #去除字符串中的空格

def is_se(s):
    if ')' in s:
        return 1

def not_se(s):
    if ')' not in s:
        return 1

def rmbracket(s):
    return s.rstrip(')')

def get_string(s):
    ls1=re.split(rex,s)
    ls2=list(filter(not_empty, ls1)) 
    ls_se=list(filter(is_se,ls2))       #获取SE
    ls_se=list(map(rmbracket,ls_se))    #去掉括号
    ls_mean=list(filter(not_se,ls2))
    s_se=','.join(ls_se)
    s_mean=','.join(ls_mean)
    print('se is',s_se)
    print('mean is',s_mean)
    return s_mean,s_se

meanlist=[]
selist=[]

while True:
    data=input('enter string, type "#" to stop.\n')
    if data=='#':
        break
    else:
        mean,se=get_string(data)
        meanlist.append(mean)
        selist.append(se)

print('meanlist is:')
for k in meanlist:
    print(k,end=',')
print()

print('selist is:')
for j in selist:
    print(j,end=',')
print()

#more convenient string for excel:
print ('more convenient meanlist is:')
for k in meanlist:
    print(k,end='\n')
print()

print('selist is:')
for j in selist:
    print(j,end='\n')
print()

input()
