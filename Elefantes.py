def incomodam(n):
    if n<1:
        return ""
    else:
        incomodam(n-1)
        return"incomodam "*n

def elefantes(n):
    if n < 1:
        return ""

    if n<2:
     return "Um elefante incomoda muita gente\n"
    elefantes(n - 1)

    if n >= 2:

        return elefantes(n - 1) + str(n) + " elefantes " + incomodam(n) +"muito mais\n" + str(n) + " elefantes incomodam muita gente\n"

print(elefantes(10))