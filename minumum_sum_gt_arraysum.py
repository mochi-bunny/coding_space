#get the minimum integer from input array for which total sum of array < integer *length of array
n = int(input('input N: ') )                 # Reading input 
arr= input('array elements: ')
arr= arr.split(' ')

a= []
for i in range(len(arr)):
  a.append(int(i))

anew = []
def summer(a):
    s = 0
    for i in range(len(a)):
        s= s+ a[i]
    return s

def sumlen(f, lg):
    d= 0 
    for i in range(lg):
        d= d+ f
    return d

if 1<=n and n<= 10**5:
    sum1 = summer(a)
    leng = len(a)
    for i in range(leng):
        if a[i] >= 1 and a[i]< 1000:
            sum2= sumlen(a[i], leng)
            if sum2> sum1:
                anew= a[i]
print(anew)

