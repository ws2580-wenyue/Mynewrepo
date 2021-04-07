def getBondPrice_E(face, couponRate, m, yc):
    temp = [0 for i in range(m)]
    bondPrice=0
    for i in range(0,m):
        temp[i]=(1+yc[i])**(-i-1)
    bondPrice=(sum(temp)*couponRate+temp[m-1])*face
        
    return(bondPrice)


