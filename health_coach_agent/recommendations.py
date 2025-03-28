from exercise_api import get_exercises_by_target
from food_api import async_search_foods
import asyncio

def generate_workout_plan(goal):
    if goal.lower() == 'build muscle':
        exercises = get_exercises_by_target('biceps')
    elif goal.lower() == 'lose weight':
        exercises = get_exercises_by_target('cardio')
    else:
        exercises = get_exercises_by_target('full body')
    return exercises[:5]    # Return top 5 exercises


# Asynchronous function to take advantage of asynchronous search_foods
async def generate_meal_plan(dietary_preference):
    foods = await async_search_foods(dietary_preference)
    return foods[:5]      # Return top 5 foods