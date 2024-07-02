import streamlit as st
from PIL import Image

def calculate_fuel_cost(mileage, distance, avg_cost):
    try:
        mileage = float(mileage)
        distance = float(distance)
        avg_cost = float(avg_cost)

        total_cost = (distance / mileage) * avg_cost
        return total_cost
    except ValueError:
        return None

def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None

def is_valid_input(mileage, distance, avg_cost):
    return all(value is not None for value in [mileage, distance, avg_cost])

def main():
    st.title("Fuel Cost Calculator")

    # Load the logo image
    logo = Image.open("Logo_design.png")

    # Create columns for layout
    col1, col2 = st.columns([2, 1])

    with col1:
        mileage = convert_to_float(st.text_input("Vehicles Mileage:"))
        distance = convert_to_float(st.text_input("Distance Traveling:"))
        avg_cost = convert_to_float(st.text_input("Avg Cost of Gas:"))

    if st.button("Calculate"):
        if is_valid_input(mileage, distance, avg_cost):
            total_cost = calculate_fuel_cost(mileage, distance, avg_cost)
            if total_cost is not None:
                st.success(f"Total Cost: ${total_cost:.2f}")
            else:
                st.error("Please enter valid numbers")
        else:
            st.error("Please enter valid numbers")

    # Display the logo in the second column
    with col2:
        st.image(logo, width=230)

if __name__ == "__main__":
    main()
