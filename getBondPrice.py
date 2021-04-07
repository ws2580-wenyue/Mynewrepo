def getBondPrice(y, face, couponRate, m, ppy=1):
    bondPrice=0
    m2=m*ppy
    for i in range(1,m2+1):
        pv_=(1+y/ppy)**(-i)
        cf=face *couponRate/ppy
        pvcf=pv_*cf
        bondPrice=bondPrice+pvcf
        
    bondPrice=bondPrice+face*pv_
    

    return(bondPrice)



