import requests
import pandas as pd
import json

# API Key
key = "uxns42qzqutpg8zvcth9pmkm"

# Player ID
wentz_id = "e9a5c16b-4472-4be9-8030-3f77be7890cb"


api_url = f"https://api.sportradar.us/nfl/official/trial/v7/en/players/{wentz_id}/profile.json?api_key={key}"
response = requests.get(api_url)
wentz_data = response.json()['seasons'][6]['teams'][0]['statistics']['passing']
df_wentz = pd.json_normalize(wentz_data)
# print(df_wentz)