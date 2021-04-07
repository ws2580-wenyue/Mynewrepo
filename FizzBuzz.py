def FizzBuzz(start, finish):
    
    n=finish-start+1
    outlist = [0 for i in range(n)]
    for i in range(n):
        temp=start+i
        outlist[i]=temp
        if temp%3==0:
            outlist[i]="fizz"
        if temp%5==0:
            outlist[i]="buzz"
        if (temp%3==0 and temp%5==0):
            outlist[i]="fizzbuzz"
    return(outlist)
