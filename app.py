import os
import mesop as me
import mesop.labs as mel
from swarmauri.standard.llms.concrete.GroqModel import GroqModel
from swarmauri.standard.agents.concrete.SimpleConversationAgent import SimpleConversationAgent
from swarmauri.standard.conversations.concrete.Conversation import Conversation

API_KEY = os.getenv("GROQ_API_KEY")

llm = GroqModel(api_key=API_KEY)
agent = SimpleConversationAgent(llm=llm, conversation=Conversation())


def converse(input: str, history: list[mel.ChatMessage]):
    result = agent.exec(input)
    yield result

@me.page(
    security_policy=me.SecurityPolicy(
        allowed_iframe_parents=["https://google.github.io"]
    ),
    path="/chat",
    title="Swarmauri Agent",
)
def page():
    mel.chat(converse, title="Swarmauri Agent", bot_user="Groq")