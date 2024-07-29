'''
Teagan Turner
Uses the functions from analyze_data.py to store user data. User data gets sent to OpenAI's chat completion feature which creates a meal plan based on the WHOOP data.
Meal plan is sent to a .json file.
'''

import os
from openai import OpenAI
from dotenv import load_dotenv
import analyze_data as ad
import json


# Load environment variables from the .env file
load_dotenv('priv_variables.env')
api_key = os.environ.get("OPENAI_API_KEY")

# Initialize OpenAI client with the API key
client = OpenAI(api_key =  api_key)

# Fetch user data using analyze_data.py functions
gender = ad.get_user_gender()
age = ad.get_user_age()
weight = ad.get_user_weight()
fitness_goal = ad.get_user_goals()
dietary_restrictions = ad.get_user_dietary_restrictions()
athlete_type = ad.get_user_athlete_type()
avg_cals_burned = ad.get_average_cals_burned()
workout_type = ad.get_common_workout()
workout_length = ad.get_average_workout_duration()
height = ad.get_user_height()

# Create a week-long meal plan and shopping list using OpenAI's chat completion feature
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
    {"role": "system", "content": "You are a nutrition expert."},
    {"role": "user", 'content': f"""
        Create a week-long meal plan and shopping list for a {age} year old {gender} that weighs {weight} kilograms, is {height} meters tall, who is trying to {fitness_goal}. 
        {gender} is a {athlete_type} and burns an average of {avg_cals_burned} per day. {gender} mainly does {workout_type} type workouts and their workouts usually last {workout_length} minutes. 
        Keep the cost under 150$. Include one snack between breakfast and lunch and one between lunch and dinner. They can’t eat {dietary_restrictions}. 
        Give me macronutrients for the meals and recipes for each day. Include calorie counts for each meal. 
        Respond with valid JSON only so that I can send it to a json file using json.loads and json.dumps. Do not include any additional text. Validate the JSON response before giving it to me.
        Format the response as follows:
        {{
            "Monday": {{
                "Meals": ["Breakfast: ...", "Snack 1: ...", "Lunch: ...", "Snack 2: ...", "Dinner: ..."],
                "Macronutrient Breakdown": {{"Breakfast": {{"Protein": 20, "Carbs": 30, "Fats": 15}}, ...}},
                "Recipes": [...],
                "Calories": [...]
            }},
            "Tuesday": {{...}},
            ...
            "Shopping List": ["Oats: 1 lb", "Protein Powder: 2 lbs", ...],
            "Cost": ...
        }}
        """}
    ]
)


# Extract JSON content from the completion response
meal_plan_content = completion.choices[0].message.content
json_start = meal_plan_content.find('{')
json_end = meal_plan_content.rfind('}') + 1
json_content = meal_plan_content[json_start:json_end]


# Parse the JSON content and save it to a file
meal_plan_json = json.loads(json_content)

with open('Meal_plan.json', 'w') as out_file:
    json.dump(meal_plan_json, out_file, indent=4)

