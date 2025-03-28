# PROJECTS DESCRIPTION:

* The aim of these projects is to build diffferent AI-powered applications using AI agents. The AI agents will be optimized, deployed in production environments, and manage their operations effectively for scalability and reliability.

## PROCEDURES:

1. create a directory and virtual environment to separate dependencies.

```bash
mkdir agentic_apps

cd agentic_apps

conda create -n agentic_apps python=3.11

conda activate agentic_apps
```

2. create a requirements.txt file for installation of necessary requirements for this applocation.

```bash
touch requirements.txt

pip install -r requirements.txt
```

## First Project : AI Agent that fetches and displays real-time Bitcoin prices using API integrations (```CoinDesk API``). 

* The script for this project [bitcoin_price_agent.py](https://github.com/bluemusk24/agentic_apps/blob/main/bitcoin_price_agent.py)

```bash
python3 bitcoin_price_agent.py
```
***Response*** : ```Current price of Bitcoin in USD : $92315```

## Second Project: AI Agent that monitors CPU usage, memory percentage in real time, and triggers alert for high CPU usage. 

* The script for this project [system_monitor.py](https://github.com/bluemusk24/agentic_apps/blob/main/system_monitor.py)

```bash
pip install psutil

python3 system_monitor.py
``` 
***Response*** : 
```Memory Usage: 45.1%```
```CPU usage is normal: 1.2%```
```Memory Usage: 45.0%```
```CPU usage is normal: 1.0%```
```Memory Usage: 45.0%```
```CPU usage is normal: 0.0%```
```Memory Usage: 45.0%```
```CPU usage is normal: 1.0%```
```Memory Usage: 45.3%```
```CPU usage is normal: 0.9%```

```Monitoring complete after 5 checks.```

**Note** : the ```cpu_threshold``` can be changed to any value.

***Testing Deepseek Model***
[test_deepseek](https://github.com/bluemusk24/agentic_apps/blob/main/test_deepseek.py) 

```bash
python3 test_deepseek.py
```

## Third Project: Health Coach AI Agent

***Description*** : This agent provides users with workout and meal plans based on their fitness goals and dietary preferences in real time. This agent uses several ```APIs```, and integrates ```Gradio``` for an interactive and user-freindly experience. Reference Link: [Exercise_Database_API](https://exercisedb-api.vercel.app/docs).

***create the following:***

* ```mkdir health_coach_agent``` directory

* ```cache_dir``` - to store and retrieve cached data. It automatically handles writing to disk while keeping frequently accessed data in memory for speed. Also, it eliminates redundant API calls, and speeds up responses to frequently queried targets.

* [exercise_api.py](https://github.com/bluemusk24/agentic_apps/blob/main/health_coach_agent/exercise_api.py) - python script to interact with the ```Exercise_Database_API```. It retrieves recommended workout routine based on ```target muscle``` group or required ```equipment```.

* [food_api.py](https://github.com/bluemusk24/agentic_apps/blob/main/health_coach_agent/food_api.py) - python script to interact with a ```Food_Database_API```. It retrieves details about food items or search for foods (diet preferences) based on user inputs.

* [recommendations.py](https://github.com/bluemusk24/agentic_apps/blob/main/health_coach_agent/recommendations.py) - python script to generate workout and meal plans from the APIs

* [main.py](https://github.com/bluemusk24/agentic_apps/blob/main/health_coach_agent/main.py) - python script to tie the entire system together using ```Gradio``` to create an interactive user interface.

***Run this script***
```bash
python3 health_coach_agent/main.py
```

***Results:***
1. Running on local URL: ```http://127.0.0.1:7860/``` - Gradio UI for seamless interaction. To create a public link, set `share=True` in `launch()`.
2. ```http://localhost:8000/``` - Prometheus UI to monitor request_processing_seconds_count 1.0

###  Deploying Health Coach AI Agent With Docker

***create the following:***

* [docker_main.py](https://github.com/bluemusk24/agentic_apps/blob/main/health_coach_agent/docker_main.py) - adjusted ```main.py``` script to include an environment variable for ```Gradio```.

* [Dockerfile](https://github.com/bluemusk24/agentic_apps/blob/main/health_coach_agent/Dockerfile) - to build a docker image and containerized our application to enable deployment. Run codes below:
```bash
docker build -t health_coach_agent:v1 .

docker run -it --rm -p 7860:7860 health_coach_agent:v1
```

```http://localhost:7860/``` - Launch Gradio UI for seamless interaction. To create a public link, set `share=True` in `launch()`.

***Pictorial View of Gradio:*** [Gradio_Image](https://github.com/bluemusk24/agentic_apps/blob/main/health_coach_agent/gradio_img.jpeg)

* [locustfile.py](https://github.com/bluemusk24/agentic_apps/blob/main/health_coach_agent/locustfile.py) - python script to simulate a large number of users interacting with our application concurrently, to test its scalability and reliability. Wait time is around 1-2 seconds for virtual users' post request to the application endpoint. 

* Run code below to load test our application with 10 users at a rate of 10 requests/sec.

```bash
locust -f locustfile.py --host http://localhost:7860
```
***Result:*** Launch Locust web interface at ```http://localhost:8089```

***Pictorial View of Locust:*** [Locust_Image](https://github.com/bluemusk24/agentic_apps/blob/main/health_coach_agent/locust_img.jpeg)

### Deployed Health Coach AI Agent as RestAPI ```Flask``` Endpoint

[rest_api.py](https://github.com/bluemusk24/agentic_apps/blob/main/health_coach_agent/rest_api.py) - python script that integrates ```Flask, Gradio and Prometheus```, and monitor logs.

```bash
python3 health_coach_agent/rest_api.py
```
```http://localhost:7860/``` - Launch Gradio UI

***Simulation and Logs Monitoring with Valid and Invalid Inputs*** - send a post request (```curl command```) to the RestAPI endpoint on the local server
* A new terminal:
```bash
curl -X POST http://localhost:5000/api/health_coach \
-H "Content-Type: application/json" \
-d '{"goal": "Build Muscle", "dietary_preference": "Vegan"}'
```
***Results:*** above curl command outputs a valid json response. 


## Fourth Project: Reciprocating Health Coach AI Agent using Agentic Framework (smolagents)

*** the following***

```bash
mkdir smolagents_framework
```

* [exercise_agent.py](https://github.com/bluemusk24/agentic_apps/blob/main/smolagents_framework/exercise_agent.py) - an agent that interacts with the ```Exercise_Database_API```. The agent retrieves recommended workout routine based on ```target muscle``` group or required ```equipment```.

* .env - a file in the ```smolagents_framework``` directory to load api keys.

* Test the exercise_agent locally:
```bash
python3 smolagents_framework/exercise_agent.py

Enter your Fitness Goal: lose weight, build muscle
```

* [food_agent.py](https://github.com/bluemusk24/agentic_apps/blob/main/smolagents_framework/food_agent.py) - an agent that interact with a ```Food_Database_API```. The agent retrieves details about food items or search for foods (diet preferences) based on user inputs.

* Test the food_agent locally:
```bash
python3 smolagents_framework/food_agent.py

Enter your Dietary Preference: Low Carb, Vegan
```

* [manager_agent.py](https://github.com/bluemusk24/agentic_apps/blob/main/smolagents_framework/manager_agent.py) - a manager agent that delegates task to the ```exercise_agent``` or ```food_agent```

* Test the food_agent locally:
```bash
python3 smolagents_framework/manager_agent.py

Enter Prefered Diet OR Fitness Plan: I want to build muscle
```

* [main_agent.py](https://github.com/bluemusk24/agentic_apps/blob/main/smolagents_framework/main_agent.py) - agentic python script to tie the entire system together using ```Gradio``` to create an interactive user interface.

***Run this script***
```bash
python3 health_coach_agent/main_agent.py
```

***Results:***
1. Running on local URL: ```http://127.0.0.1:7860/``` - Gradio UI for seamless interaction. To create a public link, set `share=True` in `launch()`.
2. ```http://localhost:8000/``` - Prometheus UI to monitor request_processing_seconds_count 1.0
3. Check [health_coach.log](https://github.com/bluemusk24/agentic_apps/blob/main/health_coach.log) for updated logs.

###  Deploying Health Coach Smolagent AI Agent With Docker

***create the following:***

* [docker_agent.py](https://github.com/bluemusk24/agentic_apps/blob/main/smolagents_framework/docker_agent.py) - adjusted ```agent_main.py``` script to include an environment variable for ```Gradio```.

* [Dockerfile](https://github.com/bluemusk24/agentic_apps/blob/main/smolagents_framework/Dockerfile) - to build a docker image and containerized our application to enable deployment. Run codes below:
```bash
docker build -t health_coach_smolagent:v1 .

docker run -it --rm -p 7860:7860 health_coach_smolagent:v1
```

```http://localhost:7860/``` - Launch Gradio UI for seamless interaction. To create a public link, set `share=True` in `launch()`.

***Pictorial View of Gradio:*** [Gradio_Image]()

* [locust_agent.py](https://github.com/bluemusk24/agentic_apps/blob/main/smolagents_framework/locust_agent.py) - python script to simulate a large number of users interacting with our application concurrently, to test its scalability and reliability. Wait time is around 1-2 seconds for virtual users' post request to the application endpoint. 

* Run code below to load test our application with 10 users at a rate of 10 requests/sec.

```bash
locust -f locust_agent.py --host http://localhost:7860
```
***Result:*** Launch Locust web interface at ```http://localhost:8089```

***Pictorial View of Locust:*** [Locust_Image]()

### Tracing Smolagents (Health_Coach Agent) with Arize Phoenix

* [agent_arize_tracing.py](https://github.com/bluemusk24/agentic_apps/blob/main/smolagents_framework/agent_arize_tracing.py) - python script to log in traces, monitor and evaluate agents with [ARIZE_PHOENIX](https://phoenix.arize.com/)
```bash 
python3 agent_arize_tracing.py
```
[PhoenixArize_Tracing1](https://github.com/bluemusk24/agentic_apps/blob/main/smolagents_framework/app.phoenix.arize.com.jpeg) 

[PhoenixArize_Tracing2](https://github.com/bluemusk24/agentic_apps/blob/main/smolagents_framework/app.phoenix.arize.jpeg)



## Tech Stack:
***LLM*** - ```deepseek-r1:1.5b```
***Gradio*** - to create a seemless user interface.
***Prometheus*** - to monitor systems performance by tracking how long each user request takes to process.
***Locust*** - python-based-load-testing framework for performance of APIs.
***Smolagents*** - huggingface agentic framework to build AI agents.




```agent_main.py``` code for JSON output in Gradio UI

```bash
import gradio as gr
from manager_agent import create_manager_agent
from loguru import logger
from prometheus_client import start_http_server, Summary
import json

# Error and Debug logs are added to track issues
logger.add("health_coach.log", rotation="1 MB")

# Prometheus server to collect metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Timing function for Prometheus
@REQUEST_TIME.time()  
def health_coach(goal, dietary_preference):
    """
    Handles both workout and meal plan generation.
    """
    try:
        logger.info(f"Workout routine for goal: {goal} and diet: {dietary_preference}")
        manager = create_manager_agent()

        # Get workout plan and meal plan
        workout_plan_result = manager.run(f"Create a workout plan for {goal}")
        logger.info(f"Generated workout plan: {type(workout_plan_result)}")

        meal_plan_result = manager.run(f"Create a meal plan for {dietary_preference}")
        logger.info(f"Generated meal plan: {type(meal_plan_result)}")

        # Parse workout plan and meal plan as JSON; if fails, use the string representation
        try:
            workout_plan = json.loads(str(workout_plan_result))
        except json.JSONDecodeError:
            workout_plan = {"result": str(workout_plan_result)}
            
        try:
            meal_plan = json.loads(str(meal_plan_result))
        except json.JSONDecodeError:
            meal_plan = {"result": str(meal_plan_result)}

        logger.info(f"Processed workout plan: {type(workout_plan)}")
        logger.info(f"Processed meal plan: {type(meal_plan)}")
        
        return workout_plan, meal_plan
    except Exception as e:
        logger.error(f"Error: {e}")
        logger.exception("Full traceback:")
        return {"error": str(e)}, {"error": str(e)}
    
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
    title="Personal Health Coach AI Agent",
    description="Enter your fitness goal and dietary preference to receive personalized workout and meal plans"
)

def main():
    # Start Prometheus metrics server and launch Gradio app
    start_http_server(8000)   
    app.launch(share=True)     

if __name__ == "__main__":
    main()
```