'''Teagan Turner
Loads the user's WHOOP data from the .csv and runs an analysis on it to store variables.
Summer 2024
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast
from datetime import datetime

# Load WHOOP data from CSV
whoop_data = pd.read_csv('whoop_data.csv')

# Dictionary mapping WHOOP sport ID numbers to sports
sport_Id_value = {
    -1 : 'Activity',
    0 : 'Running',
    1 : 'Cycling',
    16: 'Baseball',
    17: 'Basketball',
    18: 'Rowing',
    20: 'Field Hockey',
    21: 'Football',
    22: 'Golf',
    24: 'Ice Hockey',
    25: 'Lacrosee',
    26: 'Rugby',
    29: 'Skiing',
    30: 'Soccer',
    31: 'Softball',
    32: 'Squash',
    33: 'Swimming',
    34: 'Tennis',
    35: 'Track and Field',
    36: 'Volleyball',
    39: 'Boxing',
    42: 'Dance',
    43: 'Pilates',
    44: 'Yoga',
    45: 'Weightlifting',
    47: 'Cross Country Skiing',
    49: 'Duathlon',
    52: 'Hiking/Rucking',
    57: 'Mountain Biking',
    59: 'Powerlifting',
    62: 'Triathlon',
    63: 'Walking',
    64: 'Surfing',
    70: 'Meditation',
    71: 'Other',
    88: 'Ice Bath',
    96: 'HIIT',
    97: 'Spin',
    98: 'Jiu Jitsu',
    99: 'Manual Labor',
    101: 'Pickleball',
    126: 'Assault Bike',
    233: 'Sauna',
}

# Extract relevant columns from WHOOP data
cycle_score = whoop_data['cycle_score']
recovery_score = whoop_data['recovery_score']
workout_score = whoop_data['workout_score']
workout_start = whoop_data['workout_start']
workout_end = whoop_data['workout_end']
cycle_score_dict_list = []
recovery_score_dict_list = []

# Parse cycle and recovery scores from strings to dictionaries
for i in range(len(cycle_score)):
    parsed_dict = ast.literal_eval(cycle_score[i])
    cycle_score_dict_list.append(parsed_dict)

for i in range(len(recovery_score)):
    recovery_parsed_dict = ast.literal_eval(recovery_score[i])
    recovery_score_dict_list.append(recovery_parsed_dict)

def get_recent_strain():
    '''Retrieves the most recent strain score.

    Returns:
    -----------
    float. The most recent strain score.
    '''
    return cycle_score_dict_list[0]['strain']

def get_average_strain():
    '''Calculates the average strain score.

    Returns:
    -----------
    float. The average strain score.
    '''
    strain_score_list = [cycle['strain'] for cycle in cycle_score_dict_list]
    average_strain = sum(strain_score_list) / len(strain_score_list)
    return average_strain

def get_average_cals_burned():
    '''Calculates the average calories burned per day.

    Returns:
    -----------
    str. The average calories burned per day.
    '''
    kJ_burned_list = [cycle['kilojoule'] for cycle in cycle_score_dict_list]
    avg_kilojoules = sum(kJ_burned_list) / len(kJ_burned_list)
    avg_burned = avg_kilojoules / 4.184
    return f'Your average calories burned per day are: {avg_burned}.'

def get_common_workout():
    '''Identifies the three most common workouts.

    Returns:
    -----------
    str. The three most common workouts and the amount of times you did them in the last 20 workouts.
    '''
    counter = {}
    workout_id = whoop_data['workout_sport_id']
    for i in workout_id:
        counter[i] = counter.get(i, 0) + 1
    workout_type = {sport_Id_value[id]: counter[id] for id in counter if id in sport_Id_value}
    sorted_workout_type = dict(sorted(workout_type.items(), key=lambda item: item[1], reverse=True))
    common_workouts = list(sorted_workout_type.keys())[:3]
    common_counts = list(sorted_workout_type.values())[:3]
    return f'Your 3 most common workouts are {common_workouts} and you did those {common_counts} times respectively.'

def get_average_recovery_score():
    '''Calculates the average recovery score.

    Returns:
    -----------
    str. The average recovery score.
    '''
    recovery_score_list = [recovery['recovery_score'] for recovery in recovery_score_dict_list]
    avg_recovery_score = sum(recovery_score_list) / len(recovery_score_list)
    return f'Your average recovery score is: {avg_recovery_score} out of 100.'

def get_user_height():
    '''Retrieves the user's height.

    Returns:
    -----------
    Series. The user's height in meters.
    '''
    return whoop_data['user_measurements_height_meter']

def get_user_weight():
    '''Retrieves the user's weight.

    Returns:
    -----------
    Series. The user's weight in kilograms.
    '''
    return whoop_data['user_measurements_weight_kilogram']

def get_average_workout_duration():
    '''Calculates the average workout duration.

    Returns:
    -----------
    str. The average workout duration in minutes.
    '''
    duration_list = []
    for i in range(len(workout_start)):
        start_time = datetime.fromisoformat(workout_start[i].replace('Z', ''))
        end_time = datetime.fromisoformat(workout_end[i].replace('Z', ''))
        duration = (end_time - start_time).total_seconds()
        duration_list.append(duration)
    average_duration = sum(duration_list) / len(duration_list)
    average_duration_min = average_duration / 60
    return f'Your average workout duration is {average_duration_min} minutes.'

def get_user_goals():
    '''Prompt for the user to input their fitness goals.

    Returns:
    -----------
    str. The user's fitness goals.
    '''
    goals = input('What is your fitness goal? Would you like to lose weight? Would you like to build muscle? Would you like to build muscle while losing weight? Would you like to maintain weight? Please be specific: ')
    return goals

def get_user_athlete_type():
    '''Prompt for the user to input their athlete type.

    Returns:
    -----------
    str. The user's athlete type.
    '''
    user_athlete_type = input('What sport do you specialize in and what type of athlete are you? Strength? Power? Cardio? Example response is: I am a sprinter focusing on building explosivity/power. Please be specific: ')
    return user_athlete_type

def get_user_age():
    '''Prompt for the user to input their age.

    Returns:
    -----------
    str. The user's age.
    '''
    user_age = input('How old are you? ')
    return user_age

def get_user_gender():
    '''Prompt for the user to input their gender.

    Returns:
    -----------
    str. The user's gender.
    '''
    user_gender = input('What is your gender? If you prefer not to answer, please put N/A. ')
    return user_gender

def get_user_dietary_restrictions():
    '''Prompt for the user to input their dietary restrictions.

    Returns:
    -----------
    str. The user's dietary restrictions.
    '''
    user_dietary_restrictions = input('Do you have dietary restrictions? If so, what are they? Please put foods you do not enjoy/will not eat. ')
    return user_dietary_restrictions
