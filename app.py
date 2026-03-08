import os
import streamlit as st
import pandas as pd
from joblib import load
import folium
from streamlit_folium import st_folium


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# model = load(os.path.join(BASE_DIR, "model.joblib"))

st.title("Building Energy Usage Predictor")
st.subheader("Simply put in your location's latitude, longtiude, and use ID using the chart given to see your level of energy usage!")

st.write(pd.DataFrame({
        'Type of Building': ['Commercial', 'Industrial', 'Institutional','Multi-family','Other', 'Large Residential', 'Other Residential', 'Single Family'],
        'ID number': [0,1,2,3,4,5,6,7],

}))
# latitude = st.number_input(
#     "What is the latitude of your building?",
#     value=0.0
# )

# longitude = st.number_input(
#     "What is the longitude of your building?",
#     value=0.0
# )

# usetype = st.number_input(
#     "Enter a number from 0-7 for building use type",
#     min_value=0,
#     max_value=7,
#     step=1,
#     value=0
# )

# def get_app_response(prediction):

#     if prediction <= 3.21:
#         st.write("You have a generally low use of energy.")
#         st.write("Median Yearly Usage Per Square Foot (kWh):", prediction)

#     elif prediction <= 7:
#         st.write("You use a medium amount of energy.")
#         st.write("Median Yearly Usage Per Square Foot (kWh):", prediction)

#     else:
#         st.write("You use a high amount of energy.")
#         st.write("Median Yearly Usage Per Square Foot (kWh):", prediction)


# if st.button("Predict Energy Usage"):

#     input_features = [[latitude, longitude, usetype]]

#     prediction = model.predict(input_features)[0]

#     get_app_response(prediction)


# st.title("Energy Usage Map Predictor")

# bay_area_lat = 37.7749
# bay_area_lon = -122.4194

# # If user inputs coordinates, use them; otherwise stay in Bay Area center
# latitude = locals().get("latitude", bay_area_lat)
# longitude = locals().get("longitude", bay_area_lon)

# # Create map centered on Bay Area
# m = folium.Map(
#     location=[latitude, longitude],
#     zoom_start=10
# )

# # Marker for selected location
# folium.Marker(
#     [latitude, longitude],
#     popup="Energy Prediction Location",
#     tooltip="Selected Area"
# ).add_to(m)

# st_folium(m, width=700, height=500)