import math
import re


class number_helper:

    @staticmethod
    def is_number(string):
        commas_number = string.count(',')
        if commas_number > 1:
            return (False, math.nan)
        else:
            return number_helper.__is_number_with_at_least_one_dot(string)

    @staticmethod
    def __is_number_with_at_least_one_dot(string):
        string = string.replace(',', '.')
        if string.count('.') <= 1:
            try:
                number = float(string)
                return (True, number)
            except ValueError:
                return (False, math.nan)
        else:
            return number_helper.__is_number_with_more_dots(string)

    @staticmethod
    def __is_number_with_more_dots(string):
        try:
            if re.fullmatch(r'.*\.\d{3}', string) is not None:
                number = float(string.replace('.', ''))
                return (True, number)
            else:
                raise ValueError
        except ValueError:
            return number_helper.__is_number_with_more_dots_and_decimal(string)

    @staticmethod
    def __is_number_with_more_dots_and_decimal(string):
        try:
            if re.fullmatch(r'.*\.\d{1,2}', string) is not None:
                dots_number = string.count('.')
                number = float(string.replace('.', '', dots_number - 1))
                return (True, number)
            else:
                raise ValueError
        except ValueError:
            return (False, math.nan)
