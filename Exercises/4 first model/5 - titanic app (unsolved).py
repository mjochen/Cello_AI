import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# import the files, only needed for ranges in sliders
df = pd.read_excel('../files/titanic3.xlsx', engine='openpyxl')


def calculate_survival():
    # Get the information from the sliders

    # Put them into a dict
    
    # load the trained model from the pkl file
    # use it to predict the survival of the random person
    # return ...

# Using object notation
# create the input widgets for the user to fill in the information about the random person, use the ranges from the dataframe

ok_button = st.sidebar.button("OK")

# Bing AI, "could you please write an intro text for a website that uses machine learning to predict surviving the titanic. Not to long."
st.markdown("""
# **Predicting Titanic Survival with Machine Learning**

Welcome to our Titanic Survival Prediction platform! 🚢

Our cutting-edge machine learning algorithms analyze historical data from the ill-fated RMS Titanic to forecast the likelihood of passengers surviving the tragic voyage. By considering factors such as passenger class, age, gender, and cabin location, our models provide accurate predictions.

Embark on this journey with us as we unravel the mysteries of the Titanic's destiny. 🌊
""")

if ok_button:
    living = calculate_survival()
    if living == 1:
        st.markdown(f"**You would have survived the Titanic.**")
    else:
        st.markdown(f"**You would have died on the Titanic.**")
    