from time import sleep

if __name__ == '__main__':
    r = 1.08/1.04 - 1
    P = 2000000
    C = P/(1/r-(1/(r*(1+r)**15)))
    # C = P/(1-(1.04)**15/(1.08)**15)*(0.04)
    P = P * 1.08
    print(C)
    for i in range(15):
        C = C * 1.04
        P = P - C
        P = P * 1.08

        print(C)
    print(C)
    print(P)



