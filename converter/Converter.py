class Converter(object):
    @staticmethod
    def convert(amount, initial_unit, target_unit, unit_map):
        return amount / unit_map[target_unit] * unit_map[initial_unit]
