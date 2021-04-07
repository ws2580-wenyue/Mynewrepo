
def getBondPrice_Z(face, couponRate, times, yc):
    temp = [0 for i in range(len(times))]
    bondPrice=0
    n=len(times)
    for i in range(0,n):
        temp[i]=(1+yc[i])**(-times[i])
    bondPrice=(sum(temp)*couponRate+temp[n-1])*face
        
    return(bondPrice)


# Test values

yc = [.010,.015,.020,.025,.030]
times=[1,1.5,3,4,7]
face = 2000000
couponRate = 0.04

data = getBondPrice_Z(face, couponRate, times, yc)
print(data)