#TOWER OG HANOI PROBLEM USING RECURSION
def TOH(n,cur,inter,dest):
    if n==1:
        print("move 1 from "+cur+" to "+dest)
        return
    TOH(n-1,cur,dest,inter)
    print("move "+str(n)+" from "+cur+" to "+ dest)
    TOH(n-1,inter,cur,dest)
n=0
while True:
    n=int(input("enter n:"))
    TOH(n,'A','B','C')
    