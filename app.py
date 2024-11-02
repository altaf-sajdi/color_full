import streamlit as st
import math

# Set the title and color scheme
st.markdown("<h1 style='color: darkblue; text-align: center;'>Sajdi Scientific Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: darkorange; text-align: center;'>A Streamlit Calculator with Scientific Functions</h3>", unsafe_allow_html=True)

# User input for numbers and operation selection
num1 = st.number_input("Enter the first number:", value=0.0, format="%.2f")
num2 = st.number_input("Enter the second number (if needed):", value=0.0, format="%.2f")

st.write("### Choose an Operation:")
operation = st.selectbox(
    "Operation",
    ("Addition", "Subtraction", "Multiplication", "Division", "Power", "Square Root", "Sine", "Cosine", "Tangent", "Logarithm")
)

# Perform the selected operation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        color = "green"
    elif operation == "Subtraction":
        result = num1 - num2
        color = "red"
    elif operation == "Multiplication":
        result = num1 * num2
        color = "blue"
    elif operation == "Division":
        if num2 == 0:
            result = "Error! Division by zero."
            color = "purple"
        else:
            result = num1 / num2
            color = "purple"
    elif operation == "Power":
        result = math.pow(num1, num2)
        color = "orange"
    elif operation == "Square Root":
        if num1 < 0:
            result = "Error! Square root of negative number."
            color = "brown"
        else:
            result = math.sqrt(num1)
            color = "brown"
    elif operation == "Sine":
        result = math.sin(math.radians(num1))
        color = "cyan"
    elif operation == "Cosine":
        result = math.cos(math.radians(num1))
        color = "magenta"
    elif operation == "Tangent":
        result = math.tan(math.radians(num1))
        color = "teal"
    elif operation == "Logarithm":
        if num1 <= 0:
            result = "Error! Logarithm of non-positive number."
            color = "yellow"
        else:
            result = math.log10(num1)
            color = "yellow"

    # Display result with color
    st.markdown(f"<h3 style='color: {color};'>Result: {result}</h3>", unsafe_allow_html=True)
