def check_sign(num):
    if num >= 0:
        return '0'
    else:
        return '1'


def decimal_to_binary(num):
    num = int(num)
    s = ''
    while num > 0:
        s += str(num % 2)
        num //= 2
    return s[::-1]


def find_exponent(n, bias, num):
    if num == 0:
        return "00000000"
    n = n + bias
    s = ''
    for i in range(8):
        s += str(n % 2)
        n //= 2
    return s[::-1]


def fraction_to_binary(num, length):
    f = num - int(num)
    s = ''
    for i in range(23 - length):
        f *= 2
        s += str(int(f))
        f -= int(f)
    if 0 <= num < 1:
        return s[1:]
    else:
        return s


def detach(s, length):
    a = ''
    for i in range(length):
        a += s[length - i]
    return a[::-1]


def compute(num):
    sign = check_sign(num)
    if num < 0:
        num = -num
    s = decimal_to_binary(num)
    length = len(s) - 1  # finding the length of pow
    exponent = find_exponent(length, 127, num)
    significant = detach(s, length) + fraction_to_binary(num, length)
    string = f"IEEE754: {sign + exponent + significant}\n\nsign: {sign}\nexponent: {exponent}\n"
    string += f"significant: {significant}"

    return string







        
