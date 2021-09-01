##
#### Simple Encryption #1 - Alternating Split (6 kyu)
#########################################################


def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text

    mid = len(encrypted_text) // 2
    for _ in range(n):
        odds = encrypted_text[mid:]
        evens = encrypted_text[:mid]
        encrypted_text = ''.join(odds[i:i + 1] + evens[i:i + 1] for i in range(mid + 1))

    return encrypted_text


def encrypt(text, n):
    if not text or n <= 0:
        return text
    
    for _ in range(n):
        text = text[1::2] + text[::2]
    
    return text


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(encrypt("This is a test!", 0), "This is a test!")
        self.assertEqual(encrypt("This is a test!", 1), "hsi  etTi sats!")
        self.assertEqual(encrypt("This is a test!", 2), "s eT ashi tist!")
        self.assertEqual(encrypt("This is a test!", 3), " Tah itse sits!")
        self.assertEqual(encrypt("This is a test!", 4), "This is a test!")
        self.assertEqual(encrypt("This is a test!", -1), "This is a test!")
        self.assertEqual(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")

        self.assertEqual(decrypt("This is a test!", 0), "This is a test!")
        self.assertEqual(decrypt("hsi  etTi sats!", 1), "This is a test!")
        self.assertEqual(decrypt("s eT ashi tist!", 2), "This is a test!")
        self.assertEqual(decrypt(" Tah itse sits!", 3), "This is a test!")
        self.assertEqual(decrypt("This is a test!", 4), "This is a test!")
        self.assertEqual(decrypt("This is a test!", -1), "This is a test!")
        self.assertEqual(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")

        self.assertEqual(encrypt("", 0), "")
        self.assertEqual(decrypt("", 0), "")
        self.assertEqual(encrypt(None, 0), None)
        self.assertEqual(decrypt(None, 0), None)



if __name__ == '__main__':
    unittest.main()

