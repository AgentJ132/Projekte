N = int (input("Bitte Anfangszahl angeben: "))
n = N-1
sum = 0

while(N>0 or n>0):
    sum = N+n+sum
    N-=2
    n-=2
print (sum)
