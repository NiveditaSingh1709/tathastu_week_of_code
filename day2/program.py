#for even and odd
n=int(input("enter the number"))
if n%2==0:
    print(n,"it is an even")
else:
    print(n,"it is odd")
#for armstrong number
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if n==sum:
    print(n,"it is armstrong")
else:
    print(n,"it is not armstrong")
#palindrome  number
temp = n
rev = 0
while temp != 0:
    rev = (rev * 10) + (temp % 10)
    temp = temp // 10

if n== rev:
    print(n,"number is palindrome")
else:
    print(n,"number is not palindrome")
#prime number
if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
else:
    print(n, "is not a prime number")
