#CODE:
def isHappy(num):
    hs = set()
    hs.add(n)
    while n != 1:
        m = n
        while m > 0:
            rem = m % 10
            total += rem * rem
            m = m // 10
        if total in hs:
            return False
        else:
            hs.add(n)
        n = total
     
     return True      
    
