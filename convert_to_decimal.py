# The following function converts a binary notation into a decimal system
def convert_from_decimal(number, base):
    multiplier, result = 1 , 0
    while number > 0:
        result += number % base * multiplier
        multiplier *= 10
        number = number // base
    return result

def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number = number // 10
    return result

def test_convert_to_decimal():
    number, base = 9, 2
    assert (convert_from_decimal(number, base) == 1001)
    print('test passed')

def test_convert_from_decimal():
    number, base = 1001, 2
    assert(convert_to_decimal(number,base)==9)
    print('test_passed')

# the following function converts a decimal into a binary notation

if __name__ == "__main__":
    test_convert_to_decimal()
    test_convert_from_decimal()


