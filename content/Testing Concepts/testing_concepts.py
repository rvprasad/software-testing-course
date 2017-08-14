# compute(s) = (s+1)^2 mod 3 + 12

def compute(s): #0
    print("#0 {0}".format(s))
    
    s = s + 1  #1
    print("#1 {0}".format(s))
    
    s = s * 2  #2
    print("#2 {0}".format(s))
    
    s = s % 3  #3
    print("#3 {0}".format(s))
    
    s = s + 12 #4
    print("#4 {0}".format(s))
    
    return s
