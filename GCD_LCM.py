#Euclid Algo
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)
def lcm(a,b):
    prod = a*b
    p = gcd(a,b)
    return prod//p
#Number of test case
t= int(input())
while t:
    n,m = map(int,input().split())
    print("GCD ={} and LCM={}".format(gcd(n,m),lcm(n,m)))
    t = t-1