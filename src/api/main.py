from email import message
from fastapi import FastAPI
from datetime import datetime
from models.translator import Translator
from models.chatbot import Chatbox

app = FastAPI()

@app.get("/")
def read_root():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"message": f"Hello World, current time is {current_time}"}

@app.get("/translate")
def translate():
    translator = Translator('English', 'Chinese')
    message = "Hello Word! What happened? In there years, computer was more and more clever, and AGI is coming."
    translated_message = translator.translate(message)
    return {"translated_message": translated_message}

@app.get("/chat")
def chat():
    chatbot = Chatbox()
    messages = [
        "Hello, I'm clack, a computer enjineer.",
        "Do you know what's my name?",
    ] 

    # message 为 messages 的最后一个元素
    message = messages[-1]
    response = chatbot.chat1(message)
    return {"response": response}

@app.get("/chat2")
def chat2():
    chatbot = Chatbox()
    messages = [
        "Hello, I'm clack, a computer enjineer.",
        "Do you know what's my name?",
        "And what's your name?"
    ]

    response = []

    # 遍历 messages，每次调用 chat2 方法
    for message in messages:
        answer = chatbot.chat2(message)
        response.append(answer)
        print(answer)

    return {"response": response}