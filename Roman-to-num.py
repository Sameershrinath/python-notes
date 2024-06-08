class Solution:
    def intToRoman(self, num: int) -> str:
        # List of Roman numerals and their corresponding integer values
        val_to_roman = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        # Initialize the result string
        result = ""
        
        # Convert the integer to Roman numeral
        for value, roman in val_to_roman:
            # Determine how many times the Roman numeral should appear
            count = num // value
            if count > 0:
                result += roman * count
                num -= value * count
        
        return result
