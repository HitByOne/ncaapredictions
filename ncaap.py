import pandas as pd
import streamlit as st

# Set Streamlit to wide mode
st.set_page_config(layout="wide")

# Load the CSV file from the Google Drive link
csv_url = "https://drive.google.com/uc?export=download&id=1-5ZUHFQ00xGSq5wXuzjLnKnGpAd8amWn"
ncaa_predictions = pd.read_csv(csv_url)

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
