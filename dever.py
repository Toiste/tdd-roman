import unittest

def int_to_roman(num):
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = ""
    for value, numeral in roman_numerals:
        while num >= value:
            result += numeral
            num -= value
    return result

# Testes para a função
class TestIntToRoman(unittest.TestCase):
    def test_single_digits(self):
        self.assertEqual(int_to_roman(1), "I")
        self.assertEqual(int_to_roman(3), "III")
        self.assertEqual(int_to_roman(4), "IV")
        self.assertEqual(int_to_roman(9), "IX")

    def test_double_digits(self):
        self.assertEqual(int_to_roman(10), "X")
        self.assertEqual(int_to_roman(20), "XX")
        self.assertEqual(int_to_roman(40), "XL")
        self.assertEqual(int_to_roman(90), "XC")

    def test_triple_digits(self):
        self.assertEqual(int_to_roman(100), "C")
        self.assertEqual(int_to_roman(400), "CD")
        self.assertEqual(int_to_roman(900), "CM")

    def test_large_numbers(self):
        self.assertEqual(int_to_roman(1000), "M")
        self.assertEqual(int_to_roman(1987), "MCMLXXXVII")
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")

    def test_edge_cases(self):
        self.assertEqual(int_to_roman(0), "")
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")

if __name__ == "__main__":
    unittest.main()
