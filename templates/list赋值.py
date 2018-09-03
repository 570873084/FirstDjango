def m():
    a = [1,0]
    a[0],a[a[0]] = a[a[0]],a[0]
    return a

print(m())