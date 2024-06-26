from langchain_openai import ChatOpenAI
from langchain_cron import HumanMessage

class Chatbox:
    model: ChatOpenAI = None

    def __init__(self):
        self.model = ChatOpenAI(model="gpt-3.5-turbo")

    def chat1(self, message: str) -> str:
        responseOfAI = self.model.invoke(
            [HumanMessage("Hi, I'm clack")]
        )

        return responseOfAI.content