def incomodam(n):
    if n <1:
        return ""
    if n==1:
        print ("Um elefante incomoda muita gente")
    else:
        incomodam(n-1)
        inco = n*"incomodam "
        print("{} elefantes {} muito mais".format(n,inco))
        print("{} elefantes incomodam muita gente".format(n))



incomodam(10)