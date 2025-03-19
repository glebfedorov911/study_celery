from celery import Celery
import requests


app = Celery(
    "Chuck Norris",
    broker="redis://localhost:6379/0"
)

app.conf.beat_schedule = {
    "save_joke": {
        "task": "app2.mycelery.save_joke_about_chucknorris",
        "schedule": 60.0
    }
}

URL = "https://api.chucknorris.io/jokes/random"

def get_joke_about_chucknorris():
    try:
        response = requests.get(URL)    
        response.raise_for_status()
        return response.json()["value"]
    except:
        return "Not found joke"
    
@app.task
def save_joke_about_chucknorris():
    joke = get_joke_about_chucknorris()

    with open("app2/chucknorris_jokes.txt", 'a', encoding='UTF-8') as file:
        file.write(joke)        
        file.write("\n")
    print("finished")