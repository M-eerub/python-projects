import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Supported conversions
conversion_factors = {
    "Length": {"Meter": 1, "Kilometer": 0.001, "Mile": 0.000621371, "Yard": 1.09361},
    "Weight": {"Gram": 1, "Kilogram": 0.001, "Pound": 0.00220462, "Ounce": 0.035274},
    "Temperature": {"Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32, "Kelvin": lambda x: x + 273.15}
}



# Sidebar for navigation
st.sidebar.title("Unit Converter Navigation")
# st.sidebar.image("https://via.placeholder.com/150", use_column_width=True)
st.sidebar.markdown("### Select conversion category")

st.title("🌟 Advanced Unit Converter🌟")
st.markdown("---")

# Select conversion category
category = st.sidebar.selectbox("Select Category", list(conversion_factors.keys()))

# Select input and output units
units = list(conversion_factors[category].keys())
input_unit = st.selectbox("From", units)
output_unit = st.selectbox("To", units)

# Input value
value = st.number_input("Enter Value", value=1.0, step=0.1)

# Conversion logic
if category == "Temperature":
    input_to_base = conversion_factors[category][input_unit]
    base_to_output = conversion_factors[category][output_unit]
    converted_value = base_to_output(input_to_base(value))
else:
    converted_value = value * (conversion_factors[category][output_unit] / conversion_factors[category][input_unit])

st.success(f"🎯 Converted Value: {converted_value:.4f} {output_unit}")

# Generate graph
values = [value * (conversion_factors[category][unit] / conversion_factors[category][input_unit]) if category != "Temperature" else conversion_factors[category][unit](input_to_base(value)) for unit in units]
df = pd.DataFrame({"Unit": units, "Value": values})

fig, ax = plt.subplots()
ax.bar(df["Unit"], df["Value"], color=["#FF6F61", "#6B4226", "#FFD166", "#06D6A0", "#118AB2"][:len(units)])
ax.set_ylabel("Converted Values")
ax.set_title("📊 Conversion Graph")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", linestyle="--", alpha=0.7)
st.pyplot(fig)