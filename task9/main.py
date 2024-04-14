from BigINT import *

if __name__ == "__main__":
    a = BigInt(12345678901234567890)
    b = BigInt("98765432109876543210")

    print("a =", a)
    print("b =", b)

    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("a / b =", a / b)
    print("a % b =", a % b)
    print("a ** 2 =", a ** 2)

    print("a < b ?", a < b)
    print("a <= b ?", a <= b)
    print("a > b ?", a > b)
    print("a >= b ?", a >= b)
    print("a == b ?", a == b)

    # Convert BigInt to int and string
    c = a.to_int()
    d = b.to_string()
    print("c =", c, ", type:", type(c))
    print("d =", d, ", type:", type(d))
    print("Katashubian",karatsuba_multiply(a,b))
    input("Exit")