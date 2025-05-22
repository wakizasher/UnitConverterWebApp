from unit_pack import length_units as lu
from unit_pack import weight_unit as wu
from unit_pack import temperature_units as tu

def main():
    print(lu.convert_length(5.0, lu.kilometer, lu.centimeter))
    print(lu.convert_length(176.0, lu.centimeter, lu.foot))

    print(wu.convert_weight(80, wu.kilogram, wu.gram))
    print(wu.convert_weight(80, wu.kilogram, wu.pound))

    print(tu.convert_temperature(21.0, tu.celsius,tu.fahrenheit))
    print(tu.convert_temperature(21.0,tu.celsius,tu.kelvin))

if __name__ == '__main__':
    main()
