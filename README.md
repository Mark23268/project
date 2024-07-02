# Fuel Cost Calculator

This project is a simple Fuel Cost Calculator web application built using Streamlit. It allows users to input their vehicle's mileage, the distance they plan to travel, and the average cost of gas to calculate the total fuel cost for the trip.

## Features

- User-friendly web interface
- Real-time calculation of fuel cost
- Validation for user inputs
- Display of error messages for invalid inputs

## Installation

1. Clone the repository:

    ```sh
 https://github.com/Mark23268/project/blob/main/project.py.git
    
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:

    ```sh
    streamlit run project.py
    ```

2. You will automatically be transferred to another site to use the Fuel Cost Calculator.

## Project Structure

- `project.py`: Contains the main Streamlit app code.
- `test_project.py`: Contains the pytest test cases for the functions in `project.py`.
- `requirements.txt`: Lists the dependencies required for the project.
- `Untitled_design.png`: The logo used in the Streamlit app.

## Functions

- `calculate_fuel_cost(mileage, distance, avg_cost)`: Calculates the fuel cost based on mileage, distance, and average cost of gas.
- `convert_to_float(value)`: Converts a string value to a float. Returns `None` if the conversion fails.
- `is_valid_input(mileage, distance, avg_cost)`: Checks if all inputs are valid (i.e., not `None`).
- `main()`: The main function to run the Streamlit app.

## Testing

To run the tests, execute the following command in the project directory:

```sh
pytest
