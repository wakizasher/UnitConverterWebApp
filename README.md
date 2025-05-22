# Unit Converter Web Application

A simple web application built with Python and Flask that allows users to convert between different units of measurement for length, weight, and temperature. This project was developed as a learning exercise to practice Python programming, Flask web framework basics, HTML forms, and Object-Oriented Programming (OOP) principles.
The idea of the project retrieved from https://roadmap.sh/projects/unit-converter
## Features

* **Length Conversion:** Convert between Millimeter, Centimeter, Meter, Kilometer, Inch, Foot, Yard, and Mile.
* **Weight Conversion:** Convert between Milligram, Gram, Kilogram, Ounce, and Pound.
* **Temperature Conversion:** Convert between Celsius, Fahrenheit, and Kelvin.
* Simple web interface with separate pages for each conversion type.
* User-friendly forms to input values and select units.
* Displays the converted value directly on the webpage.
* Basic error handling for invalid input and missing data.
* Navigation links to easily switch between different converter pages.

## Technologies Used

* **Backend:** Python
* **Web Framework:** Flask
* **Frontend:** HTML
* **Templating Engine:** Jinja2 (comes with Flask)
* **Core Logic:** Object-Oriented Programming (OOP) principles for defining and managing units.

## Project Structure

The project is structured to separate concerns:


unit_converter_project/
|
|-- app.py                   # Main Flask application file (routes, request handling)
|
|-- unit_pack/               # Package containing unit definitions and conversion logic
|   |-- init.py          # Makes 'unit_pack' a Python package
|   |-- length_units.py      # LengthUnit class, instances, and convert_length function
|   |-- weight_units.py      # WeightUnit class, instances, and convert_weight function (assuming similar structure)
|   |-- temperature_units.py # TemperatureUnit class, instances, and convert_temperature function
|
|-- templates/               # HTML templates for the web pages
|   |-- length_converter.html
|   |-- weight_converter.html
|   |-- temp_converter.html
|   |-- (potentially a base.html or layout.html if you add one later)
|
|-- static/                  # (Optional) For CSS, JavaScript, images if added later
|
|-- README.md                # This file
|
|-- .gitignore               # (Recommended) To exclude files like venv, pycache
|
|-- requirements.txt         # (Recommended) To list project dependencies


## Setup and Installation

1.  **Clone the repository (if it's on GitHub):**
    ```bash
    git clone <your-repository-url>
    cd unit_converter_project
    ```

2.  **Create a virtual environment (recommended):**
    This keeps your project dependencies isolated.
    ```bash
    python -m venv venv
    ```
    Activate the virtual environment:
    * Windows: `venv\Scripts\activate`
    * macOS/Linux: `source venv/bin/activate`

3.  **Install dependencies:**
    The main dependency is Flask. If you create a `requirements.txt` file, you can install all dependencies with `pip install -r requirements.txt`. For now, you can install Flask directly:
    ```bash
    pip install Flask
    ```
    If you create a `requirements.txt` file, it should contain:
    ```
    Flask
    ```

## How to Run the Application

1.  **Ensure your virtual environment is activated** (see Setup step 2).
2.  **Navigate to the project's root directory** (where `app.py` is located) in your terminal.
3.  **Run the Flask application:**
    ```bash
    python app.py
    ```
4.  You should see output in your terminal indicating the server is running, typically on `http://127.0.0.1:5000/` or `http://localhost:5000/`.
5.  **Open your web browser** and go to `http://127.0.0.1:5000/`.
    * To access specific converters, navigate to:
        * `http://127.0.0.1:5000/length`
        * `http://127.0.0.1:5000/weight`
        * `http://127.0.0.1:5000/temp`

## How It Works

* **Unit Definitions (`unit_pack/`):**
    * Each unit type (Length, Weight, Temperature) has its own Python module.
    * Classes like `LengthUnit`, `WeightUnit`, and `TemperatureUnit` define the properties (name, symbol) and conversion logic for each unit.
    * For length and weight, units are defined by their factor relative to a base unit (e.g., meters for length, grams for weight).
    * For temperature, specific formulas are used to convert to and from a base unit (e.g., Kelvin).
    * Helper functions like `convert_length`, `convert_weight`, and `convert_temperature` orchestrate the conversion between any two units of the same type by first converting to the base unit and then from the base unit to the target unit.

* **Flask Application (`app.py`):**
    * Defines routes (`@app.route(...)`) for each converter page (`/length`, `/weight`, `/temp`) and the home page (`/`).
    * Handles both `GET` requests (to display the form) and `POST` requests (when the user submits the form).
    * Retrieves user input (value, from-unit, to-unit) from the HTML form.
    * Uses dictionaries (e.g., `LENGTH_UNITS_OBJECTS`) to map unit symbols from the form to the actual Python unit objects.
    * Calls the appropriate conversion function from the `unit_pack` modules.
    * Passes the result (or error messages) back to the HTML template for display.

* **HTML Templates (`templates/`):**
    * Provide the structure for the web pages.
    * Use HTML forms (`<form>`, `<input>`, `<select>`) for user input.
    * Use Jinja2 templating syntax (`{{ ... }}`) to display dynamic data passed from the Flask app (like the conversion result or dropdown options).
    * (Ideally, dropdown menus for units are populated dynamically from the Python backend to ensure consistency and ease of maintenance - if you've implemented this).

## Future Enhancements (Ideas)

* **Improved Styling:** Add CSS to make the application more visually appealing.
* **Dynamic Dropdowns:** If not already implemented, populate unit selection dropdowns dynamically from the Python unit definitions to ensure a single source of truth.
* **Base HTML Template:** Use Jinja2 template inheritance to create a base layout (e.g., for navigation, header, footer) to reduce HTML duplication.
* **More Unit Types:** Add converters for other categories like Area, Volume, Speed, Data Storage, etc.
* **Input Validation:** More robust client-side and server-side input validation.
* **User Accounts/History:** (More advanced) Allow users to save favorite conversions or see a history.
* **API Endpoints:** (More advanced) Create API endpoints so other applications could use your conversion logic.
* **Unit Tests:** Write tests to ensure the conversion logic is always correct.

---

This project serves as a great foundation for learning web development with Python and Flask, and for understanding how to structure a simple application.
