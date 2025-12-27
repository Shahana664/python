def fibbanocci(n):

    if n<=1:
        return n

    return fibbanocci(n-1)+fibbanocci(n-2)


print(fibbanocci(5))
