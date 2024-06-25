from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

class Translator:
    from_language: str = None
    target_language: str = None
    model: ChatOpenAI = None

    def __init__(self, from_language: str, target_language: str):
        self.from_language = from_language
        self.target_language = target_language
        self.model = ChatOpenAI(model="gpt-3.5-turbo")

    def translate(self, message: str) -> str:
        parser = StrOutputParser()
        system_template = "Translate the following into {language}:"
        prompt_template = ChatPromptTemplate.from_messages(
            [("system", system_template), ("user", "{text}")]
        )

        chain = prompt_template | self.model | parser
        return chain.invoke({
            "language": self.target_language,
            "text": message
        })