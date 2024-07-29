I wanted to create a meal planner with a shopping list to make it easier to follow fitness goals and create meals for a week. 
This meal planner takes statistics from WHOOP, such as calories burned, and user input to create a personalized meal planner and shopping list. 
It connects with WHOOP's API  and OAuth2.0 in order to get user authorization in order to get user data. The user data is analyzed and sent to a query built off of OpenAI's API. 
The response from OpenAI is sent to a json file which is then used in a JavaScript script to create the meal planner which is currently accessed from a local server.
A WHOOP membership is required to run along with an OpenAI API key.
