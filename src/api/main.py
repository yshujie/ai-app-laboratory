from fastapi import FastAPI
from datetime import datetime
from models.translator import Translator

app = FastAPI()

@app.get("/")
def read_root():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"message": f"Hello World, current time is {current_time}"}

@app.get("/translate")
def translate():
    translator = Translator('English', 'Chinese')
    message = "Hello Word"
    translated_message = translator.translate(message)
    return {"translated_message": translated_message}