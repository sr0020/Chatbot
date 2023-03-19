from flask import Flask, render_template, request, jsonify
import openai
import os

# OpenAI API key 설정
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Flask 앱 생성
app = Flask(__name__)

# GPT-3 모델 설정
model_engine = "text-davinci-002"
prompt = (
    "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."
    "\n\n"
    "User: Hello, who are you?"
    "\nAI:"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["text"]

    # GPT-3 모델에 입력값 전달
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt + user_message + "\n",
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # 모델이 생성한 응답 반환
    message = response.choices[0].text.strip()
    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(debug=True)