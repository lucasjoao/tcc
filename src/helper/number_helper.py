import math
import re


class number_helper:

    @staticmethod
    def is_number(string):
        if string.count('.') <= 1:
            try:
                # works fine with '1234', '1234.12' and '1234.0'
                number = float(string.replace(',', '.'))
                return (True, number)
            except ValueError:
                return (False, math.nan)
        else:
            return number_helper.__is_number_with_more_dots(string)

    @staticmethod
    def __is_number_with_more_dots(string):
        try:
            # works fine with '1.234.567'
            number = float(string.replace('.', ''))
            return (True, number)
        except ValueError:
            return number_helper.__is_number_with_more_dots_and_decimal(string)

    @staticmethod
    def __is_number_with_more_dots_and_decimal(string):
        # works fine with '1.234.567.89'
        if re.fullmatch(r'.*\.\d{2}', string) is not None:
            dots_number = string.count('.')
            # FIXME: se isso daqui jogar exception no float, entao pode dar ruim
            number = float(string.replace('.', '', dots_number - 1))
            return (True, number)
        else:
            return (False, math.nan)
