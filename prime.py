n=[1,2,3,4,5,6,7,8,9,10]
res={}
for num in n:
    res[num]=res.get(num,0)+1
    print(res)
    n=8
    def check_prime(n):
        if n<=1:
            for i in range(2,n):
                if n%i==0:
                    return "not a prime number"
                return "prime number"
            print(check_prime(8))
