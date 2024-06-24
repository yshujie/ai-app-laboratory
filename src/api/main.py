from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"message": f"Hello World, current time is {current_time}"}