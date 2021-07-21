from converter.Converter import Converter


class TemperatureConverter(Converter):
    @staticmethod
    def convert(amount, initial_unit, target_unit, unit_map):
        if initial_unit == target_unit:
            return amount
        if initial_unit == "°C" and target_unit == "°F":
            return amount*1.8 + 32
        if initial_unit == "°C" and target_unit == "K":
            return amount + 273.15
        if initial_unit == "°F" and target_unit == "°C":
            return (amount - 32) / 1.8
        if initial_unit == "°F" and target_unit == "K":
            return (amount + 459.67) * 5/9
        if initial_unit == "K" and target_unit == "°F":
            return (amount * 1.8) - 459.67
        if initial_unit == "K" and target_unit == "°C":
            return amount - 273.15
