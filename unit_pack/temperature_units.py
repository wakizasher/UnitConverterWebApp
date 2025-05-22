class TemperatureUnit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def convert_to_kelvin(self, value_in_this_unit):
        if self.symbol == 'C':
            return value_in_this_unit + 273.15
        elif self.symbol == 'F':
            return (value_in_this_unit - 32) * 1.8 + 273.15
        elif self.symbol == 'K':
            return value_in_this_unit
    def convert_from_kelvin(self, value_in_kelvin):
        if self.symbol == 'C':
            return value_in_kelvin - 273.15
        elif self.symbol == 'F':
            return (value_in_kelvin - 273.15) * 1.8 + 32
        elif self.symbol == 'K':
            return value_in_kelvin


# Temperature instances:
celsius = TemperatureUnit(name="Celsius", symbol="C")
fahrenheit = TemperatureUnit(name="Fahrenheit", symbol="F")
kelvin = TemperatureUnit(name="Kelvin", symbol="K")

def convert_temperature(value:float,from_temp_obj, to_temp_obj) -> float:
    value_in_kelvin = from_temp_obj.convert_to_kelvin(value)
    final_value = to_temp_obj.convert_from_kelvin(value_in_kelvin)
    return final_value