

def karatsuba(x,y):
    # print('my x', x)
    # print('my y', y)
    if x < 10 and y < 10:
        return x*y

    xs = str(x)
    ys = str(y)

    m = max(len(xs), len(ys))
    if m%2 != 0:
        m += 1    
    m_2 = int(m/2)

    # double slah so it gives me no remainder
    a = x//10**m_2
    # print('my a', a)
    # % sign to give me the remainder
    b = x % (10**m_2)
    # print('my b', b)

    c = y//10**m_2
    # print('my c', c)
    d = y % (10**m_2)
    # print('my d', d)


    ac = karatsuba(a,c)
    # print('my ac', ac)
    bd = karatsuba(b,d)
    # print('my bd', bd)
    e = karatsuba((a+b), (c+d)) - ac - bd
    # print('my e', e)

    return (ac*10**(2*m_2) + e*10**(m_2) + bd)

result = karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627)
print(result)   