#TOWER OG HANOI PROBLEM USING RECURSION
def TOH(n,cur,inter,dest):
    steps=0
    if n==1:
        print("move 1 from "+cur+" to "+dest)
        return 1
    steps=steps+TOH(n-1,cur,dest,inter)
    print("move "+str(n)+" from "+cur+" to "+ dest)
    steps=steps+1
    steps=steps+TOH(n-1,inter,cur,dest)
    return steps
n=0
steps=0
while True:
    n=int(input("enter n:"))
    steps=TOH(n,'A','B','C')
    print("steps:"+str(steps))
    
