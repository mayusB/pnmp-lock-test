import os

from flask import Flask
from flask import request
from huggingface_hub import InferenceClient
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from openai import OpenAI

app = Flask(__name__)


@app.route("/prompt")
def prompt():
    user_chat = request.args.get("user_chat")

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    client.chat.completions.create(
        # ruleid: prompt-injection-flask
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_chat},
        ],
        temperature=0,
    )

    huggingface = InferenceClient()
    # ruleid: prompt-injection-flask
    res = huggingface.text_generation(user_chat, stream=True, details=True)

    huggingface = InferenceClient()
    # ruleid: prompt-injection-flask
    res = huggingface.text_generation(user_chat, stream=True, details=True)

    chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)
    # ruleid: prompt-injection-flask
    chat.invoke([HumanMessage(content=user_chat)])
