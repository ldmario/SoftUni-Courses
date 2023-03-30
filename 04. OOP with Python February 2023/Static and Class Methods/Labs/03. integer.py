from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, floating_number):
        if type(floating_number) != float:
            return "value is not a float"
        return cls(floor(floating_number))

    @classmethod
    def from_roman(cls, value: str):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(value)):
            if i != 0 and rom_val[value[i]] > rom_val[value[i - 1]]:
                int_val += rom_val[value[i]] - 2 * rom_val[value[i - 1]]
            else:
                int_val += rom_val[value[i]]
        return cls(int_val)

    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, str):
            return f"wrong type"
        return cls(int(value))
