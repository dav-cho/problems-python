##
#### STring Incrementer (5 kyu)
###################################


def increment_string(strng):
    if not strng:
        return '1'
    if strng[-1].isalpha():
        return strng + '1'

    chars = ''
    digits = []
    for i in range(len(strng) - 1, -1, -1):
        if strng[i].isdigit():
            digits.append(int(strng[i]))
        else:
            chars = strng[:i + 1]
            break

    carry, val = divmod(digits[0] + 1, 10)
    digits[0] = val
    if carry:
        j = 1
        while carry:
            if j < len(digits):
                digits[j] += carry
            else:
                digits.append(carry)

            carry, val = divmod(digits[j], 10)
            digits[j] = val
            j += 1

    digits = [str(x) for x in reversed(digits)]
    return chars + ''.join(digits)


def increment_string(strng):
    chars = strng.rstrip('1234567890')
    digits = strng[len(chars):]

    if not digits:
        return strng + '1'

    return chars + str(int(digits) + 1).zfill(len(digits))


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(increment_string("foo"), "foo1")
        self.assertEqual(increment_string("foobar001"), "foobar002")
        self.assertEqual(increment_string("foobar1"), "foobar2")
        self.assertEqual(increment_string("foobar00"), "foobar01")
        self.assertEqual(increment_string("foobar99"), "foobar100")
        self.assertEqual(increment_string("foobar099"), "foobar100")
        self.assertEqual(increment_string(""), "1")


if __name__ == '__main__':
    unittest.main()

