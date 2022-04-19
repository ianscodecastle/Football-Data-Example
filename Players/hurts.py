import requests
import pandas as pd
import json

# API Key
key = "uxns42qzqutpg8zvcth9pmkm"

# Player ID
hurts_id = "64bd0f02-6a5d-407e-98f1-fd02048ea21d"

api_url = f"https://api.sportradar.us/nfl/official/trial/v7/en/players/{hurts_id}/profile.json?api_key={key}"
response = requests.get(api_url)
hurtsdata = response.json()['seasons'][2]['teams'][0]['statistics']['passing']
df_hurts = pd.json_normalize(hurtsdata)
# print(df_hurts)