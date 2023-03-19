import openai
from flask import Flask, render_template, request, jsonify
import pymysql

# flask
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# openai
OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY
model = 'gpt-3.5-turbo'

# main
@app.route("/")
def home():
    return render_template('index.html')

# chat answer
@app.route('/chat', methods=['POST'])
def chat():
    if request.method == 'POST':
        # 입력값
        user_input = request.form["answer"]

    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": user_input}
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    answer = response['choices'][0]['message']['content']

    # 로컬로 저장되는 코드
    f = open("chat_web.txt", "w")
    f.write(answer)
    f.close()

    return answer

if __name__ == '__main__':
    app.debug = True
    app.run()
