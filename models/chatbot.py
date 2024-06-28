from urllib import response
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


class Chatbox:
    model: ChatOpenAI = None

    def __init__(self):
        self.model = ChatOpenAI(model="gpt-3.5-turbo")

    def chat1(self, message: str) -> str:
        responseOfAI = self.model.invoke(
            [HumanMessage(message)]
        )

        return responseOfAI.content
    
    def chat2(self, message: str) -> str:
        config = {"configurable": {"session_id": "chat2"}}
        with_message_history = RunnableWithMessageHistory(
            self.model,
            get_session_history
        )

        responseOfAI = with_message_history.invoke(
            [HumanMessage(message)],
            config
        )

        return responseOfAI.content

    def chat3(self, message: str) -> str:
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful assistant. Answer all questions to the best of your ability."
                ),
                (
                    "system",
                    "Your name is Jarvis, you are Iron Man‘s AI assistant."
                ),
                MessagesPlaceholder(variable_name="messages")
            ]
        )

        chain = prompt | self.model

        config = {"configurable": {"session_id": "chat3"}}
        with_message_history = RunnableWithMessageHistory(
            chain,
            get_session_history
        )

        responseOfAI = with_message_history.invoke(
            [HumanMessage(message)],
            config
        )

        return responseOfAI.content
