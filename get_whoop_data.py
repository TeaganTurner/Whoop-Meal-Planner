"""
Teagan Turner
Extracts user and workout data from WHOOP API and processes it into a CSV file.
Summer 2024

NOTE: Run file, follow link by copy and pasting url or cmd + click. After authorizing access, copy the url from the webpage and paste it back into terminal.
"""

# Load environment variables from .env file
import requests
import os
from dotenv import load_dotenv
import pandas as pd
import json
from requests_oauthlib import OAuth2Session


load_dotenv('priv_variables.env')
client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')
redirect_uri = 'https://oauth.pstmn.io/v1/browser-callback'
auth_url = 'https://api.prod.whoop.com/oauth/oauth2/auth'
access_token_url = 'https://api.prod.whoop.com/oauth/oauth2/token'
scope = ['offline', 'read:recovery', 'read:cycles', 'read:workout', 'read:profile', 'read:body_measurement']

access_token = None
refresh_token = None

def Token(client_id = client_id, client_secret = client_secret):
    """
    Obtain and print the access and refresh tokens from WHOOP API.

    Parameters:
    -----------
    client_id: str. Client ID for WHOOP API.
    client_secret: str. Client secret for WHOOP API.

    Returns:
    -----------
    Tuple (str, str). Access token and refresh token.
    """
    global access_token, refresh_token
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)

    authorization_url, state = oauth.authorization_url(auth_url)

    print(f'Please go to {authorization_url} and authorize access.')
    authorization_response = input('Enter the full callback URL: ')


    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope, state = state)
    token = oauth.fetch_token(access_token_url, authorization_response = authorization_response, client_id = client_id, client_secret= client_secret, include_client_id=True)

    access_token = token.get('access_token')
    refresh_token = token.get('refresh_token')
    print(f'Access Token: {access_token}')
    print(f'Refresh Token: {refresh_token}')
    return access_token, refresh_token


def refreshToken(refresh_token, client_id, client_secret):
    """
    Refresh the access token using the refresh token.

    Parameters:
    -----------
    refresh_token: str. Refresh token.
    client_id: str. Client ID for WHOOP API.
    client_secret: str. Client secret for WHOOP API.

    Returns:
    -----------
    Tuple (str, str). New access token and refresh token.
    """
    global access_token
    url = 'https://api.prod.whoop.com/oauth/oauth2/token'
    
    data = {
    'grant_type': 'refresh_token',
    'refresh_token': refresh_token,
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'offline'
    }

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    rToken = requests.post(url, headers = headers, data = data)
    token = rToken.json()
    access_token = token.get('access_token')
    refresh_token = token.get('refresh_token', refresh_token)
    return access_token, refresh_token

def getUser(access_token):
    """
    Get user profile data from WHOOP API.

    Parameters:
    -----------
    access_token: str. Access token for WHOOP API.

    Returns:
    -----------
    dict. User profile data.
    """
    url = 'https://api.prod.whoop.com/developer/v1/user/profile/basic?'
    headers = {'Authorization': f'Bearer {access_token}'}    
    
    user = requests.get(url, headers = headers)
    return user.json()


def getUserBodyMeasurements(access_token):
    """
    Get user body measurements from WHOOP API.

    Parameters:
    -----------
    access_token: str. Access token for WHOOP API.

    Returns:
    -----------
    dict. User body measurements.
    """
    url = 'https://api.prod.whoop.com/developer/v1/user/measurement/body?'
    headers = {'Authorization': f'Bearer {access_token}'}

    userResponse = requests.get(url, headers = headers)
    return userResponse.json()


def getCurrentCycle(access_token):
    """
    Get the current cycle data from WHOOP API.

    Parameters:
    -----------
    access_token: str. Access token for WHOOP API.

    Returns:
    -----------
    dict. Current cycle data.
    """
    url = 'https://api.prod.whoop.com/developer/v1/cycle?'
    params = {'limit': 1}
    headers = {'Authorization': f'Bearer {access_token}'}

    cycleResponse = requests.get(url, params = params, headers = headers)
    return cycleResponse.json()


def getCurrentWorkout(access_token):
    """
    Get the current workout data from WHOOP API.

    Parameters:
    -----------
    access_token: str. Access token for WHOOP API.

    Returns:
    -----------
    dict. Current workout data.
    """
    url = 'https://api.prod.whoop.com/developer/v1/activity/workout?'
    params = {'limit': 1}
    headers = {'Authorization': f'Bearer {access_token}'}

    workoutResponse = requests.get(url, params = params, headers = headers)
    return workoutResponse.json()


def getCurrentRecovery(access_token):
    """
    Get the current recovery data from WHOOP API.

    Parameters:
    -----------
    access_token: str. Access token for WHOOP API.

    Returns:
    -----------
    dict. Current recovery data.
    """
    url = 'https://api.prod.whoop.com/developer/v1/recovery?'
    params = {'limit': 1}
    headers = {'Authorization': f'Bearer {access_token}'}

    workoutResponse = requests.get(url, params = params, headers = headers)
    return workoutResponse.json()


def getTenCycles(access_token):
    """
    Get the last 10 cycles data from WHOOP API.

    Parameters:
    -----------
    access_token: str. Access token for WHOOP API.

    Returns:
    -----------
    dict. Last 10 cycles data.
    """
    url = 'https://api.prod.whoop.com/developer/v1/cycle?'
    params = {'limit': 10}
    headers = {'Authorization': f'Bearer {access_token}'}

    cycleResponse = requests.get(url, params = params, headers = headers)
    return cycleResponse.json()


def getTenRecoveries(access_token):
    """
    Get the last 10 recoveries data from WHOOP API.

    Parameters:
    -----------
    access_token: str. Access token for WHOOP API.

    Returns:
    -----------
    dict. Last 10 recoveries data.
    """
    url = 'https://api.prod.whoop.com/developer/v1/recovery?'
    params = {'limit': 10}
    headers = {'Authorization': f'Bearer {access_token}'}

    workoutResponse = requests.get(url, params = params, headers = headers)
    return workoutResponse.json()


def getTwentyWorkouts(access_token):
    """
    Get the last 20 workouts data from WHOOP API.

    Parameters:
    -----------
    access_token: str. Access token for WHOOP API.

    Returns:
    -----------
    dict. Last 20 workouts data.
    """
    url = 'https://api.prod.whoop.com/developer/v1/activity/workout?'
    params = {'limit': 20}
    headers = {'Authorization': f'Bearer {access_token}'}

    workoutResponse = requests.get(url, params = params, headers = headers)
    return workoutResponse.json()

if not access_token or not refresh_token:
    Token(client_id, client_secret)
else:
    access_token, refresh_token = refreshToken(refresh_token, client_id, client_secret)


user_profile = getUser(access_token)
user_measurements = getUserBodyMeasurements(access_token)
user_data = getCurrentCycle(access_token)
ten_cycles = getTenCycles(access_token)
ten_recoveries = getTenRecoveries(access_token)
twenty_workouts = getTwentyWorkouts(access_token)


df_user_profile = pd.DataFrame([user_profile])
df_user_measurements = pd.DataFrame([user_measurements])
df_user_data = pd.DataFrame([user_data])
df_ten_cycles = pd.DataFrame(ten_cycles['records']) 
df_ten_recoveries = pd.DataFrame(ten_recoveries['records'])
df_twenty_workouts = pd.DataFrame(twenty_workouts['records']) 

df_user_profile = df_user_profile.add_prefix('user_profile_')
df_user_measurements = df_user_measurements.add_prefix('user_measurements_')
df_ten_cycles = df_ten_cycles.add_prefix('cycle_')
df_ten_recoveries = df_ten_recoveries.add_prefix('recovery_')
df_ten_workouts = df_twenty_workouts.add_prefix('workout_')

combined_df = pd.concat([df_user_data, df_user_measurements, df_user_profile, df_ten_cycles, df_ten_recoveries, df_ten_workouts], axis=1)

combined_df.to_csv('whoop_data.csv', index=False)

print("Data written to whoop_data.csv")

