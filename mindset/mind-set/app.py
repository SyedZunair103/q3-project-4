import streamlit as st
import random

# Motivational quotes
quotes = [
    "Success comes to those who work for it.",
    "A positive mindset can turn any challenge into an opportunity.",
    "Every day is a new chance to learn and grow.",
    "Failure is just a step towards a better comeback.",
    "Believe in yourself; you are capable of great things!"
]

# App title
st.title("Mindset Booster")

# Heading
st.header("Your Motivational Quote for Today")

# Display a random quote
st.write(random.choice(quotes))

# Button to show another quote
if st.button("Get Another Quote"):
    st.write(random.choice(quotes))
