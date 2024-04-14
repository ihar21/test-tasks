class BigInt:
    def __init__(self, value=0):
        if isinstance(value, int):
            self.value = str(value)
        elif isinstance(value, str):
            self.value = value.strip('0')
            if not self.value.isdigit():
                raise ValueError("Invalid input string")
        else:
            raise TypeError("Invalid input type")

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value

    def __lt__(self, other):
        return int(self.value) < int(other.value)

    def __le__(self, other):
        return int(self.value) <= int(other.value)

    def __gt__(self, other):
        return int(self.value) > int(other.value)

    def __ge__(self, other):
        return int(self.value) >= int(other.value)

    def __eq__(self, other):
        return int(self.value) == int(other.value)

    def __add__(self, other):
        return BigInt(str(int(self.value) + int(other.value)))

    def __sub__(self, other):
        return BigInt(str(int(self.value) - int(other.value)))

    def __mul__(self, other):
        return BigInt(str(int(self.value) * int(other.value)))

    def __truediv__(self, other):
        return BigInt(str(int(self.value) // int(other.value)))

    def __mod__(self, other):
        return BigInt(str(int(self.value) % int(other.value)))

    def __pow__(self, other):
        return BigInt(str(int(self.value) ** int(other)))

    def to_int(self):
        return int(self.value)

    @classmethod
    def from_int(cls, value):
        return cls(str(value))

    @classmethod
    def from_string(cls, value):
        return cls(value)

    def to_string(self):
        return self.value

    def __len__(self):
        return len(self.value)

    def zfill(self, width):
        if width <= len(self):
            return self
        return BigInt('0' * (width - len(self)) + self.value)

    def __getitem__(self, index):
        return int(self.value[index])

def karatsuba_multiply(x, y):
    x = str(x)
    y = str(y)
    if len(x) < 10 and len(y) < 10:
        return str(int(x) * int(y))

    n = max(len(x), len(y))
    if len(x) < n:
        x = '0' * (n - len(x)) + x
    if len(y) < n:
        y = '0' * (n - len(y)) + y

    m = n // 2
    high1, low1 = x[:m], x[m:]
    high2, low2 = y[:m], y[m:]

    z0 = int(karatsuba_multiply(low1, low2))
    z1 = int(karatsuba_multiply(str(int(low1) + int(high1)), str(int(low2) + int(high2))))
    z2 = int(karatsuba_multiply(high1, high2))

    result = (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0
    result_str = str(result)
    return result_str[:-1] if result_str.endswith('0') else result_str