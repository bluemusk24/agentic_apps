import gradio as gr
from recommendations import generate_meal_plan, generate_workout_plan
from loguru import logger
from prometheus_client import start_http_server, Summary
import asyncio
import os
from flask import Flask, jsonify, request
import threading


# Step 1: Flask app for Custom RestAPI endpoint
flask_app = Flask(__name__)

# Configure Logging
logger.add("health_coach.log", rotation="1 MB", retention="7 days")

# Prometheus server is started to collect metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
def health_coach(goal, dietary_preference):
    try:
        workout_plan = generate_workout_plan(goal)
        meal_plan = asyncio.run(generate_meal_plan(dietary_preference))
        return workout_plan, meal_plan
    except Exception as e:
        logger.error(f"Error occured: {e}")
        return {}, {}
    
# Step 2: Created Route for Rest API (Flask)
@flask_app.route("/api/health_coach", methods=["POST"])
def api_health_coach():
    data = request.get_json()

    if not data or "goal" not in data or "dietary_preference" not in data:
        return jsonify({"error": "invalid input"}), 400  

    response = health_coach(data["goal"], data["dietary_preference"])
    return jsonify({"workout_plan": response[0], "meal_plan": response[1]})


# Gradio app
gradio_app = gr.Interface(
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
    # Start Prometheus metrics server. Run both Flask and Gradio Apps simultaneously using threading
    start_http_server(8000)
    threading.Thread(target=lambda: flask_app.run(host="0.0.0.0", port=5000)).start()
    port = int(os.getenv("PORT", 7860))
    gradio_app.launch(server_name="0.0.0.0", server_port=port)     

if __name__ == "__main__":
    main()