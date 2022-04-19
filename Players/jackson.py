import requests
import pandas as pd
import json

# API Key
key = "uxns42qzqutpg8zvcth9pmkm"

# Player ID
jackson_id = "e06a9c07-453a-4bb0-a7e9-2c3a64166dad"

api_url = f"https://api.sportradar.us/nfl/official/trial/v7/en/players/{jackson_id}/profile.json?api_key={key}"
response = requests.get(api_url)
jackson_data = response.json()['seasons'][4]['teams'][0]['statistics']['passing']
df_jackson = pd.json_normalize(jackson_data)
# print(df_jackson)
