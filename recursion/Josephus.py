def Jos(n,k):
    if(n==1):
        return 1
    return (Jos(n-1,k)+k-1)%n +1
if __main__:
    n=int(input("enter n:))
    k=int(input("enter k:))
    print(str(Jos(n,k)))
