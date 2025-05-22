from flask import Flask, render_template, request
from unit_pack import length_units as lu
from unit_pack import weight_unit as wu
from unit_pack import temperature_units as tu

# Create an instance of the Flask class.
# __name__ helps Flask know where to look for resources like templates.
app = Flask(__name__)


# It's good practice to haee your unit objects easily accessible
# We'll create a dictionary to map symbols to the actual unti object
# Make sure these instances (lu.meter, lu.kilometer) are defined in our length_units.py
LENGTH_UNITS_OBJECTS = {
    "m": lu.meter,
    "km": lu.kilometer,
    "cm": lu.centimeter,
    "mm": lu.millimeter,
    "in": lu.inch,
    "ft": lu.foot,
    "yd": lu.yard,
    "mi": lu.mile
}


WEIGHT_UNITS_OBJECTS = {
    "g": wu.gram,
    "kg": wu.kilogram,
    "lb": wu.pound,
    "oz": wu.ounce,
    "mg": wu.milligram
}


TEMP_UNITS_OBJECTS = {
    "C": tu.celsius,
    "F": tu.fahrenheit,
    "K": tu.kelvin
}

# This is a "route". It tells Flask what function to run
# when someone visits the main page ("/") of your website

@app.route('/')
def home():
    return render_template('home.html')

#new route for our length converter page
@app.route('/length', methods=['GET', 'POST'])
def length_converter_page():
    # This tells Flask to find 'length_converter.html' in the 'templates' folder and send it to the browser.
    results_to_display = "Enter values to convert"

    if request.method == 'POST':
        try:
            value_str = request.form.get('value_to_convert')
            from_unit_symbol = request.form.get('from_unit')
            to_unit_symbol = request.form.get('to_unit')
            if not value_str or not from_unit_symbol or not to_unit_symbol:
                results_to_display = "Error: Missing form data. Please fill all fields"
            else:
                try:
                    value_number = float(value_str)
                except ValueError:
                    results_to_display = "Error: Please enter a valid number for the value."
                else:
                    from_unit_obj = LENGTH_UNITS_OBJECTS.get(from_unit_symbol)
                    to_unit_obj = LENGTH_UNITS_OBJECTS.get(to_unit_symbol)
                    if from_unit_obj and to_unit_obj:
                        converted_number = lu.convert_length(value_number,from_unit_obj,to_unit_obj)
                        results_to_display = f"{value_number}, {from_unit_symbol} is {converted_number:.4f} {to_unit_symbol}"
                    else:
                        results_to_display = "Error: Invalid unit selection."
        except Exception as e:
            print(f"An error occured: {e}")
            results_to_display = "An unexpected error occured"
    return render_template('length_converter.html', result_placeholder=results_to_display)


@app.route('/weight', methods=['GET','POST'])
def weight_converter_page():
    results_to_display = "Enter values to convert"
    if request.method == 'POST':
        try:
            # Get all raw string inputs from the form
            value_str = request.form.get('value_to_convert')
            from_unit_symbol = request.form.get('from_unit')
            to_unit_symbol = request.form.get('to_unit')
            if not value_str or not from_unit_symbol or not to_unit_symbol:
                results_to_display = "Error: Missing form data. Please fill all fields"
            else:
                try:
                    # convert the value to a number
                    value_number = float(value_str)
                except ValueError:
                    results_to_display = "Error: Please enter a valid number for the value."
                else:
                    from_unit_obj = WEIGHT_UNITS_OBJECTS.get(from_unit_symbol)
                    to_unit_obj = WEIGHT_UNITS_OBJECTS.get(to_unit_symbol)
                    if from_unit_obj and to_unit_obj:
                        converted_number = wu.convert_weight(value_number,from_unit_obj,to_unit_obj)
                        results_to_display = f"{value_number}, {from_unit_symbol} is {converted_number:.4f} {to_unit_symbol}"
                    else:
                        results_to_display = "Error: Invalid unit selection. Units not recognized."
        except Exception as e:
            print(f"An unexpected error occured in POST processing: {e}")
    return render_template('weight_converter.html', result_placeholder=results_to_display)


@app.route('/temp', methods=['GET','POST'])
def temp_converter_page():
    results_to_display = "Enter values to convert"
    if request.method == 'POST':
        try:
            # Get all raw string inputs from the form
            value_str = request.form.get('value_to_convert')
            from_unit_symbol = request.form.get('from_unit')
            to_unit_symbol = request.form.get('to_unit')
            if not value_str or not from_unit_symbol or not to_unit_symbol:
                results_to_display = "Error: Missing form data. Please fill all fields"
            else:
                try:
                    # convert the value to a number
                    value_number = float(value_str)
                except ValueError:
                    results_to_display = "Error: Please enter a valid number for the value."
                else:
                    from_unit_obj = TEMP_UNITS_OBJECTS.get(from_unit_symbol)
                    to_unit_obj = TEMP_UNITS_OBJECTS.get(to_unit_symbol)
                    if from_unit_obj and to_unit_obj:
                        converted_number = tu.convert_temperature(value_number,from_unit_obj,to_unit_obj)
                        results_to_display = f"{value_number}, {from_unit_symbol} is {converted_number:.4f} {to_unit_symbol}"
                    else:
                        results_to_display = "Error: Invalid unit selection. Units not recognized."
        except Exception as e:
            print(f"An unexpected error occured in POST processing: {e}")
    return render_template('temp_converter.html', result_placeholder=results_to_display)

# This part makes the app run when you execute this Python file.
# debug=True is super helpful during development because it gives you
# more detailed error messages and automatically reloads the server
# when you make code changes.


if __name__ == '__main__':
    app.run(debug=True)
