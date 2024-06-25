from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage 

class Tanslator:
    from_language: str = None
    target_language: str = None
    model: ChatOpenAI = None

    def __init__(self, from_language: str, target_language: str):
        self.from_language = from_language
        self.target_language = target_language
        self.model = ChatOpenAI(model="gpt-4")

    def translate(self, message: str) -> str:
        messages = [
            SystemMessage(content="Translate the following message from {} to {}".format(self.from_language, self.target_language)),
            HumanMessage(content=message)
        ]

        AIMessage = self.model.invoke(messages)
        return AIMessage.content
    