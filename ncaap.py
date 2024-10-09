import streamlit as st
import pandas as pd

# Set Streamlit to wide mode
st.set_page_config(layout="wide")

# Correct variable name for the NCAA sheet ID
ncaa_sheet_id = '19_lirG8bfTvccuBbFxfeCuRywJA0LZY1jt7_umjUCRA'

# Load data from Google Sheets directly
ncaa_predictions = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{ncaa_sheet_id}/export?format=csv")

# Create a new column combining 'Away' and 'Home' teams
ncaa_predictions['Away @ Home'] = ncaa_predictions['Away'] + ' @ ' + ncaa_predictions['Home']

# Display the title
st.title('NCAA Predictions')

# Create a filter for the combined "Away @ Home", including an "All Games" option
game_options = ['All Games'] + list(ncaa_predictions['Away @ Home'].unique())
selected_game = st.selectbox('Select Game (Away @ Home)', game_options)

# Filter the data based on the selected game or show all if "All Games" is selected
if selected_game == 'All Games':
    filtered_data = ncaa_predictions
else:
    filtered_data = ncaa_predictions[ncaa_predictions['Away @ Home'] == selected_game]

# Display the filtered data
st.dataframe(filtered_data)
