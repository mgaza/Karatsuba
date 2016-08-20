def Karatsuba(x,y):
    """
        An Algorithm to multiply 2 numbers in an efficient mannar ;)
        Better than old school algorithm!
    """
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        n = max(len(str(x)),len(str(y)))
        m = n / 2

        a = x / 10 ** m
        b = x % 10 ** m
        c = y / 10 ** m
        d = y % 10 ** m

        ac = Karatsuba(a,c)
        bd = Karatsuba(b,d)
        ad_plus_bc = Karatsuba(a+b,c+d) - ac - bd

        return ac * 10 ** (2*m) + (ad_plus_bc * 10 ** m) + bd

def test():
    assert Karatsuba(5,10) == 50
    assert Karatsuba(23,43) == 989
    print "All Tests have been passed!"


test()
