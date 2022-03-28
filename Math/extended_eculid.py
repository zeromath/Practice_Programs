def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = extended_gcd(b % a, a)
    return g, y - (b // a) * x, x
 
 
if __name__ == '__main__': 
    g, x, y = extended_gcd(126, 621)
    print('The GCD is {}. x = {}, y = {}'.format(g, x, y))
 
