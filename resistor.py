# Program for resistor colour coding calculator

def band4(B1, B2, M, T):
    r = ""
    b1 = {"black":"0","brown":"1","red":"2","orange":"3","yellow":"4","green":"5",
          "blue":"6","violet":"7","grey":"8","white":"9"}
    b2 = {"black":"0","brown":"1","red":"2","orange":"3","yellow":"4","green":"5",
          "blue":"6","violet":"7","grey":"8","white":"9"}
    m = {"black":"X1","brown":"X10","red":"X100","orange":"X1K","yellow":"X10K",
         "green":"X100K","blue":"X1M","violet":"X10M","grey":"X100M","white":"X1G",
         "gold":"X0.1","silver":"X0.01"}
    t = {"brown":"Ω ±1%","red":"Ω ±2%","gold":"Ω ±5%","silver":"Ω ±10%"}

    for i in b1:
        if i == B1:
            r +=b1[i]
    for i in b2:
        if i == B2:
            r +=b2[i]
    for i in m:
        if i == M:
            r +=m[i]
    for i in t:
        if i == T:
            r +=t[i]

    print("Resistor value:", r)


def band5(B1, B2, B3, M, T):
    r = ""
    b1 = {"black":"0","brown":"1","red":"2","orange":"3","yellow":"4","green":"5",
          "blue":"6","violet":"7","grey":"8","white":"9"}
    b2 = {"black":"0","brown":"1","red":"2","orange":"3","yellow":"4","green":"5",
          "blue":"6","violet":"7","grey":"8","white":"9"}
    b3 = {"black":"0","brown":"1","red":"2","orange":"3","yellow":"4","green":"5",
          "blue":"6","violet":"7","grey":"8","white":"9"}
    m = {"black":"X1","brown":"X10","red":"X100","orange":"X1K","yellow":"X10K",
         "green":"X100K","blue":"X1M","violet":"X10M","grey":"X100M","white":"X1G",
         "gold":"X0.1","silver":"X0.01"}
    t = {"brown":"Ω ±1%","red":"Ω ±2%","gold":"Ω ±5%","silver":"Ω ±10%"}

    for i in b1:
        if i == B1:
            r +=b1[i]
    for i in b2:
        if i == B2:
            r +=b2[i]
    for i in b3:
        if i == B3:
            r +=b3[i]
    for i in m:
        if i == M:
            r +=m[i]
    for i in t:
        if i == T:
            r +=t[i]

    print("Resistor value:", r)


# MAIN FUNCTION
band = input("Enter the number for band[4/5]:")

if band == "4":
    B1 = input("Enter the first band colour:")
    B2 = input("Enter the second band colour:")
    M = input("Enter the multiplier colour:")
    T = input("Enter the tolerance colour:")
    B1=B1.lower()
    B2=B2.lower()
    M=M.lower()
    T=T.lower()
    band4(B1, B2, M, T)

elif band == "5":
    B1 = input("Enter the first band colour:")
    B2 = input("Enter the second band colour:")
    B3 = input("Enter the third band colour:")
    M = input("Enter the multiplier colour:")
    T = input("Enter the tolerance colour:")
    B1=B1.lower()
    B2=B2.lower()
    B3=B3.lower()
    M=M.lower()
    T=T.lower()
    band5(B1, B2, B3, M, T)

else:
    print("Wrong input")
