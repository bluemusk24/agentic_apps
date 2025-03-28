import gradio as gr
from recommendations import generate_meal_plan, generate_workout_plan
from loguru import logger
from prometheus_client import start_http_server, Summary
import asyncio
import os

# Step 1: Error and Debug logs are added to track issues
logger.add("health_coach.log", rotation="1 MB")

# Step 2: Prometheus server is started to collect metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
def health_coach(goal, dietary_preference):
    try:
        workout_plan = generate_workout_plan(goal)
        meal_plan = asyncio.run(generate_meal_plan(dietary_preference))
        return workout_plan, meal_plan
    except Exception as e:
        logger.error(f"Error: {e}")
        return {}, {}
    
# Gradio app
app = gr.Interface(
    fn=health_coach,
    inputs=[
        gr.Textbox(label="Fitness Goal (e.g., Build Muscle, Lose Weight)"),
        gr.Textbox(label="Dietary Preference (e.g., Vegan, Low Carb)")
    ],
    outputs=[
        gr.JSON(label="Personalized Workout Plan"),
        gr.JSON(label="Personalized Meal Plan"),
    ],
    title="Personal Health Coach AI",
    description="Enter your fitness goal and dietary preference to receive personalized workout and meal plans"
)

def main():
    # Start Prometheus metrics server
    start_http_server(8000) 
    port = int(os.getenv("PORT", 7860))  # gradio port environment
    app.launch(server_name="0.0.0.0", server_port=port)     

if __name__ == "__main__":
    main()