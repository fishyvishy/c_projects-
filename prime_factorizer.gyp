num = int(input("Enter a postive whole number\n"))

def p_prod(lst):
    prod = 1
    for i in lst:
        prod *= i
    return prod

def mtp_check(lst, n):
    for i in lst:
        if n % i == 0:
            return False
    return True

def p_factorize(num):
    p_factors = []
    mtp = 0
    deg = 1
    for i in range(2, num):
        if num % i == 0 and mtp_check(p_factors, i) == True:
            p_factors.append(i)
            mtp = 1
            deg = 2
            while mtp > 0:
                if num % (i**deg) == 0:
                    p_factors.append(i)
                    deg += 1
                else:
                    mtp -= 1
        elif p_prod(p_factors) == num:
            break
        
            
    print("The prime factors of " + str(num) + " are " + str(p_factors))
                
            
p_factorize(num)
