from Crypto.Util.number import long_to_bytes

c = 421345306292040663864066688931456845278496274597031632020995583473619804626233684
n = 631371953793368771804570727896887140714495090919073481680274581226742748040342637
e = 65537

p = 1461849912200000206276283741896701133693
q = 431899300006243611356963607089521499045809

phi = (p-1)*(q-1) #mencari nilai phi

def abcd(a, b):
    if a == 0:
        return(b, 0, 1)
    e, f, g = abcd(b%a, a)
    return (e, g-(b//a) * f, f)
def modinv(a, m):
    e, g, f = abcd(a, m)
    if g != 1:
        raise Exception('no mular inverse')
        return g%m
d = modinv(e, phi)
m = pow(c,d,n)

print(long_to_bytes(m))