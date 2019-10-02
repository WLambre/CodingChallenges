n1, n2 = 1, 1
def fibonacci(n1,n2):
    n3=n1+n2
    return n2, n3
term=2
while len(str(n2)) <1000:
    n1,n2=fibonacci(n1,n2)
    term+=1
print (term)
