def triangle(max):
    a=[1]
    n=0
    while n<=max:
        if n==0:
            yield a
        elif n==1:
            a=[1,1]
            yield a
        elif n>1:
            i=0
            while i<n-1:                
                a.append(a[i]+a[i+1])
                i=i+1
            a.append(1)
            a=a[-n-1:]
            yield a
        n+=1

g=triangle(10)
for n in g:
    print(n)