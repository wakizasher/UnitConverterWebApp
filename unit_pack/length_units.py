# Create Length Unit Class
class LengthUnit:
    def __init__(self, name, symbol, to_base_factor):
        self.name = name
        self.symbol = symbol
        self.to_base_factor = to_base_factor

    # Convert to base value (meters)
    def convert_to_base(self, value_in_this_unit):
        return self.to_base_factor * value_in_this_unit

    # Convert from base values (meters)
    def convert_from_base(self, value_in_base):
        return value_in_base / self.to_base_factor


# Create instances of the class Length Unit
meter = LengthUnit('Meter', 'm', 1.0)
kilometer = LengthUnit('Kilometer', 'km', 1000.0)
centimeter = LengthUnit('Centimeter', 'cm', 0.01)
inch = LengthUnit('Inch', 'in', 0.0254)
foot = LengthUnit('Foot', 'ft', 0.3048)
yard = LengthUnit('Yard', 'yd', 0.9144)
mile = LengthUnit('Mile', 'mi', 1609.34)
millimeter = LengthUnit('Millimeter', 'mm', 0.001)


# Function to convert one value to the another
def convert_length(value:float, from_unit_obj, to_unit_obj) -> float:
    # Convert original value to base unit (meters)
    value_in_meters = from_unit_obj.convert_to_base(value)
    # Convert values in meters to the target unit
    final_value = to_unit_obj.convert_from_base(value_in_meters)
    return final_value