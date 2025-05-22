# Create Weight Unit Class
class WeightUnit:
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


# Weight instances using:
gram = WeightUnit('Gram', 'g', 1.0)
kilogram = WeightUnit('Kilogram', 'kg', 1000.0)
pound = WeightUnit('Pound', 'lb', 453.592) # 1 lb is approx 453.592 grams
ounce = WeightUnit('Ounce', 'oz', 28.3495) # 1 oz is approx 28.3495 grams
milligram = WeightUnit('Milligram', 'mg', 0.001)

def convert_weight(value: float, from_unit_obj, to_unit_obj) -> float:
    value_in_grams = from_unit_obj.convert_to_base(value)
    final_value = to_unit_obj.convert_from_base(value_in_grams)
    return final_value