class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ","")
        self.valores = []

    def valid(self):
        num = self.card_num[::-1]
        sum = 0
        index = 1
        if len(num) <= 1:
            return False
        for digit in num:
            if not digit.isnumeric():
                return False
            elif index % 2 == 0:
                digit = int(digit) * 2
                if digit > 9:
                    digit -= 9
            sum += int(digit)
            index += 1
        return sum % 10 == 0
