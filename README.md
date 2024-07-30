**Whoop Meal Planner**

This repository contains the code for a website that helps college athletes plan their meals based on their fitness goals, workout data from WHOOP, and personal preferences.

**Introduction**

I wanted to create a meal planner with a shopping list to make it easier to follow fitness goals and create meals for a week. 
This meal planner takes statistics from WHOOP, such as calories burned, and user input to create a personalized meal planner and shopping list. 
It connects with WHOOP's API  and OAuth2.0 in order to get user authorization in order to get user data. The user data is analyzed and sent to a query built off of OpenAI's API. 
The response from OpenAI is sent to a json file which is then used in a JavaScript script to create the meal planner which is currently accessed from a local server.
A WHOOP membership is required to run along with an OpenAI API key.

**Features**

Personalized Meal Plan: Meal plans built on user input and WHOOP health and workout data
Macronutrient Breakdown: Contains an estimate of fats, carbs, and proteins per meal
Shopping List: Contains a comprehensive shopping list, which includes a cost estimate and amount of each food item needed

**Usage and Installation**

Python 3.x
Node.js and npm (for running a local server)
WHOOP API access
Environment Variables: Create a file named priv_variables.env in the root directory and add your OpenAI API key: OPENAI_API_KEY=your_openai_api_key

**To Run:**
Make sure all repository files are in one main repository folder. In a terminal whose directory points to that folder, run the command python3 main.py
From there, follow the directions in the terminal, the callback URL is the URL in the search bar after authorizing access. Once you have answered the questions and the meal plan has been generated, go to http://localhost:8000 in your search bar or cmd + click that link from terminal. You should see your personalized meal plan.
