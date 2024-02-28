from flask import Flask, request, render_template
from openai import OpenAI
import config

client = OpenAI(api_key=config.API_KEY)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_text,
            }
        ],
        model="gpt-4",
        max_tokens=1024,
        temperature=0.8,
        n=1,
    )

    return str(chat_completion.choices[0].message.content)

if __name__ == "__main__":
    app.run()