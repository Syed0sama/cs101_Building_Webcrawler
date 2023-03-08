def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
#we are again calling factorial procedure but n is less than now. factorial procedure will again start when we call again it in else statement

print factorial(3)



def is_palindrome(n):
    if n=='':
        return True
    else:
        if n[0]==n[-1]:
            return is_palindrome(n[1:-1])
        else:
            return False
print is_palindrome('level')
            


def fibonacci(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

print fibonacci(6 )


