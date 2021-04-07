
def getBondDuration(y, face, couponRate, m):
    bondPrice=0
    sumt=0
    cf=face*couponRate
    for i in range(1,m+1):
        pv_=(1+y)**(-i)
        pvcf=pv_*cf
        sumt=sumt+pvcf*i
        bondPrice=bondPrice+pvcf
    bondPrice=bondPrice+face*pv_
    sumt=sumt+face*pv_*i
    bondDuration=sumt/bondPrice
    return(bondDuration)
