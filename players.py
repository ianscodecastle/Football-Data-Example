import requests
import pandas as pd
import json

# API Key
key = "uxns42qzqutpg8zvcth9pmkm"

# Player & Team IDs
hurts_id = "64bd0f02-6a5d-407e-98f1-fd02048ea21d"
jackson_id = "e06a9c07-453a-4bb0-a7e9-2c3a64166dad"
wentz_id = "e9a5c16b-4472-4be9-8030-3f77be7890cb"

# Season statistics
def get_hurts_passing_stats():
    api_url = f"https://api.sportradar.us/nfl/official/trial/v7/en/players/{hurts_id}/profile.json?api_key={key}"
    response = requests.get(api_url)
    hurtsdata = response.json()['seasons'][2]['teams'][0]['statistics']['passing']
    df_hurts = pd.json_normalize(hurtsdata)
    return df_hurts

def get_jackson_passing_stats():
    api_url = f"https://api.sportradar.us/nfl/official/trial/v7/en/players/{jackson_id}/profile.json?api_key={key}"
    response = requests.get(api_url)
    response.raise_for_status()
    jackson_data = json.loads(response.text)['seasons'][4]['teams'][0]['statistics']['passing']
    df_jackson = pd.json_normalize(jackson_data)
    return print(df_jackson)

def get_wentz_passing_stats():
    api_url = f"https://api.sportradar.us/nfl/official/trial/v7/en/players/{wentz_id}/profile.json?api_key={key}"
    response = requests.get(api_url)
    response.raise_for_status()
    wentz_data = json.loads(response.text)['seasons'][6]['teams'][0]['statistics']['passing']
    df_wentz = pd.json_normalize(wentz_data)
    return print(df_wentz)

# get_jackson_passing_stats()
get_wentz_passing_stats()