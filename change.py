
def change(num):
    s=0
    h=0
    q=0
    d=0
    n=0
    p=0
    while num > 0:
        if num >= 100:
            s=s+1
            num=num-100
            print(num)
            print(s)
        elif num >= 50:
            h=h+1
            num=num-50
            print(num)
            print(h)
        elif num >= 25:
            q=q+1
            num=num-25
            print(num)
            print(q)
        elif num >= 10:
            d=d+1
            num=num-10
            print(num)
            print(d)
        elif num >= 5:
            n=n+1
            num=num-5
            print(num)
            print(n)
        elif num > 0:
            p=p+1
            num=num-1
            print(num)
            print(p)
    chang={}
    chang["dollars"]=s
    print(chang["dollars"])
    chang["half dollars"]=h
    chang["quarters"]=q
    chang["dimes"]=d
    chang["nickels"]=n
    chang["pennies"]=p
    print(chang)
print(change())
